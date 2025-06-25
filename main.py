import sys 
import os
from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QApplication, QFileDialog
from PyQt5 import QtWidgets

class File_name_editor_app(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.configure_window()

        layout = QtWidgets.QFormLayout()

        self.label = QLabel("")
        self.select_directory_button = QPushButton("Wybierz folder")

        layout.addWidget(self.select_directory_button)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.select_directory_button.clicked.connect(self.select_directory_action)

    def configure_window(self):
        self.setWindowTitle("app")
        self.setMinimumSize(400, 400)

    def select_directory_action(self):
        file_directory = str(QFileDialog.getExistingDirectory(self, "Wybierz odpowiedni folder"))
        self.label.setText(file_directory)

        try:
            files = [file_name for file_name in os.listdir(file_directory)]
        except FileNotFoundError as e: #nie dziala 
            print(e)
            files = []

        if not files:
            self.label.setText("Brak plików do zmiany")
            



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = File_name_editor_app()

    window.show()
    sys.exit(app.exec_())