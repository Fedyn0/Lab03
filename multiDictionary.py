import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dizionari = {}

    def printDic(self, language):
        language = language.capitalize()
        if language not in self.dizionari:
            nuovo_dizionario = d.Dictionary()
            nuovo_dizionario.loadDictionary(f"resources/{language}.txt")
            self.dizionari[language] = nuovo_dizionario
        self.dizionari[language].printAll()


    def searchWord(self, words, language):
        pass


