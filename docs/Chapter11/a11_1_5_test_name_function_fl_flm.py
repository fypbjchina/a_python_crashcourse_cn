# a11_1_5_test_name_function_fl_flm.py
# 创建类NamesTestCase,继承unittest.TestCase
# unittest 类最有用的功能之一：断言方法, 调用方法unittest.assertEqual()
# 测试用例，def两个方法，测试程序的两种情况
# 方法名必须以test_打头，这样它才会在运行test_xx.py时自动运行

import unittest
from a11_1_4_f_name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试a11_1_4_f_name_function.py"""
    
    def test_first_last_name(self):
        """能够正确地处理像Zhang san这样的姓名吗？"""
        formatted_name = get_formatted_name('san', 'zhang')
        self.assertEqual(formatted_name, 'San Zhang')
        
    def test_first_last_middle_name(self):
        """能够正确地处理像wang xiao wu这样的姓名吗？"""
        formatted_name = get_formatted_name('wu', 'wang', 'xiao')
        self.assertEqual(formatted_name, 'Wu Xiao Wang')
    
if __name__ == '__main__':
    unittest.main()