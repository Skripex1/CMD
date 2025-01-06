from .base_process_command import ProcessCommand
import psutil
from ..command_types import CommandType
from exceptions import CustomError,ErrorType


class KillProcessCommand(ProcessCommand):
    def __init__(self,pid):
        super().__init__(CommandType.DELETE_PROC,"kill_proc <pid>")
        self.pid = pid
    def execute(self):
        if not self.pid:
            raise CustomError(ErrorType.INVALID_COMMAND, f"Missing arguments. Usage : {self.usage}")
        try:
            process = psutil.Process(self.pid)
            process.terminate()
            process.wait()
            return f"Process with PID {self.pid} has been terminated."
        except psutil.NoSuchProcess:
            raise Exception(f"No such process with PID {self.pid}.")
        except psutil.AccessDenied:
            raise Exception(f"Access denied to terminate process with PID {self.pid}.")
        except Exception as e:
            raise Exception(f"Failed to terminate process: {e}")

    