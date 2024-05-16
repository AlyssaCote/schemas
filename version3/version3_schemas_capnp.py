"""This is an automatically generated stub for `version3_schemas.capnp`."""
import os

import capnp  # type: ignore

capnp.remove_import_hook()
here = os.path.dirname(os.path.abspath(__file__))
module_file = os.path.abspath(os.path.join(here, "version3_schemas.capnp"))
ChannelDescriptor = capnp.load(module_file).ChannelDescriptor
ChannelDescriptorBuilder = ChannelDescriptor
ChannelDescriptorReader = ChannelDescriptor
Request = capnp.load(module_file).Request
RequestBuilder = Request
RequestReader = Request
TensorKey = capnp.load(module_file).TensorKey
TensorKeyBuilder = TensorKey
TensorKeyReader = TensorKey
Response = capnp.load(module_file).Response
ResponseBuilder = Response
ResponseReader = Response
Tensor = capnp.load(module_file).Tensor
TensorBuilder = Tensor
TensorReader = Tensor
TensorDescriptor = capnp.load(module_file).TensorDescriptor
TensorDescriptorBuilder = TensorDescriptor
TensorDescriptorReader = TensorDescriptor
