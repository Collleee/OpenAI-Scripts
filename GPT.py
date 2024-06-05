import openai
import clipboard

# Replace with your OpenAI API key
openai.api_key = 'your_api_key'

# Function to send a message to OpenAI and receive a response
def ask_openai(prompt):
    messages = [{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or another model you prefer
            messages=messages
        )
        response_text = response.choices[0].message.content.strip()
        clipboard.set(response_text)  # Copy the response to clipboard
        print(f"AI: {response_text} (copied to clipboard)")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Get the input prompt from the clipboard
    prompt = clipboard.get().strip()
    if prompt:
        ask_openai(prompt)
    else:
        print("Clipboard is empty. Please copy some text and try again.")

if __name__ == "__main__":
    main()
