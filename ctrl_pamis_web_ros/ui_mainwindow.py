# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(735, 302)
        MainWindow.setMinimumSize(QSize(90, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_rotation = QLineEdit(self.centralwidget)
        self.lineEdit_rotation.setObjectName(u"lineEdit_rotation")

        self.horizontalLayout.addWidget(self.lineEdit_rotation)

        self.sendButton_rotation = QPushButton(self.centralwidget)
        self.sendButton_rotation.setObjectName(u"sendButton_rotation")

        self.horizontalLayout.addWidget(self.sendButton_rotation)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_translation = QLineEdit(self.centralwidget)
        self.lineEdit_translation.setObjectName(u"lineEdit_translation")

        self.horizontalLayout_2.addWidget(self.lineEdit_translation)

        self.sendButton_translation = QPushButton(self.centralwidget)
        self.sendButton_translation.setObjectName(u"sendButton_translation")

        self.horizontalLayout_2.addWidget(self.sendButton_translation)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 0))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.lineEdit_XYT_x = QLineEdit(self.centralwidget)
        self.lineEdit_XYT_x.setObjectName(u"lineEdit_XYT_x")

        self.horizontalLayout_3.addWidget(self.lineEdit_XYT_x)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(60, 0))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.lineEdit_XYT_y = QLineEdit(self.centralwidget)
        self.lineEdit_XYT_y.setObjectName(u"lineEdit_XYT_y")

        self.horizontalLayout_3.addWidget(self.lineEdit_XYT_y)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(60, 0))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.lineEdit_XYT_theta = QLineEdit(self.centralwidget)
        self.lineEdit_XYT_theta.setObjectName(u"lineEdit_XYT_theta")
        self.lineEdit_XYT_theta.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_3.addWidget(self.lineEdit_XYT_theta)

        self.sendButton_XYT = QPushButton(self.centralwidget)
        self.sendButton_XYT.setObjectName(u"sendButton_XYT")

        self.horizontalLayout_3.addWidget(self.sendButton_XYT)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(150, 0))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.lineEdit_recalage_distance = QLineEdit(self.centralwidget)
        self.lineEdit_recalage_distance.setObjectName(u"lineEdit_recalage_distance")

        self.horizontalLayout_4.addWidget(self.lineEdit_recalage_distance)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.comboBox_recalage = QComboBox(self.centralwidget)
        self.comboBox_recalage.addItem("")
        self.comboBox_recalage.addItem("")
        self.comboBox_recalage.setObjectName(u"comboBox_recalage")
        self.comboBox_recalage.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_4.addWidget(self.comboBox_recalage)

        self.sendButton_recalage = QPushButton(self.centralwidget)
        self.sendButton_recalage.setObjectName(u"sendButton_recalage")

        self.horizontalLayout_4.addWidget(self.sendButton_recalage)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 735, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rotation (en deg \u00b0)", None))
        self.sendButton_rotation.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Translation (en mm)", None))
        self.sendButton_translation.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Position X, Y et theta", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"X (mm)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Y (mm)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"theta (\u00b0)", None))
        self.sendButton_XYT.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Recalage", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"distance (mm)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"coordonn\u00e9e", None))
        self.comboBox_recalage.setItemText(0, QCoreApplication.translate("MainWindow", u"x", None))
        self.comboBox_recalage.setItemText(1, QCoreApplication.translate("MainWindow", u"y", None))

        self.sendButton_recalage.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

