# import ipdb

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.set_all_pets(self)


    @classmethod
    def set_all_pets(cls, pet):
        cls.all.append(pet)

    def get_pet_type(self):
        return self._pet_type

    def set_pet_type (self, pet_type):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception

    pet_type = property(get_pet_type, set_pet_type)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet,Pet):
            pet.owner = self
        else:
            raise Exception
        
    def get_sorted_pets(self):
        # print(sorted(Pet.all))
        return sorted(Pet.all, key=lambda pet: pet.name)

# ben = Owner("Ben")
# fluffy = Pet("fluffy", "cat", "Ben")
# stuffy = Pet("stuffy", "cat")
# doggy = Pet("doggy", "dog", "Ben")





# ipdb.set_trace()