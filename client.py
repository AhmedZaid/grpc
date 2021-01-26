import grpc

import Contracts_pb2_grpc
from Contracts_pb2 import CarCreateRequest


def client():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = Contracts_pb2_grpc.CarServiceStub(channel)
        request = CarCreateRequest(name="BMW")
        r = stub.Create(request)
        print(r)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client()
