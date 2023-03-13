import unittest
import requests


class TestAPI(unittest.TestCase):

    def test1(self):
        resp = requests.get("http://10.0.2.15:5000/")
        self.assertEqual(resp.status_code, 200)
        print("test1: OK")

    def test2(self):
        resp = requests.get("http://10.0.2.15:5000/class")
        self.assertEqual(resp.status_code, 200)
        print("test2: OK")

    def test3(self):
        resp = requests.post("http://10.0.2.15:5000/login")
        self.assertEqual(resp.status_code, 200)
        print("test3: OK")


if __name__ == '__main__':
    tester = TestAPI()
    tester.test1()
    tester.test2()
    tester.test3()