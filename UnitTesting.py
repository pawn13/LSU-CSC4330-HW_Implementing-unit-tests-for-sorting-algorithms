import unittest
import random

class TestMergeSort(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(mergeSort([5, 2, 8, 4, 9, 6], 0, 5), [2, 4, 5, 6, 8, 9])

    def test_negative(self):
        with self.assertRaises(TypeError, msg="Input should be an array"):
            mergeSort(2, 4, 3)
        with self.assertRaises(NameError, msg="Variables must be defined"):
            mergeSort([4, 2, 3, 1], s, 4)

    def test_performance(self):
        size = random.randint(1000, 5000)
        sorting_array = [random.randint(0, 100) for _ in range(size)]
        result = mergeSort(sorting_array, 0, size - 1)
        self.assertEqual(result, sorted(sorting_array))

    def test_boundary(self):
        with self.assertRaises(SyntaxError, msg="Empty Array"):
            mergeSort([], 0, 0)
        self.assertEqual(mergeSort([1], 0, 0), [1])
        self.assertEqual(mergeSort([2, 2, 2], 0, 2), [2, 2, 2])

    def test_idempotency(self):
        array = [5, 2, 8, 4, 9, 6]
        sorted_once = mergeSort(array[:], 0, len(array) - 1)
        for _ in range(10):
            self.assertEqual(mergeSort(array[:], 0, len(array) - 1), sorted_once)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if not isinstance(arr, list):
        raise TypeError("Input should be an array")
    if not isinstance(l, int) or not isinstance(r, int):
        raise TypeError("Indices should be integers")

    if len(arr) == 0:
        raise SyntaxError("Empty Array")
    
    if l < 0 or r >= len(arr):
        raise IndexError("Indices out of bounds")

    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
    return arr

if __name__ == '__main__':
    unittest.main()
