'''
class: a blueprint 
object: created from a class, an entity, it has own behavior, function
self: self is used to represent the instance of the class, with this self keyword we can
access a class functions, variables
'''

class Godzilla:
    color = 'blue'
    def __init__(self, name, color):
        self.name = name
        self.color = color


    def skill(self):
        print('It is Huge with RED power')
        print('its name is '+ self.name)
        print(2+5)
    
    


clone_Godzilla = Godzilla('Destroyer', 'RED')

print('The color of clone godzilla is ', clone_Godzilla.color)

clone_Godzilla.skill()



# print(clone_Godzilla.name)

# clone_Godzilla.skill()


# clone_Godzilla = Godzilla('MechaGodzilla')

# print(clone_Godzilla.name)

# clone_Godzilla.skill2()

# clone_Godzilla2 = Godzilla('Survivor')

# print(clone_Godzilla2.name)


# clone_Godzilla.name('Destruction')

# clone_Godzilla.skill()

