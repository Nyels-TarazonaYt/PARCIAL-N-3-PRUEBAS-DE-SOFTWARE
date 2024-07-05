import unittest
import tkinter as tk
from PIL import Image, ImageTk
import os
from test_video_player_limit_value_analysis import VideoPlayer

class TestVideoPlayer(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = VideoPlayer(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_image_1x1(self):
        self._test_image_loading("image_1x1.png")

    def test_image_640x480(self):
        self._test_image_loading("image_640x480.png")

    def test_image_639x479(self):
        self._test_image_loading("image_639x479.png")

    def test_image_641x481(self):
        self._test_image_loading("image_641x481.png")

    def _test_image_loading(self, image_filename):
        
        self.app.video_file = image_filename
        self.app.display_image(self.app.video_file)
        
        loaded_image = self.app.photo
        
        self.assertIsNotNone(loaded_image, "La imagen no se cargó correctamente.")
        
        image = Image.open(image_filename)
        expected_size = (640, 480) if image.size[0] > 640 or image.size[1] > 480 else image.size
        self.assertEqual(loaded_image.width(), expected_size[0], "El ancho de la imagen cargada es incorrecto.")
        self.assertEqual(loaded_image.height(), expected_size[1], "El alto de la imagen cargada es incorrecto.")

if __name__ == "__main__":
    
    image_sizes = [(1, 1), (640, 480), (639, 479), (641, 481)]
    image_filenames = ["image_1x1.png", "image_640x480.png", "image_639x479.png", "image_641x481.png"]

    for size, filename in zip(image_sizes, image_filenames):
        if not os.path.exists(filename):
            image = Image.new("RGB", size, color=(255, 0, 0))
            image.save(filename)

    unittest.main()
