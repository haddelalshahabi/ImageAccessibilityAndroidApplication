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


"""
class TouchableImage(Image):

    def on_touch_down(self, touch):
        # For now, just navigate to the next image on touch
        GalleryAccess.navigate_images("next", "touch")

    def on_touch_move(self, touch):
        # Handle swipe gestures
        if touch.dx > 10:  # Swipe right
            GalleryAccess.navigate_images("previous", "voice")  # Changed mode to "voice"
        elif touch.dx < -10:  # Swipe left
            GalleryAccess.navpythoigate_images("next", "voice")  # Changed mode to "voice"

    def on_touch_up(self, touch):
        # Handle double-tap for detailed description
        if touch.is_double_tap:
            detailed_description = ObjectDetection.get_detailed_description(self.source)
            # Display detailed_description in a text box for deaf users

"""