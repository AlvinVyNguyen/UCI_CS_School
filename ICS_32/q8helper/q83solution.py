from   bag import Bag
import unittest  # use unittest.TestCase
import random    # use random.shuffle,random.randint

#random.shuffle(alist) mutates its alist argument, to be a random permutation
#random.randint(1,10)  returns a random number in the range 1-10 inclusive


class Test_Bag(unittest.TestCase):
    def setUp(self):
        self.alist = ['d','a','b','d','c','b','d']
        self.bag = Bag(self.alist)
    
    def test_len(self):
        if len(self.bag) != 7:
            raise
        count = 0
        random.shuffle(self.alist)
        count += 7
        for i in self.alist:
            self.bag.remove(i)
            count -= 1
            if len(self.bag) != count:
                raise
        if len(self.bag) != 0:
            raise
        
    def test_unique(self):
        if self.bag.unique() != 4:
            raise
        random.shuffle(self.alist)
        for i in self.alist:
            self.bag.remove(i)
            if self.bag.unique() != len(set(self.bag)):
                raise
        
    def test_contains(self):
        for i in ['a','b','c','d']:
            if i not in self.bag:
                raise
        if 'x' in self.bag:
            raise 
        
    def test_count(self):
        for a,b in zip(('a','b','c','d'), (1,2, 1, 3)):
            if self.bag.count(a) != b:
                raise
        random.shuffle(self.alist)
        size = 7
        for i in self.alist:
            self.bag.remove(i)
            size -= 1
            sum_count = sum([self.bag.count(c) for c in ['a','b','c','d']])
            if sum_count != size:
                raise
        if len(self.bag) != 0:
            raise

        
    def test_equals(self):
        alist = []
        for i in range(1000):
            alist.append(random.randint(1,10))
        b1 = Bag(alist)
        random.shuffle(alist)
        b2 = Bag(alist)
        if b1 != b2:
            raise
        b1.remove(alist[0])
        if b1 == b2:
            raise
        
    def test_add(self):
        alist = []
        for i in range(1000):
            alist.append(random.randint(1,10))
        b1 = Bag(alist)
        random.shuffle(alist)
        b2 = Bag()
        for a in alist:
            b2.add(a)
        if b1 != b2:
            raise
        
    def test_remove(self):
        alist = []
        for i in range(1000):
            alist.append(random.randint(1,10))
        b1 = Bag(alist)
        self.assertRaises(ValueError,b1.remove,11)
        b2 = Bag(alist)
        random.shuffle(alist)
        for v in alist:
            b2.add(v)
        for v in alist:
            b2.remove(v)
        if b1 != b2:
            raise
