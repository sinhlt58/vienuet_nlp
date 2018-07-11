"""
Statement pre-processors.
"""


def preprocess_vi(chatbot, statement):
    """
    Remove any consecutive whitespace characters from the statement text.
    """
    import re
    import pyvi.ViTokenizer as tokenizer

    tokenized_text = tokenizer.tokenize(statement.text)
    statement.add_extra_data('tokenized_text', tokenized_text)

    #statement.text = statement.text.lower()

    return statement