from .base_file_folder_command import FileFolderCommand
from ..command_types import CommandType
from utils import file_folder_exits , delete_src
from exceptions import CustomError, ErrorType

class DeleteFileFolderCommand(FileFolderCommand):
    def __init__(self,src):
        super().__init__(CommandType.DELETE_FILE, "delete <src>")
        self.src = src

    def execute(self):
        if not self.src :
            raise CustomError(ErrorType.INVALID_COMMAND, f"Missing arguments. Usage : {self.usage}")
        file_folder_exits(self.src)   
        delete_src(self.src)
        return f"File or Folder was sucessfuly deleted from {self.src} !" 