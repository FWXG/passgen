import sys
import os
import random
import binascii
from PyQt5.QtWidgets import QApplication, QTextEdit, QPlainTextEdit,QLineEdit, \
     QWidget, QPushButton, QMainWindow,QLabel, QCheckBox, QMessageBox, QMenu, QAction,QDialog,QFileDialog
from PyQt5.QtCore import QObject, Qt


class GenApplication(QMainWindow):
    
    def __init__(self):
        super().__init__()
        #Toolbar
        self._createActions()
        self._createMenuBar()
        self._connectActions()

        self.openAction.triggered.connect(self._browsePassword)
        self.saveAction.triggered.connect(self._savePassword)
        #self.openDocs.triggered.connect(self._openDocs)

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
        
    def _generate_pass(self):
        length = self.length_window.text()

        if length == "" or length.isalpha():
            self.len_err()
            return 0
        
        if length and int(length) > 30 or int(length) < 1:
            self.len_err()
            self.length_window.clear()
            return 0

        if self.save_for.text() == "":
            self.name_err()
            return 0

        if self.show_pass.isChecked():
            self.text_window.setEchoMode(QLineEdit.Password)
        else:
            self.text_window.setEchoMode(QLineEdit.Normal)
                 
        self.password = self._main(int(length))
        self.text_window.setAlignment(Qt.AlignCenter)
        self.text_window.setText(self.password)
        #Save from push generate button
        #self._save(self.password, self.save_for.text())
        #self.pass_name_info()

    def _createMenuBar(self):
        menuBar  = self.menuBar()
        fileMenu = QMenu('&File',self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        editMenu = menuBar.addMenu('&Edit')
        editMenu.addAction(self.Letters)
        editMenu.addAction(self.Numbers)
        editMenu.addAction(self.Symbols)
        helpMenu = menuBar.addMenu('&Help')
        helpMenu.addAction(self.openDocs)

    def _createActions(self):
        self.newAction  = QAction(self)
        self.newAction.setText('&New')
        self.openAction = QAction('&Open...',self)
        self.saveAction = QAction('&Save',self)
        self.Letters  = QAction('&Letters', self)
        self.Letters.setCheckable(True)
        self.Letters.setChecked(True)
        self.Numbers  = QAction('&Numbers', self)
        self.Numbers.setCheckable(True)
        self.Numbers.setChecked(True)
        self.Symbols  = QAction('&Symbols', self)
        self.Symbols.setCheckable(True)
        self.Symbols.setChecked(True)
        self.openDocs = QAction('&About', self)

    def _connectActions(self):
        self.newAction.triggered.connect(self._newPass)

    def _newPass(self):
        self.length_window.clear()
        self.save_for.clear()
        self.text_window.clear()

    def _browsePassword(self):
        fname = QFileDialog.getOpenFileName(self,'Open file','*.txt', filter = 'Text Files(.txt)')
        basename = os.path.basename(fname[0])

        with open(fname[0], 'r') as file:
            pass_file = int(file.read(), 2)
            tmp = pass_file.to_bytes((pass_file.bit_length() + 7)// 8 ,'big').decode()
            
        if basename.endswith('.txt'):
            basename = basename[:basename.find('.txt')]

        self.save_for.setText(basename)
        self.length_window.setText(str(len(tmp)))
        self.text_window.setAlignment(Qt.AlignCenter)
        self.text_window.setText(tmp)
        

    def _savePassword(self):
        sname = QFileDialog.getSaveFileName(self,'Save file','{}'.format(self.save_for.text()),\
                                            filter = 'Text Files(.txt)')

        if sname == ('',''):
            return 0
        
        if self.save_for.text() == "":
            self.name_err()
            return 0
        
        self._save(self.password,sname[0])
        self.pass_name_info()

    #def _openDoc(self):
        #with open('doc.txt', 'r') as doc_file:
            #about = doc_file.read()
        
    def keyPressEvent(self, event):
        #print(event.text())
        if event.key() == Qt.Key_Return:
            self._generate_pass()
        elif event.key() == Qt.Key_Enter:
            self._generate_pass()

    def len_err(self):
        self.msg_err = QMessageBox()
        self.msg_err.setIcon(QMessageBox.Critical)
        self.msg_err.setText("<p align='bottom'>Length Error</p>") #Not work
        self.msg_err.setWindowTitle("PassGen")
        self.msg_err.exec_()

    def name_err(self):
        self.msg_nerr = QMessageBox()
        self.msg_nerr.setIcon(QMessageBox.Critical)
        self.msg_nerr.setText("Name Error")
        self.msg_nerr.setWindowTitle("PassGen")
        self.msg_nerr.exec_()

    def pass_name_info(self):
        self.msg_info = QMessageBox()
        self.msg_info.setIcon(QMessageBox.Information)
        self.msg_info.setText("Password was saved")
        self.msg_info.setWindowTitle("PassGen")
        self.msg_info.exec_()

    def _main(self,length):
        count = 0
        res   = ""
        state = 0

        if not self.Letters.isChecked() and not self.Numbers.isChecked() and not self.Symbols.isChecked():
            state = 7
        elif not self.Letters.isChecked() and not self.Numbers.isChecked():
            state = 1
        elif not self.Numbers.isChecked() and not self.Symbols.isChecked():
            state = 2
        elif not self.Letters.isChecked() and not self.Symbols.isChecked():
            state = 3
        elif not self.Numbers.isChecked():
            state = 4
        elif not self.Letters.isChecked():
            state = 5
        elif not self.Symbols.isChecked():
            state = 6


        print(state)

        if state == 0:
            while count < length:
                res   += chr(random.randint(33,126))
                count += 1
            return res
        elif state == 1:
            while count < length:
                tmp = chr(random.randint(33,126))
                if 47 <= ord(tmp) <=57 or 65 <= ord(tmp) <=90 or 97 <= ord(tmp) <=122:
                    continue
                res   += tmp
                count += 1
            return res
        elif state == 2:
            while count < length:
                tmp = chr(random.randint(33,122))
                if 47 <= ord(tmp) <=57 or 33 <= ord(tmp) <=47 or 58 <= ord(tmp) <=64 or\
                   91 <= ord(tmp) <=97:
                    continue
                res   += tmp
                count += 1
            return res
        elif state == 3:
            while count < length:
                tmp = chr(random.randint(33,122))
                if 65 <= ord(tmp) <=90 or 97 <= ord(tmp) <=122 or 33 <= ord(tmp) <=47 or\
                   58 <= ord(tmp) <=64 or 91 <= ord(tmp) <=97:
                    continue
                res   += tmp
                count += 1
            return res
        elif state == 4:
            while count < length:
                tmp = chr(random.randint(33,126))
                if 47 <= ord(tmp) <=57:
                    continue
                res   += tmp
                count += 1
            return res
        elif state == 5:
            while count < length:
                tmp = chr(random.randint(33,126))
                if 65 <= ord(tmp) <=90 or 97 <= ord(tmp) <=122:
                    continue
                res   += tmp
                count += 1
            return res
        elif state == 6:
            while count < length:
                tmp = chr(random.randint(33,122))
                if 33 <= ord(tmp) <=47 or 58 <= ord(tmp) <=64 or 91 <= ord(tmp) <=97:
                    continue
                res   += tmp
                count += 1
            return res
        elif state == 7:
            return ""

            

    def _save(self,my_pass,pass_for):
        path = pass_for
        with open("{}.txt".format(path), "w") as file:
            tmp = bin(int.from_bytes(my_pass.encode(), 'big'))
            file.write(tmp)


def main():
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    app    = QApplication(sys.argv)
    window = GenApplication()
    app.exit(app.exec())

if __name__ == '__main__':
    main()

