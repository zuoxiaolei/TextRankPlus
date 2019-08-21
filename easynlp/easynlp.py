from .utils import stringPrepareHandle


class EasyNLP:
    '''
    easy use toolkit for nlp
    '''

    def __init__(self):
        pass

    def get_keyword(self, raw_text, algorithm='textrank'):
        if algorithm == 'textrank':
            return stringPrepareHandle.get_sort_keyword(raw_text)
        else:
            raise NotImplementedError

    def get_keysentence(self, raw_text, algorithm='textrank'):
        if algorithm == 'textrank':
            return stringPrepareHandle.get_sort_keyword(raw_text)
        else:
            raise NotImplementedError


easynlp = EasyNLP()
