import speech_recognition as sr

def listen_to_user():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = r.listen(source)
        try:
            text = r.recognize_google(audio_data)
            if 'open gallery' in text.lower():
                open_gallery()
        except:
            # Handle exceptions (e.g., re-prompt the user or handle other commands)
            pass


"""
def get_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)
    
"""

"""
import speech_recognition as sr

def capture_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for a command:")
        audio = recognizer.listen(source)

        try:
            command_text = recognizer.recognize_google(audio)
            print(f"Recognized command: {command_text}")
            return command_text.lower()  # Converting to lower case for easy comparison

        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None


def interpret_command(command):
    if command:
        if "open gallery" in command:
            return "open_gallery"
        elif "describe image" in command:
            return "describe_image"
        elif "help" in command:
            return "show_help"
        # Add more elif conditions to handle additional voice commands
        else:
            print("Command not recognized.")
            return None
    else:
        return None

"""