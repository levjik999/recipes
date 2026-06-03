import pytest
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

def test_ingredient_init_attributes():
    ing = Ingredient("Мука", 500, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"

def test_ingredient_quantity_is_float():
    ing = Ingredient("Яйца", 2, "шт")
    assert isinstance(ing.quantity, float)

def test_ingredient_quantity_negative_raises():
    with pytest.raises(ValueError, match="Количество должно быть положительным"):
        Ingredient("Мука", -100, "г")
        
def test_ingredient_quantity_zero_raises():
    with pytest.raises(ValueError):
        Ingredient("Мука", 0, "г")

def test_ingredient_str():
    ing = Ingredient("Мука", 500, "г")
    assert str(ing) == "Мука: 500.0 г"

def test_ingredient_repr():
    ing = Ingredient("Мука", 500, "г")
    assert repr(ing) == "Ingredient('Мука', 500.0, 'г')"

def test_ingredient_eq_same_name_and_unit_different_quantity():
    a = Ingredient("Мука", 100, "г")
    b = Ingredient("Мука", 999, "г")
    assert a == b

def test_ingredient_eq_different_name():
    a = Ingredient("Мука", 100, "г")
    b = Ingredient("Сахар", 100, "г")
    assert a != b

def test_ingredient_quantity_setter_updates_value():
    ing = Ingredient("Соль", 10, "г")
    ing.quantity = 50
    assert ing.quantity == 50.0

def test_ingredient_eq_different_unit():
    a = Ingredient("Мука", 100, "г")
    b = Ingredient("Мука", 100, "кг")
    assert a != b
