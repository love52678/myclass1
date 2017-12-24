from survey import AnonymousSurver
question = 'what language did you first learn to speak?'
my_survey = AnonymousSurver(question)
my_survey.show_question()
print "Enter 'q' at any time to quit.\n"
while True:
    respose = raw_input("language:")
    if respose == 'q':
        break
    my_survey.store_question(respose)
print "\nThank you to everyOne who participated in the survey!"
my_survey.show_results()