"""This is an automatically generated stub for `version2_schemas.capnp`."""
from __future__ import annotations

from contextlib import contextmanager
from io import BufferedWriter
from typing import Iterator, Literal, Sequence, overload

WorkerTypes = Literal["torch", "tensorflow", "onnx"]
Order = Literal["c", "f"]
Device = Literal["cpu", "gpu"]
NumericalType = Literal[
    "int8",
    "int16",
    "int32",
    "int64",
    "uInt8",
    "uInt16",
    "uInt32",
    "uInt64",
    "float32",
    "float64",
]

class ChannelDescriptor:
    reply: bytes
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[ChannelDescriptorReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ChannelDescriptorReader: ...
    @staticmethod
    def new_message() -> ChannelDescriptorBuilder: ...
    def to_dict(self) -> dict: ...

class ChannelDescriptorReader(ChannelDescriptor):
    def as_builder(self) -> ChannelDescriptorBuilder: ...

class ChannelDescriptorBuilder(ChannelDescriptor):
    @staticmethod
    def from_dict(dictionary: dict) -> ChannelDescriptorBuilder: ...
    def copy(self) -> ChannelDescriptorBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> ChannelDescriptorReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class TensorKey:
    key: bytes
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[TensorKeyReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> TensorKeyReader: ...
    @staticmethod
    def new_message() -> TensorKeyBuilder: ...
    def to_dict(self) -> dict: ...

class TensorKeyReader(TensorKey):
    def as_builder(self) -> TensorKeyBuilder: ...

class TensorKeyBuilder(TensorKey):
    @staticmethod
    def from_dict(dictionary: dict) -> TensorKeyBuilder: ...
    def copy(self) -> TensorKeyBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> TensorKeyReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class BaseIndirectRequest:
    modelName: str
    inputKeys: Sequence[TensorKey | TensorKeyBuilder | TensorKeyReader]
    outputKeys: Sequence[TensorKey | TensorKeyBuilder | TensorKeyReader]
    device: Device
    workerType: WorkerTypes
    replyChannel: ChannelDescriptor | ChannelDescriptorBuilder | ChannelDescriptorReader
    def init(self, name: Literal["replyChannel"]) -> ChannelDescriptor: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[BaseIndirectRequestReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> BaseIndirectRequestReader: ...
    @staticmethod
    def new_message() -> BaseIndirectRequestBuilder: ...
    def to_dict(self) -> dict: ...

class BaseIndirectRequestReader(BaseIndirectRequest):
    inputKeys: Sequence[TensorKeyReader]
    outputKeys: Sequence[TensorKeyReader]
    replyChannel: ChannelDescriptorReader
    def as_builder(self) -> BaseIndirectRequestBuilder: ...

class BaseIndirectRequestBuilder(BaseIndirectRequest):
    inputKeys: Sequence[TensorKey | TensorKeyBuilder | TensorKeyReader]
    outputKeys: Sequence[TensorKey | TensorKeyBuilder | TensorKeyReader]
    replyChannel: ChannelDescriptor | ChannelDescriptorBuilder | ChannelDescriptorReader
    @staticmethod
    def from_dict(dictionary: dict) -> BaseIndirectRequestBuilder: ...
    def copy(self) -> BaseIndirectRequestBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> BaseIndirectRequestReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class TensorDescriptor:
    dimensions: Sequence[int]
    order: str
    dataType: str
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[TensorDescriptorReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> TensorDescriptorReader: ...
    @staticmethod
    def new_message() -> TensorDescriptorBuilder: ...
    def to_dict(self) -> dict: ...

class TensorDescriptorReader(TensorDescriptor):
    def as_builder(self) -> TensorDescriptorBuilder: ...

class TensorDescriptorBuilder(TensorDescriptor):
    @staticmethod
    def from_dict(dictionary: dict) -> TensorDescriptorBuilder: ...
    def copy(self) -> TensorDescriptorBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> TensorDescriptorReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class Tensor:
    tensorData: bytes
    tensorDescriptor: TensorDescriptor | TensorDescriptorBuilder | TensorDescriptorReader
    def init(self, name: Literal["tensorDescriptor"]) -> TensorDescriptor: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[TensorReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> TensorReader: ...
    @staticmethod
    def new_message() -> TensorBuilder: ...
    def to_dict(self) -> dict: ...

class TensorReader(Tensor):
    tensorDescriptor: TensorDescriptorReader
    def as_builder(self) -> TensorBuilder: ...

class TensorBuilder(Tensor):
    tensorDescriptor: TensorDescriptor | TensorDescriptorBuilder | TensorDescriptorReader
    @staticmethod
    def from_dict(dictionary: dict) -> TensorBuilder: ...
    def copy(self) -> TensorBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> TensorReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class BaseDirectRequest:
    modelName: str
    modelData: bytes
    modelKey: bytes
    inputData: Sequence[Tensor | TensorBuilder | TensorReader]
    replyChannel: ChannelDescriptor | ChannelDescriptorBuilder | ChannelDescriptorReader
    device: Device
    workerType: WorkerTypes
    def which(self) -> Literal["modelData", "modelKey"]: ...
    def init(self, name: Literal["replyChannel"]) -> ChannelDescriptor: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[BaseDirectRequestReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> BaseDirectRequestReader: ...
    @staticmethod
    def new_message() -> BaseDirectRequestBuilder: ...
    def to_dict(self) -> dict: ...

class BaseDirectRequestReader(BaseDirectRequest):
    inputData: Sequence[TensorReader]
    replyChannel: ChannelDescriptorReader
    def as_builder(self) -> BaseDirectRequestBuilder: ...

class BaseDirectRequestBuilder(BaseDirectRequest):
    inputData: Sequence[Tensor | TensorBuilder | TensorReader]
    replyChannel: ChannelDescriptor | ChannelDescriptorBuilder | ChannelDescriptorReader
    @staticmethod
    def from_dict(dictionary: dict) -> BaseDirectRequestBuilder: ...
    def copy(self) -> BaseDirectRequestBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> BaseDirectRequestReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class BaseResponse:
    status: int
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[BaseResponseReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> BaseResponseReader: ...
    @staticmethod
    def new_message() -> BaseResponseBuilder: ...
    def to_dict(self) -> dict: ...

class BaseResponseReader(BaseResponse):
    def as_builder(self) -> BaseResponseBuilder: ...

class BaseResponseBuilder(BaseResponse):
    @staticmethod
    def from_dict(dictionary: dict) -> BaseResponseBuilder: ...
    def copy(self) -> BaseResponseBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> BaseResponseReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class DirectResponse:
    base: BaseResponse | BaseResponseBuilder | BaseResponseReader
    result: Tensor | TensorBuilder | TensorReader
    @overload
    def init(self, name: Literal["base"]) -> BaseResponse: ...
    @overload
    def init(self, name: Literal["result"]) -> Tensor: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[DirectResponseReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> DirectResponseReader: ...
    @staticmethod
    def new_message() -> DirectResponseBuilder: ...
    def to_dict(self) -> dict: ...

class DirectResponseReader(DirectResponse):
    base: BaseResponseReader
    result: TensorReader
    def as_builder(self) -> DirectResponseBuilder: ...

class DirectResponseBuilder(DirectResponse):
    base: BaseResponse | BaseResponseBuilder | BaseResponseReader
    result: Tensor | TensorBuilder | TensorReader
    @staticmethod
    def from_dict(dictionary: dict) -> DirectResponseBuilder: ...
    def copy(self) -> DirectResponseBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> DirectResponseReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class IndirectResponse:
    base: BaseResponse | BaseResponseBuilder | BaseResponseReader
    result: Sequence[TensorKey | TensorKeyBuilder | TensorKeyReader]
    def init(self, name: Literal["base"]) -> BaseResponse: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[IndirectResponseReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> IndirectResponseReader: ...
    @staticmethod
    def new_message() -> IndirectResponseBuilder: ...
    def to_dict(self) -> dict: ...

class IndirectResponseReader(IndirectResponse):
    base: BaseResponseReader
    result: Sequence[TensorKeyReader]
    def as_builder(self) -> IndirectResponseBuilder: ...

class IndirectResponseBuilder(IndirectResponse):
    base: BaseResponse | BaseResponseBuilder | BaseResponseReader
    result: Sequence[TensorKey | TensorKeyBuilder | TensorKeyReader]
    @staticmethod
    def from_dict(dictionary: dict) -> IndirectResponseBuilder: ...
    def copy(self) -> IndirectResponseBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> IndirectResponseReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...