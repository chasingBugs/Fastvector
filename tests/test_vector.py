'''Test vector.
'''
import unittest

from fastvector import VectorND
from fastvector import computations


class VectorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.v1 = VectorND(0, 0)
        self.v2 = VectorND(-1, 1)
        self.v3 = VectorND(2.5, -2.5)

    def test_string_init(self) -> None:
        self.assertRaises(TypeError, VectorND.__init__, 'hello')

    def test_python_clipping(self) -> None:
        vec_1 = VectorND([2, 4, 6, 8, 9, 7, 5])
        vec_2 = VectorND([2, 4, 6, 8, 9, 7, 5])
        computations.python_clip_vector(vec_1, 3, 7, vec_2)
        expected_result = VectorND([3, 4, 6, 7, 7, 7, 5])
        self.assertEqual(vec_2, expected_result)

    def test_python_clipping_stupid(self) -> None:
        vec_1 = VectorND([2, 4, 6, 8, 9, 7, 5])
        vec_2 = VectorND([2, 4, 6, 8, 9, 7, 5])
        self.assertRaises(ValueError, computations.python_clip_vector, vec_1, 5, 4, vec_2)

    def test_naive_cython_clipping(self) -> None:
        vec_1 = VectorND([2, 4, 6, 8, 9, 7, 5])
        vec_2 = VectorND([2, 4, 6, 8, 9, 7, 5])
        computations.naive_cython_clip_vector(vec_1, 3, 7, vec_2)
        expected_result = VectorND([3, 4, 6, 7, 7, 7, 5])
        self.assertEqual(vec_2, expected_result)

    def test_naive_cython_clipping_stupid(self) -> None:
        vec_1 = VectorND([2, 4, 6, 8, 9, 7, 5])
        vec_2 = VectorND([2, 4, 6, 8, 9, 7, 5])
        self.assertRaises(ValueError, computations.naive_cython_clip_vector, vec_1, 5, 4, vec_2)

    def test_cython_clipping(self) -> None:
        vec_1 = VectorND([2, 4, 6, 8, 9, 7, 5])
        vec_2 = VectorND([2, 4, 6, 8, 9, 7, 5])
        computations.cython_clip_vector(vec_1, 3, 7, vec_2)
        expected_result = VectorND([3, 4, 6, 7, 7, 7, 5])
        self.assertEqual(vec_2, expected_result)

    def test_cython_clipping_stupid(self) -> None:
        vec_1 = VectorND([2, 4, 6, 8, 9, 7, 5])
        vec_2 = VectorND([2, 4, 6, 8, 9, 7, 5])
        self.assertRaises(ValueError, computations.cython_clip_vector, vec_1, 5, 4, vec_2)

    def test_equality(self) -> None:
        ''' Tests the equality operator.
        '''
        self.assertNotEqual(self.v1, self.v2)
        expected_result = VectorND(-1, 1)
        self.assertEqual(self.v2, expected_result)

    def test_add(self) -> None:
        ''' Tests the addition operator.
        '''
        result = self.v1 + self.v2
        expected_result = VectorND(-1, 1)
        self.assertEqual(result, expected_result)

    def test_sub(self) -> None:
        ''' Tests the subtraction operator.
        '''
        result = self.v2 - self.v3
        expected_result = VectorND(-3.5, 3.5)
        self.assertEqual(result, expected_result)

    def test_mul(self) -> None:
        ''' Tests the multiplication operator.
        '''
        result1 = self.v1 * 5
        expected_result1 = VectorND(0.0, 0.0)
        self.assertEqual(result1, expected_result1)
        result2 = self.v1 * self.v2
        expected_result2 = 0.0
        self.assertEqual(result2, expected_result2)

    def test_div(self) -> None:
        ''' Tests the multiplication operator.
        '''
        result = self.v3 / 5
        expected_result = VectorND(0.5, -0.5)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
