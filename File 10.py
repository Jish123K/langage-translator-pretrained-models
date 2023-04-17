import tkinter as tk

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Define the translation function

def translate(text, src_lang, dst_lang):

  # Load the translation model and tokenizer

  tokenizer = AutoTokenizer.from_pretrained(f"Helsinki-NLP/opus-mt-{src_lang}-{dst_lang}")

  model = AutoModelForSeq2SeqLM.from_pretrained(f"Helsinki-NLP/opus-mt-{src_lang}-{dst_lang}")

  # Encode the text

  encoded_input = tokenizer(text, return_tensors="pt")

  # Generate the translation

  output = model.generate(**encoded_input)

  # Decode the translation

  translated_text = tokenizer.batch_decode(output, skip_special_tokens=True)[0]

  # Return the translation

  return translated_text

# Create the main window

root = tk.Tk()

# Create the input text box

input_text = tk.Entry(root)

# Create the source language label

source_language_label = tk.Label(root, text="Source Language")

# Create the source language dropdown menu

source_language_dropdown = tk.OptionMenu(root, "", "en", "de", "fr", "es", "it", "pt")

# Create the destination language label

destination_language_label = tk.Label(root, text="Destination Language")

# Create the destination language dropdown menu

destination_language_dropdown = tk.OptionMenu(root, "", "en", "de", "fr", "es", "it", "pt")

# Create the translate button

translate_button = tk.Button(root, text="Translate", command=lambda: translate(input_text.get(), source_language_dropdown.get(), destination_language_dropdown.get()))
# Pack all the widgets

input_text.pack()

source_language_label.pack()

source_language_dropdown.pack()

destination_language_label.pack()

destination_language_dropdown.pack()

translate_button.pack()

# Start the main loop

root.mainloop()
