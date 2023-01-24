import unittest


class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("#" * 30)
        print("I will run before all test")
        print("#" * 30)

    def test_methodA(self):
        print("running method A")

    def test_methodB(self):
        print("running method B")

    def test_assert_true(self):
        a = True
        self.assertTrue(a, "as is not true")
        b = False
        self.assertFalse(b, "b is not true")

    def test_assertEqual(self):
        a = 'Text'
        b = 'Text'
        self.assertEqual(a, b, "a is not equal to b")

    @classmethod
    def tearDownClass(cls):
        print("#" * 30)
        print("I will run after all test")
        print("#" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)
