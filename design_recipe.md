## problem
```
As a User
So that I can have toys
I want to have a Toy.

As a User
So that I know which toy I got
I want my Toy to have a name.

As a User
So that I know what colour my toy is
I want my Toy to have a colour.

As a User
So that I know which toy I got
I want my toy to tell me its name.

As a User
So that I know what colour my Toy is
I want my toy to tell me its colour.

As a User
So that I can paint my Toy
I want to change my toys colour.
```

## class/functions signature
```python
# Parameters:
# - name, colour, both strings
# Return
# - None
# Side effect
# - sets name to self.name, colour to self.colour
class Toy():
    def __init__(self, name, colour):
        pass

    # Parameters
    # - None
    # Returns
    # - name, string
    # Side effect
    # - None
    def get_name(self):
        pass

    # Parameters
    # - None
    # Returns
    # - colour, string
    # Side effect
    # - None
    def get_colour(self):
        pass

    # Parameters
    # - colour, string
    # Returns
    # - Nothing
    # Side effect
    # - changes the self.colour to colour
    def set_colour(self, colour):
        pass


```

## examples
```python
# scenario 1
toy = Toy('Teddy', 'brown')
assert toy.name == 'Teddy'
assert toy.colour == 'brown'

# scenario 2
toy = Toy('Teddy', 'brown')
assert toy.get_name() == 'Teddy'

# scenario 3
toy = Toy('Teddy', 'brown')
assert toy.get_colour() == 'brown'

# scenario 4
toy = Toy('Teddy', 'brown')
assert toy.get_colour() == 'brown'

toy.set_colour('red')

assert toy.get_colour() == 'red'
```