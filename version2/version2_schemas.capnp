@0x9eef0faad93c5657;

enum WorkerTypes {
  torch @0;
  tensorflow @1;
  onnx @2;
}

enum Order {
  c @0; # row major (contiguous layout)
  f @1; # column major (fortran contiguous layout)
}

enum Device {
  cpu @0;
  gpu @1;
}

# union of numerical type, string, callable?
enum NumericalType {
  int8 @0;
  int16 @1;
  int32 @2;
  int64 @3;
  uInt8 @4;
  uInt16 @5;
  uInt32 @6;
  uInt64 @7;
  float32 @8; 
  float64 @9;
}


struct ChannelDescriptor {
    reply @0 :Data;
}


#input keys: do we really want to build batches for them or do we want to take in a single key that represents all of their tensors and operate on that instead
#output keys: single tensorkey that points to a n x n tensor?
struct BaseIndirectRequest {
  modelName @0 :Text;
  inputKeys @1 :List(TensorKey); # list of strings (tensor keys?). references to things in the feature store
  outputKeys @2 :List(TensorKey); # list of strings (tensor keys?)
  device @3 :Device;
  workerType @4 :WorkerTypes;
  replyChannel @5 :ChannelDescriptor;
}


struct BaseDirectRequest {
  modelName @0 :Text;
  union {
    modelData @1 :Data; 
    modelKey @2 :Data;
  }
  inputData @3 :List(Tensor);
  replyChannel @4 :ChannelDescriptor;
  device @5 :Device;
  workerType @6 :WorkerTypes;
}


struct BaseResponse {
    status @0 :Int32;
}

struct DirectResponse {
    base @0 :BaseResponse;
    result @1 :Tensor;
}

struct IndirectResponse {
    base @0 :BaseResponse;
    result @1 :List(TensorKey); # is this a single tensor stacked?
}


struct Tensor {
  tensorData @0 :Data;
  tensorDescriptor @1 :TensorDescriptor;
}

# types will be Order and NumericalType once there's mappings
struct TensorDescriptor {
  dimensions @0 :List(Int32);
  order @1 :Text;
  dataType @2 :Text;
}

struct TensorKey {
  key @0 :Data;
}
