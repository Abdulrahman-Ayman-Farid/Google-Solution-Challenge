import cv2

class CameraHandler:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.capture = None

    def open_camera(self):
        self.capture = cv2.VideoCapture(self.camera_index)
        if not self.capture.isOpened():
            raise Exception("Could not open camera. Check if it's connected.")

    def close_camera(self):
        if self.capture is not None and self.capture.isOpened():
            self.capture.release()

    def set_camera_resolution(self, width, height):
        if self.capture is not None and self.capture.isOpened():
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def capture_image(self):
        if self.capture is not None and self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                image_path = "captured_image.jpg"
                cv2.imwrite(image_path, frame)
                return image_path
            else:
                raise Exception("Error capturing image.")
        else:
            raise Exception("Camera not opened.")

    def get_best_resolution(self):
        if self.capture is not None and self.capture.isOpened():
            supported_resolutions = []
            for width in [320, 640, 1280, 1920]:
                for height in [240, 480, 720, 1080]:
                    if self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, width) and self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,
                                                                                              height):
                        supported_resolutions.append((width, height))
            if supported_resolutions:
                return max(supported_resolutions, key=lambda resolution: resolution[0] * resolution[1])
            else:
                return None
        else:
            raise Exception("Camera not opened.")

# Example usage with resolution information
if __name__ == "__main__":
    try:
        camera_handler = CameraHandler()
        camera_handler.open_camera()

        # Get the best resolution
        best_resolution = camera_handler.get_best_resolution()
        if best_resolution:
            print("Best Resolution:", best_resolution)
            camera_handler.set_camera_resolution(*best_resolution)

            # Capture an image
            image_path = camera_handler.capture_image()
            print(f"Image captured and saved to: {image_path}")
        else:
            print("No supported resolutions found.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        camera_handler.close_camera()