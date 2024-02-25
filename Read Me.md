# Solar Cell Defect Detection

This project aims to detect defects in solar cell images using AI. The defect detection is powered by Google's Generative AI (Gemini Pro Vision) and integrated with a Telegram bot for real-time alerts.

## Prerequisites

- Python 3.9

## Telegram Bot Integration

- This project includes a Telegram bot for image analysis and defect detection.
- You can configure the Telegram bot by obtaining an API key from the BotFather on Telegram.
- Update the Telegram bot API key in the `TeleBot` instantiation in the `main.py` script.

## How to Run and Use

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Abdulrahman-Ayman-Farid/SolScan.git
    ```

2. **Install dependencies (if any):**
    ```bash
    pip3 install telebot
    pip3 install -q -U google-generativeai
    pip3 install Pillow
    ```

3. **Search for the Telegram Bot:**
    - Search in the telegram app by the name : SOLSCAN.xbot
    - Or just open that link "https://t.me/SOLSCAN_xbot"

4. **Run the script:**


5. Send a Solar Panel photo and it will tell you whether the solar panel is healthy or not 
    

## Alert System

- The script sends alerts to a specified Telegram user when defects are detected in an image.
- Configure the recipient's chat ID in the `another_user_chat_id` variable in the `main.py` script.



