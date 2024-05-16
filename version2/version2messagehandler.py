from dataclasses import dataclass
from version2_schemas_capnp import *
import typing as t
from abc import ABC, abstractmethod
import torch
import numpy as np
import tensorflow as tf


# return classes? needs work
@dataclass
class IndirectRequest:
    modelName: str
    inputKeys: t.List[TensorKey]
    outputKeys: t.List[TensorKey]
    device: "Device"
    workerType: "WorkerTypes"
    replyChannel: ChannelDescriptor


@dataclass
class DirectRequest:
    modelName: str
    modelData: t.Optional[t.ByteString]
    modelKey: t.Optional[t.ByteString]
    inputData: t.List[Tensor]
    replyChannel: ChannelDescriptor
    device: "Device"
    workerType: "WorkerTypes"


@dataclass
class IndirectResponseClass:
    base_status: BaseResponse
    result: t.List[TensorKey]


@dataclass
class DirectResponseClass:
    base_status: BaseResponse
    result: Tensor


class NewMessageHandler(ABC):
    @abstractmethod
    def create_request(self):
        pass

    @abstractmethod
    def serialize_request(self):
        pass

    @abstractmethod
    def deserialize_request(self):
        pass

    @abstractmethod
    def create_response(self):
        pass

    def create_tensor(
        self,
        data: t.Union[torch.Tensor, tf.Tensor],
        order: str,
        data_type: str,
    ) -> "Tensor":
        tensor = Tensor.new_message()
        tensor.tensorData = data.numpy().tobytes()
        description = TensorDescriptor.new_message()
        description.order = order
        description.dataType = data_type
        description.dimensions = list(data.shape)
        tensor.tensorDescriptor = description

        return tensor

    def create_tensor_descriptor(
        self,
        dimensions: t.List[int],
        order: str,
        data_type: str,
    ) -> "TensorDescriptor":
        description = TensorDescriptor.new_message()
        description.dimensions = dimensions
        description.order = order
        description.dataType = data_type

        return description

    def create_tensor_key(self, name: str) -> "TensorKey":
        return TensorKey.new_message(key=name)


class IndirectMessageHandler(NewMessageHandler):
    def __init__(self) -> None:
        super().__init__()

    def create_request(
        self,
        model_name: str,
        input_keys: t.List["TensorKey"],
        output_keys: t.List["TensorKey"],
        device: "Device",
        worker_type: "WorkerTypes",
        reply_channel: t.ByteString,
    ) -> "BaseIndirectRequest":
        request = BaseIndirectRequest.new_message()
        channel_descriptor = ChannelDescriptor.new_message()
        channel_descriptor.reply = reply_channel
        request.modelName = model_name
        request.inputKeys = input_keys
        request.outputKeys = output_keys
        request.device = device
        request.workerType = worker_type
        request.replyChannel = channel_descriptor

        return request

    def serialize_request(
        self,
        message_data: "BaseIndirectRequestBuilder",
    ):
        return message_data.to_bytes()

    def deserialize_request(self, bytes_data) -> t.Dict:
        bytes_message = BaseIndirectRequest.from_bytes(bytes_data)

        with bytes_message as message:
            deserialized_data = message.to_dict()

        # return IndirectRequest(**deserialized_data)
        return deserialized_data

    def create_response(self, status: int, result: t.ByteString) -> "IndirectResponse":
        base_message = BaseResponse.new_message()
        base_message.status = status
        indirect_message = IndirectResponse.new_message()
        indirect_message.base = base_message
        indirect_message.result = result

        return indirect_message

    def deserialize_response(self, bytes_data: t.ByteString) -> t.Dict:
        bytes_message = IndirectResponse.from_bytes(bytes_data)

        with bytes_message as message:
            deserialized_data = message.to_dict()

        # return IndirectResponse(**deserialized_data)
        return deserialized_data

    def serialize_response(
        self,
        return_data: "BaseIndirectRequestBuilder",
    ) -> t.ByteString:
        return return_data.to_bytes()


class DirectMessageHandler(NewMessageHandler):
    def __init__(self) -> None:
        super().__init__()

    # should serialization just be part of create?
    def create_request(
        self,
        model_name: str,
        input_data: t.List["Tensor"],
        reply_channel: t.ByteString,
        device: "Device",
        worker_type: "WorkerTypes",
        model_data: t.Optional[t.ByteString] = None,
        model_key: t.Optional[t.ByteString] = None,
    ) -> "BaseDirectRequest":
        if (model_data is None and model_key is None) or (
            model_data is not None and model_key is not None
        ):
            raise ValueError(
                "Either model data or model key must be provided. Not both."
            )

        request = BaseDirectRequest.new_message()
        channel_descriptor = ChannelDescriptor.new_message()
        channel_descriptor.reply = reply_channel
        request.modelName = model_name
        request.inputData = input_data
        request.replyChannel = channel_descriptor
        request.device = device
        request.workerType = worker_type

        if model_data is not None:
            request.modelData = model_data

        if model_key is not None:
            request.modelKey = model_key

        return request

    def serialize_request(
        self,
        message_data: "BaseDirectRequestBuilder",
    ):
        return message_data.to_bytes()

    def deserialize_request(self, bytes_data) -> t.Dict:
        bytes_message = BaseDirectRequest.from_bytes(bytes_data)

        with bytes_message as message:
            deserialized_data = message.to_dict()

        # return DirectRequest(**deserialized_data)
        return deserialized_data

    def create_response(self, status: int, result: t.ByteString) -> "DirectResponse":
        base_message = BaseResponse.new_message()
        base_message.status = status
        direct_message = DirectResponse.new_message()
        direct_message.base = base_message
        direct_message.result = result

        return direct_message

    def deserialize_response(self, bytes_data: t.ByteString) -> t.Dict:
        bytes_message = DirectResponse.from_bytes(bytes_data)

        with bytes_message as message:
            deserialized_data = message.to_dict()

        # return DirectResponse(**deserialized_data)
        return deserialized_data

    def serialize_response(
        self,
        return_data: "BaseDirectRequestBuilder",
    ) -> t.ByteString:
        return return_data.to_bytes()


def rehydrate_torch_tensor(tensor_dict: t.Dict):
    tensor_data = np.frombuffer(
        tensor_dict["tensorData"], dtype=tensor_dict["tensorDescriptor"]["dataType"]
    )
    tensor_data = tensor_data.reshape(tensor_dict["tensorDescriptor"]["dimensions"])
    return torch.tensor(tensor_data)


def rehydrate_tf_tensor(tensor_dict: t.Dict):
    tensor_data = np.frombuffer(
        tensor_dict["tensorData"], dtype=tensor_dict["tensorDescriptor"]["dataType"]
    )
    tensor_data = tensor_data.reshape(tensor_dict["tensorDescriptor"]["dimensions"])
    return tf.constant(tensor_data)


def rehydrate_tf_tensor_list(tensor_list: t.List):
    return [rehydrate_tf_tensor(tensor) for tensor in tensor_list]


def rehydrate_torch_tensor_list(tensor_list: t.List):
    return [rehydrate_torch_tensor(tensor) for tensor in tensor_list]
