from kivy.uix.image import Image

class TouchableImage(Image):

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            # This means the touch occurred within the boundaries of this Image widget.
            print("Image touched at position:", touch.pos)
            # Here, you'd typically call some function to identify the object at touch.pos and provide audio feedback.
            return True
        return super(TouchableImage, self).on_touch_down(touch)
