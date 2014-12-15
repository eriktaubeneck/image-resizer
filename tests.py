from main import crop_coordinates
from unittest import TestCase


class ResizeTestCase(TestCase):
    def test_crop_coordinates(self):
        self.assertEquals(
            crop_coordinates((1000, 1000), (200, 200)),
            (0, 0, 1000, 1000))
        self.assertEquals(
            crop_coordinates((1000, 1500), (200, 200)),
            (0, 250, 1000, 1250))
        self.assertEquals(
            crop_coordinates((1500, 1000), (200, 200)),
            (250, 0, 1250, 1000))
        self.assertEquals(
            crop_coordinates((1000, 1000), (200, 300)),
            (167, 0, 833, 1000))
        self.assertEquals(
            crop_coordinates((1000, 2000), (200, 300)),
            (0, 250, 1000, 1750))
        self.assertEquals(
            crop_coordinates((2000, 1000), (200, 300)),
            (667, 0, 1333, 1000))
        self.assertEquals(
            crop_coordinates((1000, 1000), (300, 200)),
            (0, 167, 1000, 833))
        self.assertEquals(
            crop_coordinates((1000, 2000), (300, 200)),
            (0, 667, 1000, 1333))
        self.assertEquals(
            crop_coordinates((2000, 1000), (300, 200)),
            (250, 0, 1750, 1000))

        self.assertEquals(
            crop_coordinates((4510, 2995), (2000, 1000)),
            (0, 370, 4510, 2625))
        self.assertEquals(
            crop_coordinates((4510, 2995), (2500, 1000)),
            (0, 596, 4510, 2400))
        self.assertEquals(
            crop_coordinates((4510, 2995), (2500, 2000)),
            (383, 0, 4127, 2995))
