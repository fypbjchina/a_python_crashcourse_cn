# a11_2_3b_test_survey_single_three.py
# 测试AnonymousSurvey类的一个行为store_response()
# 测试用例包含两个测试：测试单个输入_single_response()和多个输入_three_responses()

import unittest
from a11_2_2_c_AnonymousSurvey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试。"""
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储。"""
        question = "Which language can you speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
        
    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储。"""
        question = "Which language can you speak?"
        my_survey = AnonymousSurvey(question)
        my_responses = ['English', 'Spanish', 'Mandarin']
        for response in my_responses:
            my_survey.store_response(response)
        
        for my_response in my_responses:
            self.assertIn(my_response, my_survey.responses)
        
if __name__ == '__main__':
    unittest.main()