from lib.toy import Toy
import pytest

# scenario 1
def test_toy_instantiates():
    toy = Toy('Teddy', 'brown')
    assert toy.name == 'Teddy'
    assert toy.colour == 'brown'

# scenario 2
def test_toy_can_tell_its_name():
    toy = Toy('Teddy', 'brown')
    assert toy.get_name() == 'Teddy'

# scenario 3
def test_toy_can_tell_its_colour():
    toy = Toy('Teddy', 'brown')
    assert toy.get_colour() == 'brown'

# scenario 4
def test_toy_can_change_its_colour():
    toy = Toy('Teddy', 'brown')
    assert toy.get_colour() == 'brown'

    toy.set_colour('red')

    assert toy.get_colour() == 'red'

# scenario 5
def test_toy_raises_typeeror_when_not_string_used_to_change_colour():
    toy = Toy('Teddy', 'brown')
    assert toy.get_colour() == 'brown'
    with pytest.raises(TypeError) as error:
        toy.set_colour(3.2)

    error_message = str(error.value)

    assert error_message == "Only strings can be used to set colour"