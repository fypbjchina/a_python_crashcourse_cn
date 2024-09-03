# a11_1_4_test_name_function_flm.py
# 创建类NamesTestCase,继承unittest.TestCase
# unittest 类最有用的功能之一：断言方法, 调用方法unittest.assertEqual()
# 测试用例，def一个方法，未通过的测试情况

import unittest
from a11_1_4_f_name_function_flm import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试a11_1_4_f_name_function.py"""
    
    def test_first_last_name(self):
        """能够正确地处理像Zhang San这样的姓名吗？"""
        formatted_name = get_formatted_name('san', 'zhang')
        self.assertEqual(formatted_name, 'San Zhang')
    
if __name__ == '__main__':
    unittest.main()