import random
import webbrowser
from playsound import playsound
from tkinter import *

class RandomNameSelector:
    def __init__(self):
        self.namesAndURLs=[]
        self.currentURL=""
        self.choiceWindow=Tk()
        self.msgWindow=Tk()
        self.msgFunc=self.performSkip
    
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

    def CloseWindow(self):
        self.choiceWindow.destroy()
        self.choiceWindow=Tk()
        self.choiceWindow.withdraw()
        
        self.msgWindow.destroy()
        self.msgWindow=Tk()
        self.msgWindow.withdraw()
        
    
    def OpenURL(self, event):
        self.CloseWindow()
        try:
            if len(self.currentURL) > 0:
                webbrowser.open(self.currentURL.strip())
            self.msgbox("If the collective are satisfied with your tribute.", title="Reckoning...", ok_button="Press here to subjugate next victim.")
        except Exception:
            pass

        self.SelectRandomName()

    def performSkip(self, event):
        self.CloseWindow()
        self.SelectRandomName()

    def msgbox(self, label, title, ok_button):
        lbl=Label(self.msgWindow, text=label, fg='red', font=("Helvetica", 16))
        lbl.place(x=225, y=20, anchor="center")

        okButton=Button(self.msgWindow, text=ok_button, fg='black')
        okButton.place(x=225, y=60, anchor='center')
        okButton.bind('<Button-1>', self.msgFunc) # <Button-1> is left button click.

        self.msgWindow.title(title)
        self.msgWindow.geometry("450x80+10+10")
        self.msgWindow.eval('tk::PlaceWindow . center')
        self.msgWindow.attributes('-topmost',1)  
        self.msgWindow.mainloop()  

    def choicesbox(self, name, title, choices):
        lbl=Label(self.choiceWindow, text=name, fg='red', font=("Helvetica", 16))
        lbl.place(x=150, y=20, anchor='center')

        okButton=Button(self.choiceWindow, text=choices[0], fg='black')
        okButton.place(x=150, y=60, anchor='center')
        okButton.bind('<Button-1>', self.OpenURL) # <Button-1> is left button click.

        skipButton=Button(self.choiceWindow, text=choices[1], fg='black')
        skipButton.place(x=150, y=100, anchor='center')
        skipButton.bind('<Button-1>', self.performSkip) # <Button-1> is left button click.
        
        self.choiceWindow.title(title)
        self.choiceWindow.geometry("300x140+10+10")
        self.choiceWindow.eval('tk::PlaceWindow . center')
        self.choiceWindow.attributes('-topmost',1)  
        self.choiceWindow.mainloop()  

    def finish(self):
        self.msgFunc=self.exit
        try:
            playsound('sounds/ThatsAllFolks.mp3')
        except Exception:
            pass
        self.msgbox("That's all folks.", title="Finisher...",ok_button="Get back to work.")
        
    def exit(self, event):
        self.msgWindow.destroy()
        self.choiceWindow.destroy()
        exit


    def SelectRandomName(self):
        if len(self.namesAndURLs) > 0:
            try:
                playsound('sounds/DrumRoll.wav')
            except Exception:
                pass
            
            nameAndURL = random.choice(self.namesAndURLs)
            nameAndUrlList = nameAndURL.split(",")
            name=nameAndUrlList[0].strip()
            
            skipPhrase="Spare from subjugation"
            continuePhrase="Press here to being subjugation..."
            
            try:
                self.currentURL=nameAndUrlList[1]
            except Exception:
                self.currentURL=""

            self.namesAndURLs.remove(nameAndURL)

            self.choicesbox(name, title="Victim...",choices=[continuePhrase, skipPhrase])
        else:
              self.finish()
        
if __name__ == "__main__":
    rns = RandomNameSelector()
    rns.CloseWindow()
    if (rns.LoadNames('names.txt')):
        rns.SelectRandomName()
