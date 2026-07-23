import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from loop_node import SimpleForLoop, SimpleForLoopRange


class SimpleForLoopTests(unittest.TestCase):
    def test_count(self):
        self.assertEqual(SimpleForLoop().execute(5), ([0, 1, 2, 3, 4],))

    def test_invalid_count(self):
        with self.assertRaisesRegex(ValueError, "at least 1"):
            SimpleForLoop().execute(0)


class SimpleForLoopRangeTests(unittest.TestCase):
    def test_positive_range(self):
        self.assertEqual(
            SimpleForLoopRange().execute(0, 10, 3),
            ([0, 3, 6, 9],),
        )

    def test_empty_positive_ranges(self):
        for start, stop in ((5, 5), (10, 0)):
            with self.subTest(start=start, stop=stop):
                with self.assertRaisesRegex(ValueError, "stop > start"):
                    SimpleForLoopRange().execute(start, stop, 1)

    def test_negative_range(self):
        self.assertEqual(
            SimpleForLoopRange().execute(10, 0, -3),
            ([10, 7, 4, 1],),
        )

    def test_empty_negative_range(self):
        with self.assertRaisesRegex(ValueError, "stop < start"):
            SimpleForLoopRange().execute(0, 10, -1)

    def test_zero_step(self):
        with self.assertRaisesRegex(ValueError, "must not be 0"):
            SimpleForLoopRange().execute(0, 10, 0)

    def test_negative_bounds(self):
        self.assertEqual(
            SimpleForLoopRange().execute(-4, 3, 2),
            ([-4, -2, 0, 2],),
        )


if __name__ == "__main__":
    unittest.main()
