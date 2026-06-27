import random , string
class Robot:
    names=set()
    def __init__(self):
        self.name=self.naming()
        
    def naming(self) :
        while True: 
            name1 = [random.choice(string.ascii_uppercase) for _ in range(2)]
            name1+= [str(random.randint(1, 9)) for _ in range(3) ]
            name = ''.join(name1)
            if name  not in Robot.names:
                Robot.names.add(name)
                return name

    def reset (self) :
        self.name=self.naming() 
        
            
        
        
        
