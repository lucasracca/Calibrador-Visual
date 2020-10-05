# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'concentradr.ui'
#
# Created: Thu Jun 23 22:32:32 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ventana(object):
    def setupUi(self, ventana):
        ventana.setObjectName("ventana")
        ventana.resize(689, 469)
        self.fondo = QtWidgets.QLabel(ventana)
        self.fondo.setGeometry(QtCore.QRect(-10, 0, 701, 471))
        self.fondo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fondo.setText("")
        self.fondo.setObjectName("fondo")
        self.labelPhysic = QtWidgets.QLabel(ventana)
        self.labelPhysic.setGeometry(QtCore.QRect(10, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.labelPhysic.setFont(font)
        self.labelPhysic.setText("Physic Value:")
        self.labelPhysic.setObjectName("labelPhysic")
        self.labelRaw = QtWidgets.QLabel(ventana)
        self.labelRaw.setGeometry(QtCore.QRect(10, 50, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.labelRaw.setFont(font)
        self.labelRaw.setText("Raw Value:")
        self.labelRaw.setObjectName("labelRaw")
        self.medidoPhysic =QtWidgets.QLabel(ventana)
        self.medidoPhysic.setGeometry(QtCore.QRect(150, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.medidoPhysic.setFont(font)
        self.medidoPhysic.setText("Physic")
        self.medidoPhysic.setObjectName("medidoPhysic")
        self.medidoRaw = QtWidgets.QLabel(ventana)
        self.medidoRaw.setGeometry(QtCore.QRect(150, 50, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.medidoRaw.setFont(font)
        self.medidoRaw.setText("Raw")
        self.medidoRaw.setObjectName("medidoRaw")
        self.botonExit = QtWidgets.QPushButton(ventana)
        self.botonExit.setGeometry(QtCore.QRect(550, 410, 90, 29))
        self.botonExit.setObjectName("botonExit")
        self.tabWidget = QtWidgets.QTabWidget(ventana)
        self.tabWidget.setGeometry(QtCore.QRect(20, 100, 651, 301))
        self.tabWidget.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"border-color: rgb(1, 93, 44);")
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tabLineal = QtWidgets.QWidget()
        self.tabLineal.setObjectName("tabLineal")
        self.labelCalibracion = QtWidgets.QLabel(self.tabLineal)
        self.labelCalibracion.setGeometry(QtCore.QRect(10, 10, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(50)
        font.setBold(False)
        self.labelCalibracion.setFont(font)
        self.labelCalibracion.setObjectName("labelCalibracion")
        self.tabLineales = QtWidgets.QTabWidget(self.tabLineal)
        self.tabLineales.setGeometry(QtCore.QRect(10, 40, 631, 211))
        self.tabLineales.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.tabLineales.setObjectName("tabLineales")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.medidoM = QtWidgets.QLabel(self.tab)
        self.medidoM.setGeometry(QtCore.QRect(210, 120, 61, 17))
        self.medidoM.setText("(PendM)")
        self.medidoM.setObjectName("medidoM")
        self.botonEnviar1 = QtWidgets.QPushButton(self.tab)
        self.botonEnviar1.setGeometry(QtCore.QRect(450, 30, 90, 29))
        self.botonEnviar1.setObjectName("botonEnviar1")
        self.labelAltura1 = QtWidgets.QLabel(self.tab)
        self.labelAltura1.setGeometry(QtCore.QRect(60, 40, 121, 17))
        self.labelAltura1.setText("Altura Referencia 1:")
        self.labelAltura1.setObjectName("labelAltura1")
        self.labelM = QtWidgets.QLabel(self.tab)
        self.labelM.setGeometry(QtCore.QRect(60, 120, 81, 17))
        self.labelM.setText("Pendiente M:")
        self.labelM.setObjectName("labelM")
        self.labelAltura2 = QtWidgets.QLabel(self.tab)
        self.labelAltura2.setGeometry(QtCore.QRect(60, 80, 121, 17))
        self.labelAltura2.setText("Altura Referencia 2:")
        self.labelAltura2.setObjectName("labelAltura2")
        self.entrada1 = QtWidgets.QLineEdit(self.tab)
        self.entrada1.setGeometry(QtCore.QRect(320, 30, 91, 29))
        self.entrada1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entrada1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.entrada1.setObjectName("entrada1")
        self.medido = QtWidgets.QLabel(self.tab)
        self.medido.setGeometry(QtCore.QRect(210, 80, 61, 17))
        self.medido.setText("(AltRef2)")
        self.medido.setObjectName("medido")
        self.medido1 = QtWidgets.QLabel(self.tab)
        self.medido1.setGeometry(QtCore.QRect(210, 40, 61, 17))
        self.medido1.setText("(AltRef1)")
        self.medido1.setObjectName("medido1")
        self.botonEnviar2 = QtWidgets.QPushButton(self.tab)
        self.botonEnviar2.setGeometry(QtCore.QRect(450, 70, 90, 29))
        self.botonEnviar2.setObjectName("botonEnviar2")
        self.entrada2 = QtWidgets.QLineEdit(self.tab)
        self.entrada2.setGeometry(QtCore.QRect(320, 70, 91, 29))
        self.entrada2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entrada2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.entrada2.setObjectName("entrada2")
        self.medidoM_4 =QtWidgets.QLabel(self.tab)
        self.medidoM_4.setGeometry(QtCore.QRect(270, 120, 71, 17))
        self.medidoM_4.setText("[cm/pulsos]")
        self.medidoM_4.setObjectName("medidoM_4")
        self.medido1_4 = QtWidgets.QLabel(self.tab)
        self.medido1_4.setGeometry(QtCore.QRect(270, 40, 31, 17))
        self.medido1_4.setText("[cm]")
        self.medido1_4.setObjectName("medido1_4")
        self.medido1_5 = QtWidgets.QLabel(self.tab)
        self.medido1_5.setGeometry(QtCore.QRect(270, 80, 31, 17))
        self.medido1_5.setText("[cm]")
        self.medido1_5.setObjectName("medido1_5")
        self.tabLineales.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.labelAltura1_2 = QtWidgets.QLabel(self.tab_2)
        self.labelAltura1_2.setGeometry(QtCore.QRect(60, 70, 121, 17))
        self.labelAltura1_2.setText("Altura Referencia 1:")
        self.labelAltura1_2.setObjectName("labelAltura1_2")
        self.medidoM_2 = QtWidgets.QLabel(self.tab_2)
        self.medidoM_2.setGeometry(QtCore.QRect(190, 120, 61, 17))
        self.medidoM_2.setText("(PendM)")
        self.medidoM_2.setObjectName("medidoM_2")
        self.labelM_2 = QtWidgets.QLabel(self.tab_2)
        self.labelM_2.setGeometry(QtCore.QRect(60, 120, 81, 17))
        self.labelM_2.setText("Pendiente M:")
        self.labelM_2.setObjectName("labelM_2")
        self.entradaPyMm = QtWidgets.QLineEdit(self.tab_2)
        self.entradaPyMm.setGeometry(QtCore.QRect(330, 110, 91, 29))
        self.entradaPyMm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entradaPyMm.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.entradaPyMm.setObjectName("entradaPyMm")
        self.botonEnviarPyM =QtWidgets.QPushButton(self.tab_2)
        self.botonEnviarPyM.setGeometry(QtCore.QRect(450, 110, 121, 29))
        self.botonEnviarPyM.setObjectName("botonEnviarPyM")
        self.entradaPyM1 = QtWidgets.QLineEdit(self.tab_2)
        self.entradaPyM1.setGeometry(QtCore.QRect(330, 60, 91, 29))
        self.entradaPyM1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entradaPyM1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.entradaPyM1.setObjectName("entradaPyM1")
        self.medido1_2 = QtWidgets.QLabel(self.tab_2)
        self.medido1_2.setGeometry(QtCore.QRect(190, 70, 61, 17))
        self.medido1_2.setText("(AltRef1)")
        self.medido1_2.setObjectName("medido1_2")
        self.medido1_3 = QtWidgets.QLabel(self.tab_2)
        self.medido1_3.setGeometry(QtCore.QRect(250, 70, 31, 17))
        self.medido1_3.setText("[cm]")
        self.medido1_3.setObjectName("medido1_3")
        self.medidoM_3 = QtWidgets.QLabel(self.tab_2)
        self.medidoM_3.setGeometry(QtCore.QRect(250, 120, 71, 17))
        self.medidoM_3.setText("[cm/pulsos]")
        self.medidoM_3.setObjectName("medidoM_3")
        self.tabLineales.addTab(self.tab_2, "")
        self.medidoStatusLineal = QtWidgets.QLabel(self.tabLineal)
        self.medidoStatusLineal.setGeometry(QtCore.QRect(420, 10, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.medidoStatusLineal.setFont(font)
        self.medidoStatusLineal.setText("Calib Status")
        self.medidoStatusLineal.setObjectName("medidoStatusLineal")
        self.tabWidget.addTab(self.tabLineal, "")
        self.tabRig = QtWidgets.QWidget()
        self.tabRig.setObjectName("tabRig")
        self.labelGeometria = QtWidgets.QLabel(self.tabRig)
        self.labelGeometria.setGeometry(QtCore.QRect(10, 10, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelGeometria.setFont(font)
        self.labelGeometria.setObjectName("labelGeometria")
        self.labelDiametro =QtWidgets.QLabel(self.tabRig)
        self.labelDiametro.setGeometry(QtCore.QRect(20, 50, 111, 17))
        self.labelDiametro.setObjectName("labelDiametro")
        self.labelPpr = QtWidgets.QLabel(self.tabRig)
        self.labelPpr.setGeometry(QtCore.QRect(20, 90, 56, 17))
        self.labelPpr.setObjectName("labelPpr")
        self.labelAparejo = QtWidgets.QLabel(self.tabRig)
        self.labelAparejo.setGeometry(QtCore.QRect(20, 130, 121, 17))
        self.labelAparejo.setObjectName("labelAparejo")
        self.labelCable = QtWidgets.QLabel(self.tabRig)
        self.labelCable.setGeometry(QtCore.QRect(330, 50, 101, 17))
        self.labelCable.setObjectName("labelCable")
        self.labelHpc = QtWidgets.QLabel(self.tabRig)
        self.labelHpc.setGeometry(QtCore.QRect(340, 80, 56, 17))
        self.labelHpc.setObjectName("labelHpc")
        self.line = QtWidgets.QFrame(self.tabRig)
        self.line.setGeometry(QtCore.QRect(0, 150, 651, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setAutoFillBackground(False)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.labelAjuste = QtWidgets.QLabel(self.tabRig)
        self.labelAjuste.setGeometry(QtCore.QRect(10, 160, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAjuste.setFont(font)
        self.labelAjuste.setObjectName("labelAjuste")
        self.labelAlturaRef = QtWidgets.QLabel(self.tabRig)
        self.labelAlturaRef.setGeometry(QtCore.QRect(20, 200, 121, 17))
        self.labelAlturaRef.setObjectName("labelAlturaRef")
        self.labelHiladas = QtWidgets.QLabel(self.tabRig)
        self.labelHiladas.setGeometry(QtCore.QRect(20, 240, 201, 17))
        self.labelHiladas.setObjectName("labelHiladas")
        self.labelCapas =QtWidgets.QLabel(self.tabRig)
        self.labelCapas.setGeometry(QtCore.QRect(330, 190, 111, 17))
        self.labelCapas.setObjectName("labelCapas")
        self.botonEnviarAjuste = QtWidgets.QPushButton(self.tabRig)
        self.botonEnviarAjuste.setGeometry(QtCore.QRect(530, 230, 90, 29))
        self.botonEnviarAjuste.setObjectName("botonEnviarAjuste")
        self.botonEnviarGeometria = QtWidgets.QPushButton(self.tabRig)
        self.botonEnviarGeometria.setGeometry(QtCore.QRect(510, 120, 111, 29))
        self.botonEnviarGeometria.setObjectName("botonEnviarGeometria")
        self.entradaDiametro = QtWidgets.QLineEdit(self.tabRig)
        self.entradaDiametro.setGeometry(QtCore.QRect(212, 40, 91, 29))
        self.entradaDiametro.setObjectName("entradaDiametro")
        self.entradaDiametro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entradaPpr = QtWidgets.QLineEdit(self.tabRig)
        self.entradaPpr.setGeometry(QtCore.QRect(212, 80, 91, 29))
        self.entradaPpr.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.entradaPpr.setObjectName("entradaPpr")
        self.entradaPpr.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entradaAparejo = QtWidgets.QLineEdit(self.tabRig)
        self.entradaAparejo.setGeometry(QtCore.QRect(212, 120, 91, 29))
        self.entradaAparejo.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.entradaAparejo.setObjectName("entradaAparejo")
        self.entradaAparejo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entradaCable = QtWidgets.QLineEdit(self.tabRig)
        self.entradaCable.setGeometry(QtCore.QRect(512, 40, 101, 29))
        self.entradaCable.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.entradaCable.setObjectName("entradaCable")
        self.entradaCable.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entradaCapas = QtWidgets.QLineEdit(self.tabRig)
        self.entradaCapas.setGeometry(QtCore.QRect(522, 180, 91, 29))
        self.entradaCapas.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.entradaCapas.setObjectName("entradaCapas")
        self.entradaCapas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entradaHpc = QtWidgets.QLineEdit(self.tabRig)
        self.entradaHpc.setGeometry(QtCore.QRect(512, 70, 101, 29))
        self.entradaHpc.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.entradaHpc.setObjectName("entradaHpc")
        self.entradaHpc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entradaAlturaRef = QtWidgets.QLineEdit(self.tabRig)
        self.entradaAlturaRef.setGeometry(QtCore.QRect(232, 190, 91, 29))
        self.entradaAlturaRef.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.entradaAlturaRef.setObjectName("entradaAlturaRef")
        self.entradaAlturaRef.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entradaHiladas = QtWidgets.QLineEdit(self.tabRig)
        self.entradaHiladas.setGeometry(QtCore.QRect(280, 230, 91, 29))
        self.entradaHiladas.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.entradaHiladas.setObjectName("entradaHiladas")
        self.entradaHiladas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.medidoDiametro = QtWidgets.QLabel(self.tabRig)
        self.medidoDiametro.setGeometry(QtCore.QRect(130, 50, 56, 17))
        self.medidoDiametro.setObjectName("medidoDiametro")
        self.medidoPpr = QtWidgets.QLabel(self.tabRig)
        self.medidoPpr.setGeometry(QtCore.QRect(60, 90, 56, 17))
        self.medidoPpr.setObjectName("medidoPpr")
        self.medidoAparejo = QtWidgets.QLabel(self.tabRig)
        self.medidoAparejo.setGeometry(QtCore.QRect(130, 130, 56, 17))
        self.medidoAparejo.setObjectName("medidoAparejo")
        self.medidoCable = QtWidgets.QLabel(self.tabRig)
        self.medidoCable.setGeometry(QtCore.QRect(430, 50, 56, 17))
        self.medidoCable.setObjectName("medidoCable")
        self.medidoHpc = QtWidgets.QLabel(self.tabRig)
        self.medidoHpc.setGeometry(QtCore.QRect(370, 80, 56, 17))
        self.medidoHpc.setObjectName("medidoHpc")
        self.medidoAlturaRef = QtWidgets.QLabel(self.tabRig)
        self.medidoAlturaRef.setGeometry(QtCore.QRect(150, 200, 56, 17))
        self.medidoAlturaRef.setObjectName("medidoAlturaRef")
        self.medidoHiladas = QtWidgets.QLabel(self.tabRig)
        self.medidoHiladas.setGeometry(QtCore.QRect(220, 240, 56, 17))
        self.medidoHiladas.setObjectName("medidoHiladas")
        self.medidoCapas =QtWidgets.QLabel(self.tabRig)
        self.medidoCapas.setGeometry(QtCore.QRect(440, 190, 56, 17))
        self.medidoCapas.setObjectName("medidoCapas")
        self.botonEnviarAparejo = QtWidgets.QPushButton(self.tabRig)
        self.botonEnviarAparejo.setGeometry(QtCore.QRect(310, 120, 151, 29))
        self.botonEnviarAparejo.setObjectName("botonEnviarAparejo")
        self.medido1_7 = QtWidgets.QLabel(self.tabRig)
        self.medido1_7.setGeometry(QtCore.QRect(200, 200, 31, 17))
        self.medido1_7.setText("[cm]")
        self.medido1_7.setObjectName("medido1_7")
        self.medido1_8 = QtWidgets.QLabel(self.tabRig)
        self.medido1_8.setGeometry(QtCore.QRect(190, 50, 21, 17))
        self.medido1_8.setText("[\'\']")
        self.medido1_8.setObjectName("medido1_8")
        self.medido1_9 = QtWidgets.QLabel(self.tabRig)
        self.medido1_9.setGeometry(QtCore.QRect(480, 50, 31, 17))
        self.medido1_9.setText("[\'\']")
        self.medido1_9.setObjectName("medido1_9")
        self.medidoStatusRig = QtWidgets.QLabel(self.tabRig)
        self.medidoStatusRig.setGeometry(QtCore.QRect(420, 10, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.medidoStatusRig.setFont(font)
        self.medidoStatusRig.setText("Calib Status")
        self.medidoStatusRig.setObjectName("medidoStatusRig")
        self.tabWidget.addTab(self.tabRig, "")
        self.estado = QtWidgets.QLineEdit(ventana)
        self.estado.setGeometry(QtCore.QRect(32, 410, 481, 29))
        self.estado.setStyleSheet("border-color: rgb(236, 236, 236);")
        self.estado.setObjectName("estado")
        self.medido1_6 = QtWidgets.QLabel(ventana)
        self.medido1_6.setGeometry(QtCore.QRect(230, 20, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.medido1_6.setFont(font)
        self.medido1_6.setText("[cm]")
        self.medido1_6.setObjectName("medido1_6")
        self.medidoRed =QtWidgets.QLabel(ventana)
        self.medidoRed.setGeometry(QtCore.QRect(500, 90, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.medidoRed.setFont(font)
        self.medidoRed.setText("Network Status")
        self.medidoRed.setObjectName("medidoRed")
        self.label = QtWidgets.QLabel(ventana)
        self.label.setGeometry(QtCore.QRect(450, 10, 201, 64))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logoNetLog.png"))
        self.label.setObjectName("label")

        self.retranslateUi(ventana)
        self.tabWidget.setCurrentIndex(0)
        self.tabLineales.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ventana)

    def retranslateUi(self, ventana):
        ventana.setWindowTitle(QtWidgets.QApplication.translate("ventana", "Calibrar Net-Log v2.0.1", None))
        self.botonExit.setText(QtWidgets.QApplication.translate("ventana", "Exit", None))
        self.labelCalibracion.setText(QtWidgets.QApplication.translate("ventana", "Calibración Lineal", None))
        self.botonEnviar1.setText(QtWidgets.QApplication.translate("ventana", "Enviar Punto 1", None))
        self.botonEnviar2.setText(QtWidgets.QApplication.translate("ventana", "Enviar Punto 2", None))
        self.tabLineales.setTabText(self.tabLineales.indexOf(self.tab), QtWidgets.QApplication.translate("ventana", "Dos Puntos", None))
        self.botonEnviarPyM.setText(QtWidgets.QApplication.translate("ventana", "Enviar Punto 1 y M", None))
        self.tabLineales.setTabText(self.tabLineales.indexOf(self.tab_2), QtWidgets.QApplication.translate("ventana", "Punto y Pendiente", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLineal), QtWidgets.QApplication.translate("ventana", "Lineal", None))
        self.labelGeometria.setText(QtWidgets.QApplication.translate("ventana", "Geometría", None))
        self.labelDiametro.setText(QtWidgets.QApplication.translate("ventana", "Diametro tambor:", None))
        self.labelPpr.setText(QtWidgets.QApplication.translate("ventana", "Ppr:", None))
        self.labelAparejo.setText(QtWidgets.QApplication.translate("ventana", "Lineas del Aparejo:", None))
        self.labelCable.setText(QtWidgets.QApplication.translate("ventana", "Diametro Cable:", None))
        self.labelHpc.setText(QtWidgets.QApplication.translate("ventana", "Hpc:", None))
        self.labelAjuste.setText(QtWidgets.QApplication.translate("ventana", "Ajuste", None))
        self.labelAlturaRef.setText(QtWidgets.QApplication.translate("ventana", "Altura de Referencia:", None))
        self.labelHiladas.setText(QtWidgets.QApplication.translate("ventana", "Cantidad de Hiladas Última Capa:", None))
        self.labelCapas.setText(QtWidgets.QApplication.translate("ventana", "Capas Completas:", None))
        self.botonEnviarAjuste.setText(QtWidgets.QApplication.translate("ventana", "Enviar Ajuste", None))
        self.botonEnviarGeometria.setText(QtWidgets.QApplication.translate("ventana", "Enviar Geometría", None))
        self.medidoDiametro.setText(QtWidgets.QApplication.translate("ventana", "(Tambor)", None))
        self.medidoPpr.setText(QtWidgets.QApplication.translate("ventana", "(Ppr)", None))
        self.medidoAparejo.setText(QtWidgets.QApplication.translate("ventana", "(Aparejo)", None))
        self.medidoCable.setText(QtWidgets.QApplication.translate("ventana", "(Cable)", None))
        self.medidoHpc.setText(QtWidgets.QApplication.translate("ventana", "(Hpc)", None))
        self.medidoAlturaRef.setText(QtWidgets.QApplication.translate("ventana", "(Altura)", None))
        self.medidoHiladas.setText(QtWidgets.QApplication.translate("ventana", "(Hiladas)", None))
        self.medidoCapas.setText(QtWidgets.QApplication.translate("ventana", "(capas)", None))
        self.botonEnviarAparejo.setText(QtWidgets.QApplication.translate("ventana", "Enviar Lineas de Aparejo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRig), QtWidgets.QApplication.translate("ventana", "Rig Description", None))

