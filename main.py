import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input("Scegli cosa vuoi fare inserendo il numero corrispondente. Inserire un numero: ").strip()
    if not (txtIn.isdigit()):
        print("Errore: inserisci un numero valido.")
        continue
    if int(txtIn) < 1 or int(txtIn) > 4:
        print("Errore: inserisci un numero valido.")
        continue


    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn,"italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        parola_pulita = sc.replaceChars(txtIn)
        sc.handleSentence(txtIn,"english")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn,"spanish")
        continue

    if int(txtIn) == 4:
        break


