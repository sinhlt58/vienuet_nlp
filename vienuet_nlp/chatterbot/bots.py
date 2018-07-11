from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from vienuet_nlp.chatterbot.trainers import ViFQAListTrainer

class EnglishSimpleBot(ChatBot):
    
    def __init__(self, name):
        super().__init__(name,
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            input_adapter='chatterbot.input.TerminalAdapter',
            output_adapter='chatterbot.output.TerminalAdapter',
            logic_adapters=[
                # 'chatterbot.logic.MathematicalEvaluation',
                # 'chatterbot.logic.TimeLogicAdapter',
                "chatterbot.logic.BestMatch"
            ],
            database='./database.sqlite3',
            read_only=False          
        )
        super().set_trainer(ChatterBotCorpusTrainer)

class VietnameseFQABot(ChatBot):

    def __init__(self, name, database_name):
        super().__init__(name,
            input_adapter='chatterbot.input.TerminalAdapter',
            output_adapter='chatterbot.output.TerminalAdapter',
            preprocessors=[
                'vienuet_nlp.chatterbot.preprocessors.preprocess_vi'
            ],
            logic_adapters=[
                # 'chatterbot.logic.MathematicalEvaluation',
                # 'chatterbot.logic.TimeLogicAdapter',
                {
                    'import_path': 'chatterbot.logic.BestMatch'
                },
                {
                    'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                    'threshold': 0.4,
                    'default_response': 'Xin lỗi mình không hiểu.'
                }
            ],
            storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
            database=database_name,
            read_only=True
        )
        super().set_trainer(ViFQAListTrainer)