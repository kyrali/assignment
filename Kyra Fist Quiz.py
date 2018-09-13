import unittest
import random
import itertools
# Given a string (e.g. "What the hell?"), returns a list of the following pattern
# ['What the hell?', 'What the hell', 'What the hel', 'What the he', 'What the h', 'What the ',
#  'What the', 'What th', 'What t', 'What ', 'What', 'Wha', 'Wh', 'W']
def input_nput_put_ut_t(input_str: str) ->list:
    a=[]
    b=len(input_str)
    for n in range (1,b+1):       
        a.append(input_str[:n])   # make the list of the following pattern
    a.reverse()                   # make the order from long string to short string
    return a 
    raise NotImplementedError()

# add two vectors
def vector_addition(v1: list, v2: list) -> list:
    a=[]
    for b in range (0,len(v1)):
        c=v1[b]+v2[b]             # make the numbers add successively
        a.append(c)
    return a
    raise NotImplementedError()

# given two lists of integers, find a slice in list 1 and a slice in list 2 whose sums are equal
# using enumeration is fine
def find_equal_sum_slice(list1: list, list2: list) -> [int, int, int, int]:
    for i in range(0,len(list1)):
        for j in range(0,len(list1)):
            a=list1[i:j]                   # choose a slice in list 1
            for b in range(0,len(list2)):
                for c in range(0,len(list2)):
                    d=list2[b:c]           # choose a slice in list 2
                    if a!=[] and d != [] and sum(a) == sum(d):   # make sure the two slices are equal and the all slices are not empty 
                        return i,j-1,b,c-1
    raise NotImplementedError()

# use a sorting algorithm (your choice) to sort a list of ten unsorted integers. Do not use the python sort function.
def basic_sort(int_list: list) -> list:
    a=[]
    for j in range (1,10):                    
        b=int_list[0]
        for i in range (0,len(int_list)-1):   # choose the smallest number in the list
            if b<int_list[i+1]:
                continue
            elif b>int_list[i+1]:
                b=int_list[i+1]
        a.append(b)                          # put it in list a
        int_list.remove(b)                   # remove it
        j=j+1                                # do it again and again, make sure every time just choose the smallest number in the present int_list 
    a.append(int_list[0])                    # put the last number in int_list into list a
    return a
    
    raise NotImplementedError()		

# A well-known NP-complete problem
# Given a set of integers, find a non-empty subset (if exists) summing to a given number k
# Note: make use of itertools.combinations. See python documentation online
def subset_sum(s: set or list or tuple, k: int) -> set or list or tuple:

    raise NotImplementedError()

class UnitTest(unittest.TestCase):
    def test_input(self):
        self.assertEqual(input_nput_put_ut_t("What the hell?"),
                         ['What the hell?', 'What the hell', 'What the hel', 'What the he', 'What the h', 'What the ',
                          'What the', 'What th', 'What t', 'What ', 'What', 'Wha', 'Wh', 'W']
                         )
    def test_eq_sum_slice(self):
        for i in range(10):
            list1 = [random.randint(0, 150) for i in range(150)]
            list2 = [random.randint(0, 60) for i in range(75)]
            a, b, c, d = find_equal_sum_slice(list1, list2)
            s1, s2 = sum(list1[a:b + 1]), sum(list2[c:d + 1])
            self.assertEqual(s1, s2)
    def test_add_vectors(self):
        self.assertEqual(vector_addition([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(vector_addition([1], [-1]), [0])
    def test_basic_sort(self):
        self.assertEqual([1,3,5,7,9,11,13,15,17,10000], basic_sort([3,1,5,7,9,11,15,17,10000,13]))  
    def test_subset_sum(self):
        s = {random.randint(-200, 200) for i in range(random.randint(100))}
        k = random.randint(-50, 50)
        subset = subset_sum(s, k)
        self.assertTrue(set(subset).issubset(s))
        self.assertEqual(sum(subset), k)
if __name__ == "__main__":
    unittest.main()
