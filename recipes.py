class Ingredient: 
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
 
    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
 
    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.unit == other.unit

class Recipe: 
    def __init__(self, title: str, ingredients: list = None):
        self.title = title
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients
    def add_ingredient(self, ingredient: Ingredient):
        for existing in self.ingredients:
            if existing == ingredient:
                existing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        return isinstance(ratio, (int, float)) and ratio > 0

    def scale(self, ratio: float) -> "Recipe":
        if not self.is_valid_ratio(ratio):
            raise ValueError("Количество должно быть положительным")
        new_ingredients = [Ingredient(ing.name, ing.quantity * ratio, ing.unit)
                           for ing in self.ingredients]
        return Recipe(self.title, new_ingredients)
    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        lines = [self.title]
        for ing in self.ingredients:
            lines.append(f"  - {ing}")
        return "\n".join(lines)

class ShoppingList:
    def __init__(self):
        self._items = []
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)
        for ing in scaled.ingredients:
            self._items.append((ing, recipe.title))

    def remove_recipe(self, title: str):
        self._items = [(ing, t) for ing, t in self._items if t != title]
    def get_list(self) -> list:
        totals = {}
        for ing, _ in self._items:
            key = (ing.name, ing.unit)
            if key in totals:
                totals[key] += ing.quantity
            else:
                totals[key] = ing.quantity
        result = [Ingredient(name, qty, unit) for (name, unit), qty in totals.items()]
        result.sort(key=lambda ing: ing.name)
        return result

    def __add__(self, other: "ShoppingList") -> "ShoppingList":
        new_list = ShoppingList()
        new_list._items = self._items[:] + other._items[:]
        return new_list

class DietaryRecipe(Recipe): 
    def __init__(self, title: str, diet_type: str, ingredients: list = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    def scale(self, ratio: float) -> "DietaryRecipe":
        if not self.is_valid_ratio(ratio):
            raise ValueError("Количество должно быть положительным")
        scaled_base = super().scale(ratio)
        return DietaryRecipe(self.title, self.diet_type, scaled_base.ingredients)
    def __str__(self):
        base = super().__str__()
        return f"[{self.diet_type}] {base}"
