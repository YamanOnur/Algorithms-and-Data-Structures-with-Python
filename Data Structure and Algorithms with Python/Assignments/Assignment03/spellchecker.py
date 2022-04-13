from collections.abc import MutableMapping
from abc import abstractmethod
from random import randrange

class MapBase(MutableMapping):

    class _Item:
        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key

class UnsortedTableMap(MapBase):

    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError("KeyError: " + repr(k))

    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError("KeyError: " + repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key

class HashMapBase(MapBase):

    def __init__(self, cap=11, p=109345121):
        self._table = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v

    @abstractmethod
    def _bucket_getitem(self, j, k):
        pass

    @abstractmethod
    def _bucket_setitem(self, j, k, v):
        pass

    @abstractmethod
    def _bucket_delitem(self, j, k):
        pass

    @abstractmethod
    def __iter__(self):
        pass

class ChainHashMap(HashMapBase):
    lst=[]
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("KeyError: " + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if not j in self.lst:
            self.lst.append(j)
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: " + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

print("Note that you should initiate SpellChecker object as SpellChecker(data_file_path)"
      "\nwhere data_file_path is the path of the most common 10.000 words of English")

class SpellChecker:

    def __init__(self, data_file_path):
        self.hash_table = ChainHashMap()
        data = open(data_file_path, "r")
        for d in data.readlines():
            d = d.strip()
            if len(d) > 5:
                self.hash_table[d] = d
        data.close()

    def check(self, input_path):
        table = self.hash_table
        input_file = open(input_path, "r")
        input_words = input_file.read().split()
        input_file.close()
        chars = [chr(i) for i in range(97,123)]
        output_file = open("output.Assignment3.OnurYaman.txt", "w")

        def construct_each_line(word):
            word = word.lower()
            try:return table[word] + " --> OK"
            except:
                recommend_list = []
                recommend_list.append(word)
                recommend_list.append(" --> ")
                for i in range(len(word)):
                    _word = word[0:i] + word[i+1:len(word)]
                    try:recommend_list.append(table[_word] + ",")
                    except:pass
                    for j in range(len(chars)):
                        word_ = word[0:i] + chars[j] + word[i:len(word)]
                        if i == len(word) - 1:
                            word_ = word + chars[j]
                        try:recommend_list.append(table[word_] + ",")
                        except:pass
                if len(recommend_list) == 2:
                    recommend_list.append("No Recommendation")
                recommend_list = recommend_list[0:4]
                return "".join(recommend_list).strip(",")

        for word in input_words:
            line = construct_each_line(word)
            output_file.write(line)
            output_file.write("\n")
        output_file.close()