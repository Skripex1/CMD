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
    if not os.path.isfile(path) and not os.path.isdir(path):
        raise CustomError(ErrorType.FILE_NOT_FOUND, f"'{path}' is neither a file nor a directory.")
    
def continue_after_arguments (number,args,ce : CustomError) :
    print(f"Warning: Extra arguments detected: {args[number:]}")
    print(f"Source: {args[0]}")
    print(f"Destination: {args[1]}")
    user_input = input("Do you want to continue with the copy operation? (yes/no): ").strip().lower()
    if user_input not in ["yes", "y"]:
        raise ce

def is_file(src):
    if os.path.isfile(src):
        return True
    
def copy_src_dest(src, dest):

    if os.path.isdir(src):
        final_dest = os.path.join(dest, os.path.basename(src)) if os.path.isdir(dest) else dest

        try:
            shutil.copytree(src, final_dest)
        except FileExistsError:
            raise CustomError(ErrorType.INVALID_COMMAND, f"Destination '{final_dest}' already exists.")
        except Exception as e:
            raise CustomError(ErrorType.UNKNOWN_ERROR, f"Failed to copy directory: {str(e)}")
    else:
        try:
            shutil.copy(src, dest)
        except Exception as e:
            raise CustomError(ErrorType.UNKNOWN_ERROR, f"Failed to copy file: {str(e)}")


def move_src_dest(src, dest):
    if os.path.exists(dest) and os.path.isdir(dest):
        final_dest = os.path.join(dest, os.path.basename(src))
    else:
        final_dest = dest
    try:
        shutil.move(src, final_dest)
    except Exception as e:
        raise CustomError(ErrorType.UNKNOWN_ERROR, f"Failed to move '{src}' to '{dest}': {str(e)}")

def delete_src(src):
    if os.path.isfile(src):
        os.remove(src)
    else:
        shutil.rmtree(src)