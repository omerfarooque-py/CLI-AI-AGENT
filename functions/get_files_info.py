import os

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
  print(f"result for '{directory}' directory:") 
  return response
  
