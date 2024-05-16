"""This is an automatically generated stub for `version2_schemas.capnp`."""
import os

import capnp  # type: ignore

capnp.remove_import_hook()
here = os.path.dirname(os.path.abspath(__file__))
module_file = os.path.abspath(os.path.join(here, "version2_schemas.capnp"))
ChannelDescriptor = capnp.load(module_file).ChannelDescriptor
ChannelDescriptorBuilder = ChannelDescriptor
ChannelDescriptorReader = ChannelDescriptor
BaseIndirectRequest = capnp.load(module_file).BaseIndirectRequest
BaseIndirectRequestBuilder = BaseIndirectRequest
BaseIndirectRequestReader = BaseIndirectRequest
TensorKey = capnp.load(module_file).TensorKey
TensorKeyBuilder = TensorKey
TensorKeyReader = TensorKey
BaseDirectRequest = capnp.load(module_file).BaseDirectRequest
BaseDirectRequestBuilder = BaseDirectRequest
BaseDirectRequestReader = BaseDirectRequest
Tensor = capnp.load(module_file).Tensor
TensorBuilder = Tensor
TensorReader = Tensor
TensorDescriptor = capnp.load(module_file).TensorDescriptor
TensorDescriptorBuilder = TensorDescriptor
TensorDescriptorReader = TensorDescriptor
BaseResponse = capnp.load(module_file).BaseResponse
BaseResponseBuilder = BaseResponse
BaseResponseReader = BaseResponse
DirectResponse = capnp.load(module_file).DirectResponse
DirectResponseBuilder = DirectResponse
DirectResponseReader = DirectResponse
IndirectResponse = capnp.load(module_file).IndirectResponse
IndirectResponseBuilder = IndirectResponse
IndirectResponseReader = IndirectResponse
