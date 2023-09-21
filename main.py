"""from kivy.app import App
from ui_components import MainLayout
from gallery_access import open_filechooser
from audio_feedback import speak_text
from object_detection import process_image
from voice_commands import get_voice_command

class MainApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    MainApp().run()
"""
""""
from kivy.app import App
from kivy.logger import Logger
from ui_components import MainLayout
from gallery_access import open_filechooser
from audio_feedback import speak_text
from object_detection import process_image
from voice_commands import get_voice_command

class MainApp(App):

    def build(self):
        return MainLayout()

    def on_start(self):
        Kommentar 
        This method is called when the app starts.
        Use this to provide any initial feedback or setup.
       
        speak_text("Welcome to the Image Accessibility App. Please select an image or use voice commands.")

    def handle_image_selection(self, *args):
        
        Kommentar
        Handle the event when an image is selected.
       
        try:
            image_path = open_filechooser()
            detected_objects = process_image(image_path)
            feedback_message = f"Detected objects are: {', '.join(detected_objects)}"
            speak_text(feedback_message)
        except Exception as e:
            Logger.error(f"Error during image selection: {e}")
            speak_text("Sorry, an error occurred while processing the image.")

    # Add more handlers for other events or functionalities as needed.


"""

from kivy.app import App
from main_layout import MainLayout  # Import the MainLayout you created

class MainApp(App):

    def build(self):
        return MainLayout()

if __name__ == "__main__":
    MainApp().run()