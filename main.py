import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input("Scegli la lingua inserendo il numero corrispondente. Inserire un numero: ").strip()
    if not (txtIn.isdigit()):
        print("Errore: inserisci un numero valido.")
        continue
    if int(txtIn) < 1 or int(txtIn) > 4:
        print("Errore: inserisci un numero valido.")
        continue


    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        frase_pulita = sc.replaceChars(txtIn)
        sc.handleSentence(frase_pulita,"italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        frase_pulita = sc.replaceChars(txtIn)
        sc.handleSentence(frase_pulita,"english")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        frase_pulita = sc.replaceChars(txtIn)
        sc.handleSentence(frase_pulita,"spanish")
        continue

    if int(txtIn) == 4:
        break


