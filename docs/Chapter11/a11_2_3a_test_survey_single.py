# a11_2_3a_test_survey_single.py
# 测试AnonymousSurvey类的一个行为store_response()

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
        
if __name__ == '__main__':
    unittest.main()