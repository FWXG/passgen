import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QVBoxLayout


def _main(length):
    count = 0
    res   = ""
    while count < length:
        res   += chr(random.randint(33,125))
        count += 1
    return res

def _save(my_pass,pass_for):
    path = pass_for
    with open("all_pass/{}.txt".format(path), "w") as file:
        file.write(my_pass)
        
        

class GenApplication(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PassGen")
        self.setFixedWidth(400)
        self.setFixedHeight(200)

        

def main():
    app    = QApplication([])

    window = GenApplication()
    layout = QVBoxLayout()

    layout.addWidget(QPushButton("QQQ"))
    window.setLayout(layout)
    window.show()


    app.exec()

if __name__ == '__main__':
    main()

