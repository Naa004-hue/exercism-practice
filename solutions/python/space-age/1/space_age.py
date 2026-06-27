class SpaceAge:
    period={'Mercury':0.2408467,'Venus':0.61519726,'Mars':1.8808158,'Jupiter':11.862615,'Saturn':29.447498,'Uranus':84.016846,'Neptune':164.79132}
    EARTH_S=31557600 
    def __init__(self, seconds):
        self.seconds=seconds
        self.on_earth_y=self.seconds/self.EARTH_S
    def on_earth(self) :
        return round(self.seconds/self.EARTH_S,2)
    def on_mercury(self):
        return  round(self.on_earth()/self.period['Mercury'],2)
    def on_venus(self):
        return  round(self.on_earth_y/self.period['Venus'],2)
    def on_mars(self):
        return  round(self.on_earth()/self.period['Mars'],2)
    def on_jupiter(self):
        return  round(self.on_earth()/self.period['Jupiter'],2)
    def on_saturn(self):
        return  round(self.on_earth()/self.period['Saturn'],2)
    def on_uranus(self):
        return  round(self.on_earth()/self.period['Uranus'],2)
    def on_neptune(self):
        return  round(self.on_earth()/self.period['Neptune'],2)

        
    
        
    
