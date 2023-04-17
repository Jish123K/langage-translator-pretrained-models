import bert_translate

import tkinter as tk

# Create the main window

root = tk.Tk()

# Create the input and output text boxes

input_text = tk.Text(root)

output_text = tk.Text(root)

# Create the translate button

translate_button = tk.Button(root, text="Translate", command=translate)

# Layout the widgets

input_text.pack()

output_text.pack()

translate_button.pack()

# Bind the translate button to the translate function

translate_button.config(command=translate)

# Define the translate function

def translate():

    # Get the input code

    input_code = input_text.get("1.0", "end-1c")

    # Translate the code

    translated_code = bert_translate.translate(input_code)

    # Set the output code

    output_text.delete("1.0", "end")

    output_text.insert("1.0", translated_code)

# Start the main loop

root.mainloop()
