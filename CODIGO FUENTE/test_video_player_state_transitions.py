import unittest
import tkinter as tk
from video_player import VideoPlayer

class TestVideoPlayerStateTransitions(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = VideoPlayer(self.root)

    def tearDown(self):
        self.root.destroy()

# Asserts
    def test_initial_state(self):

        self.assertIsNone(self.app.video_file)
        self.assertFalse(self.app.is_playing)

    def test_load_video(self):
    
        self.assertIsNone(self.app.video_file)
        self.assertFalse(self.app.is_playing)

        self._simulate_load_video("image_640x480.png")

        self.assertIsNotNone(self.app.video_file)
        self.assertFalse(self.app.is_playing)

    def test_play_video(self):
        
        self._simulate_load_video("image_640x480.png")
        
        self.app.play_video()

        self.assertTrue(self.app.is_playing)

    def test_pause_video(self):

        self._simulate_load_video("image_640x480.png")
        
        self.app.play_video()
        self.assertTrue(self.app.is_playing)


        self.app.pause_video()


        self.assertFalse(self.app.is_playing)

    def test_resume_video(self):

        self._simulate_load_video("image_640x480.png")
        

        self.app.play_video()
        self.assertTrue(self.app.is_playing)

        self.app.pause_video()
        self.assertFalse(self.app.is_playing)


        self.app.play_video()

        self.assertTrue(self.app.is_playing)

    def _simulate_load_video(self, video_path):

        self.app.video_file = video_path
        self.app.display_image(self.app.video_file)

if __name__ == "__main__":
    unittest.main()
