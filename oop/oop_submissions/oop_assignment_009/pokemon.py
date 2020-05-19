class Pokemon:
    
    magnitude=1
    def __init__(self,name,level=1):
        self._name=name
        self._level=level
        self._master=None
        
        if len(self._name)==0:
            raise ValueError("name cannot be empty")
        if self._level<=0:
            raise ValueError("level should be > 0")
        
    @property
    def name(self):
        return self._name
        
    @property
    def level(self):
        return self._level    
        
    @property
    def master(self):
        if  self._master==None:
            print("No Master")
        else:    
            return self._master        
    
    sound=""
    nature=""
    k=0
    @classmethod
    def make_sound(self):
        print(self.sound)
        
    def attack(self):
        self.k=self.magnitude*int(self._level)
        print("{} attack with {} damage".format(self.nature,self.k))
    
    def __str__(self):
        return ("{} - Level {}".format(self._name,str(self._level)))
        
class WaterPokemon(Pokemon):
    nature="Water"
    swimming="Squirtle swimming..."
    @classmethod
    def swim(self):
        print(self.swimming)
        
class FlyingPokemon(Pokemon):
    flying="Pidgey flying..."
    nature="Air"
    @classmethod   
    def fly(self):
        print(self.flying)
        
class ElectricPokemon(Pokemon):
    nature="Electric"
    running="Pikachu running..."
    @classmethod
    def run(self):
        print(self.running)
        
class Pikachu(ElectricPokemon):
    sound="Pika Pika"
    magnitude=10
    
class Squirtle(WaterPokemon,ElectricPokemon):
    running="Squirtle running..."
    sound="Squirtle...Squirtle"
    magnitude=9
    
class Pidgey(FlyingPokemon):
    sound="Pidgey...Pidgey"
    magnitude=5  
    
class Swanna(WaterPokemon,FlyingPokemon):
    sound="Swanna...Swanna"
    swimming="Swanna swimming..."
    flying="Swanna flying..."
    magnitude=9
    nature="Water"
    def attack(self):
        super().attack()
        print("Air attack with {} damage".format(self._level*5))
    
class Zapdos(ElectricPokemon,FlyingPokemon):
    sound="Zap...Zap"
    flying="Zapdos flying..."
    nature="Electric"
    magnitude=10
    def attack(self):
        super().attack()
        print("Air attack with {} damage".format(self._level*5))
    
class Island(Pokemon):
    li=[]
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        self.li.append(self)
        
    def __str__(self):
        return "{} - {} pokemon - {} food".format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs)
     
    def add_pokemon(self,pokemon):
        if self._pokemon_left_to_catch < self._max_no_of_pokemon:
            self._pokemon_left_to_catch += 1 
        else:
            print("Island at its max pokemon capacity")
            
    @classmethod       
    def get_all_islands(self):
        return self.li    
    
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch   
        
        
class Trainer(Island,Pokemon):
    def __init__(self,name):
        self._name=name
        self._experience=100
        self._food_in_bag=0
        self._max_food_in_bag=10*self._experience
        self.list1=[]
        self._current_island=None
    
    def collect_food(self):
        if self._current_island==None:
            print("Move to an island to collect food")
        else:
            if self._current_island._total_food_available_in_kgs<self._max_food_in_bag:
                self._food_in_bag=self._current_island._total_food_available_in_kgs
                self._current_island._total_food_available_in_kgs=0
                
            elif self._food_in_bag<self._max_food_in_bag:
                self._food_in_bag=self._max_food_in_bag  
                self._current_island._total_food_available_in_kgs-=self._max_food_in_bag
              
                
    def catch(self,pokemon_value):
        if self._experience>=(100*pokemon_value._level):
            self.list1.append(pokemon_value)
            print("You caught {}".format(pokemon_value.name))
            self._experience+=20*pokemon_value._level
            pokemon_value._master = self
        else:
            print("You need more experience to catch {}".format(pokemon_value.name))
            
    def get_my_pokemon(self):
        return (self.list1)
    
    def move_to_island(self,island):
        self._current_island=island   
            
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
        
    @property
    def food_in_bag(self):
        return self._food_in_bag
        
    @property
    def experience(self):
        return self._experience
        
    @property
    def current_island(self):
        if self._current_island==None:
            print("You are not on any island")
        else:
            return self._current_island
        