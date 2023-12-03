import json
import pickle


class HashTable:
    def __init__(self):
        self.hash_table = []
        self.keys = {}

    def add_key(self, word):
        self.keys[word.lower()] = len(self.hash_table)
        self.hash_table.append(word.lower())

    def check_word(self, word):
        index = self.keys.get(word.lower())
        if index is not None and self.hash_table[index] == word.lower():
            return True
        return False


def save_hash(hash, file):
    # profanities.pkl
    # Save the object to a pickle file
    with open(file, 'wb') as pickle_file:
        pickle.dump(hash, pickle_file)



def load_hash(file):
    # Read the object from the pickle file
    hash_obj = HashTable()

    with open(file, 'rb') as pickle_file:
        data = pickle.load(pickle_file)
        hash_obj.hash_table = data.hash_table
        hash_obj.keys = data.keys

    return hash_obj


'''
if __name__ == "__main__":
    
    hash_table = HashTable()
    f = open("profanity.txt", "r")
    for x in f:
        hash_table.add_key(x[:-1])
        #print(x[:-1])
    save_hash(hash_table, 'profanities.pkl')
    
    hash_table = load_hash('profanities.pkl')
    print(hash_table.check_word("EjaKulate"))
'''