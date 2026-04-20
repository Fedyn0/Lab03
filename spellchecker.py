import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multidizionario = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        language = language.capitalize()
        lista = txtIn.split()

        self.multidizionario._check_and_load(language)

        print("------------------------------------")
        print("Using contains")

        parole_errate = []
        start = time.time()

        for word in lista:
            risultato = self.multidizionario.searchWord(word, language)
            if risultato.corretta == False:
                parole_errate.append(risultato)

        end = time.time()

        if len(parole_errate) == 0:
            print("Errori trovati: 0")
            print(f"Time elapsed: {end - start} seconds")

        else:
            print("Errori trovati:")
            for errore in parole_errate:
                print(errore)
            print(f"Time elapsed: {end - start} seconds")

        print("------------------------------------")
        print("Using Linear Research")

        parole_errate_linear = []
        start_linear = time.time()

        for word in lista:
            risultato = self.multidizionario.searchWordLinear(word, language)
            if risultato.corretta == False:
                parole_errate_linear.append(risultato)

        end_linear = time.time()

        if len(parole_errate_linear) == 0:
            print("Errori trovati: 0")
            print(f"Time elapsed: {end_linear - start_linear} seconds")

        else:
            print("Errori trovati:")
            for errore in parole_errate_linear:
                print(errore)
            print(f"Time elapsed: {end_linear - start_linear} seconds")

        print("------------------------------------")
        print("Using Dichotomic Research")

        parole_errate_dichotomic = []
        start_dichotomic = time.perf_counter()

        for word in lista:
            risultato = self.multidizionario.searchWordDichotomic(word, language)
            if risultato.corretta == False:
                parole_errate_dichotomic.append(risultato)

        end_dichotomic = time.perf_counter()

        if len(parole_errate_dichotomic) == 0:
            print("Errori trovati: 0")
            print(f"Time elapsed: {end_dichotomic - start_dichotomic} seconds")

        else:
            print("Errori trovati:")
            for errore in parole_errate_dichotomic:
                print(errore)
            print(f"Time elapsed: {end_dichotomic - start_dichotomic} seconds")



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
        chars = "\\`'*_{}[]()>#+-.!$%^;,=_~?:§°/&£123456789"
        for c in chars:
            text = text.replace(c, "")
        text = text.lower()
        return text