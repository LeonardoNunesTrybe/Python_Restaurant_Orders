from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1

def test_ingredient():
    ingredient = Ingredient('manteiga')
    assert ingredient.name == 'manteiga'
    assert ingredient.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }

    assert repr(ingredient) == "Ingredient('manteiga')"

    assert hash(ingredient) == hash('manteiga')
    assert hash(ingredient) != hash('salmão')

    assert ingredient.__eq__(Ingredient('manteiga')) is True
    assert ingredient.__eq__(Ingredient('salmão')) is False
