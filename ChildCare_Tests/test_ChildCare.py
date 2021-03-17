import unittest
import sys
sys.path.append('./PublishPythonLibChildCare')
import ChildCare as ChildCare_Class

# Unit tests for the ChildCare Class
class TestChildCare(unittest.TestCase):
    # New class instance
    cc = ChildCare_Class.ChildCare()

    # Valid test for function set_category with 
    # valid value "Tageseinrichtung"
    def test_0_set_category(self):
        self.cc.set_category("Tageseinrichtung")        
        result = self.cc.get_category()
        self.assertIs(result, "Tageseinrichtung")

    # Valid test for function set_category with 
    # valid value "Tagespflege"
    def test_1_set_category(self):
        self.cc.set_category("Tagespflege")        
        result = self.cc.get_category()
        self.assertIs(result, "Tagespflege")

    # Invalid test for function set_category with 
    # a not allowed value
    def test_2_set_category(self):
        with self.assertRaises(Exception) as context:
            self.cc.set_category("Tagesmutter") 
        self.assertTrue("Type of care facility not allowed." 
            in str(context.exception))

    # Valid test for function set_num_kids with 
    # none-negativ integers
    def test_0_set_num_kids(self):
        num = ["123", "456" , "789"]
        self.cc.set_num_kids(num)        
        result = self.cc.get_num_kids()
        self.assertListEqual(result, num)    

    # Valid test for function set_num_kids with 
    # allowed character "X" (meaning "value not available")
    def test_1_set_num_kids(self):
        num = ["X", "4562" , "7389"]
        self.cc.set_num_kids(num) 
        result = self.cc.get_num_kids()
        self.assertListEqual(result, ["0", "4562", "7389"])  

    # Invalid test for function set_num_kids with 
    # characters, but not numbers
    def test_2_set_num_kids(self):
        num = ["X", "y" , "abc"]
        with self.assertRaises(Exception) as context:
            self.cc.set_num_kids(num)
        self.assertTrue("Only X, 0 and positiv numbers are allowed."
            in str(context.exception))

    # Invalid test for function set_num_kids with 
    # negativ number
    def test_3_set_num_kids(self):
        num = ["36145", "-78" , "0"]
        with self.assertRaises(Exception) as context:
            self.cc.set_num_kids(num)
        self.assertTrue("Only X, 0 and positiv numbers are allowed."
            in str(context.exception))

    # Valid test for function set_num_lunches with 
    # allowed values
    def test_0_set_num_lunches(self):
        num = "98561"
        self.cc.set_num_lunches(num)        
        result = self.cc.get_num_lunches()
        self.assertEqual(result, num)    

    # Valid test for function set_num_lunches with 
    # allowed character "X" (meaning "value not available")
    def test_1_set_num_lunches(self):
        num = "X"
        self.cc.set_num_lunches(num) 
        result = self.cc.get_num_lunches()
        self.assertEqual(result, "0")  

    # Invalid test for function set_num_lunches with 
    # characters, but not numbers
    def test_2_set_num_lunches(self):
        num = "abc"
        with self.assertRaises(Exception) as context:
            self.cc.set_num_lunches(num)
        self.assertTrue("Only X, 0 and positiv numbers are allowed."
            in str(context.exception))

    # Invalid test for function set_num_lunches with 
    # negativ number
    def test_3_set_num_lunches(self):
        num = "-2378"
        with self.assertRaises(Exception) as context:
            self.cc.set_num_lunches(num)
        self.assertTrue("Only X, 0 and positiv numbers are allowed."
            in str(context.exception))

    # Valid test for function set_year with 
    # valid values between 2007 and 2020
    def test_0_set_year(self):
        self.cc.set_year("2018")        
        result = self.cc.get_year()
        self.assertEqual(result, "2018")

    # Invalid test for function set_year with 
    # out-of-range values 
    def test_1_set_year(self):
        with self.assertRaises(Exception) as context:
            self.cc.set_year("2001")
        self.assertTrue("Only years between 2007 and 2020 are allowed." 
            in str(context.exception))

    # Invalid test for function set_year with 
    # characters as year value
    def test_2_set_year(self):
        with self.assertRaises(Exception) as context:
            self.cc.set_year("10xy")
        self.assertTrue("Only years between 2007 and 2020 are allowed." 
            in str(context.exception))
            
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()