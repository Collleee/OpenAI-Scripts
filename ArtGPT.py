import openai
import requests
from PIL import Image
from io import BytesIO
from art import text2art
from datetime import datetime

# Create the banner text
banner_text = text2art("ArtGPT")

# Initialize the OpenAI API client
openai.api_key = 'your_api_key'

# Function to generate an image using OpenAI and return the image and prompt
def generate_image(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,  # Number of images to generate
            size="1024x1024"  # Size of the generated image
        )
        image_url = response['data'][0]['url']

        # Fetch the image
        image_response = requests.get(image_url)
        img = Image.open(BytesIO(image_response.content))

        return img, prompt

    except Exception as e:
        print(f"Error: {e}")
        return None, None

def main():
    conversation = []

    print("\n" * 5)  # Add initial spacing before any text shows up
    print(banner_text)
    print("I'm your artist, ask me to draw anything.\n")

    while True:
        user_input = input("Generate an image of ")
        if user_input.lower() == 'exit':
            break

        img, text = generate_image(user_input)
        if img and text:
            img.show()
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"\nImage generated on: {current_time}")
            print("\n" * 3)  # Add spacing after displaying the image and time
            conversation.append(f"Master: {user_input}\n\nAI: Generated an image based on the description '{user_input}'\nGenerated on: {current_time}\n\n")
    
    # Save the conversation to a text file
    with open("conversation.txt", 'w', encoding='utf-8') as file:
        for line in conversation:
            file.write(line)

    print("Conversation saved to conversation.txt")

if __name__ == "__main__":
    main()
