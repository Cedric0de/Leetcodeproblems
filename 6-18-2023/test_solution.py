from solution import Solution
import unittest
from ast import literal_eval

class TestSolution(unittest.TestCase):
    def test_solution(self):
        with open('6-18-2023/testcases.txt') as ifile: 
            for iline in ifile:
                with self.subTest(line=iline):
                    iline = iline.strip("\n")
                    lineList = iline.split(", ")
                    self.assertEqual(Solution.isValidSudoku(self, literal_eval(lineList[0])), literal_eval(lineList[1]))

if __name__ == '__main__':
    unittest.main()