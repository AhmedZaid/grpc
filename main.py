# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from concurrent import futures

import Contracts_pb2_grpc

import grpc

from Contracts_pb2_grpc import CarServiceServicer


def serve():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        Contracts_pb2_grpc.add_CarServiceServicer_to_server(
            CarServiceServicer(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    serve()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
