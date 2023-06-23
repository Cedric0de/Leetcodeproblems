from solution import MinStack
import unittest
from ast import literal_eval

class TestSolution(unittest.TestCase):
    def test_solution(self):
        with open('6-22-2023/testcases.txt') as ifile: 
            for iline in ifile:
                with self.subTest(line=iline):
                    iline = iline.strip("\n")
                    lineList = iline.split(", ")
                    for i in range(len(literal_eval(lineList[0]))):
                        if literal_eval(lineList[0])[i] == "MinStack":
                            obj = MinStack()
                        if literal_eval(lineList[0])[i] == "push":
                            obj.push(literal_eval(lineList[1])[i])
                        if literal_eval(lineList[0])[i] == "pop":
                            obj.pop()
                        if literal_eval(lineList[0])[i] == "top":
                            param_3 = obj.top()[0]
                            self.assertEqual(param_3, literal_eval(lineList[2])[i])
                        if literal_eval(lineList[0])[i] == "getMin":
                            param_4 = obj.getMin()[0]
                            self.assertEqual(param_4, literal_eval(lineList[2])[i])

if __name__ == '__main__':
    unittest.main()