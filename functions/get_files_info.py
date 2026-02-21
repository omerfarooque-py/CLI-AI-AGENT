import os
from google.genai import types
def get_files_info(working_directory, directory="."):
    #absolute path of the working directory
  working_dir_abs = os.path.abspath(working_directory)
  #
  target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
  valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
  
  if not valid_target_dir:
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
  if not target_dir:
     return f'Error: "{directory}" is not a directory'
   
  contents = os.listdir(target_dir)
  response = " "
  try:
     for content in contents:
       name = content
       size = os.path.getsize(os.path.join(target_dir, content))
       is_dir = os.path.isdir(os.path.join(target_dir, content))
       response += f'{name}: file_size={size}, bytes, is_dir={is_dir}\n'
        
  except Exception as e:
       return f"Error: {str(e)}"
  return response
  
  
  
  
  
  
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)



schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes content to a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file as a string",
            ),
        },
      
    ),
)


