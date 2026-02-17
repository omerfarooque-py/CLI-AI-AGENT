import os
from google.genai import types

def get_file_content(working_directory, file_path):
    
    absolute_working_directory = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(os.path.join(absolute_working_directory, file_path))
    valid_target_file = os.path.commonpath([absolute_working_directory, target_file_path])
    if valid_target_file != absolute_working_directory:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    response = ""
    try:
        with open(target_file_path, 'r') as file:
            response = file.read(10000)
            MAX_CHARS = len(response) 
            # Read up to 10,000 characters     
    except Exception as e:
        return f"Error: {str(e)}"
    print(f"Content of '{response}':")
    if len(response) == 10000:
        response += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    print(response)
get_file_content("calculator", "lorem.txt")


def write_file(working_directory, file_path, content):
    
    absolute_working_directory = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(os.path.join(absolute_working_directory, file_path))
    valid_target_file = os.path.commonpath([absolute_working_directory, target_file_path])
    if valid_target_file != absolute_working_directory:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    is_dir = os.path.isdir(target_file_path)
    if os.path.exists(target_file_path) and is_dir:
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    if not valid_target_file:
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
        print(f'Created directories for "{file_path}"')
    try:
        with open(target_file_path, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"
    
  
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="reads content of a specified file relative to the working directory, providing the content of the file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={ 
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to the file to read, relative to the working directory",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Name of the file to read",
            ),
        },
        
    ),
)
