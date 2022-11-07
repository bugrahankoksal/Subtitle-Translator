from googletrans import Translator
import pysrt
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import * 
from PyQt5 import QtWidgets, QtCore

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Translator'
        self.left = 700
        self.top = 200
        self.width = 600
        self.height = 300
        self.initUI()
        QMessageBox.about(self, "Nasil Kullanilir?", "Cevirmek istediginiz altyaziyi dosyasinin path'ini (ornek= /home/bugrahan/Desktop/yenidosya/Midsommar-2019-30fps-EN.srt) soldaki kutuya, cevirmek istediginiz dilin universal kodunu (english=en, german=de, turkish=tr, french=fr, russian=ru, italian=it et cetera) sagdaki kutuya girip butona basiniz. ")
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLineEdit(self)
        self.textbox.move(50, 50)
        self.textbox.resize(500,50)
        
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(552, 50)
        self.textbox2.resize(30,50)

        self.button = QPushButton('Cevir!', self)
        self.button.move(50,150)
       
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        lang = self.textbox2.text()
        QMessageBox.question(self, 'Ceviri', "Islem bitince bilgilendirileceksiniz, biraz zaman alabilir. Cevrilecek Altyazi: " + textboxValue, QMessageBox.Ok)

        subs = pysrt.open(textboxValue)
        

        c=0
        while True:

            sub = subs[c]
        
            translated_sub = Translator().translate(sub.text, dest=lang)
            sub.text = translated_sub.text
            print(c)
            print(translated_sub.text)
            c=c+1
            if c > len(subs)-1:
                QMessageBox.about(self, "Sonuc", "Islem tamamlandi, yeni altyazi dosyasi eskisiyle ayni dizinde.")
                break
        reverse_index = textboxValue[::-1].find("/")
        yeniisim = textboxValue[:len(textboxValue)-reverse_index]+"TR-"+textboxValue[len(textboxValue)-reverse_index:len(textboxValue)-3]+".srt"
        

        subs.save(yeniisim, encoding='utf-8')
        print("bitti.")
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec()
    
    

    









