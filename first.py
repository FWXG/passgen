import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QMainWindow, QLabel, QVBoxLayout


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
        


    

class GenApplication(QMainWindow):

    password = _main(random.randint(10,30))
    _str = ""
    
    def __init__(self):
        super().__init__()

        #Screen param
        self.setWindowTitle("PassGen")
        self.setFixedWidth(400)
        self.setFixedHeight(150)
        
        #Button param
        self.UIComponents()
        self.show()


    def UIComponents(self):
        #Button param
        button = QPushButton("Generate",self)
        button.setGeometry(100,90,200,25)
        button.clicked.connect(self.generate_pass)
        print(self._str)

        text_window = QTextEdit(self)
        text_window.setReadOnly(True)
        text_window.setGeometry(100,50,200,25)
        text_window.setHtml("<p align=\"center\">{}".format(self.password))

    def generate_pass(self):
        self.password = _main(random.randint(10,30))
        _str = self.password
        

def main():
    app    = QApplication(sys.argv)
    window = GenApplication()
    app.exit(app.exec())

if __name__ == '__main__':
    main()

