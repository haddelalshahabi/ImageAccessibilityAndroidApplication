from audio_feedback import AudioFeedback
from object_detection import ObjectDetection
from voice_commands import VoiceCommands


class GalleryAccess:
    current_image_index = 0
    images = []  # List of image paths

    @classmethod
    def navigate_images(cls, direction, mode="voice"):
        if direction == "next":
            cls.current_image_index += 1
        elif direction == "previous":
            cls.current_image_index -= 1

        # Ensure we don't go out of bounds
        cls.current_image_index = max(0, min(cls.current_image_index, len(cls.images) - 1))

        # Return the current image path
        current_image = cls.images[cls.current_image_index]

        # If using voice, describe the image
        if mode == "voice":
            description = ObjectDetection.get_image_description(current_image)
            AudioFeedback.speak(description)

        # Ask user for more details
        command = VoiceCommands.on_voice_command()
        if command == "yes":
            detailed_description = ObjectDetection.get_detailed_description(current_image)
            AudioFeedback.speak(detailed_description)
        elif command in ["go to the next image", "next"]:
            cls.navigate_images("next", "voice")
        elif command in ["go to the previous image", "previous"]:
            cls.navigate_images("previous", "voice")

"""
def open_gallery():
    filechooser = FileChooserIconView(path='/path_to_gallery/')
    # Here you can add further logic to display images and handle the file chosen

def open_filechooser():
    file_path = filechooser.open_file()
    return file_path

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def capture_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            return command
        except sr.UnknownValueError:
            return "Sorry, I did not get that."
        except sr.RequestError:
            return "API unavailable."
"""