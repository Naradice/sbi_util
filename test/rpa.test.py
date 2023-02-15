import json
import os
import sys
import unittest

import dotenv

base_dir = os.path.dirname(__file__)
env_file = os.path.join(base_dir, ".env")
dotenv.load_dotenv(env_file)


if "sbi_id" not in os.environ:
    raise Exception("env file is required")

try:
    import sbi_util
except ImportError:
    try:
        module_path = os.path.abspath(os.path.join(base_dir, ".."))
        sys.path.append(module_path)
    except Exception as e:
        raise e

import sbi_util.rpa as rpa


class TestStockRPA(unittest.TestCase):
    client = rpa.STOCK(os.environ["sbi_id"], os.environ["sbi_password"], os.environ["sbi_trade_password"])

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def test_get_buget(self):
        buget = self.client.get_available_budget()
        self.assertGreaterEqual(buget, 0)

    def test_get_a_rating(self):
        rating = self.client.get_rating("8031")
        self.assertTrue(type(rating), dict)
        print(rating)

    def test_get_ratings(self):
        rating = self.client.get_ratings(["1928", "8031", "5108"])
        self.assertTrue(type(rating), dict)
        print(rating)


if __name__ == "__main__":
    unittest.main()
