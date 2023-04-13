from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("queijo mussarela")
    same_ingredient = Ingredient("queijo mussarela")
    another_ingredient = Ingredient("farinha")

    assert ingredient.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    assert repr(ingredient) == "Ingredient('queijo mussarela')"

    assert ingredient == same_ingredient
    assert ingredient != another_ingredient

    assert hash(ingredient) == hash(same_ingredient)
    assert hash(ingredient) != hash(another_ingredient)

    assert ingredient.name == "queijo mussarela"
