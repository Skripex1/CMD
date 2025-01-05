from .base_file_folder_command import FileFolderCommand
from ..command_types import CommandType
from utils import file_folder_exits , move_src_dest
from exceptions import CustomError, ErrorType

class MoveFileFolderCommand(FileFolderCommand):
    def __init__(self,src,dest):
        super().__init__(CommandType.MOVE_FILE, "move <src> <dest>")
        self.src = src
        self.dest = dest
    def execute(self):
        if not self.src or not self.dest:
            raise CustomError(ErrorType.INVALID_COMMAND, f"Missing arguments. Usage : {self.usage}")
        file_folder_exits(self.src)   
        move_src_dest(self.src, self.dest)
        return f"File or Folder was sucessfuly moved from {self.src} to {self.dest} !"