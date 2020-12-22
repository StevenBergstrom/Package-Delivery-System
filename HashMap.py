class HashMap:

    def __init__(self):
        self.size = 40
        self.map = [None] * self.size

    def _get_hash(self, key):
        return key % self.size


    def add(self, key, value):
        location = self._get_hash(key)
        key_value = [key, value]

        if self.map[location] is None:
            self.map[location] = list([key_value])
            return
        else:
            for pair in self.map[location]:
                if pair[0] == key:
                    pair[1] == value
                    return
            self.map[location].append(key_value)
            return

    def get(self, key):
        location = self._get_hash(key)
        if self.map[location] is not None:
            for pair in self.map[location]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        location = self._get_hash(key)
        if self.map[location] is not None:
            for i in range(0, len(self.map[location])):
                if self.map[location][i][0] == key:
                    self.map[location].pop(i)
                    return
        else:
            return

    def print(self):
        print('--Packages--')
        for slot in self.map:
            if slot is not None:
                print(slot[0][1].packageID, '|', slot[0][1].address, '|', slot[0][1].deadline, '|', slot[0][1].status, '|', slot[0][1].deliveryTime)

