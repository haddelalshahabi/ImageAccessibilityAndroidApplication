import speech_recognition as sr

def recognize_voice_command():
    """
    Recognize voice command using Google Speech Recognition.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = r.listen(source)
        try:
            text = r.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return None


"""
from plyer import stt
from audio_feedback import voice_output
from gallery_access import navigate_to_folder, get_images_from_folder

def listen_for_commands():
    command = stt.recognize()
    return command

def process_command(command):
    if "open gallery" in command:
        voice_output("Opening gallery...")
        # Here, you'd trigger a function to open/display the gallery in your UI.

    elif "navigate to" in command:
        folder_name = command.split("navigate to")[-1].strip()  # Extract folder name from command
        navigate_to_folder(folder_name)
        voice_output(f"Navigating to {folder_name}")

    elif "images from" in command:
        folder_name = command.split("images from")[-1].strip()  # Extract folder name from command
        images = get_images_from_folder(folder_name)
        # Here, you'd display the images or handle them as needed in your UI.
        voice_output(f"Showing images from {folder_name}")

    else:
        voice_output("Sorry, I didn't understand that command.")
"""