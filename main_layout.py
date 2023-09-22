from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from touchable_image import TouchableImage  # Import the custom widget you created
from kivy.core.window import Window
from gallery_access import open_gallery


class MainLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)

        # Bind the gesture recognition logic to the touch move event
        Window.bind(on_touch_move=self.on_touch_move)

    def on_touch_move(self, instance, touch):
        if touch.dx > 40:  # For instance, a right swipe
            open_gallery()


"""
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