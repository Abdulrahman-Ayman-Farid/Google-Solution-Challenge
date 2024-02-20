import requests
import logging
from camera_handler import CameraHandler
from image_analyzer import ImageAnalyzer
from datetime import datetime, time

# Configure logging
logging.basicConfig(filename='monitoring.log', level=logging.INFO)

# Replace with your configuration values
gemini_api_url = "https://your_gemini_api_endpoint"
gemini_api_token = "your_gemini_api_token"
capture_interval = 60  # Seconds

# Initialize camera and analyzer
camera_handler = CameraHandler()
image_analyzer = ImageAnalyzer()

def main():
    while True:
        try:
            # Capture and analyze image
            image_data, analysis_results = camera_handler.capture_and_analyze()

            # Check for damage and send data if needed
            if analysis_results.damage_detected and analysis_results.severity > 0.5:
                data = {
                    "image_data": image_data,
                    "analysis_results": analysis_results.to_dict()
                }
                send_data_to_gemini(data)
            else:
                logging.info("No significant damage detected.")

        except Exception as e:
            logging.error(f"Error occurred: {e}")

        # Wait before next capture
        time.sleep(capture_interval)

def send_data_to_gemini(data):
    headers = {"Authorization": f"Bearer {gemini_api_token}"}
    response = requests.post(gemini_api_url, json=data, headers=headers)
    if response.status_code == 200:
        logging.info("Data sent to Gemini API successfully.")
    else:
        logging.error("Error sending data to Gemini API.")

if __name__ == "__main__":
    main()
