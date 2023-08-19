from collections import UserDict


class BidirectionalDict(UserDict):
    def __getitem__(self, item):
        if item in self:
            return super().__getitem__(item)

        elif item in list(self.values()):
            return [i for i, j in self.items() if j == item][0]

        else:
            return "Value not found in either key or value"

    def __len__(self):
        return super().__len__()  // 2

    def __delitem__(self, item):
        super().__delitem__(self[item])
        super().__delitem__(item)

    def __setitem__(self, key, value):

        if key in self:
            del self[key]

        if value in self:
            del self[value]

        super().__setitem__(key,value)
        super().__setitem__(value,key)


b1 = BidirectionalDict({'x': 'y', 'y': 'x', 'a': 'b', 'b': 'a', 'c': 'd', 'e': 'f'})

print(b1)
# print(len(b1))


# del b1['x']
# del b1['a']
# del b1['g']
#
# b1['u']='v'
#
# print(b1)
