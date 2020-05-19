class Deer:
    sound="Buck Buck"
    breath="Breathe in air"

    def __init__(self,age_in_months, breed,required_food_in_kgs):
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        
        if self._age_in_months>1:
            raise ValueError ("Invalid value for field age_in_months: {}".format(self._age_in_months))
            
        if self._required_food_in_kgs<=0:
            raise ValueError ("Invalid value for field required_food_in_kgs: {}".format(self._required_food_in_kgs))    
    k=required_food_in_kgs+2
    def grow(self):
        self._age_in_months+=1
        return self.k
        #self._required_food_in_kgs+=2
        
    @classmethod    
    def breathe(self):
        print(self.breath)
        
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
        
class Lion(Deer):
    sound="Roar Roar"
    count=0
    k=required_food_in_kgs+4
    #self._required_food_in_kgs+=4   
        
    def hunt(self,animal):
        if animal=="deer":
            self.count+=1
        elif self.count==0:    
            print("No deers to hunt")  
    
class Shark(Deer):
    count=0
    sound="Shark Sound"
    breath="Breathe oxygen from water"
    
    def hunt(self,animal):
        if animal=="gold_fish":
            self.count+=1
        elif self.count==0:      
            print("No GoldFish to hunt") 
      
class GoldFish(Shark):
    
    sound="Hum Hum"

class Snake(Deer):
    count=0
    sound="Hiss Hiss"
   

    def hunt(self,animal):
        if animal=="deer":
            self.count+=1
        elif self.count==0:    
            print("No deers to hunt")     
       
            
class Zoo:

    li=[]
    def __init__(self,reserved_food_in_kgs=0):
        self._reserved_food_in_kgs=reserved_food_in_kgs
    
    def add_food_to_reserve(self,food):
        self.reserved_food_in_kgs+=food
        
    def add_animal(self,animal):
        self.li.append(animal)
        
    def count_animals(self):
        return len(self.li)
        
    @classmethod    
    def count_animals_in_all_zoos(cls):
        pass
    
    @staticmethod
    def count_animals_in_given_zoos(cls):
        pass
        
    def feed(self,animal):
            if animal=="deer":
                self.reserved_food_in_kgs-=2
                #super().grow()
                
            elif animal=='lion':    
                self.reserved_food_in_kgs-=4
               
            elif animal=='Shark':    
                self.reserved_food_in_kgs-=8
               
            elif animal=='gold_fish':    
                self.reserved_food_in_kgs-=0.2

            elif animal=='snake':    
                self.reserved_food_in_kgs-=0.5 
              
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs

