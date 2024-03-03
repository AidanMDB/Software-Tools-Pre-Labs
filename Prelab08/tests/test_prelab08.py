# ######################################################
# Author : Aidan Dannhausen-Brun
# email : adannhau@purdue.edu
# ID : ee364a10
# Date : 3/3/2024
# ######################################################

import unittest
import sys
sys.path.insert(0, "./")
from src import convertToBoolean as task1
from src import convertToInteger as task2
from src import getStreakProduct as task3

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

class TestSuite(unittest.TestCase):

    def test_convertToBoolean(self):

        with self.subTest(name="Normal Input Test"):
            expected_list = [True, False, False, False, False, False, False, False]
            actual_list = task1.converToBoolean(128, 5)
            self.assertListEqual(expected_list, actual_list)

        with self.subTest(name="Non-Integer Input Test"):
            with self.assertRaises(ValueError):
                task1.converToBoolean(10.543, 7)

                
    def test_getStreakProduct(self):

        with self.subTest(name="180"):
            expected_list = ["549", "5491"]
            actual_list = task3.getStreakProduct("54912346543439485756", 5, 180)
            self.assertListEqual(expected_list, actual_list)

        with self.subTest(name="400"):
            expected_list = ["5445", "54451", "51445", "14455", "144551", "4455", "44551", "45514", "514514", "145145", "45145", ]
            actual_list = task3.getStreakProduct("544514455145145798779789", 6, 400)
            self.assertListEqual(expected_list, actual_list)

        with self.subTest(name="300"):
            expected_list = []
            actual_list = task3.getStreakProduct("11111111111111111111111111111", 3, 300)
            self.assertListEqual(expected_list, actual_list)


    def test_convertToInteger(self):

        with self.subTest(name="Normal Input Test"):
            bool_list = [True, False, True]
            expected_value = 5
            actual_value = task2.convertToInteger(bool_list)
            self.assertEqual(expected_value, actual_value)

        with self.subTest(name="Non-List Test"):
            non_list = "not list"
            expected_value = None
            actual_value = task2.convertToInteger(non_list)
            self.assertEqual(expected_value, actual_value)

        with self.subTest(name="Invalid List Test"):
            invalid_list = [1, 3, 67]
            expected_value = None
            actual_value = task2.convertToInteger(invalid_list)
            self.assertEqual(expected_value, actual_value)

        with self.subTest(name="Empty List Test"):
            empty = []
            expected_value = None
            actual_value = task2.convertToInteger(empty)
            self.assertEqual(expected_value, actual_value)

# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################

if __name__ == '__main__':
    with open('testrun.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)