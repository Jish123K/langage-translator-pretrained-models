import pytorch_translate

from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.source_language = QComboBox()

        self.target_language = QComboBox()

        self.code_editor = QPlainTextEdit()

        self.translated_code_editor = QPlainTextEdit()

        self.translate_button = QPushButton("Translate")

        self.clear_button = QPushButton("Clear")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.source_language)

        self.layout.addWidget(self.target_language)

        self.layout.addWidget(self.code_editor)

        self.layout.addWidget(self.translated_code_editor)

        self.layout.addWidget(self.translate_button)

        self.layout.addWidget(self.clear_button)

        self.setLayout(self.layout)

        self.source_languages = pytorch_translate.get_available_languages()

        self.target_languages = pytorch_translate.get_available_languages()

        self.source_language.addItems(self.source_languages)

        self.target_language.addItems(self.target_languages)

        self.translate_button.clicked.connect(self.translate)

        self.clear_button.clicked.connect(self.clear)
def translate(self):

        source_language = self.source_language.currentText()

        target_language = self.target_language.currentText()

        code = self.code_editor.toPlainText()

        translated_code = pytorch_translate.translate(code, source_language, target_language)

        self.translated_code_editor.setPlainText(translated_code)

    def clear(self):

        self.code_editor.clear()

        self.translated_code_editor.clear()

if __name__ == "__main__":

    app = QApplication([])

    main_window = MainWindow()

    main_window.show()

    app.exec()
