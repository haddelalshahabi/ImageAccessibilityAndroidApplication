from kivy.uix.image import Image


class TouchableImage(Image):
    def on_touch_move(self, touch):
        # Check for horizontal swipe (right)
        if touch.dx > 40:
            # Logic to show the next image
            pass
        # Check for vertical swipe (up)
        if touch.dy > 40:
            # Logic to go back to main gallery
            pass
