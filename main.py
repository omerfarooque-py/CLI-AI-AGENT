import argparse
import os
from tabnanny import verbose
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import  schema_get_files_info, schema_write_file
from functions.run_python_file import schema_run_python_file
from functions.get_file_content import schema_get_file_content
from functions.call_function import call_function


def main():

    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')

    client = genai.Client(api_key = api_key)
    
    parser = argparse.ArgumentParser(description='Chatbot')
    parser.add_argument("user_prompt", type = str, help = "User prompt:")
    parser.add_argument("--verbose", action = "store_true", help = "Enable verbose output")
    args = parser.parse_args()
    
    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=args.user_prompt)]
        )
    ]
    
    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info, 
        schema_run_python_file,
        schema_get_file_content,
        schema_write_file
        ]
     )

    
    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories
        - Read file content
        - Write content to files
        - Run Python scripts

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
        """
    response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = messages,
        config=types.GenerateContentConfig(
            tools = [available_functions],
            system_instruction=system_prompt,
            temperature=0
    )
        )
    
    
    print(response.text)

    if response is None or response.usage_metadata is None:
        print("response or usage metadata has malfunctioned") 
        return
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.function_calls:
        for function_call in response.function_calls:
          function_call_result = call_function(function_call, verbose)
          print(f"Function call result: {function_call_result}")
          
    try:      
        if function_call_result.parts is not None:
          print(f"Function call result: {function_call_result}")
        if function_call_result.parts[0].response is not None and function_call_result.parts[0].response.get("result") is not None:
          print(f"Function call response: {function_call_result.parts[0].response}")   
        if args.verbose:
         print(f"-> {function_call_result.parts[0].function_response.response}")          
    except Exception as e:
        print(f"Error processing function call result: {e}")
    else:
      print(response.text)
      
    
main()

