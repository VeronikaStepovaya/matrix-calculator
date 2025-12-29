"""Головна програма для демонстрації."""

from matrix import Matrix

def main():
    print("=== Демонстрація Matrix Calculator ===")
    
    # Створення матриць
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    
    print("\n1. Матриця A:")
    print(A)
    
    print("\n2. Матриця B:")
    print(B)
    
    print("\n3. A + B:")
    print(A + B)
    
    print("\n4. A * 2:")
    print(A * 2)
    
    print("\n5. A * B:")
    print(A * B)
    
    print("\n6. Транспонування A:")
    print(A.transpose())
    
    # Перевірка помилок
    print("\n7. Перевірка помилок:")
    C = Matrix([[1, 2, 3], [4, 5, 6]])
    try:
        print("Спроба A + C (різні розміри):")
        print(A + C)
    except ValueError as e:
        print(f"Очікувана помилка: {e}")

if __name__ == "__main__":
    main()
