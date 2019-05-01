import unittest
import reduce_file_path as rfp

class TestReduceFilePath(unittest.TestCase):
    def test_when_path_is_passed_then_return_it_reduced(self):
        path = "/srv/./././././"
        exp = "/srv"

        self.assertEqual(rfp.reduce_file_path(path), exp)

if __name__ == "__main__":
    unittest.main()