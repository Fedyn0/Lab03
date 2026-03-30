import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multidizionario = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        language = language.capitalize()
        lista = txtIn.split()
        print(lista)
        start = time.time()
        for word in lista:
            self.multidizionario.searchWord(word, language)
        end = time.time()
        tempo_impiegato = end - start
        print(f"Tempo impiegato: {tempo_impiegato}")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    @staticmethod
    def replaceChars(text):
        chars = "\\`'*_{}[]()>#+-.!$%^;,=_~?:§°/&£"
        for c in chars:
            text = text.replace(c, "")
        text = text.lower()
        return text