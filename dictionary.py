import resources

class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        with open(path,'r', encoding="utf-8") as f:
            righe = f.readlines()
            for riga in righe:
                parola_pulita = riga.strip().lower()
                self._dict.append(parola_pulita)


    def printAll(self):
        for p in self._dict:
            print(p)


    @property
    def dict(self):
        return self._dict