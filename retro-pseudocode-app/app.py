# app.py

import os
import google.generativeai as genai
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# --- Gemini API Configuration ---
# It's best practice to use environment variables for API keys
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    # A more user-friendly error handling
    print("Error: GOOGLE_API_KEY not found in environment variables.")
    print("Please create a .env file and add your key: GOOGLE_API_KEY='Your-API-Key'")
    # In a real app, you might want to handle this more gracefully
    # For this example, we'll allow it to raise an error if genai.configure fails.

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"Failed to configure GenerativeAI: {e}")
    # The application might not function correctly without the model.
    # We'll let it run so the user can see the front-end,
    # but the generation will fail.
    model = None


def generate_pseudocode(python_code):
    """
    Sends the Python code to the Gemini API and returns the generated pseudocode.
    """
    if not model:
        return "Error: Generative model is not configured. Check API key."
    
    # The prompt is carefully crafted to get the desired output format.
    prompt = f"""
    You are a pseudocode generator. 
    Your task is to read the given Python code and output clear, structured pseudocode. 
    
    Guidelines:
    - Write in plain English, not Python syntax.  
    - Use indentation for loops and blocks.  
    - Be concise but cover all logic.  
    - Do not add explanations, titles, or any text other than the pseudocode itself.  
    
    Here is the Python code:
    ```python
    {python_code}
    ```

    Now generate the pseudocode:
    """
    
    try:
        response = model.generate_content(prompt)
        # We add a bit of error handling for the response
        if response.text:
            return response.text.strip()
        else:
            return "Error: Received an empty response from the model."
    except Exception as e:
        print(f"An error occurred during API call: {e}")
        return f"An error occurred while generating pseudocode: {e}"


@app.route('/', methods=['GET', 'POST'])
def home():
    python_code = ""
    pseudocode = ""

    if request.method == 'POST':
        python_code = request.form.get('code_input')
        if python_code:
            pseudocode = generate_pseudocode(python_code)

    return render_template('index.html', python_code=python_code, pseudocode=pseudocode)


if __name__ == '__main__':
    # Using debug=True is great for development, but should be False in production
    app.run(debug=True)