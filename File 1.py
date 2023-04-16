from googletrans import Translator

import tkinter as tk

# function to translate text

def translate():

    # get user input from entry widget

    text = entry.get()

    # get selected language from drop-down menu

    lang = languages.get()

    # create translator object

    translator = Translator()

    # translate text to selected language

    translation = translator.translate(text, dest=lang)

    # display translated text in label widget

    output.config(text=translation.text)

# create GUI window

window = tk.Tk()

window.title("Google Translate")

# create label widget for user input

label = tk.Label(window, text="Enter text to translate:")

label.pack()

# create entry widget for user input

entry = tk.Entry(window)

entry.pack()

# create label widget for language selection

label2 = tk.Label(window, text="Select language:")

label2.pack()

# create drop-down menu for language selection

languages = tk.StringVar(window)

languages.set('fr') # set default value to French

options = ['fr', 'es', 'de', 'it', 'pt'] # French, Spanish, German, Italian, Portuguese

dropdown = tk.OptionMenu(window, languages, *options)

dropdown.pack()

# create button widget for translation

button = tk.Button(window, text="Translate", command=translate)

button.pack()

# create label widget for translated output

label3 = tk.Label(window, text="Translation:")

label3.pack()

# create label widget to display translated output

output = tk.Label(window, text="")

output.pack()

# run GUI window

window.mainloop()

