# Система управления рецептами

Консольное приложение на Python для создания и управления рецептами, масштабирования ингредиентов и генерации списка покупок.

## Возможности проекта

* Создание ингредиентов и рецептов
* Добавление ингредиентов в рецепт
* Автоматическое объединение одинаковых ингредиентов
* Масштабирование рецептов по количеству порций
* Создание списка покупок
* Поддержка диетических рецептов
* Перегрузка магических методов (`__str__`, `__repr__`, `__len__`, `__eq__`)
* Покрытие функционала тестами `pytest`

---

## Структура проекта

```text
recipes/
│
├── recipes.py
├── test_recipes.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Установка

Клонировать репозиторий:

```
git clone https://github.com/levjik999/recipes.git
```

Перейти в папку проекта:

```
cd recipes
```

Установить зависимости:

```
py -m pip install -r requirements.txt
```

---

## Использование

```python
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

# Создание рецепта
pizza = Recipe("Пицца Маргарита")

pizza.add_ingredient(Ingredient("Мука", 500, "г"))
pizza.add_ingredient(Ingredient("Томатный соус", 200, "мл"))

# Масштабирование рецепта
pizza_x2 = pizza.scale(2)

# Создание списка покупок
shopping = ShoppingList()

shopping.add_recipe(pizza, 2)

print(shopping.get_list())

# Диетический рецепт
vegan = DietaryRecipe("Пицца Маргарита", "веган")

print(vegan)
```

---

## Запуск тестов
```
py -m pytest
```

---

## Используемые технологии

* Python
* OOP
* pytest
* Git / GitHub

---

## Автор

Мелкумов Владимир
бби2502
