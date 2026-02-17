from google.genai import types
from .get_files_info import get_files_info
from .run_python_file import run_python_file
from .get_file_content import get_file_content, write_file


working_directory = "calculator"

def call_function(function_call, verbose=False):
    if verbose:
        print(f"Calling function: {function_call.name} with arguments: {function_call.args}")
    else:
        print(f" - Calling function: {function_call.name}")
    function_map = {
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "get_file_content": get_file_content,
        "write_file": write_file
    }
    function_name = function_call.name
    
    if function_name is None:
        return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_call.name}"},
            )
        ],
    )
    args = dict(function_call.args) if function_call.args else {}
    
    
    if function_call.name == "get_files_info":
        function_result = get_files_info(working_directory, **args)  
    if function_call.name == "run_python_file":
        function_result = run_python_file(working_directory, **args)
    if function_call.name == "get_file_content":     
       function_result = get_file_content(working_directory, **args)
    if function_call.name == "write_file":
        function_result = write_file(working_directory, **args)     
        
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                #Because from_function_response requires the response to be a dictionary, we just shove the string result into a "result" field.
                response={"result": function_result},
                )
            ],
        )  
                