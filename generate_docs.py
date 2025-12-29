"""Генератор документації для модуля matrix.py"""

def generate_documentation():
    """Генерує HTML документацію."""
    
    html = '''<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Документація Matrix Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #2c3e50; }
        .class { background: #f5f5f5; padding: 20px; margin: 20px 0; border-radius: 5px; }
        .method { margin: 10px 0; padding: 10px; background: #e8f4f8; }
        code { background: #2c3e50; color: white; padding: 2px 5px; }
    </style>
</head>
<body>
    <h1>📚 Документація Matrix Calculator</h1>
    
    <div class="class">
        <h2>Клас: <code>Matrix</code></h2>
        <p>Клас для роботи з матрицями. Підтримує основні математичні операції.</p>
        
        <div class="method">
            <h3><code>__init__(data)</code></h3>
            <p>Конструктор класу. Приймає двовимірний список.</p>
        </div>
        
        <div class="method">
            <h3><code>__add__(other)</code></h3>
            <p>Додавання двох матриць. Матриці повинні мати однакові розміри.</p>
        </div>
        
        <div class="method">
            <h3><code>__mul__(other)</code></h3>
            <p>Множення матриці на скаляр або іншу матрицю.</p>
        </div>
        
        <div class="method">
            <h3><code>transpose()</code></h3>
            <p>Транспонування матриці (рядки стають стовпцями).</p>
        </div>
        
        <div class="method">
            <h3><code>__str__()</code></h3>
            <p>Повертає рядкове представлення матриці.</p>
        </div>
    </div>
    
    <h2>Приклад використання:</h2>
    <pre><code>from matrix import Matrix

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

print(A + B)  # Додавання
print(A * 2)  # Множення на скаляр
print(A * B)  # Множення матриць
print(A.transpose())  # Транспонування</code></pre>
    
    <h2>Юніт-тести:</h2>
    <p>Проєкт включає 5 юніт-тестів для перевірки всіх операцій.</p>
    
    <footer>
        <p>Документація згенерована автоматично</p>
    </footer>
</body>
</html>'''
    
    # Зберегти HTML файл
    with open('docs.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("✅ Документацію згенеровано: docs.html")

if __name__ == "__main__":
    generate_documentation()
