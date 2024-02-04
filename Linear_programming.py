import pulp as plp

# Створення моделі
prob = plp.LpProblem("Beverage Production", plp.LpMaximize)

# Визначення змінних
# кількість Лимонаду
x1 = plp.LpVariable("Лимонад", 0, None, cat=plp.LpInteger)
# кількість Фруктового соку
x2 = plp.LpVariable("Фруктовий сік", 0, None, cat=plp.LpInteger)

# Функція цілі: максимізація загальної кількості продуктів
prob += x1 + x2, "Total Product"

# Обмеження ресурсів
prob += 2 * x1 + 1 * x2 <= 100, "Water"       
prob += 1 * x1 <= 50, "Sugar"                 
prob += 1 * x1 <= 30, "Lemon Juice"          
prob += 2 * x2 <= 40, "Fruit Puree"         

# Розв'язання задачі
prob.solve()

# Вивід результатів
print(f"Status: {plp.LpStatus[prob.status]}")
print(f"Лимонад = {plp.value(x1)}")
print(f"Фруктовий сік = {plp.value(x2)}")
print(f"Загальна кількість продуктів = {plp.value(prob.objective)}")