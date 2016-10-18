import unittest
from copy import deepcopy

ready = True
if ready:
    from code import normalize, SudokuNode, solveSimpleSudoku
else:
    from solution import normalize, SudokuNode, solveSimpleSudoku

class TestNormalize(unittest.TestCase):
    def test0(self):
        dist = {"a":1,"b":2,"c":1}
        result = normalize(dist)

        # make sure dist wasn't mutated
        self.assertEqual(dist['a'], 1)
        self.assertEqual(dist['b'], 2)
        self.assertEqual(dist['c'], 1)

        # make sure dist wasn't mutated
        self.assertAlmostEqual(result['a'], 0.25, places=3)
        self.assertAlmostEqual(result['b'], 0.5, places=3)
        self.assertAlmostEqual(result['c'], 0.25, places=3)

class TestSudokuNode(unittest.TestCase):
    def test0(self):
        node = SudokuNode(4)
        # make sure it uses uniform distribution
        self.assertAlmostEqual(node.dist[1], 0.25, places=3)
        self.assertAlmostEqual(node.dist[2], 0.25, places=3)
        self.assertAlmostEqual(node.dist[3], 0.25, places=3)
        self.assertAlmostEqual(node.dist[4], 0.25, places=3)

    def test1(self):
        node = SudokuNode(2, {1:0.25,2:0.75})
        # make sure it uses dist parameter
        self.assertAlmostEqual(node.dist[1], 0.25, places=3)
        self.assertAlmostEqual(node.dist[2], 0.75, places=3)

    def test2(self):
        node = SudokuNode(2, {1:1,2:3})
        # make sure it normalizes dist parameter
        self.assertAlmostEqual(node.dist[1], 0.25, places=3)
        self.assertAlmostEqual(node.dist[2], 0.75, places=3)

    def test3(self):
        node = SudokuNode(3)
        node.receive({1:1.0})
        # make sure receive works properly
        self.assertAlmostEqual(node.dist[1], 1.0, places=3)
        self.assertAlmostEqual(node.dist[2], 0.0, places=3)
        self.assertAlmostEqual(node.dist[3], 0.0, places=3)

    def test4(self):
        node = SudokuNode(3,{1:0.5,2:0.5,3:0.0})
        node.receive({2:0.8,3:0.2})
        # make sure receive works properly
        self.assertAlmostEqual(node.dist[1], 0.0, places=3)
        self.assertAlmostEqual(node.dist[2], 1.0, places=3)
        self.assertAlmostEqual(node.dist[3], 0.0, places=3)

    def test5(self):
        node1 = SudokuNode(3)
        node2 = SudokuNode(3,{1:0.25,2:0.25,3:0.5})
        node1.add(node2)
        node1.send()
        # make sure it sending from a node with a uniform distribution
        # doesn't actually change anything
        self.assertAlmostEqual(node2.dist[1], 0.25, places=3)
        self.assertAlmostEqual(node2.dist[2], 0.25, places=3)
        self.assertAlmostEqual(node2.dist[3], 0.5, places=3)

    def test6(self):
        node1 = SudokuNode(3,{1:1.0})
        node2 = SudokuNode(3,{1:0.5,2:0.25,3:0.25})
        node3 = SudokuNode(3,{1:0.25,2:0.5,3:0.25})
        node1.add(node2).add(node3)
        node1.send()

        self.assertAlmostEqual(node2.dist[1], 0, places=3)
        self.assertAlmostEqual(node2.dist[2], 0.5, places=3)
        self.assertAlmostEqual(node2.dist[3], 0.5, places=3)

        self.assertAlmostEqual(node3.dist[1], 0, places=3)
        self.assertAlmostEqual(node3.dist[2], 2.0/3.0, places=3)
        self.assertAlmostEqual(node3.dist[3], 1.0/3.0, places=3)

if __name__ == '__main__':
    unittest.main(exit=False)
    print("Unit tests complete. Attempting to solve a 3x3 sudoku puzzle...")
    solveSimpleSudoku()
