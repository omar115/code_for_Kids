'''
class: a blueprint 
object: created from a class, an entity, it has own behavior, function
self: self is used to represent the instance of the class, with this self keyword we can
access a class functions, variables
'''


from pygame.constants import K_PRINTSCREEN


class Godzilla:

    def __init__(self, name):
        self.name = name

    def skill(self):
        print('It is Huge with Blue power')
        print('its name is '+ self.name)
    
    def skill2(self):
        print('It is the largest among all Godzillas')
        print(self.name)
    
    

clone_Godzilla = Godzilla('Destroyer')

print(clone_Godzilla.name)

clone_Godzilla.skill()


clone_Godzilla = Godzilla('MechaGodzilla')

print(clone_Godzilla.name)

clone_Godzilla.skill2()

# clone_Godzilla2 = Godzilla('Survivor')

# print(clone_Godzilla2.name)


# clone_Godzilla.name('Destruction')

# clone_Godzilla.skill()

