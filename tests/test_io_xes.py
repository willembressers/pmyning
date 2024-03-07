# python core packages
import unittest
from pathlib import Path

# 3rd party packages
import pandas as pd

# custom packages
import pmyning as pmy

# GLOBALS
CURRENT_DIR = Path(__file__).resolve().parent


class TestIOXES(unittest.TestCase):
    def test_read_xes(self):
        df = pmy.read_xes(CURRENT_DIR / "assets" / "general_example.xes")
        self.assertEqual(type(df), pd.DataFrame)


if __name__ == "__main__":
    unittest.main()
