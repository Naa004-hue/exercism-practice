"""Solution to Ellen's Alien Game exercise."""

class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate."""
    total_aliens_created = 0
    def __init__(self,x_coordinate, y_coordinate):
        self.x_coordinate=x_coordinate
        self.y_coordinate=y_coordinate
        self.health= 3
        
        Alien.total_aliens_created += 1
    def hit(self):
        if self.health > 0 :
            self.health -= 1
            
    def is_alive(self) :
        return self.health > 0
    def teleport(self,x_coordinate, y_coordinate) :
        self.x_coordinate=x_coordinate
        self.y_coordinate=y_coordinate
        
    def collision_detection (self,other_object):
        pass
        
def new_aliens_collection(alien_start_positions):
    a_list=[]
    for position in alien_start_positions :
        a_list.append(Alien(*position))
    return a_list
    