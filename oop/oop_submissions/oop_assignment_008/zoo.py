class Animals:
    k=0
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        
        if self._age_in_months>1:
            raise ValueError ("Invalid value for field age_in_months: {}".format(self._age_in_months))
            
        if self._required_food_in_kgs<=0:
            raise ValueError ("Invalid value for field required_food_in_kgs: {}".format(self._required_food_in_kgs))
    
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs=self._required_food_in_kgs+self.k
    
    sound=""
    
    @classmethod    
    def make_sound(self):  
        print(self.sound)
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    @property
    def breed(self):
        return self._breed
        
    @property
    def age_in_months(self):
        return self._age_in_months         
        
class LandAnimals:
    breath="Breathe in air"
    
    @classmethod    
    def breathe(self):
        print(self.breath)
        
class WaterAnimals(LandAnimals):
    breath="Breathe oxygen from water"
    
class Zoo(Animals):
    c=[]
    def __init__(self,reserved_food_in_kgs=0):
        self._reserved_food_in_kgs=reserved_food_in_kgs
        self.li=[]
     
    def add_animal(self,animal):
        self.li.append(animal)
        self.c.append(animal)
        
    def count_animals(self):
        return len(self.li)
        
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs+=food
        
    def feed(self,animal):
        if self._reserved_food_in_kgs>0:
            self._reserved_food_in_kgs-=animal._required_food_in_kgs
            animal.grow()
        
    @classmethod    
    def count_animals_in_all_zoos(cls):
        return len(cls.c)
    
    @staticmethod
    def count_animals_in_given_zoos(different_zoos=[]):
        s=0
        for i in different_zoos:
            s+=i.count_animals()
        return s    
        
    
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
class HuntingAnimals:
    
    animal="Deer"
    no_animal="deers"
    def hunt(self,animal):
        count=0
        for i in animal.li:
            if self.animal in str(type(i)):
                count=1
                animal.li.remove(i)
                break

        if count==0:
            print("No {} to hunt".format(self.no_animal))
    
class Deer(LandAnimals,Animals):
    
    sound="Buck Buck"
    k=2  
    
class Lion(LandAnimals,Animals,HuntingAnimals):
    sound="Roar Roar"
    k=4
    
class Shark(WaterAnimals,Animals,HuntingAnimals):
    sound="Shark Sound"
    k=8
    animal="GoldFish"
    no_animal="GoldFish"
    
class Snake(LandAnimals,Animals,HuntingAnimals):
    sound="Hiss Hiss"
    k=0.5
    
class GoldFish(WaterAnimals,Animals):
    sound="Hum Hum"
    k=0.2
    
    