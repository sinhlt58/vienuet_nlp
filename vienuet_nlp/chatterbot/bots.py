from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

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
        super().set_trainer(ListTrainer)

class VietnameseFQABot(ChatBot):

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
            read_only=True          
        )
        super().set_trainer(ListTrainer)