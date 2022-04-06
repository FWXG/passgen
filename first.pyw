import sys
import random
from PyQt5.QtWidgets import QApplication, QTextEdit, QPlainTextEdit,QLineEdit, QWidget, QPushButton, QMainWindow,QLabel, QCheckBox, QMessageBox, QMenu, QAction,QDialog
from PyQt5.QtCore import QObject, Qt

def len_err():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Length Error")
    msg.setWindowTitle("PassGen")
    msg.exec_()

def name_err():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Name Error")
    msg.setWindowTitle("PassGen")
    msg.exec_()

def pass_name_info():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Password was saved")
    msg.setWindowTitle("PassGen")
    msg.exec_()

def _main(length):
    count = 0
    res   = ""

    while count < length:
        res   += chr(random.randint(33,125))
        count += 1
    return res

def _save(my_pass,pass_for):
    path = pass_for
    with open("{}.txt".format(path), "w") as file:
        file.write(my_pass)
        
    

class GenApplication(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self._createActions()
        self._createMenuBar()


        #Screen param
        self.setWindowTitle("PassGen")
        self.setFixedWidth(400)
        self.setFixedHeight(150)
        
        #Main UI param
        self.UIComponents()
        self.show()

    def UIComponents(self):
        #Button Param
        self.button = QPushButton("Generate",self)
        self.button.setGeometry(100,110,200,25)
        self.button.clicked.connect(self._generate_pass)

        #PassGen Text Param
        self.text_window = QLineEdit(self)
        self.text_window.setReadOnly(True)
        self.text_window.setGeometry(100,75,200,25)

        #SaveFor Param
        self.save_for = QLineEdit(self)
        self.save_for.setReadOnly(False)
        self.save_for.setMaxLength(10)
        self.save_for.setGeometry(175,30,75,25)

        #Length Param
        self.length_window = QLineEdit(self)
        self.length_window.setReadOnly(False)
        self.length_window.setAlignment(Qt.AlignCenter)
        self.length_window.setMaxLength(2)
        self.length_window.setGeometry(60,30,25,25)

        #Text 
        self.length_text   = QLabel(self)
        self.length_text.setText("Length:")
        self.length_text.setGeometry(15,34,40,15)
        self.pass_for_text = QLabel(self)
        self.pass_for_text.setText("Password for:")
        self.pass_for_text.setGeometry(105,34,70,15)
        self.hide_pass = QLabel(self)
        self.hide_pass.setText("Hide password:")
        self.hide_pass.setGeometry(265,34,80,15)

        #CheckBox ShowPassword
        self.show_pass = QCheckBox(self)
        self.show_pass.setGeometry(347,33, 20, 20)

        #CheckBox Numbers
        #self.show_pass = QCheckBox(self)
        #self.show_pass.setGeometry(347,35, 20, 20)

        #CheckBox Symbol
        #self.show_pass = QCheckBox(self)
        #self.show_pass.setGeometry(347,57, 20, 20)

        #CheckBox Letters
        #self.show_pass = QCheckBox(self)
        #self.show_pass.setGeometry(347,79, 20, 20)
        

    def _generate_pass(self):
        length = self.length_window.text()
        print(type(length), length)

        if length == "" or length.isalpha():
            len_err()
            return 0
        
        if length and int(length) > 30 or int(length) < 1:
            len_err()
            self.length_window.clear()
            return 0

        if self.save_for.text() == "":
            name_err()
            return 0

        if self.show_pass.isChecked():
            print(True)
            self.text_window.setEchoMode(QLineEdit.Password)
        else:
            self.text_window.setEchoMode(QLineEdit.Normal)
                 
        password = _main(int(length))
        self.text_window.setAlignment(Qt.AlignCenter)
        self.text_window.setText(password)
        _save(password, self.save_for.text())
        pass_name_info()

    def _createMenuBar(self):
        menuBar  = self.menuBar()
        fileMenu = QMenu('&File',self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        editMenu = menuBar.addMenu('&Edit')
        helpMenu = menuBar.addMenu('&Help')

    def _createActions(self):
        self.newAction = QAction(self)
        self.newAction.setText('&New')
        self.openAction = QAction('&Open...',self)
        self.saveAction = QAction('&Save',self)
        
    def keyPressEvent(self, event):
        #print(event.text())
        if event.key() == Qt.Key_Enter:
            self._generate_pass()

        

def main():
    app    = QApplication(sys.argv)
    window = GenApplication()
    app.exit(app.exec())

if __name__ == '__main__':
    main()

