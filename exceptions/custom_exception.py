from enum import Enum

class ErrorType(Enum) : 
    FILE_NOT_FOUND = 'FILE_NOT_FOUND'
    DIRECTORY_NOT_FOUND = 'DIRECTORY_NOT_FOUND'
    INVALID_COMMAND = 'INVALID_COMMAND'
    UNKNOWN_ERROR = 'UNKNOWN_ERROR'
    NOT_EXISTING_PATH = 'NOT_EXISTING_PATH'

class CustomError(Exception):
    def __init__ (self,error_type : ErrorType , message: str ):
        self.error_type = error_type
        self.message = message
        super().__init__(f"[{error_type}] {message}")