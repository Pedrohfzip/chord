from hashlib import sha256
class HashTable():
    class Element:
        def __init__(self,key,value):
            self.key = key
            self.value = value


        def __init__(self):
            self.capacity = 5 # internal table capacity/size
            self.internList = [[] for _ in range(self.capacity)] 
            self.length = 0 # number of elements saved in the hash table
        
        def __len__(self):
            return self.length
        
        
        def hashCreate(self, key):
            codificado = str(key).encode()
            return int(sha256(codificado).hexdigest(), 16)
        
        # def verifyHash(key):
        #     hash(key)

        def find_index(self,key):
            return self.hashCreate(key) % self.capacity

        def setItem(self,key,value):
            # self.verifyHash(key)

            index = self.find_index(key)

            for element in self.internList[index]:
                if element.key == key:
                    element.value = value
                    return
            
            new_element = self.Element(key, value)
            print(new_element)
            self.internList[index].append(new_element)
            self.length += 1


def main():
    node = HashTable()
    node.setitem('1', 'Joao')


if __name__ == "__main__":
    main()