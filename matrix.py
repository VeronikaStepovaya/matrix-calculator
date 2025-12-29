"""Модуль для роботи з матрицями."""

class Matrix:
    """Клас для операцій з матрицями."""
    
    def __init__(self, data):
        """Ініціалізація матриці."""
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
    
    def __add__(self, other):
        """Додавання матриць."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Розміри матриць повинні співпадати")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)
    
    def __mul__(self, other):
        """Множення на скаляр або матрицю."""
        if isinstance(other, (int, float)):
            # Множення на число
            result = [
                [self.data[i][j] * other for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return Matrix(result)
        else:
            # Множення матриць
            if self.cols != other.rows:
                raise ValueError("Несумісні розміри для множення")
            result = [
                [
                    sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                    for j in range(other.cols)
                ]
                for i in range(self.rows)
            ]
            return Matrix(result)
    
    def transpose(self):
        """Транспонування матриці."""
        result = [
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ]
        return Matrix(result)
    
    def __str__(self):
        """Рядкове представлення."""
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
