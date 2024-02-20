from telebot import TeleBot
import google.generativeai as genai
import PIL.Image
from io import BytesIO

bot = TeleBot("6384034441:AAH9mTBkUTIRdExjeS2dFs3WY4yr5RC7yVo")
genai.configure(api_key="AIzaSyCsbDluFtfIiCzxnUljPpH4R2Nse5l9c-c")
model = genai.GenerativeModel('gemini-pro-vision')

@bot.message_handler(commands=['start'])
def handle_first_message(message):
    bot.send_message(message.chat.id, "Welcome to the image description bot! Please send me a photo to analyze.")

@bot.message_handler(content_types=['photo'])
def handle_image_message(message):
    # Send a loading message
    loading_message = bot.send_message(message.chat.id, "Processing the image, please wait...")

    global img

    try:
        image_file = bot.get_file(message.photo[-1].file_id)
        image_data = bot.download_file(image_file.file_path)
        img = PIL.Image.open(BytesIO(image_data))

        # Create Gemini Pro Vision request object
        response = model.generate_content(["Describe the photo.", img], stream=True)
        response.resolve()
        image_description = response.text

        # Check for the presence of specific elements in the description
        presence_info = check_presence(image_description)

        # Send the answer directly without displaying the prompt to the user
        bot.send_message(message.chat.id, presence_info)

        # Continue with any additional processing or handling as needed...

    except Exception as e:
        # Handle any errors that might occur during image processing
        bot.send_message(message.chat.id, f"Error processing the image: {str(e)}")

    finally:
        # Remove the loading message
        bot.delete_message(message.chat.id, loading_message.message_id)

# Function to check the presence of specific elements in the image description
def check_presence(description):
    # Replace this with your logic based on the image description
    # For example, you can use keywords in the description to determine presence
    if "dust" in description.lower():
        return "The photo contains dust."
    elif "snow" in description.lower():
        return "The photo contains snow."
    elif "damage" in description.lower():
        return "The photo contains damage."
    elif "burning" in description.lower():
        return "The photo contains burning."
    else:
        return "No specific elements detected in the photo."

# Start polling
bot.polling()
