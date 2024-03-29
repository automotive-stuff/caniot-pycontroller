# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import model_pb2 as model__pb2


class CanControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendGarage = channel.unary_unary(
                '/cancontroller.ipc.CanController/SendGarage',
                request_serializer=model__pb2.GarageCommand.SerializeToString,
                response_deserializer=model__pb2.GarageResponse.FromString,
                )
        self.ReadAttribute = channel.unary_unary(
                '/cancontroller.ipc.CanController/ReadAttribute',
                request_serializer=model__pb2.AttributeRequest.SerializeToString,
                response_deserializer=model__pb2.AttributeResponse.FromString,
                )
        self.WriteAttribute = channel.unary_unary(
                '/cancontroller.ipc.CanController/WriteAttribute',
                request_serializer=model__pb2.AttributeRequest.SerializeToString,
                response_deserializer=model__pb2.AttributeResponse.FromString,
                )


class CanControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendGarage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadAttribute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteAttribute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CanControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendGarage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendGarage,
                    request_deserializer=model__pb2.GarageCommand.FromString,
                    response_serializer=model__pb2.GarageResponse.SerializeToString,
            ),
            'ReadAttribute': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadAttribute,
                    request_deserializer=model__pb2.AttributeRequest.FromString,
                    response_serializer=model__pb2.AttributeResponse.SerializeToString,
            ),
            'WriteAttribute': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteAttribute,
                    request_deserializer=model__pb2.AttributeRequest.FromString,
                    response_serializer=model__pb2.AttributeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cancontroller.ipc.CanController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CanController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendGarage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cancontroller.ipc.CanController/SendGarage',
            model__pb2.GarageCommand.SerializeToString,
            model__pb2.GarageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadAttribute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cancontroller.ipc.CanController/ReadAttribute',
            model__pb2.AttributeRequest.SerializeToString,
            model__pb2.AttributeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteAttribute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cancontroller.ipc.CanController/WriteAttribute',
            model__pb2.AttributeRequest.SerializeToString,
            model__pb2.AttributeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
