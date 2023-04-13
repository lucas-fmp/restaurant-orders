from models.ingredient import Ingredient, Restriction
import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish = Dish("macarronada", 20)
    same_dish = Dish("macarronada", 20)
    another_dish = Dish("lasanha", 30)

    assert dish.name == "macarronada"

    assert dish == same_dish

    assert hash(dish) == hash(same_dish)
    assert hash(dish) != hash(another_dish)

    assert dish.get_ingredients() == same_dish.get_ingredients()

    assert repr(dish) == "Dish('macarronada', R$20.00)"

    dish.add_ingredient_dependency(Ingredient("queijo mussarela"), 1)
    assert dish.get_ingredients() == {Ingredient("queijo mussarela")}
    assert dish.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    with pytest.raises(ValueError):
        dish = Dish("macarronada", -10)

    with pytest.raises(TypeError):
        dish = Dish("macarronada", [])
