class ImageEditor:
    def __init__(self, image: bytes):
        self.image = image

    def render(self):
        return f"Rendering {self.image}"
