"""Юніт-тести для класу Matrix."""

import unittest
from matrix import Matrix

class TestMatrix(unittest.TestCase):
    """Тести для Matrix."""
    
    def test_addition(self):
        """Тест додавання матриць."""
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        result = m1 + m2
        self.assertEqual(result.data, [[6, 8], [10, 12]])
    
    def test_addition_error(self):
        """Тест помилки при додаванні різних розмірів."""
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(ValueError):
            m1 + m2
    
    def test_scalar_multiplication(self):
        """Тест множення на скаляр."""
        m = Matrix([[1, 2], [3, 4]])
        result = m * 3
        self.assertEqual(result.data, [[3, 6], [9, 12]])
    
    def test_matrix_multiplication(self):
        """Тест множення матриць."""
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[2, 0], [1, 2]])
        result = m1 * m2
        self.assertEqual(result.data, [[4, 4], [10, 8]])
    
    def test_transpose(self):
        """Тест транспонування."""
        m = Matrix([[1, 2, 3], [4, 5, 6]])
        result = m.transpose()
        self.assertEqual(result.data, [[1, 4], [2, 5], [3, 6]])

if __name__ == '__main__':
    unittest.main()
