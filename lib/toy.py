class Toy:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    
    def get_name(self):
        return self.name
    
    def get_colour(self):
        return self.colour
    
    def set_colour(self, new_colour):
        self.colour = new_colour