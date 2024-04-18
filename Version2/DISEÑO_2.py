# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DISEÑO_2COPIA.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 0))
        self.frame_superior.setMaximumSize(QSize(16777215, 50))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"background-color: rgb(114, 255, 7);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(114, 255, 7);\n"
"border-radius:20px;\n"
"border:1px solid white;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:  rgb(255, 177, 21);\n"
"border-radius:20px;\n"
"	\n"
"}")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_superior)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 14pt \"Agency FB\";\n"
"")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(535, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.MINIMIZAR_BUTTON = QPushButton(self.frame_superior)
        self.MINIMIZAR_BUTTON.setObjectName(u"MINIMIZAR_BUTTON")
        self.MINIMIZAR_BUTTON.setMinimumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(u"imagenes_app/window-minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MINIMIZAR_BUTTON.setIcon(icon)
        self.MINIMIZAR_BUTTON.setIconSize(QSize(32, 16))

        self.horizontalLayout.addWidget(self.MINIMIZAR_BUTTON)

        self.MAXIMIZAR_BUTTON = QPushButton(self.frame_superior)
        self.MAXIMIZAR_BUTTON.setObjectName(u"MAXIMIZAR_BUTTON")
        self.MAXIMIZAR_BUTTON.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u"imagenes_app/stacked-scrolling-1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MAXIMIZAR_BUTTON.setIcon(icon1)
        self.MAXIMIZAR_BUTTON.setIconSize(QSize(37, 37))

        self.horizontalLayout.addWidget(self.MAXIMIZAR_BUTTON)

        self.CERRAR_BUTTON = QPushButton(self.frame_superior)
        self.CERRAR_BUTTON.setObjectName(u"CERRAR_BUTTON")
        self.CERRAR_BUTTON.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u"imagenes_app/window-close_2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CERRAR_BUTTON.setIcon(icon2)
        self.CERRAR_BUTTON.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.CERRAR_BUTTON)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 237, 38);\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 75 11pt \"Agency FB\";\n"
"background-color: rgb(114, 255, 7);\n"
"\n"
"border-radius: 5px;\n"
"border:1px solid white;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:  rgb(255, 177, 21);\n"
"\n"
"	\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.frame_3)
        self.frame_menu.setObjectName(u"frame_menu")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menu.sizePolicy().hasHeightForWidth())
        self.frame_menu.setSizePolicy(sizePolicy)
        self.frame_menu.setMaximumSize(QSize(200, 16777215))
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 9, 8, 6)
        self.SAVE_DATA_BUTTON = QPushButton(self.frame_menu)
        self.SAVE_DATA_BUTTON.setObjectName(u"SAVE_DATA_BUTTON")
        self.SAVE_DATA_BUTTON.setLayoutDirection(Qt.LeftToRight)
        self.SAVE_DATA_BUTTON.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"imagenes_app/brain.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.SAVE_DATA_BUTTON.setIcon(icon3)
        self.SAVE_DATA_BUTTON.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.SAVE_DATA_BUTTON)

        self.SPELLER_BUTTON = QPushButton(self.frame_menu)
        self.SPELLER_BUTTON.setObjectName(u"SPELLER_BUTTON")
        self.SPELLER_BUTTON.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"imagenes_app/teclado.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.SPELLER_BUTTON.setIcon(icon4)
        self.SPELLER_BUTTON.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.SPELLER_BUTTON)

        self.TRIQUI_BUTTON = QPushButton(self.frame_menu)
        self.TRIQUI_BUTTON.setObjectName(u"TRIQUI_BUTTON")
        self.TRIQUI_BUTTON.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"imagenes_app/triqui (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TRIQUI_BUTTON.setIcon(icon5)
        self.TRIQUI_BUTTON.setIconSize(QSize(36, 36))

        self.verticalLayout_4.addWidget(self.TRIQUI_BUTTON)


        self.horizontalLayout_2.addWidget(self.frame_menu)

        self.frame_PRINCIPAL = QFrame(self.frame_3)
        self.frame_PRINCIPAL.setObjectName(u"frame_PRINCIPAL")
        self.frame_PRINCIPAL.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 237, 38);\n"
"}")
        self.frame_PRINCIPAL.setFrameShape(QFrame.StyledPanel)
        self.frame_PRINCIPAL.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_PRINCIPAL)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_PRINCIPAL)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MENU_BUTTON = QPushButton(self.frame_5)
        self.MENU_BUTTON.setObjectName(u"MENU_BUTTON")
        icon6 = QIcon()
        icon6.addFile(u"imagenes_app/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MENU_BUTTON.setIcon(icon6)
        self.MENU_BUTTON.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.MENU_BUTTON)

        self.horizontalSpacer_2 = QSpacerItem(610, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.frame_SUBPRINCIPAL = QFrame(self.frame_PRINCIPAL)
        self.frame_SUBPRINCIPAL.setObjectName(u"frame_SUBPRINCIPAL")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_SUBPRINCIPAL.sizePolicy().hasHeightForWidth())
        self.frame_SUBPRINCIPAL.setSizePolicy(sizePolicy1)
        self.frame_SUBPRINCIPAL.setFrameShape(QFrame.StyledPanel)
        self.frame_SUBPRINCIPAL.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_SUBPRINCIPAL)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.label_2 = QLabel(self.frame_SUBPRINCIPAL)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(1648, 1648))
        self.label_2.setPixmap(QPixmap(u"../Downloads/actividadcerebral.svg"))

        self.verticalLayout_5.addWidget(self.label_2)

        self.label_EVOKED = QLabel(self.frame_SUBPRINCIPAL)
        self.label_EVOKED.setObjectName(u"label_EVOKED")
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setPointSize(50)
        font.setBold(True)
        self.label_EVOKED.setFont(font)

        self.verticalLayout_5.addWidget(self.label_EVOKED, 0, Qt.AlignHCenter)

        self.label_IMAGEN_CEREBRO = QLabel(self.frame_SUBPRINCIPAL)
        self.label_IMAGEN_CEREBRO.setObjectName(u"label_IMAGEN_CEREBRO")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_IMAGEN_CEREBRO.sizePolicy().hasHeightForWidth())
        self.label_IMAGEN_CEREBRO.setSizePolicy(sizePolicy2)
        self.label_IMAGEN_CEREBRO.setPixmap(QPixmap(u"imagenes_app/actividadcerebral.svg"))

        self.verticalLayout_5.addWidget(self.label_IMAGEN_CEREBRO, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.frame_SUBPRINCIPAL)


        self.horizontalLayout_2.addWidget(self.frame_PRINCIPAL)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.verticalLayout_2.setStretch(0, 1)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TRABAJO DE GRADO ", None))
        self.MINIMIZAR_BUTTON.setText("")
        self.MAXIMIZAR_BUTTON.setText("")
        self.CERRAR_BUTTON.setText("")
        self.SAVE_DATA_BUTTON.setText(QCoreApplication.translate("MainWindow", u"SAVE DATA", None))
        self.SPELLER_BUTTON.setText(QCoreApplication.translate("MainWindow", u"SPELLER", None))
        self.TRIQUI_BUTTON.setText(QCoreApplication.translate("MainWindow", u"TRIQUI", None))
        self.MENU_BUTTON.setText("")
        self.label_2.setText("")
        self.label_EVOKED.setText(QCoreApplication.translate("MainWindow", u"EVOKED POTENTIAL P300", None))
        self.label_IMAGEN_CEREBRO.setText("")
    # retranslateUi

