from car import Car
import math
class RaceCar(Car):
    horn="Peep Peep\nBeep Beep"
    def __init__(self,max_speed,acceleration,tyre_friction,color=0):
        super().__init__(max_speed,acceleration,tyre_friction,color)
        self._nitro=0
     
    
    @property  
    def nitro(self):
        return self._nitro     
    
    def accelerate(self):
       
        if self._nitro>0:    
            self._current_speed=(self._acceleration+self._current_speed+math.ceil(0.3*self._acceleration))
            self._nitro-=10
            if self._current_speed>self._max_speed:
                self._current_speed=self._max_speed
        else:
            super().accelerate()
          
  
    def apply_brakes(self):
       
        if self._current_speed>(self._max_speed//2):
            self._current_speed-=self._tyre_friction
            self._nitro+=10
        else:
            
            super().apply_brakes()
                                  