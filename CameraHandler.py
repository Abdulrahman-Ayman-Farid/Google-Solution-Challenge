import cv2
import time


def capture_image():
    # Capture an image using the webcam
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    capture.release()

    # Check if capture was successful
    if ret:
        # Save the image with a timestamp
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        image_name = f"captured_image_{timestamp}.jpg"
        cv2.imwrite(image_name, frame)
        print(f"Image saved as {image_name}")
    else:
        print("Failed to capture image")


if __name__ == "__main__":
    # Infinite loop to capture image every 20 seconds
    while True:
        capture_image()
        time.sleep(20)  # Wait for 20 seconds
