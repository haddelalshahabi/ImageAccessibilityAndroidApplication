"""
from kivy.app import App
from main_layout import MainLayout  # Import the MainLayout you created
from voice_commands import capture_voice_command, interpret_command  # Import the voice command functions

class MainApp(App):

    def build(self):
        return MainLayout()

    def handle_voice_command(self):
        captured_command = capture_voice_command()
        action = interpret_command(captured_command)

        if action == "open_gallery":
            # Code to open the gallery
            self.root.open_gallery(None)  # Assuming your open_gallery method in MainLayout doesn't require the 'instance' argument
        elif action == "describe_image":
            # Code to describe the currently displayed image
            pass
        elif action == "show_help":
            # Code to show help instructions
            pass
        # ... additional actions based on other voice commands

if __name__ == "__main__":
    app = MainApp()
    app.run()

"""

from kivy.app import App
from main_layout import MainLayout  # Import the MainLayout you created

class MainApp(App):

    def build(self):
        return MainLayout()

if __name__ == "__main__":
    MainApp().run()