# -*- coding: utf-8 -*-
"""Microservice for RiveNorm normalization method."""
from concurrent import futures
import logging

import grpc
import rivescript

import normalization_pb2
import normalization_pb2_grpc


def get_normalization(normaliser, message):
    """Normalizes the message.

    Args:
        normaliser {rivescript.RiveScript} -- [instance of Rivescript]
        message {string} -- [original message]
    Returns:
        message [string or None] -- [normalized string]
    """
    try:
        username = "dummy"
        return normaliser.reply(username, message)
    except AttributeError:
        return None


class NormalizationServicer(normalization_pb2_grpc.NormalizationServicer):
    """Provides methods that implement functionality of normalization server."""

    def __init__(self):
        self.normaliser = rivescript.RiveScript(
            debug=True,
            utf8=True
        )
        self.normaliser.load_directory("brain")
        self.normaliser.sort_replies()

    def GetNormalization(self, request, context):
        reply = get_normalization(self.normaliser, request.text)
        if reply is None:
            return normalization_pb2.Message(text="")
        else:
            return normalization_pb2.Message(text=reply)


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    normalization_pb2_grpc.add_NormalizationServicer_to_server(
        NormalizationServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
