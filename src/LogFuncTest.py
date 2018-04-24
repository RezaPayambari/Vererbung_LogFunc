import unittest
import LogFunc
from AndGate import AndGate
from OrGate import OrGate
from NandGate import NandGate

class AndGateTest(unittest.TestCase):

    def testcase_01(self):
        a=AndGate()
        a.Input0=False
        a.Input1=False
        a.execute()
        self.assertFalse(a.Output,"Class ANDKlasse: TestCase 1 failed.")

    def testcase_02(self):
        a=AndGate()
        a.Input0=True
        a.Input1=False
        a.execute()
        self.assertFalse(a.Output,"Class ANDKlasse: TestCase 1 failed.")
        
    def testcase_03(self):
        a=AndGate()
        a.Input0=False
        a.Input1=True
        a.execute()
        self.assertFalse(a.Output,"Class ANDKlasse: TestCase 1 failed.")

    def testcase_04(self):
        a=AndGate()
        a.Input0=True
        a.Input1=True
        a.execute()
        self.assertTrue(a.Output,"Class ANDKlasse: TestCase 1 failed.")

class OrGateTest(unittest.TestCase):

    def testcase_01(self):
        a=OrGate()
        a.Input0=False
        a.Input1=False
        a.execute()
        self.assertFalse(a.Output,"Class OrGate: TestCase 1 failed.")

    def testcase_02(self):
        a=OrGate()
        a.Input0=True
        a.Input1=False
        a.execute()
        self.assertTrue(a.Output,"Class OrGate: TestCase 1 failed.")
        
    def testcase_03(self):
        a=OrGate()
        a.Input0=False
        a.Input1=True
        a.execute()
        self.assertTrue(a.Output,"Class OrGate: TestCase 1 failed.")

    def testcase_04(self):
        a=OrGate()
        a.Input0=True
        a.Input1=True
        a.execute()
        self.assertTrue(a.Output,"Class OrGate: TestCase 1 failed.")


class NandGateTest(unittest.TestCase):

    def testcase_01(self):
        a=NandGate()
        a.Input0=False
        a.Input1=False
        a.execute()
        self.assertTrue(a.Output,"Class NandGate: TestCase 1 failed.")

    def testcase_02(self):
        a=NandGate()
        a.Input0=True
        a.Input1=False
        a.execute()
        self.assertTrue(a.Output,"Class NandGate: TestCase 1 failed.")
        
    def testcase_03(self):
        a=NandGate()
        a.Input0=False
        a.Input1=True
        a.execute()
        self.assertTrue(a.Output,"Class NandGate: TestCase 1 failed.")

    def testcase_04(self):
        a=NandGate()
        a.Input0=True
        a.Input1=True
        a.execute()
        self.assertFalse(a.Output,"Class NandGate: TestCase 1 failed.")


if  __name__ == "__main__" :
    unittest.main()
