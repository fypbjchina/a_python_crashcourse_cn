# a11_1_3_test_name_function_fml.py
# 创建类NamesTestCase,继承unittest.TestCase
# unittest 类最有用的功能之一：断言方法, 调用方法unittest.assertEqual()
# 测试用例，def一个方法，未通过的测试情况

import unittest
from a11_1_3_f_name_function_fml import get_fml_name

class NamesTestCase(unittest.TestCase):
    """测试a11_1_3_f_name_function.py"""
    
    def test_first_last_name(self):
        """能够正确地处理像Zhang san这样的姓名吗？"""
        test_name = get_fml_name('san', 'zhang')
        self.assertEqual(test_name, 'San Zhang')
    
if __name__ == '__main__':
    unittest.main()