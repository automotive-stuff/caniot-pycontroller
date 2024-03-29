from cancontroller.can import DeviceId

from cancontroller.ipc import model_pb2
from cancontroller.ipc import model_pb2_grpc

from typing import Union

import grpc


class CLIClient:
    def __init__(self, grpc_target: str):
        self.grpc_target = grpc_target

    def ReadAttribute(self, deviceid: Union[int, DeviceId], key: int) -> int:
        with grpc.insecure_channel(self.grpc_target) as channel:
            stub = model_pb2_grpc.CanControllerStub(channel)
            response = stub.ReadAttribute(model_pb2.AttributeRequest(
                device=model_pb2.Device(
                    id=int(deviceid)
                ),
                key=key,
                timeout=10
            ))
            # print(model_pb2._STATUS.values_by_number[response.status].name, response.value)
            return response


if __name__ == "__main__":
    client = CLIClient('localhost:50051')
    did = DeviceId(DeviceId.DataType.CRT, 1)
    response = client.ReadAttribute(did, 0x1010)

    print(response)
