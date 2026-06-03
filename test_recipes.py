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

def test_recipe_init_attributes():
    r = Recipe("Пицца Маргарита")
    assert r.title == "Пицца Маргарита"
    assert r.ingredients == []

def test_recipe_add_new_ingredient():
    r = Recipe("Пицца")
    ing = Ingredient("Мука", 500, "г")
    r.add_ingredient(ing)
    assert len(r) == 1

def test_recipe_add_ingredient_merges_duplicate():
    r = Recipe("Пицца")
    r.add_ingredient(Ingredient("Мука", 300, "г"))
    r.add_ingredient(Ingredient("Мука", 200, "г"))
    assert len(r) == 1
    assert r.ingredients[0].quantity == 500.0

def test_recipe_str_contains_title():
    r = Recipe("Борщ")
    r.add_ingredient(Ingredient("Свёкла", 300, "г"))
    assert "Борщ" in str(r)

def test_recipe_add_different_units_not_merged():
    r = Recipe("Пицца")
    r.add_ingredient(Ingredient("Мука", 500, "г"))
    r.add_ingredient(Ingredient("Мука", 1, "кг"))
    assert len(r) == 2

def test_recipe_scale_returns_new_object():
    r = Recipe("Пицца")
    r.add_ingredient(Ingredient("Мука", 500, "г"))
    scaled = r.scale(2)
    assert scaled is not r

def test_recipe_scale_multiplies_quantities():
    r = Recipe("Пицца")
    r.add_ingredient(Ingredient("Мука", 500, "г"))
    scaled = r.scale(3)
    assert scaled.ingredients[0].quantity == 1500.0

def test_recipe_scale_does_not_modify_original():
    r = Recipe("Пицца")
    r.add_ingredient(Ingredient("Мука", 500, "г"))
    r.scale(2)
    assert r.ingredients[0].quantity == 500.0

def test_recipe_scale_negative_ratio_raises():
    r = Recipe("Пицца")
    r.add_ingredient(Ingredient("Мука", 500, "г"))
    with pytest.raises(ValueError):
        r.scale(-1)

def test_recipe_scale_zero_ratio_raises():
    r = Recipe("Пицца")
    r.add_ingredient(Ingredient("Мука", 500, "г"))
    with pytest.raises(ValueError):
        r.scale(0)

def test_recipe_len():
    r = Recipe("Пицца")
    r.add_ingredient(Ingredient("Мука", 500, "г"))
    r.add_ingredient(Ingredient("Соль", 5, "г"))
    assert len(r) == 2

def test_recipe_len_with_merge():
    r = Recipe("Пицца")
    r.add_ingredient(Ingredient("Мука", 300, "г"))
    r.add_ingredient(Ingredient("Мука", 200, "г"))
    assert len(r) == 1
