from version3_schemas_capnp import *
import typing as t
import torch
import tensorflow as tf


class MessageHandler:

    # could also serialize in this step
    def create_request(
        self,
        model_key: str,
        reply_channel: t.ByteString,
        input_keys: t.Optional[t.List["TensorKey"]] = None,
        input_model_data: t.Optional[t.ByteString] = None,
        output_keys: t.Optional[t.List["TensorKey"]] = None,
        device: t.Optional["Device"] = None,
    ) -> "Request":
        if (input_keys is None and input_model_data is None) or (
            input_keys is not None and input_model_data is not None
        ):
            raise ValueError(
                "Either input keys or input model data must be provided. Not both."
            )
        channel_descriptor = ChannelDescriptor.new_message()
        channel_descriptor.reply = reply_channel
        request = Request.new_message()
        request.replyChannel = channel_descriptor
        request.modelKey = model_key

        if input_keys is not None:
            request.input.inputKeys = input_keys
        else:
            request.input.modelData = input_model_data

        if output_keys:
            request.output.outputKeys = output_keys
        else:
            request.output.modelOutput = None

        if device:
            request.device.deviceType = device
        else:
            request.device.noDevice = None

        return request

    def serialize_request(self, request: "RequestBuilder") -> t.ByteString:
        return request.to_bytes()

    def deserialize_request(self, request_bytes: t.ByteString) -> "RequestReader":
        bytes_message = Request.from_bytes(request_bytes)

        with bytes_message as message:
            # TODO return a Request dataclass
            return message

    def create_response(
        self,
        status: int,
        status_message: str,
        result_keys: t.Optional[t.List["TensorKey"]] = None,
        result_data: t.Optional[t.ByteString] = None,
    ) -> "Response":
        if (result_keys is None and result_data is None) or (
            result_keys is not None and result_data is not None
        ):
            raise ValueError(
                "Either result keys or result data must be provided. Not both."
            )
        response = Response.new_message()
        response.status = status
        response.statusMessage = status_message

        if result_keys:
            response.result.keys = result_keys
        else:
            response.result.data = result_data

        return response

    def serialize_response(self, response: "ResponseBuilder") -> t.ByteString:
        return response.to_bytes()

    def deserialize_response(self, response_bytes: t.ByteString) -> "ResponseReader":
        bytes_message = Response.from_bytes(response_bytes)

        with bytes_message as message:
            # TODO return a Response dataclass
            return message

    # these methods made more sense when direct inference request data was lists of tensors
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
