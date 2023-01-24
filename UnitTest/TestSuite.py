import unittest

from UnitTest.TestCase_Demo import TestCaseDemo

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo)

smoke_test = unittest.TestSuite([tc1])
unittest.TextTestRunner(verbosity=2).run(smoke_test)