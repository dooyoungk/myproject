class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other.data:             # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other.data:                # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            if not x in self.data:     # Removes duplicates
                self.data.append(x)            

    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:

    def issubset(self, other):
        for x in self.data:
            if x in other:
                if len(other) == len(self.data):
                    return True
                elif len(other) > len(self.data):
                    return True
                elif len(other) < len(self.data):
                    return False
                else:
                    return None
            else:
                return False
            
    def issuperset(self, other):
        for x in other:
            if x in self.data:
                if len(self.data) == len(other):
                    return True
                elif len(self.data) > len(other):
                    return True
                elif len(self.data) < len(other):
                    return False
                else:
                    return None
            else:
                self.data.append(x)
            
    def intersection_update(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        self.data = res
        return Set(self.data)
    
    def difference_update(self, other):
        res = []
        for x in self.data:
            if x not in other:
                res.append(x)
        self.data = res
        return Set(self.data)
    
    def symmetric_difference_update(self, other):
        res = []
        for x in self.data:
            if x not in other:
                res.append(x)
        for y in other:
            if y not in self.data:
                res.append(y)
        
        self.data = res
        return Set(self.data)
    
    def add(self, elem):        
        if elem not in self.data:
            self.data.append(elem)
            return Set(self.data)
        
        else:
            return print("elem is already belongs to set.")
    
    def remove(self, elem):
        if elem in self.data:
            self.data.remove(elem)
            return Set(self.data)
        
        
        else:
            raise KeyError("elem is not contained in the set.")
            
x = Set([1,3,5,7, 1, 3])
y = Set([2,1,4,5,6])

a = Set([7,8,9,11,12])
b = Set([7,8,9,10])
c = Set([6])

print(x, y, len(x))
print(x.intersection(y), y.union(x))
print(x & y, x | y)
print(x[2], y[:2])
for element in x:
    print(element, end=' ')
print()
print(3 not in y)  # membership test
print(list(x))# convert to list because x is iterable

print("==================================")
print(a.issubset(b))
print(b.issuperset(a))
print(c.issubset(a))
print(c.issubset(y))

a = Set([7,8,9,11,12])
b = Set([7,8,9,10])
print(a.intersection_update(b))

a = Set([7,8,9,11,12])
b = Set([7,8,9,10])
print(a.difference_update(b))

a = Set([7,8,9,11,12])
b = Set([7,8,9,10])
print(a.symmetric_difference_update(b))

a = Set([7,8,9,11,12])
b = Set([7,8,9,10])
print(a.add(13))
a.add(7)
print(b.remove(7))
b.remove(15)