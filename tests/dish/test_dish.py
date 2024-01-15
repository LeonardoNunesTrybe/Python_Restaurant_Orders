from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish = Dish('lasanha berinjela', 27.00)
    ingredient = Ingredient('berinjela')

    assert dish.name == 'lasanha berinjela'
    assert dish.price == 27.00

    assert dish.__hash__() == hash("Dish('lasanha berinjela', R$27.00)")

    assert dish.__eq__(Dish("lasanha berinjela", 27.00)) is True
    assert dish.__eq__(Dish("lasanha berinjela", 25.00)) is False

    assert dish.__repr__() == "Dish('lasanha berinjela', R$27.00)"

    with pytest.raises(TypeError):
        Dish("lasanha berinjela", "28.00")

    with pytest.raises(ValueError):
        Dish('lasanha berinjela', -1.00)

    dish.add_ingredient_dependency(ingredient, 15)
    assert dish.recipe.get(ingredient) == 15

    assert dish.get_restrictions() == ingredient.restrictions

    assert dish.get_ingredients() == {ingredient}
