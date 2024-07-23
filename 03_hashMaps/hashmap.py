class HashMap:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]  # Assign all elements None

    def get_hash(self, key):   # hash function using ascii
        h = 0
        for char in key:
            h += ord(char) # to retrieve ascii value
        return h % self.MAX
    
    def add(self, key, val):  # __setItem__
        h = self.get_hash(key)
        found = False


        for idx, element in enumerate(self.arr[h]):  #to handle if key already exists pour l'ecraser
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val )
                found =True
                break

        if not found:
            #if key does not exist add a new one
            self.arr[h].append( (key, val) )
        
    def get(self, key):    # __getItem__
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
            
    def delete(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]


    


if __name__ == '__main__':
    t = HashMap()
    t.get_hash('march 6')
    t.add('march 6', 130)
    t.add('march 17', 240) # problem of collision
    t.delete('march 6')
    print(t.get('march 17'))