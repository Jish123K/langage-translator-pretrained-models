import os

import sys

import io

import time

import threading

import numpy as np

import matplotlib.pyplot as plt

from tqdm import tqdm

from transformers import MarianMTModel, MarianMTTokenizer

# Load the MarianMT model and tokenizer

model = MarianMTModel.from_pretrained("facebook/mbart-large-en-ro")

tokenizer = MarianMTTokenizer.from_pretrained("facebook/mbart-large-en-ro")

# Define the function that will translate the code

def translate_code(code, target_lang):

    # Tokenize the code

    code_tokens = tokenizer(code, return_tensors="pt")

    # Translate the code

    translated_code = model.generate(code_tokens, target_lang=target_lang)

    # Decode the translated code

    translated_code = tokenizer.decode(translated_code, skip_special_tokens=True)

    return translated_code

# Define the function that will create the graphic interface

def create_gui():

    # Create the main window

    main_window = tk.Tk()

    # Create the code entry field

    code_entry_field = tk.Entry(main_window)

    code_entry_field.pack()

    # Create the target language dropdown menu

    target_language_dropdown = tk.OptionMenu(main_window, variable=target_language,

                                              values=["en", "ro"])

    target_language_dropdown.pack()
    target_language_dropdown.pack()

    # Create the translate button

    translate_button = tk.Button(main_window, text="Translate", command=translate)

    translate_button.pack()

    # Create the output text box

    output_text_box = tk.Text(main_window)

    output_text_box.pack()

    # Start the main loop

    main_window.mainloop()

# Define the function that will translate the code and update the output text box

def translate():

    # Get the code from the entry field

    code = code_entry_field.get()

    # Get the target language from the dropdown menu

    target_lang = target_language.get()

    # Translate the code

    translated_code = translate_code(code, target_lang)

    # Update the output text box

    output_text_box.delete("1.0", "end")

    output_text_box.insert("1.0", translated_code)

# Define the main function

def main():

    # Create the graphic interface

    create_gui()

if __name__ == "__main__":

    main()
