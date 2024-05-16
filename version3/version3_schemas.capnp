@0x811e927e4e2f1799;

enum Order {
  c @0; # row major (contiguous layout)
  f @1; # column major (fortran contiguous layout)
}

enum Device {
  cpu @0;
  gpu @1;
}

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

# device is implicit with the model. optional with a subset of devices available to the worker
struct Request {
  modelKey @0 :Text;
  input :union {
    inputKeys @1 :List(TensorKey);
    inputModelData @2 :Data;
  }
  output :union {
    outputKeys @3 :List(TensorKey);
    modelOutput @4 :Void;
  }
  device :union {
    deviceType @5 :Device;
    noDevice @6 :Void;
  }
  replyChannel @7 :ChannelDescriptor;
}

struct Response {
    status @0 :Int32;
    statusMessage @1 :Text;
    result :union {
      keys @2 :List(TensorKey);
      data @3 :Data; # or Tensor?
    }
}

struct Tensor {
  tensorData @0 :Data;
  tensorDescriptor @1 :TensorDescriptor;
}

struct TensorDescriptor {
  dimensions @0 :List(Int32);
  order @1 :Order;
  dataType @2 :NumericalType;
}

struct TensorKey {
  key @0 :Data; # or Text?
}

