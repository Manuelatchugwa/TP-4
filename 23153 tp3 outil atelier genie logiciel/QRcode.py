# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QRcode.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap # importation de la pixmap
import qrcode

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(607, 490)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 491, 281))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 410, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 410, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(180, 340, 171, 31))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "image"))
        self.pushButton.setText(_translate("Form", "valider"))
        self.pushButton_2.setText(_translate("Form", "Effacer"))
        self.pushButton.clicked.connect(self.genererQRcode)
        self.pushButton_2.clicked.connect(self.Effacer)

    def genererQRcode(self):
        #recuperer le texte saisi
        texteSaisi = self.textEdit.toPlainText()
        # creation du QRcode en image
        image = qrcode.make(texteSaisi)
        qr = ImageQt(image)
        # creation de la pixmap
        pix = QPixmap. fromImage(qr)
        # afficher la pixmap dans le label
        self.label.setPixmap(pix)
        
    def Effacer(self):
        
        self.textEdit.setText('')   
        self.label.setText('Image')
        
        
        
        
        
if __name__ == "__main__" :
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())