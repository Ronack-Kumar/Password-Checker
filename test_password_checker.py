
import unittest
from password_checker import check_password_strength

class TestPasswordStrength(unittest.TestCase):
    
    def test_weak_passwords(self):
        # Too short
        res = check_password_strength("1234567")
        self.assertEqual(res['strength'], "Weak")
        self.assertTrue(any("too short" in f for f in res['feedback']))

        # Only 1 type (lowercase)
        res = check_password_strength("abcdefgh")
        self.assertEqual(res['strength'], "Weak")
        
        # Only 2 types (lower + digit)
        res = check_password_strength("password123")
        self.assertEqual(res['strength'], "Weak")

    def test_medium_passwords(self):
        # 3 types (Upper, Lower, Digit)
        res = check_password_strength("Password1")
        self.assertEqual(res['strength'], "Medium")
        
        # 3 types (Lower, Digit, Special)
        res = check_password_strength("pass123!")
        self.assertEqual(res['strength'], "Medium")

    def test_strong_passwords(self):
        # All 4 types
        res = check_password_strength("P@ssword1")
        self.assertEqual(res['strength'], "Strong")
        self.assertEqual(len(res['criteria_met']), 5) # 4 types + length

    def test_edge_cases(self):
        # Empty string
        res = check_password_strength("")
        self.assertEqual(res['strength'], "Weak")
        
        # Long string with only one char type
        res = check_password_strength("a" * 100)
        self.assertEqual(res['strength'], "Weak")
        
if __name__ == '__main__':
    unittest.main()
