import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dizionari = {}

    def printDic(self, language):
        self._check_and_load(language)
        lingua_esatta =language.capitalize()
        self.dizionari[lingua_esatta].printAll()

    def searchWord(self, word, language):
        self._check_and_load(language)
        lingua_esatta =language.capitalize()
        dizionario = self.dizionari[lingua_esatta].dict
        parola_ricca = rw.RichWord(word)
        if word in dizionario:
            parola_ricca.corretta = True
        else:
            parola_ricca.corretta = False
        return parola_ricca

    def searchWordLinear(self, word, language):
        self._check_and_load(language)
        lingua_esatta =language.capitalize()
        dizionario = self.dizionari[lingua_esatta].dict
        parola_ricca = rw.RichWord(word)
        parola_ricca.corretta = False
        for parola in dizionario:
            if parola == word:
                parola_ricca.corretta = True
                break
        return parola_ricca

    def searchWordDichotomic(self, word, language):

        self._check_and_load(language)
        lingua_esatta = language.capitalize()
        dizionario = self.dizionari[lingua_esatta].dict
        parola_ricca = rw.RichWord(word)

        inizio = 0
        fine = len(dizionario) - 1
        meta = (inizio + fine ) // 2

        parola_ricca.corretta = False

        while inizio <= fine:

            if word == dizionario[meta]:
                parola_ricca.corretta = True
                break
            elif word > dizionario[meta]:
                inizio = meta + 1
            elif word < dizionario[meta]:
                fine = meta - 1
            meta = (inizio + fine ) // 2

        return parola_ricca

    def _check_and_load(self, language):
        language = language.capitalize()
        if language not in self.dizionari:
            nuovo_dizionario = d.Dictionary()
            nuovo_dizionario.loadDictionary(f"resources/{language}.txt")
            self.dizionari[language] = nuovo_dizionario
