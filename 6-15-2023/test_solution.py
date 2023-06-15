from solution import Solution
import unittest
from ast import literal_eval

class TestSolution(unittest.TestCase):
    def test_solution(self):
        with open('6-15-2023/testcases.txt') as ifile: 
            for iline in ifile:
                with self.subTest(line=iline):
                    iline = iline.strip("\n")
                    lineList = iline.split(", ")
                    solutionPost = []
                    solutionPre = Solution.groupAnagrams(self, literal_eval(lineList[0]))
                    for elem in solutionPre:
                        solutionPost.append(sorted(elem))

                    self.assertEqual(sorted(solutionPost), sorted(literal_eval(lineList[1])))

if __name__ == '__main__':
    unittest.main()

