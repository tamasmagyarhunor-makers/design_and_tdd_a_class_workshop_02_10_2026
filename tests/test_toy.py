from lib.toy import Toy

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