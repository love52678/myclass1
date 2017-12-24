class AnonymousSurver:
    def __init__(self,question):
        self.question = question
        self.response = []
    def show_question(self):
        print self.question
    def store_question(self,new_response):
        self.response.append(new_response)

    def show_results(self):
        print 'Survey results:'
        for response in self.response:
            print '-'+response
