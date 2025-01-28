from together import Together
from dotenv import load_dotenv
import os
import base64

# Load the .env file
load_dotenv()

# Access the variable
api_key = os.getenv("TOGETHER_API_KEY")
if not api_key:
    raise ValueError("TOGETHER_API_KEY environment variable is not set in the .env file.")

# Initialize the Together client with the API key
client = Together(api_key=api_key)

# Generate an image using the Together API
response = client.images.generate(
    prompt="A cat drinking coffee and behind have a beautiful sunset over a mountain range",  # Replace with your desired prompt
    model="black-forest-labs/FLUX.1-schnell-Free",
    width=1024,
    height=768,
    steps=1,
    n=1,
    response_format="b64_json"
)

# Decode the base64-encoded image and save it as a file
image_data = response.data[0].b64_json
image_bytes = base64.b64decode(image_data)

# Save the image to a file
output_path = "generated_image.png"
with open(output_path, "wb") as image_file:
    image_file.write(image_bytes)

print(f"Image saved to {output_path}")


