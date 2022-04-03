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
        #Button Param
        self.button = QPushButton("Generate",self)
        self.button.setGeometry(100,90,200,25)
        self.button.clicked.connect(self.generate_pass)

        #PassGen Text Param
        self.text_window = QTextEdit(self)
        self.text_window.setReadOnly(True)
        self.text_window.setGeometry(100,50,200,25)

        #SaveFor Param
        self.save_for = QTextEdit(self)
        self.save_for.setReadOnly(False)
        self.save_for.setGeometry(175,10,75,25)
        #self.save_for.setHtml("<p align=\"center\">{}".format("test"))

        #Length Param
        self.length_window = QTextEdit(self)
        self.length_window.setReadOnly(False)
        self.length_window.setGeometry(60,10,25,25)

        #Text 
        self.length_text = QLabel(self)
        self.length_text.setText("Length:")
        self.length_text.setGeometry(15,14,40,15)
        self.pass_for_text = QLabel(self)
        self.pass_for_text.setText("Pass for:")
        self.pass_for_text.setGeometry(130,14,40,15)

    def generate_pass(self):
        password = _main(random.randint(10,30))
        print(self.length_window.toPlainText())
        print(type(self.length_window.toPlainText()))
        self.text_window.setHtml("<p align=\"center\">{}".format(password))
        #_save(self.password, save_for.toPlainText())
        

def main():
    app    = QApplication(sys.argv)
    window = GenApplication()
    app.exit(app.exec())

if __name__ == '__main__':
    main()

