# a11_2_4_test_survey_setUp().py
# 测试AnonymousSurvey类的一个行为store_response()
# 测试用例包含setUp()属性和两个测试：setUp(),_single_response()和_three_responses()

import unittest
from a11_2_2_c_AnonymousSurvey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试。"""
    
    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用。
        """
        question = "Which language can you speak?"
        self.my_survey = AnonymousSurvey(question)
        self.my_responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储。"""
        self.my_survey.store_response(self.my_responses[0])
        self.assertIn(self.my_responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """ 测试三个答案会被妥善地存储。
            第一个for循环，遍历属性列表my_resonses元素，存储到类的列表中responses
            第二个for循环，遍历属性列表元素，使用assertIn()方法检查属性列表元素是否存储在类列表中responses
        """
        for response in self.my_responses:
            self.my_survey.store_response(response)
        for my_response in self.my_responses:
            self.assertIn(my_response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()