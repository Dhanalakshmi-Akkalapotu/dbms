class Item:
    def __init__(self,name,price,category):
        self._name=name
        self._price=price        
        self._category=category
        
        if self._price<=0:
            raise ValueError ("Invalid value for price, got {}".format(self._price))
            
    def __str__(self):
        return "{}@{}-{}".format(self._name,self._price,self._category)
        
    @property
    def name(self):
        return self._name
        
    @property
    def price(self):
        return self._price
        
    @property
    def category(self):
        return self._category    
        
class Query:
    
    def __init__(self,field,operation,value):
        self._field=field
        self._operation=operation
        self._value=value
        li=['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
        
        if self._operation not in li:
            raise ValueError ("Invalid value for operation, got {}".format(self._operation))
            
    def __str__(self):
        return "{} {} {}".format(self._field,self._operation,self._value)
    
    @property
    def operation(self):
        return self._operation
    
    @property
    def field(self):
        return self._field
        
    @property
    def value(self):
        return self._value       
        
class Store:
    
    def __init__(self):
        self.list_items=[]
    
    def add_item(self,item):
        self.list_items.append(item)
        
    def count(self):
        return len(self.list_items)
        
    def __str__(self):  
        if len(self.list_items)==0:
            return "No items"
        else:  
            return '\n'.join(map(str,self.list_items))
        
    def filter(self,query):
        x=Store()
        
        if query._operation=='EQ':
            for i in self.list_items:
                if i._name==query._value or i._price==query._value or i._category==query._value:
                    x.add_item((i))
               
        elif query._operation=='GT':
            for i in self.list_items:
                if i._price>query._value:
                    x.add_item((i))
                
        elif query._operation=='LT':
            for i in self.list_items:    
                if query._value>i._price:
                    x.add_item((i))
                
        elif query._operation=='GTE':
            for i in self.list_items:
                if query._value<=i._price:
                   x.add_item((i))
                
        elif query._operation=='LTE':
            for i in self.list_items:
                if query._value>=i._price:
                   x.add_item((i))
               
        elif query._operation=='STARTS_WITH' or query._operation=='ENDS_WITH':
            for i in self.list_items:
                if query._value in i._name or  query._value in i._category:
                   x.add_item((i))
                
        elif query._operation=='IN':
            for i in self.list_items:
                if i._name in query._value or i._price in query._value or i._category in query._value:
                   x.add_item((i))
                
        elif query._operation=='CONTAINS':
            for i in self.list_items:
                if (query._field=="name" and (query._value in i._name)) or (query._field=="category" and (query._value in i._category)):
                   x.add_item((i))         
        return x
        
    def exclude(self,query):
        d=Store()
        a=self.filter(query)
        for i in self.list_items:
            if i not in a.list_items:
                d.add_item((i))
        return d
        