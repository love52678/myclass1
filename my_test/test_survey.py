import unittest
from survey import AnonymousSurver
class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "what language did you first learn to speak?"
        my_survey = AnonymousSurver(question)
        my_survey.store_question('English')
        self.assertIn('English',my_survey.response)

    def test_store_three_response(self):
        question = "what language did you first learn to speak?"
        my_survey = AnonymousSurver(question)
        responses = ['Chinese','English','Janpa']
        for response in responses:
            my_survey.store_question(response)
        for response in responses:
            self.assertIn(response,my_survey.response)
unittest.main()