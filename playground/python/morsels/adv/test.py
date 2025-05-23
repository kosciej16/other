from collections.abc import Generator
from functools import partial
import sys
from timeit import timeit
import unittest


from float_range import float_range


class FloatRangeTests(unittest.TestCase):

    """Tests for float_range."""

    def test_has_iterability(self):
        self.assertEqual(list(float_range(1, 11, 2)), [1, 3, 5, 7, 9])
        self.assertEqual(
            list(float_range(0.5, 7, 0.75)),
            [0.5, 1.25, 2.0, 2.75, 3.5, 4.25, 5.0, 5.75, 6.5]
        )

    def test_optional_step(self):
        self.assertEqual(list(float_range(1, 6, 1)), [1, 2, 3, 4, 5])
        self.assertEqual(list(float_range(1, 6)), [1, 2, 3, 4, 5])
        self.assertEqual(
            list(float_range(0.5, 6)),
            [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
        )

    def test_optional_start(self):
        self.assertEqual(list(float_range(0, 6)), [0, 1, 2, 3, 4, 5])
        self.assertEqual(list(float_range(6)), [0, 1, 2, 3, 4, 5])
        self.assertEqual(
            list(float_range(4.2)),
            [0, 1, 2, 3, 4]
        )

    def test_string_representation(self):
        self.assertEqual(str(float_range(0, 6, 0.5)), "float_range(0, 6, 0.5)")
        self.assertEqual(repr(float_range(0, 6)), "float_range(0, 6, 1)")

    def test_fractional_step_size(self):
        self.assertEqual(
            list(float_range(1, 6, 0.5)),
            [1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
        )
        self.assertEqual(
            list(float_range(1, 5.6, 0.5)),
            [1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
        )

    def test_negative_step(self):
        with self.assertRaises(StopIteration):
            # Should be empty so StopIteration should be raised
            next(iter(float_range(1, 6, -1)))
        self.assertEqual(list(float_range(5, 0, -1)), [5, 4, 3, 2, 1])
        self.assertEqual(
            list(float_range(0.5, 6)),
            [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
        )
        self.assertEqual(
            list(float_range(6, 1, -0.5)),
            [6, 5.5, 5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5]
        )

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            float_range()

    def test_too_many_arguments(self):
        with self.assertRaises(TypeError):
            float_range(0, 5, 1, 1)
        with self.assertRaises(TypeError):
            float_range(0, 5, 1, 1, 1)

    def test_no_memory_used(self):
        """Make sure float_range response isn't a giant list of numbers."""
        response = float_range(0, 1024, 2**-4)
        if isinstance(response, Generator):
            next(response)
            size = sum(
                sys.getsizeof(obj)
                for obj in response.gi_frame.f_locals.values()
            )
        else:
            size = sys.getsizeof(response)
        self.assertLess(size, 8000, 'Too much memory used')
        self.assertNotEqual(type(response), list)
        self.assertNotEqual(type(response), tuple)

    def test_can_be_looped_over_multiple_times(self):
        expected = [0.5, 1.25, 2.0, 2.75, 3.5, 4.25, 5.0, 5.75, 6.5]
        output = float_range(0.5, 7, 0.75)
        self.assertEqual(list(output), list(output))
        self.assertEqual(list(output), expected)

    def test_has_length(self):
        time = partial(timeit, globals=globals(), number=30)
        small = time("assert len(float_range(1)) == 1")
        big = time("assert len(float_range(1000)) == 1000")
        self.assertLess(big, small*500, "Timing shouldn't grow with size")

        self.assertEqual(len(float_range(100)), 100)
        self.assertEqual(len(float_range(1, 100)), 99)
        self.assertEqual(len(float_range(1, 11, 2)), 5)
        self.assertEqual(len(float_range(1, 11, -10)), 0)
        self.assertEqual(len(float_range(0.5, 7, 0.75)), 9)
        self.assertEqual(len(float_range(0.5, 7, 0.75)), 9)
        self.assertEqual(len(float_range(1000000)), 1000000)
        self.assertEqual(len(float_range(11, 1.2, -2)), 5)
        self.assertEqual(len(float_range(11, 1.2, 2)), 0)
        r = float_range(1, 6, 0.5)
        self.assertEqual(
            list(r),
            [1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
        )
        self.assertEqual(
            list(r),
            [1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_can_be_indexed_and_reversed(self):
        # Indexing
        r = float_range(0.5, 7, 0.75)
        self.assertEqual(r[0], 0.5)
        self.assertEqual(r[1], 1.25)
        self.assertEqual(r[3], 2.75)
        self.assertEqual(r[6], 5.0)
        self.assertEqual(r[8], 6.5)
        self.assertEqual(r[-1], 6.5)
        self.assertEqual(r[-3], 5.0)
        self.assertEqual(r[-6], 2.75)
        self.assertEqual(r[-9], 0.5)
        with self.assertRaises(IndexError):
            r[9]
        with self.assertRaises(IndexError):
            r[-10]
        self.assertEqual(float_range(5, 0, -1)[1], 4)

        # Reversing
        r = reversed(float_range(0.5, 7, 0.75))
        self.assertEqual(
            list(r),
            [6.5, 5.75, 5.0, 4.25, 3.5, 2.75, 2.0, 1.25, 0.5]
        )
        big_num = 1000000
        self.assertEqual(next(reversed(float_range(big_num))), big_num-1)

    # @unittest.expectedFailure
    def test_equality(self):
        time = partial(timeit, globals=globals(), number=100)
        small = time(
            "assert float_range(0, 9.5, 1) == float_range(0, 10, 1)"
        )
        big = time(
            "assert float_range(0, 5000.5, 1) == float_range(0, 5000.2, 1)"
        )
        self.assertLess(big, small*50, "Timing shouldn't grow with size")
        self.assertEqual(float_range(0, 5, 0.5), float_range(0, 5, 0.5))
        self.assertEqual(float_range(5, 5), float_range(10, 10))
        self.assertEqual(float_range(5, 11, 5), float_range(5, 12, 5))
        self.assertEqual(float_range(10), float_range(0, 10))
        self.assertNotEqual(
            float_range(0, 2**10, 2**-10),
            float_range(0, 2**10+1, 2**-10),
        )
        self.assertEqual(float_range(1000000), range(1000000))
        self.assertEqual(range(1000000), float_range(1000000))
        self.assertFalse(float_range(0, 5, 0.5) != float_range(0, 5, 0.5))
        class EqualToEverything:
            def __eq__(self, other):
                return True
        self.assertEqual(float_range(1000000), EqualToEverything())
        self.assertEqual(float_range(0, 5, 3), float_range(0, 4, 3))
        self.assertEqual(float_range(0, 0.3, 0.5), float_range(0, 0.4, 1.5))
        self.assertNotEqual(float_range(0, 11, 0.5), float_range(0, 11, 1.5))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_can_be_sliced_and_supports_equality(self):
        r = float_range(0.5, 7, 0.75)
        t = float_range(0, 524288, 2**-4)
        self.assertEqual(list(r[0:2]), [0.5, 1.25])
        self.assertEqual(list(r[:2]), [0.5, 1.25])
        self.assertEqual(list(r[-3:]), [5.0, 5.75, 6.5])
        self.assertEqual(list(r[-100:0]), [])
        self.assertEqual(list(r[-1:100]), [6.5])
        self.assertEqual(list(r[::2]), [0.5, 2.0, 3.5, 5.0, 6.5])
        self.assertEqual(list(r[len(r)::]), [])
        self.assertEqual(list(t[:3]), [0, 0.0625, 0.125])


if __name__ == "__main__":
    unittest.main(verbosity=2)
