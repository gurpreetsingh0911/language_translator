from tkinter import *
from translate import Translator

print('Translator application')

Screen = Tk()
Screen.title("Language Translation Using Python : Gurpreet 11904073")

input_language = StringVar()
translate_language= StringVar()

LanguageChoices = {'English','Spanish','Hindi', 'French','German','Bengali'}
input_language.set('English')
translate_language.set('Hindi')

def fxn():
    translator = Translator(from_lang= input_language.get(),to_lang=translate_language.get())
    Translation = translator.translate(TextVar.get())
    Output.set(Translation)


# choice for input language
InputLanguageChoiceMenu = OptionMenu(Screen, input_language, *LanguageChoices)
Label(Screen, text="Choose a Language").grid(row=0, column=1)
InputLanguageChoiceMenu.grid(row=1, column=1)

# choice in which the language is to be translated
NewLanguageChoiceMenu = OptionMenu(Screen, translate_language, *LanguageChoices)
Label(Screen, text="Translated Language").grid(row=0, column=2)
NewLanguageChoiceMenu.grid(row=1, column=2)

Label(Screen, text="Enter Text").grid(row=2, column=0)
TextVar = StringVar()
TextBox = Entry(Screen, textvariable=TextVar).grid(row=2, column=1)

Label(Screen, text="Output Text").grid(row=2, column=2)
Output = StringVar()
TextBox = Entry(Screen, textvariable=Output).grid(row=2, column=3)

# Button for calling function
B = Button(Screen, text="Translate", command=fxn, relief=GROOVE).grid(row=3, column=1, columnspan=3)

mainloop()