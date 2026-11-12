import unittest
from organizer import categorize_file

class CategorizeFileTests(unittest.TestCase):
    def test_image_extension_is_case_insensitive(self):
        self.assertEqual(categorize_file("photo.JPG"), "Images")
    def test_audio_file(self):
        self.assertEqual(categorize_file("song.mp3"), "Audio")
    def test_unknown_extension(self):
        self.assertEqual(categorize_file("file.xyz"), "Other")

if __name__ == "__main__":
    unittest.main()