class Toy:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    
    def get_name(self):
        return self.name
    
    def get_colour(self):
        return self.colour
    
    def set_colour(self, new_colour):
        if not isinstance(new_colour, str):
            raise TypeError('Only strings can be used to set colour')
        self.colour = new_colour