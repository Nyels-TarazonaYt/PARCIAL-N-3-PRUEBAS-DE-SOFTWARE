import unittest
import tkinter as tk
from video_player import VideoPlayer

class TestVideoPlayerDecisionTable(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = VideoPlayer(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_no_video_no_action(self):
        self._simulate_button_clicks(load=False, play=False, pause=False)
        self.assertFalse(self.app.is_playing)
        self.assertIsNone(self.app.video_file)

    def test_no_video_play(self):
        self._simulate_button_clicks(load=False, play=True, pause=False)
        self.assertFalse(self.app.is_playing)
        self.assertIsNone(self.app.video_file)

    def test_video_loaded_no_action(self):
        self._simulate_button_clicks(load=True, play=False, pause=False)
        self.assertFalse(self.app.is_playing)
        self.assertIsNotNone(self.app.video_file)

    def test_video_loaded_play(self):
        self._simulate_button_clicks(load=True, play=True, pause=False)
        self.assertTrue(self.app.is_playing)
        self.assertIsNotNone(self.app.video_file)

    def test_video_loaded_play_pause(self):
        self._simulate_button_clicks(load=True, play=True, pause=True)
        self.assertFalse(self.app.is_playing)
        self.assertIsNotNone(self.app.video_file)

    def test_video_loaded_pause_no_play(self):
        self._simulate_button_clicks(load=True, play=False, pause=True)
        self.assertFalse(self.app.is_playing)
        self.assertIsNotNone(self.app.video_file)

    def _simulate_button_clicks(self, load, play, pause):
    
        if load:
            self.app.video_file = "image_640x480.png" 
            self.app.display_image(self.app.video_file)

        if play:
            self.app.play_video()

        if pause:
            self.app.pause_video()

if __name__ == "__main__":
    unittest.main()
