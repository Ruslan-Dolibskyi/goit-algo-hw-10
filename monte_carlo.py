import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
import random

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

# Метод Монте-Карло


def monte_carlo_integration(func, a, b, num_samples=10000):
    sum_value = 0
    for _ in range(num_samples):
        x = random.uniform(a, b)
        sum_value += func(x)
    return (b - a) * sum_value / num_samples

# Аналітичний метод


def analytical_integration(func, a, b):
    result, _ = quad(func, a, b)
    return result


# Визначення меж інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()

# Виконання інтеграції
monte_carlo_result = monte_carlo_integration(f, a, b)
analytical_result = analytical_integration(f, a, b)

plt.show()

# Виведення результатів
print("Метод Монте-Карло: ", monte_carlo_result)
print("Аналітичний метод: ", analytical_result)