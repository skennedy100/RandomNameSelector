import random
import easygui as gui
import webbrowser
from playsound import playsound

class RandomNameSelector:
    def __init__(self):
        self.namesAndURLs=[]

    def LoadNames(self, filename):
        status = True
        try:
            file = open(filename, 'r')

            for line in file:
                self.namesAndURLs.append(line.strip())

            file.close()
        except FileNotFoundError:
            print('Invalid file path:', filename)
            status = False

        return status

    def SelectRandomNames(self):
        length = len(self.namesAndURLs)
        i = 0
        while i < length:
            try:
                playsound('sounds/DrumRoll.wav')
            except Exception:
                pass
            
            nameAndURL = random.choice(self.namesAndURLs)
            nameAndUrlList = nameAndURL.split(",")
            name=nameAndUrlList[0]
            gui.msgbox(name, title="Victim",ok_button="Press here to being subjugation...")
            
            try:
                url=nameAndUrlList[1]
                if len(url) > 0:
                    webbrowser.open(url.strip())
            except Exception:
                pass
            
            self.namesAndURLs.remove(nameAndURL)
            i = i + 1
            gui.msgbox("If the collective are Satisfied with your tribute.", title="Proceeding...",ok_button="Press here to subjugate next victim.")

if __name__ == "__main__":
    rns = RandomNameSelector()
    if (rns.LoadNames('names.txt')):
        rns.SelectRandomNames()
