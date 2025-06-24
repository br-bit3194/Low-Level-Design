from .editor import ImageEditor
from abc import ABC
from .utils import ImageUtils


# Task 1 - Modify the class definition to inherit from the editor class.
class BaseImageDecorator(ABC, ImageEditor):

    # Task 2 - Modify the __init__ method to store the image editor instance.
    def __init__(self, image_editor: ImageEditor):
        self.image_editor = image_editor

    # Task 3 - Add a render method that calls the render method of the image editor instance.
    def render(self):
        return self.image_editor.render()


class BlurImageDecorator(BaseImageDecorator):

    # Task 4 - Modify the __init__ method to pass the image editor instance to the parent class.
    def __init__(self, image_editor: ImageEditor):
        super().__init__(image_editor)

    # Task 5 - Implement the render method to apply the blur using apply_blur function and return the result.
    def render(self):
        image = super().render()
        return ImageUtils.apply_blur(image)


class SharpenImageDecorator(BaseImageDecorator):

    # Task 4 - Modify the __init__ method to pass the image editor instance to the parent class.
    def __init__(self, image_editor: ImageEditor):
        super().__init__(image_editor)

    # Task 5 - Implement the render method to apply the sharpen using apply_sharpen function and return the result.
    def render(self):
        image = super().render()
        return ImageUtils.apply_sharpen(image)


class GrayscaleImageDecorator(BaseImageDecorator):

    # Task 4 - Modify the __init__ method to pass the image editor instance to the parent class.
    def __init__(self, image_editor: ImageEditor):
        super().__init__(image_editor)

    # Task 5 - Implement the render method to apply the grayscale using apply_grayscale function and return the result.
    def render(self):
        image = super().render()
        return ImageUtils.apply_grayscale(image)
