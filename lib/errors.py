#!/usr/bin/env python3


class ParserError(Exception):
    """
    The base error class for all other parsing errors.
    """
    pass


class ParserSyntaxError(ParserError):
    """
    Thrown when a syntax error occurs in the parser.
    """
    pass


class ParserNameError(ParserError):
    """
    Thrown when a name error occurs in the parser.
    """
    pass


class ParserTypeError(ParserError):
    """
    Thrown when a type error occurs in the parser.
    """
    pass


class ParserRuntimeError(ParserError):
    """
    Thrown when a runtime error occurs in the parser.
    """
    pass
