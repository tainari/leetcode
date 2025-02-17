class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def print_table(self):
        print(self.data_map)

    def __hash(self, key):
        my_hash = sum([ord(letter) for letter in key]) % len(self.data_map)
        print(f"Hash for key {key} is {my_hash}.")
        return my_hash

    def set_item(self, key, value):
        key_hash = self.__hash(key)
        if not self.data_map[key_hash]:
            self.data_map[key_hash] = []
        for n, pair in enumerate(self.data_map[key_hash]):
            existing_key, existing_value = pair
            if existing_key == key:
                self.data_map[key_hash][n][1] = value
                return True
        self.data_map[key_hash].append([key, value])
        return True

    def get_item(self, key):
        key_hash = self.__hash(key)
        if not self.data_map[key_hash]:
            return None
        for n, pair in enumerate(self.data_map[key_hash]):
            if pair[0] == key:
                return pair[1]
        return None

    def keys(self):
        key_list = []
        for address in self.data_map:
            if not address:
                continue
            for key, value in address:
                key_list.append(key)
        return key_list

hash_table = HashTable()
hash_table.set_item("key", "value")
hash_table.print_table()
hash_table.set_item("different_key", "different_value")
hash_table.print_table()
hash_table.set_item("key", "other value")
hash_table.print_table()
print(hash_table.keys())