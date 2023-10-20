from kivy.uix.boxlayout import BoxLayout
from audio_feedback import voice_output

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Assuming you have a method to check if it's the user's first time
        if self.is_first_time_user():
            self.show_tutorial()
        # Here you can add other UI components to your main layout

    def is_first_time_user(self):
        # Mock logic, should be replaced with actual logic to check if it's the user's first time
        return True

    """
    def show_tutorial(self):
        voice_output("This is the tutorial. Here are the app's functions...")
    """


"""
class MainLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)

        # Bind the gesture recognition logic to the touch move event
        Window.bind(on_touch_move=self.on_touch_move)

    def on_touch_move(self, instance, touch):
        if touch.dx > 40:  # For instance, a right swipe
            open_gallery()


class MainLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)

        # Use the actual name of your image file here
        self.image_widget = TouchableImage(source='office.jpg')
        self.add_widget(self.image_widget)

        # For demonstration, adding a button to open gallery
        btn = Button(text="Open Gallery")
        btn.bind(on_press=self.open_gallery)
        self.add_widget(btn)

    def open_gallery(self, instance):
        # Handle gallery opening logic here
        pass
"""