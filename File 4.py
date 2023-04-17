import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton

from transformers import pipeline

class CodeTranslator(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(100, 100, 800, 600)

        self.setWindowTitle('Code Translator')

        self.inputTextEdit = QTextEdit(self)

        self.outputTextEdit = QTextEdit(self)

        self.translateButton = QPushButton('Translate', self)

        self.translateButton.clicked.connect(self.translateCode)

        vbox = QVBoxLayout()

        vbox.addWidget(self.inputTextEdit)

        vbox.addWidget(self.outputTextEdit)

        vbox.addWidget(self.translateButton)

        self.setLayout(vbox)

    def translateCode(self):

        input_text = self.inputTextEdit.toPlainText()

        translator = pipeline('translation_en_to_es')

        output_text = translator(input_text, max_length=1000)[0]['translation_text']

        self.outputTextEdit.setText(output_text)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    translator = CodeTranslator()

    translator.show()

    sys.exit(app.exec_())

