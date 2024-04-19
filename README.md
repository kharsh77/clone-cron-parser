import unittest
from expression_parser import ExpressionParser
from datetime import datetime

datetime_str = '30/04/22 21:30:00'
time_obj= datetime.strptime(datetime_str, '%d/%m/%y %H:%M:%S')

class TestClass(unittest.TestCase):
    def test_expression_1(self):
        expected_dict_output= {'Command': ['/usr/bin/find'],
            'DayOfMonth': [1, 11, 21, 31],
            'DayOfWeek': [1, 2, 3, 4, 5, 6, 7],
            'Hour': [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],
            'Minute': [0, 30],
            'Month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}
        e = ExpressionParser("*/30 */2 */10 * * /usr/bin/find")
        assert e.expand() == expected_dict_output

    def test_expression_2(self):
        expected_dict_output= {'Command': ['/usr/bin/find'],
            'DayOfMonth': [1, 15],
            'DayOfWeek': [1, 2, 3, 4, 5],
            'Hour': 0,
            'Minute': [0, 15, 30, 45],
            'Month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}
        e = ExpressionParser("*/15 0 1,15 * 1-5 /usr/bin/find")
        assert e.expand() == expected_dict_output

    def test_expression_3(self):
        expected_dict_output= {'Command': ['/usr/bin/find'],
            'DayOfMonth': 15,
            'DayOfWeek': [1, 2, 3, 4, 5],
            'Hour': [10],
            'Minute': 30,
            'Month': 'JAN'}
        e = ExpressionParser("30 10/20 15 JAN 1-5 /usr/bin/find")
        assert e.expand() == expected_dict_output

    def test_expression_4(self):
        expected_dict_output= {'Command': ['/usr/bin/find'],
            'DayOfMonth': [1, 15],
            'DayOfWeek': ['MON', 'TUE', 'WED'],
            'Hour': 22,
            'Minute': 10,
            'Month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}
        e = ExpressionParser("10 22 1,15 * MON,TUE,WED /usr/bin/find")
        assert e.expand() == expected_dict_output

    def test_expression_5(self):
        expected_dict_output= {'Command': ['/usr/bin/find'],
            'DayOfMonth': [1, 15],
            'DayOfWeek': [1, 2, 3, 4, 5],
            'Hour': 0,
            'Minute': [0, 15, 30, 45],
            'Month': ['JAN', 'JUL']}
        e = ExpressionParser("*/15 0 1,15 JAN,JUL 1-5 /usr/bin/find")
        assert e.expand() == expected_dict_output

	