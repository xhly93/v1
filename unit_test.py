import unittest

import pytest


class Test_py(unittest.TestCase):
    def setUp(self):
        print('setUp')
        pass

    def tearDown(self):
        print('tearDown')
        pass



    def test_01(self):
        print('3333333')
        pass

    def test_02(self):
        print('002')
        aa
        pass


    @classmethod
    def setUpClass(cls):
        print('setUpClass')
        pass

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
        pass


if __name__ == '__main__':
    # pytest.main(["s", "-q", "--alluredir", "./report"])
    # pytest.main('--alluredir = C:/Users/Administrator/.jenkins/workspace/test/allure-result')
    suit = unittest.TestSuite()
    suit.addTest(Test_py('test_01'))
    suit.addTest(Test_py('test_02'))
    runner = unittest.TextTestRunner()
    runner.run(suit)
