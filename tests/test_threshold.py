import unittest

from numena.image import image_new


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.image = image_new((16, 16))
        self.image[0:8, :] = 255
        self.image[8:, :] = 128

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == "__main__":
    unittest.main()
