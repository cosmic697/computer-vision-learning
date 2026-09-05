import unittest
import numpy as np

from image_processor.edges import (
    detect_edges,
)

class TestEdges(unittest.TestCase):

    def setUp(self):
        self.gray_image = np.zeros((400, 600),dtype=np.uint8)

    def test_detect_edges(self):
        edges = detect_edges(self.gray_image,100,200)

        self.assertIsInstance(edges,np.ndarray)

        self.assertEqual(edges.shape,self.gray_image.shape)

    def test_detect_edges_none(self):
        with self.assertRaises(ValueError):
            detect_edges(None,100,200)

    def test_invalid_lower_threshold(self):
        with self.assertRaises(ValueError):
            detect_edges(self.gray_image,-1,200)

    def test_invalid_upper_threshold(self):
        with self.assertRaises(ValueError):
            detect_edges(
                self.gray_image,100,300)


if __name__ == "__main__":
    unittest.main()