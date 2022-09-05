import os

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

directory = './data'


def getmyresponse(question):
    my_bot = ChatBot(name='MedBot', read_only=True,
                     logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                     {'import_path': 'chatterbot.logic.BestMatch',
                                      'default_response': 'I am sorry, but I do not understand.',
                                      'maximum_similarity_threshold': 0.90}],
                     preprocessors=['chatterbot.preprocessors.clean_whitespace',
                                    'chatterbot.preprocessors.unescape_html',
                                    'chatterbot.preprocessors.convert_to_ascii'])

    corpus_trainer = ChatterBotCorpusTrainer(my_bot)

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        if os.path.isfile(f):
            corpus_trainer.train(f.replace("\\", "/"))

    return my_bot.get_response(question)
