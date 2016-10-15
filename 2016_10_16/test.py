import unittest
from copy import deepcopy

ready = True
if ready:
    from code import FloodFill
else:
    from solution import FloodFill

class TestFloodFill(unittest.TestCase):
    def test0(self):
        arr = [
            [0, 1],
            [0, 0],
        ]
    	ff = FloodFill(arr)
        res = ff.fill(0, 0, 3)
        self.assertEquals(res[0][0], 3)
        self.assertEquals(res[0][1], 1)
        self.assertEquals(res[1][0], 3)
        self.assertEquals(res[1][1], 3)

    def test1(self):
        arr = [
            [0, 1],
            [1, 0],
        ]
        ff = FloodFill(arr)

        res = ff.fill(0, 1, 2)
        self.assertEquals(res[0][0], 0)
        self.assertEquals(res[0][1], 2)
        self.assertEquals(res[1][0], 1)
        self.assertEquals(res[1][1], 0)

        res = ff.fill(0, 0, 3)
        self.assertEquals(res[0][0], 3)
        self.assertEquals(res[0][1], 1)
        self.assertEquals(res[1][0], 1)
        self.assertEquals(res[1][1], 0)

    def test2(self):
        arr = [[0]*100 for _ in range(100)]
        arr[0][0] = 1

        ff = FloodFill(arr)
        res = ff.fill(1, 1, 2)

        self.assertEquals(res[0][0], 1)
        for i in range(100):
            for j in range(100):
                if i == 0 and j == 0:
                    continue
                self.assertEquals(res[i][j], 2)

    def test3(self):
        arr = [[0]*1000 for _ in range(1000)]
        arr[0][0] = 1

        ff = FloodFill(arr)
        res = ff.fill(1, 1, 2)

        self.assertEquals(res[0][0], 1)
        for i in range(100):
            for j in range(100):
                if i == 0 and j == 0:
                    continue
                self.assertEquals(res[i][j], 2)

if __name__ == '__main__':
    unittest.main()
