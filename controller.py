import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def checkLanguage(self, e):
        language = self._view._linguaSelezionata.value
        if language is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! inserire una lingua valida", color="red")
            )
            self._view.page.update()
            return





        self._view._lvOut.controls.append(
            ft.Text("lingua inserita correttamente",
                    color="green")
        )
        self._view.page.update()


    def checkModality(self,e):
        self._view._lvOut.controls.clear()
        modalita=self._view._ricercaSelezionata.value
        if modalita is None :
            self._view.lvOut.controls.append(
                ft.Text("Attenzione modalita inserita incorrettamente",
                        color="red")
            )
            self._view.page.update()
            return False
        self._view._lvOut.controls.append(
            ft.Text("Modalita inserita correttamente",
                    color="green")
        )
        self._view.page.update()


    def handleSpellCheck(self,e):
        self._view._lvOut.controls.clear()
        language = self._view._linguaSelezionata.value
        modalita = self._view._ricercaSelezionata.value
        frase = self._view._txtInFrase.value
        if language is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione inserire una lingua valida",
                        color="red")
            )
            self._view.page.update()
            return

        elif modalita is None:
            self._view._lvOut.controls.clear()
            self._view._lvOut.controls.append(
                ft.Text("Attenzione modalita inserita incorrettamente",
                        color="red")
            )
            self._view.page.update()
            return

        elif frase == "":
            self._view._lvOut.controls.clear()
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! inserire una frase",
                        color="red")
            )
            self._view.page.update()
            return


        else:
            self._view._lvOut.controls.clear()
            self._view._lvOut.controls.append(
                ft.Text(f"frase inserita è : {frase}")
            )
        self._view.page.update()

        paroleErrate,tempo=self.handleSentence(frase, language, modalita)
        self._view._lvOut.controls.append(
            ft.Text(f"parole errate : {paroleErrate} \n tempo richiesto dalla ricerca {tempo}")
        )
        self._view._txtInFrase.value = ""
        self._view.page.update()





    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                tempo=t2-t1
                return paroleErrate,tempo

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                tempo=t2-t1
                return paroleErrate, tempo

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                tempo=t2-t1
                return paroleErrate,tempo
            case _:
                return None

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


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text














