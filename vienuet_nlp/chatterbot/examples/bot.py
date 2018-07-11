from vienuet_nlp.chatterbot.bots import VietnameseFQABot
import json

bot = VietnameseFQABot("fqa", database_name='fqa-test')

fqa_data = json.load(open('fqna_data.json', encoding='utf-8'))

bot.train(fqa_data)

while True:
    try:
        response_text = bot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break