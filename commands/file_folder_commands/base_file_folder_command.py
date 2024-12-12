from abc import ABC , abstractmethod
from commands.command_types import CommandType

class FileFolderCommand(ABC):
    def __init__(self, command_type: CommandType, usage: str):
        self.command_type = command_type
        self.usage = usage

    @abstractmethod
    def execute(self):
        pass