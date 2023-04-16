import tkinter as tk

import marianmt

class TranslatorGUI:

    def __init__(self, master):

        self.master = master

        master.title("Translator")

        self.source_label = tk.Label(master, text="Source Language:")

        self.source_label.grid(row=0, column=0)

        self.source_entry = tk.Entry(master)

        self.source_entry.grid(row=0, column=1)

        self.target_label = tk.Label(master, text="Target Language:")

        self.target_label.grid(row=1, column=0)

        self.target_entry = tk.Entry(master)

        self.target_entry.grid(row=1, column=1)

        self.input_label = tk.Label(master, text="Input Text:")

        self.input_label.grid(row=2, column=0)

        self.input_entry = tk.Entry(master)

        self.input_entry.grid(row=2, column=1)

        self.output_label = tk.Label(master, text="Translated Text:")

        self.output_label.grid(row=3, column=0)

        self.output_text = tk.Text(master, height=5, width=40)

        self.output_text.grid(row=3, column=1)

        self.translate_button = tk.Button(master, text="Translate",

                                          command=self.translate)

        self.translate_button.grid(row=4, column=1)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)

        self.quit_button.grid(row=4, column=0)

    def translate(self):

        # Load the model

        model = marianmt.Translator(

            source_language=self.source_entry.get(),

            target_language=self.target_entry.get(),

            model_name="Helsinki-NLP/opus-mt-{}-{}".format(

                self.source_entry.get(),

                self.target_entry.get()))

        # Translate the input text

        input_text = self.input_entry.get()

        translation = model.translate(input_text)

        # Update the output text

        self.output_text.delete(1.0, tk.END)

        self.output_text.insert(tk.END, translation)

root = tk.Tk()

translator = TranslatorGUI(root)

root.mainloop()

