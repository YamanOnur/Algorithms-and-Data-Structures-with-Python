class SparseArray():
    class _Node():
        __slots__ = "_element", "_next"
        def __init__(self, element, next):
            self._element=element
            self._next=next
        def __str__(self):
            return str(self._element)
    def __init__(self, length):
        self._data=[None]*length
        self._noods=[]
    def __getitem__(self, index):
        return self._data[index]
    def __setitem__(self, index, value):
        new_nood=self._Node(value, None)
        self._data[index]=new_nood
        self._noods.append(new_nood)
        for n in range(len(self._noods)-1):
            self._noods[n]._next=self._noods[n+1]
print("Note that time complexitiy of __getitem__ is clearly O(1) because this method\n"
      "is one time operation in selected index.\n")
print("Note that time complexity of __setitem__ is O(m) where m is the number of noods in the array\n"
      "when we want to set (m+1)th item as a nood.If we want to set n items to array,it would be\n"
      "worst case(since array length is n),then the time complexity of __setitem__ would be O(n).\n")

