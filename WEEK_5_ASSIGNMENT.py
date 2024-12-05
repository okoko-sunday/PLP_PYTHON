# Question 1

class Book():
    def __init__(self, name):
        self.name = name 
        
    def value(self):
        return self.name
    
class Author():
    def __init__(self, name):
        self.name = name
        
    def value(self):
        return self.name
    
for values in [Book('Things fall apart'), Author('Chinue Achibe')]:
    print(values.value())



# Question 2

class Car():
    def move(self):
        return "Driving"
    
class Plane():
    def move(self):
        return "Flying"
    
print(Car().move())
print(Plane().move())