from message_handler import *
import torch
import tensorflow as tf


# INDIRECT
# indirect_mh = MessageHandler()
# this portion happens outside of the ML task queue
# input_key_1 = indirect_mh.create_tensor_key("key1")
# input_key_2 = indirect_mh.create_tensor_key("key2")
# ouput_key_1 = indirect_mh.create_tensor_key("key3")
# ouput_key_2 = indirect_mh.create_tensor_key("key4")

# attributes = indirect_mh.create_torchcnn_request_attributes("tensor")

# indirect_request_data = indirect_mh.create_request(
#     reply_channel="reply_channel_byte_string",
#     model="model key",
#     input=[input_key_1, input_key_2],
#     output=[ouput_key_1, ouput_key_2],
#     device="cpu",
#     custom_attributes=attributes
# )
# serialized_request = indirect_mh.serialize_request(indirect_request_data)


# # this happens inside of the MLtask queue
# deserialized_request = indirect_mh.deserialize_request(serialized_request)
# print("Deserialized Request:", deserialized_request)
# print(deserialized_request["replyChannel"])

# # work was done and there are results!
# # fake result tensor key
# result_tensor_key = indirect_mh.create_tensor_key("result_key")
# return_data = indirect_mh.create_response(200, [result_tensor_key])
# print(return_data.to_dict())

# serialized_return = indirect_mh.serialize_response(return_data)


# # this happens wherever we send the return to
# deserialized_return = indirect_mh.deserialize_response(serialized_return)
# print("Deserialized Return:", deserialized_return)
# print()
# print()
# print("END OF INDIRECT")
# print()
# print()


# DIRECT TORCH
direct_mh = MessageHandler()
torch1 = torch.zeros((3, 2, 5), dtype=torch.int8, layout=torch.strided)
torch2 = torch.ones((3, 2, 5), dtype=torch.int8, layout=torch.strided)

t1 = direct_mh.create_tensor(torch1, "c", "int8", list(torch1.shape))
t2 = direct_mh.create_tensor(torch2, "c", "int8", list(torch2.shape))

tens = Tensor.init()
cd = ChannelDescriptor.new_message().init()

print(tens)
print(type(tens))
print(cd)
print(type(cd))

t_list = [t1, t2]
attributes = direct_mh.create_torchcnn_request_attributes("tensor")
# print(type(attributes))
# print(type(t1))
# print(Tensor)
# print(type(Tensor))
# # print(Tensor.__bases__)
# print(vars(Tensor))
# print(vars(ChannelDescriptor))
# print(type())
# version with model data
direct_request_data = direct_mh.create_request(
    reply_channel="reply channel",
    model = bytes("model bytes", "utf-8"),
    device="cpu",
    input=t1,
    output=t2,
    custom_attributes=attributes)
serialized_request = direct_mh.serialize_request(direct_request_data)
print(serialized_request)

# # SEND TO ML TASK QUEUE?

# deserialized_request = direct_mh.deserialize_request(serialized_request)
# print("Deserialized Request:", deserialized_request)

# rehydrated_torch_list = rehydrate_torch_tensor_list(deserialized_request["inputData"])
# print(rehydrated_torch_list)
# print("pytorch equal")
# print(torch.eq(torch1, rehydrated_torch_list[0]))
# print(torch.allclose(torch1, rehydrated_torch_list[0]))
# print(torch.eq(torch2, rehydrated_torch_list[1]))
# print(torch.allclose(torch2, rehydrated_torch_list[1]))

# # work was done and there are results!
# torch_result = torch.zeros((3, 2, 5), dtype=torch.int8, layout=torch.strided)
# result_tensor = direct_mh.create_tensor(torch_result, str(torch_result.layout), "int8")
# return_data = direct_mh.create_response(200, result_tensor)

# serialized_return = direct_mh.serialize_response(return_data)


# # this happens wherever we send the return to
# deserialized_return = direct_mh.deserialize_response(serialized_return)
# print("Deserialized Return:", deserialized_return)

# print(deserialized_return["base"]["status"])
# print()
# print()
# print("END OF TORCH")
# print()
# print()


# # DIRECT TF
# tf_direct_mh = MessageHandler()
# tflow1 = tf.zeros((3, 2, 5), dtype=tf.int8)
# tflow2 = tf.ones((3, 5, 6, 7), dtype=tf.int8)

# t1 = tf_direct_mh.create_tensor(tflow1, "C", "int8")
# t2 = tf_direct_mh.create_tensor(tflow2, "C", "int8")

# t_list = [t1, t2]

# # version with model data
# direct_request_data = tf_direct_mh.create_request(
#     "tf_direct_model_name",
#     t_list,
#     "reply channel byte string",
#     "cpu",
#     "torch",
#     model_data="THIS IS MODEL DATA",
# )
# serialized_request = tf_direct_mh.serialize_request(direct_request_data)
# print(serialized_request)

# # SEND TO ML TASK QUEUE?

# deserialized_request = tf_direct_mh.deserialize_request(serialized_request)
# print("Deserialized Request:", deserialized_request)

# rehydrated_tf_list = rehydrate_tf_tensor_list(deserialized_request["inputData"])
# print(rehydrated_tf_list)
# print("tf equal")
# print(tf.equal(tflow1, rehydrated_tf_list[0]))
# print(tf.debugging.assert_equal(tflow1, rehydrated_tf_list[0]))
# print(tf.equal(tflow2, rehydrated_tf_list[1]))
# print(tf.debugging.assert_equal(tflow2, rehydrated_tf_list[1]))

# # work was done and there are results!
# tf_result = tf.zeros((3, 2, 5), dtype=tf.int8)
# result_tensor = tf_direct_mh.create_tensor(tf_result, "C", "int8")
# return_data = tf_direct_mh.create_response(200, result_tensor)

# serialized_return = tf_direct_mh.serialize_response(return_data)


# # this happens wherever we send the return to
# deserialized_return = tf_direct_mh.deserialize_response(serialized_return)
# print("Deserialized Return:", deserialized_return)

# print(deserialized_return["base"]["status"])
# print()
# print()
# print("END OF TF")
# print()
# print()
