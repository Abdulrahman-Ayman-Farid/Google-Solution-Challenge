from telebot import TeleBot
import google.generativeai as genai
import PIL.Image
from io import BytesIO

bot = TeleBot("6384034441:AAH9mTBkUTIRdExjeS2dFs3WY4yr5RC7yVo")
genai.configure(api_key="AIzaSyCsbDluFtfIiCzxnUljPpH4R2Nse5l9c-c")
model = genai.GenerativeModel('gemini-pro-vision')

def check_presence(description):
    # Replace this with your logic based on the image description
    # For example, you can use keywords in the description to determine presence
    if "dust" in description.lower():
        return "Alert: The photo contains dust."
    elif "snow" in description.lower():
        return "Alert: The photo contains snow."
    elif "damage" in description.lower() or "crack" in description.lower() or "broken" in description.lower():
        return "Alert: The photo contains damage or potential issues."
    elif "burning" in description.lower() or "fire" in description.lower():
        return "Alert: The photo contains burning or fire."
    elif "shadow" in description.lower():
        return "Alert: The photo contains shadows affecting solar cells."
    elif "obstacle" in description.lower():
        return "Alert: The photo contains obstacles blocking solar cells."
    elif "corrosion" in description.lower():
        return "Alert: The photo shows signs of corrosion on solar cells."
    elif "hotspot" in description.lower():
        return "Alert: The photo indicates potential hotspots on solar cells."
    elif "discoloration" in description.lower() or "stain" in description.lower():
        return "Alert: The photo shows discoloration or stains on solar cells."
    elif "misalignment" in description.lower():
        return "Alert: The photo suggests misalignment of solar cells."
    elif "reflection" in description.lower() or "glare" in description.lower():
        return "Alert: The photo contains reflections or glare affecting solar cells."
    elif "bird droppings" in description.lower():
        return "Alert: The photo contains bird droppings on solar cells."
    elif "electrical damage" in description.lower() or "short circuit" in description.lower():
        return "Alert: The photo shows signs of electrical damage on solar cells."
    else:
        return "No specific elements detected in the photo."

# Example usage
@bot.message_handler(content_types=['photo'])
def handle_image_message(message):
    # Send a loading message
    loading_message = bot.send_message(message.chat.id, "Processing the image, please wait...")

    try:
        # Get the sender's name
        sender_name = message.from_user.first_name if message.from_user.first_name else "Unknown User"

        image_file = bot.get_file(message.photo[-1].file_id)
        image_data = bot.download_file(image_file.file_path)
        img = PIL.Image.open(BytesIO(image_data))

        # Create Gemini Pro Vision request object
        response = model.generate_content(["Describe the photo.", img], stream=True)
        response.resolve()
        image_description = response.text

        # Check for the presence of specific elements in the description
        alert_message = check_presence(image_description)

        if alert_message:
            # Send the answer directly without displaying the prompt to the user
            bot.send_message(message.chat.id, alert_message)

            # Notify another user with the sender's name in the message
            another_user_chat_id = '1415370035' 
            bot.send_message(another_user_chat_id, f"Alert: {sender_name} detected an issue in their photo.")

            # Send the photo to the user with the provided chat ID
            bot.send_photo(another_user_chat_id, img)

        
    except Exception as e:
        # Handle any errors that might occur during image processing
        bot.send_message(message.chat.id, f"Error processing the image: {str(e)}")

    finally:
        # Remove the loading message
        bot.delete_message(message.chat.id, loading_message.message_id)

# Start polling
bot.polling()
