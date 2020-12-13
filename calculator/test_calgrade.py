from calgrade import calGrade
import unittest


class test_Calculator(unittest.TestCase):
    def testCalGradeA(self):
        self.assertEqual(calGrade(80),"A") 

    def testCalGradeB(self):
        self.assertEqual(calGrade(70),"B")

    def testCalGradeC(self):
        self.assertEqual(calGrade(60),"C")

    def testCalGradeD(self):
        self.assertEqual(calGrade(50),"D")

    def testCalGradeF(self):
        self.assertEqual(calGrade(40),"F")


  