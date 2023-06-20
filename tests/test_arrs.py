
from utils import arrs
import unittest


class TestFunctions(unittest.TestCase):

    def test_get_existing_index(self):
        array = [1, 2, 3, 4, 5]
        index = 2
        result = arrs.get(array, index)
        self.assertEqual(result, 3)



    def test_get_negative_index(self):
        array = [1, 2, 3, 4, 5]
        index = -1
        default = None
        result = arrs.get(array, index)
        self.assertEqual(result, default)

    def test_my_slice_with_start_and_end(self):
        coll = [1, 2, 3, 4, 5]
        start = 1
        end = 4
        result = arrs.my_slice(coll, start, end)
        self.assertEqual(result, [2, 3, 4])

    def test_my_slice_with_start(self):
        coll = [1, 2, 3, 4, 5]
        start = 2
        result = arrs.my_slice(coll, start)
        self.assertEqual(result, [3, 4, 5])

    def test_my_slice_with_negative_start(self):
        coll = [1, 2, 3, 4, 5]
        start = -3
        result = arrs.my_slice(coll, start)
        self.assertEqual(result, [3, 4, 5])

    def test_my_slice_with_end(self):
        coll = [1, 2, 3, 4, 5]
        end = 3
        result = arrs.my_slice(coll, end=end)
        self.assertEqual(result, [1, 2, 3])

    def test_my_slice_with_negative_end(self):
        coll = [1, 2, 3, 4, 5]
        end = -2
        result = arrs.my_slice(coll, end=end)
        self.assertEqual(result, [1, 2, 3])

    def test_my_slice_empty_list(self):
        coll = []
        result = arrs.my_slice(coll)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()









