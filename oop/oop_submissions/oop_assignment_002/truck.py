from car import Car
class Truck(Car):
    horn="Honk Honk"
    def __init__(self,max_speed,acceleration,tyre_friction,max_cargo_weight,color=0):
        super().__init__(max_speed,acceleration,tyre_friction,color)
        self._max_cargo_weight=max_cargo_weight
        self._current_load=0
        if self._max_cargo_weight<0:
            raise ValueError('Invalid value for cargo_weight')  
            
    
    @property  
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    @property  
    def current_load(self):
        return self._current_load      
        
      
            
    def load(self,total_load):
        if total_load<0:
            raise ValueError('Invalid value for cargo_weight')  
            
        #else:    
        if self._current_speed>0:
            print("Cannot load cargo during motion")
        else:
            if (self._current_load+total_load)<=self._max_cargo_weight:
                self._current_load+=total_load
            else:
                print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
              
    def unload(self,total_load):
        if total_load<0:
            raise ValueError('Invalid value for cargo_weight')  
        #else:
        if self._current_speed>0:
            print("Cannot unload cargo during motion")
        else:
                
            if total_load>=self._current_load:
                self._current_load=0
            else:
                self._current_load-=total_load
           
                                                                                                                                                                                                                                