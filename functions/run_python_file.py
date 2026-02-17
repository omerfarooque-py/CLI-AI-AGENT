import os
import subprocess

def run_python_file(working_directory, file_path, args= None):
    #absolute path of the working directory
    absolute_file_path = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(absolute_file_path, file_path))
    valid_target_file = os.path.commonpath([absolute_file_path, target_file]) == absolute_file_path
    
    if not valid_target_file:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    is_file = os.path.isfile(target_file)
    
    if not valid_target_file or not is_file:
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if target_file.endswith('.py'):
       # command = ["python",absolute_file_path]
        try:
            final_args =["python3", target_file]
            final_args.extend(args or [])
             
            CompletedProcess = subprocess.run(
                
                final_args,
                cwd=absolute_file_path,
                timeout=30,
                capture_output=True,
                text=True
            )
            final_string = f"""
STDOUT: {CompletedProcess.stdout}
STDERR: {CompletedProcess.stderr}
    """
            if CompletedProcess.stdout == "" and CompletedProcess.stderr == "":
                    final_string += "No output produced.\n"
            if CompletedProcess.returncode != 0:
                final_string += f"Script exited with return code {CompletedProcess.returncode}."
            return final_string        
        except Exception as e:
            return f"Error: executing Python file:{e}"
        
    
    else:
         return f'Error: "{file_path}" is not a Python file'   