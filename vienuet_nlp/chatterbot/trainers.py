from chatterbot.trainers import Trainer
from chatterbot.conversation import Statement, Response
from chatterbot import utils

class ViFQAListTrainer(Trainer):

    def __init__(self, storage, **kwargs):
        super(ViFQAListTrainer, self).__init__(storage, **kwargs)

    def train(self, data):
        self.logger.info("Start ViFQAListTrainer training...")

        for qna_pair in data:
            answer_text = qna_pair.get('answer')

            questions = qna_pair.get('questions')

            for question_count, question_text in enumerate(questions):
                answer_statement = self.get_or_create(answer_text)
                question_statement = self.get_or_create(question_text)

                answer_statement.add_response(Response(question_text))

                self.storage.update(question_statement)
                self.storage.update(answer_statement)

        self.logger.info("Finished ViFQAListTrainer training!")

class ViFQANerualTrainer(Trainer):

    def __init__(self, storage, **kwargs):
        super(ViFQANerualTrainer, self).__init__(storage, **kwargs)

    def train(self, data):
        pass
        # we will use tensorflow here