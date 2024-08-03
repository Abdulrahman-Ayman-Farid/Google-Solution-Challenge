# Solar Cell Defect Detection

This project aims to detect defects in solar cell images using AI. The defect detection is powered by Google's Generative AI (Gemini Pro Vision) and integrated with a Telegram bot for real-time alerts.

## Prerequisites

- Python 3.9
- Installing the dependencies(Libraries) mentioned below.

## Telegram Bot Integration

- This project includes a Telegram bot for testing our prototype.
- You'll need your `Telegram API` to insert it in the code
- The Code Include the `API Token` for our bot in the telegram app.
- It Includes Our `API Key` for the Gemini pro vision.

## How to Run and Use

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Abdulrahman-Ayman-Farid/SolScan.git
    ```

2. **Install dependencies:**
    ```bash
    pip3 install telebot
    pip3 install -q -U google-generativeai
    pip3 install Pillow
    ```

3. **Run the script:**
   - Run the script by installing the dependencies and running the main.py file


4. **Search for the Telegram Bot:**
    - After running the script,Search in the telegram app by the name : SOLSCAN.xbot
    - Or just open the link "https://t.me/SOLSCAN_xbot"
    


5. **Send a Solar Panel photo to the bot without writing any text or prompt and it shall tell you whether the solar panel is working properly or it contains a defect:** 
    

## Alert System

- The script sends alerts upon finding a deffect to the user trying it with the specific type of defect detected in the image entered.
- Also we simulated the idea of alert system by adding a feature in our script that enables us to choose a user to be admin(by putting his chat id) This user also will get the image entered by the other user trying the prototype and also will recieve the alert upon this photo. You can try this feature by entering a different telegram chat id(not the same chat ID trying the prototype) in the script by Configuring the recipient's chat ID in the `another_user_chat_id` variable in the `main.py` script.

## Notes
- Our Bot doesn't support text messages as inputting images only and getting the output ready makes the bot smarter.
- Only send the desired Photo without Entering any Prompt.
- You must run the python script while trying the bot as the bot is programmed with this script.
