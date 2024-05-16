from version3_schemas_capnp import *
from version3messagehandler import *
import torch
import tensorflow as tf

### INCOMPLETE!!! NEEDS DIRECT EXAMPLES STILL

# INDIRECT
indirect_mh = MessageHandler()
# this portion happens outside of the ML task queue
input_key_1 = indirect_mh.create_tensor_key("key1")
input_key_2 = indirect_mh.create_tensor_key("key2")
ouput_key_1 = indirect_mh.create_tensor_key("key3")
ouput_key_2 = indirect_mh.create_tensor_key("key4")
indirect_request_data = indirect_mh.create_request(
    model_key="model_name",
    input_keys=[input_key_1, input_key_2],
    output_keys=[ouput_key_1, ouput_key_2],
    reply_channel="reply channel byte string",
)
serialized_request = indirect_mh.serialize_request(indirect_request_data)


# this happens inside of the MLtask queue
deserialized_request = indirect_mh.deserialize_request(serialized_request)
print("Deserialized Request:", deserialized_request)

# work was done and there are results!
# fake result tensor key
result_tensor_key = indirect_mh.create_tensor_key("result_key")
return_data = indirect_mh.create_response(
    status=200, status_message="It worked!", result_keys=[result_tensor_key]
)

serialized_return = indirect_mh.serialize_response(return_data)


# this happens wherever we send the return to
deserialized_return = indirect_mh.deserialize_response(serialized_return)
print("Deserialized Return:")
print(deserialized_return)
print()
print()
print("END OF INDIRECT")
print()
print()
