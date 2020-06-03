from Reg import check_time 

import unittest

class TestReg(unittest.TestCase):
    def test_secs(self):
        case="12:45 PM"
        expected=True
        self.assertEqual(check_time(case),expected)
    
    def test_sec(self):
        case="6:60am"
        expected=True
        self.assertEqual(check_time(case),expected)
    


unittest.main()