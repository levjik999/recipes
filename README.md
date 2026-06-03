\# Система управления рецептами



Консольное приложение для создания блюд, управления рецептами,

масштабирования порций и генерации списка покупок.



\## Установка



```bash

git clone <ссылка-на-репозиторий>

cd recipes

pip install -r requirements.txt

```



\## Использование



```python

from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe



\# Создать рецепт

pizza = Recipe("Пицца Маргарита")

pizza.add\_ingredient(Ingredient("Мука", 500, "г"))

pizza.add\_ingredient(Ingredient("Томатный соус", 200, "мл"))



\# Масштабировать на 2 порции

pizza\_x2 = pizza.scale(2)



\# Добавить в список покупок

sl = ShoppingList()

sl.add\_recipe(pizza, 2)

print(sl.get\_list())



\# Диетический рецепт

vegan = DietaryRecipe("Пицца Маргарита", "веган")

print(vegan)

```



\## Запуск тестов



```bash

pytest

```



\## Автор



Фамилия Имя, учебная группа

