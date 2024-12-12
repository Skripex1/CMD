
from .base_file_folder_command import FileFolderCommand
from ..command_types import CommandType
from exceptions import CustomError, ErrorType
from utils import file_exists , copy_src_dest

class CopyFileFolderCommand(FileFolderCommand):
    def __init__(self,src,dest):
        super().__init__(CommandType.COPY_FILE, "copy <src> <dest>")
        self.src = src
        self.dest = dest
    def execute(self):
        if not self.src or not self.dest:
            raise CustomError(ErrorType.INVALID_COMMAND, f"Missing arguments. Usage : {self.usage}")
        file_exists(self.src)   
        copy_src_dest(self.src, self.dest)
        return f"File was sucessfuly copied from {self.src} to {self.dest} !"