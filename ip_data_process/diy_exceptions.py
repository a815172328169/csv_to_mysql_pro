# -*- coding: utf-8 -*-

"""
cmcc.exceptions

This module contains the set of Cmccs' exceptions.
"""


class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class DBConnectError(MyException):
    """Connect to DB has an error occurred."""


class DBProcessError(MyException):
    """Process with DB has an error occurred."""


class IPTypeError(MyException):
    """IP Type has an error occurred."""