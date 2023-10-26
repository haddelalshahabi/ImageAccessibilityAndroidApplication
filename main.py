from kivy.app import App
from main_layout import MainLayout
from audio_feedback import start_app_voice_guide
from voice_commands import recognize_and_handle_command


class AudioVisionApp(App):
    def build(self):
        start_app_voice_guide()  # Start Google Talk to guide users
        # Optional: Start voice command recognition
        recognize_and_handle_command()
        return MainLayout()


if __name__ == '__main__':
    AudioVisionApp().run()
