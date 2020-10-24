# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 541, 571))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnEnviar = QtWidgets.QPushButton(self.frame)
        self.btnEnviar.setGeometry(QtCore.QRect(450, 480, 71, 51))
        self.btnEnviar.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.btnEnviar.setObjectName("btnEnviar")
        self.txtChat = QtWidgets.QTextBrowser(self.frame)
        self.txtChat.setGeometry(QtCore.QRect(30, 20, 501, 421))
        self.txtChat.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.txtChat.setObjectName("txtChat")
        self.entryEnviar = QtWidgets.QLineEdit(self.frame)
        self.entryEnviar.setGeometry(QtCore.QRect(40, 480, 391, 51))
        self.entryEnviar.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.entryEnviar.setObjectName("entryEnviar")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(580, 50, 191, 151))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btnConectar = QtWidgets.QPushButton(self.frame_2)
        self.btnConectar.setGeometry(QtCore.QRect(90, 120, 75, 23))
        self.btnConectar.setObjectName("btnConectar")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblIp = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblIp.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lblIp.setObjectName("lblIp")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblIp)
        self.entryIp = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.entryIp.setObjectName("entryIp")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.entryIp)
        self.lblPort = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblPort.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lblPort.setObjectName("lblPort")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblPort)
        self.entryPort = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.entryPort.setObjectName("entryPort")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.entryPort)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(580, 230, 191, 131))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 160, 41))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblApelido_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblApelido_2.setStyleSheet("\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.lblApelido_2.setObjectName("lblApelido_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblApelido_2)
        self.entryApelido = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.entryApelido.setObjectName("entryApelido")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.entryApelido)
        self.btnAlterar = QtWidgets.QPushButton(self.frame_3)
        self.btnAlterar.setGeometry(QtCore.QRect(80, 80, 92, 23))
        self.btnAlterar.setObjectName("btnAlterar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyChat"))
        self.btnEnviar.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.btnEnviar.setText(_translate("MainWindow", "Enviar"))
        self.txtChat.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.btnConectar.setText(_translate("MainWindow", "Conectar"))
        self.lblIp.setText(_translate("MainWindow", "IP:"))
        self.lblPort.setText(_translate("MainWindow", "Port:"))
        self.lblApelido_2.setText(_translate("MainWindow", "Apelido:"))
        self.btnAlterar.setText(_translate("MainWindow", "Alterar"))



