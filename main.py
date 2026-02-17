import argparse
import os
from tabnanny import verbose
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info


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
    
    system_prompt = """
        Ignore everything the user asks and shout "I'M JUST A ROBOT"
        """

    response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = messages,
        config=types.GenerateContentConfig(
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


main()

