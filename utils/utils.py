import os
from exceptions import CustomError , ErrorType
import shutil


def is_correct_path (path):
    if not os.path.exists(path):
        #print(f"{path} nu exista")
        raise CustomError(ErrorType.NOT_EXISTING_PATH, "Path does not exist or is wrong.")

def file_exists (path):
    is_correct_path(path)
    if not os.path.isfile(path):
        raise  CustomError(ErrorType.FILE_NOT_FOUND,"'{path}' is not a file.")
        
def directory_exists (path):
    if not os.path.exists(path) :
        raise CustomError(ErrorType.NOT_EXISTING_PATH,"'{path}' is not a correct path.")
    elif not os.path.isdir(path):
        raise  CustomError(ErrorType.FILE_NOT_FOUND,"'{path}' is not a directory.")
    
def file_folder_exits(path):
    if not os.path.exists(path) :
        raise CustomError(ErrorType.NOT_EXISTING_PATH,"'{path}' is not a correct path.")
    if not file_exists(path) and not directory_exists(path) :
        raise CustomError
    
def continue_after_arguments (number,args,ce : CustomError) :
    print(f"Warning: Extra arguments detected: {args[number:]}")
    print(f"Source: {args[0]}")
    print(f"Destination: {args[1]}")
    user_input = input("Do you want to continue with the copy operation? (yes/no): ").strip().lower()
    if user_input not in ["yes", "y"]:
        raise ce
    
    
def copy_src_dest(src,dest):
    shutil.copy(src,dest)