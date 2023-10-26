import speech_recognition as sr
from audio_feedback import voice_output


def recognize_and_handle_command():
    """
    Recognize voice command and handle it accordingly.
    """
    command = recognize_voice_command()
    if command:
        # Here you can add conditions to handle specific commands
        # For example: navigate to a specific folder, open settings, etc.
        voice_output(f"You said: {command}")
    else:
        voice_output("Sorry, I could not understand your command. Please try again.")


def recognize_voice_command():
    """
    Recognize voice command using Google Speech Recognition.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        voice_output("Please say your command.")
        audio_data = r.listen(source)
        try:
            text = r.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return None
