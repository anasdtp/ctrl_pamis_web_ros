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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1106, 626)
        MainWindow.setMinimumSize(QSize(90, 90))
        MainWindow.setInputMethodHints(Qt.ImhMultiLine)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(150, 0))
        self.label_15.setLayoutDirection(Qt.LeftToRight)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_15)

        self.textEdit_strategie = QTextEdit(self.centralwidget)
        self.textEdit_strategie.setObjectName(u"textEdit_strategie")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_strategie.sizePolicy().hasHeightForWidth())
        self.textEdit_strategie.setSizePolicy(sizePolicy)
        self.textEdit_strategie.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout.addWidget(self.textEdit_strategie)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ClearButton_strategie = QPushButton(self.centralwidget)
        self.ClearButton_strategie.setObjectName(u"ClearButton_strategie")
        self.ClearButton_strategie.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_7.addWidget(self.ClearButton_strategie)

        self.sendButton_strategie = QPushButton(self.centralwidget)
        self.sendButton_strategie.setObjectName(u"sendButton_strategie")
        self.sendButton_strategie.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_7.addWidget(self.sendButton_strategie)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.sendButton_wait_for_jack = QPushButton(self.centralwidget)
        self.sendButton_wait_for_jack.setObjectName(u"sendButton_wait_for_jack")
        self.sendButton_wait_for_jack.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_5.addWidget(self.sendButton_wait_for_jack)

        self.sendButton_jack = QPushButton(self.centralwidget)
        self.sendButton_jack.setObjectName(u"sendButton_jack")
        self.sendButton_jack.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_5.addWidget(self.sendButton_jack)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 0))
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 45))
        self.comboBox.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_5)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 0))
        self.label_16.setMaximumSize(QSize(260, 16777215))
        self.label_16.setLayoutDirection(Qt.LeftToRight)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_16)

        self.comboBox_reglage_couleur = QComboBox(self.centralwidget)
        self.comboBox_reglage_couleur.addItem("")
        self.comboBox_reglage_couleur.addItem("")
        self.comboBox_reglage_couleur.setObjectName(u"comboBox_reglage_couleur")
        self.comboBox_reglage_couleur.setMinimumSize(QSize(0, 45))
        self.comboBox_reglage_couleur.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_15.addWidget(self.comboBox_reglage_couleur)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_15)

        self.sendButton_reglage_couleur = QPushButton(self.centralwidget)
        self.sendButton_reglage_couleur.setObjectName(u"sendButton_reglage_couleur")
        self.sendButton_reglage_couleur.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_16.addWidget(self.sendButton_reglage_couleur)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
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
        self.lineEdit_rotation.setMinimumSize(QSize(0, 45))

        self.horizontalLayout.addWidget(self.lineEdit_rotation)

        self.sendButton_rotation = QPushButton(self.centralwidget)
        self.sendButton_rotation.setObjectName(u"sendButton_rotation")
        self.sendButton_rotation.setMinimumSize(QSize(0, 45))

        self.horizontalLayout.addWidget(self.sendButton_rotation)


        self.formLayout_3.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(150, 0))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(60, 0))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_12)

        self.lineEdit_XYT_x_2 = QLineEdit(self.centralwidget)
        self.lineEdit_XYT_x_2.setObjectName(u"lineEdit_XYT_x_2")
        self.lineEdit_XYT_x_2.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_6.addWidget(self.lineEdit_XYT_x_2)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(60, 0))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_13)

        self.lineEdit_XYT_y_2 = QLineEdit(self.centralwidget)
        self.lineEdit_XYT_y_2.setObjectName(u"lineEdit_XYT_y_2")
        self.lineEdit_XYT_y_2.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_6.addWidget(self.lineEdit_XYT_y_2)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(60, 0))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_14)

        self.lineEdit_XYT_theta_2 = QLineEdit(self.centralwidget)
        self.lineEdit_XYT_theta_2.setObjectName(u"lineEdit_XYT_theta_2")
        self.lineEdit_XYT_theta_2.setMinimumSize(QSize(90, 45))

        self.horizontalLayout_6.addWidget(self.lineEdit_XYT_theta_2)

        self.sendButton_XYT_2 = QPushButton(self.centralwidget)
        self.sendButton_XYT_2.setObjectName(u"sendButton_XYT_2")
        self.sendButton_XYT_2.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_6.addWidget(self.sendButton_XYT_2)


        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_translation = QLineEdit(self.centralwidget)
        self.lineEdit_translation.setObjectName(u"lineEdit_translation")
        self.lineEdit_translation.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_2.addWidget(self.lineEdit_translation)

        self.sendButton_translation = QPushButton(self.centralwidget)
        self.sendButton_translation.setObjectName(u"sendButton_translation")
        self.sendButton_translation.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_2.addWidget(self.sendButton_translation)


        self.formLayout_3.setLayout(1, QFormLayout.LabelRole, self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(150, 0))
        self.label_19.setLayoutDirection(Qt.LeftToRight)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_19)

        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(140, 0))
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_22)

        self.lineEdit_reglage_largeurRobot = QLineEdit(self.centralwidget)
        self.lineEdit_reglage_largeurRobot.setObjectName(u"lineEdit_reglage_largeurRobot")
        self.lineEdit_reglage_largeurRobot.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_8.addWidget(self.lineEdit_reglage_largeurRobot)

        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(120, 0))
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_21)

        self.lineEdit_reglage_RayonRoue = QLineEdit(self.centralwidget)
        self.lineEdit_reglage_RayonRoue.setObjectName(u"lineEdit_reglage_RayonRoue")
        self.lineEdit_reglage_RayonRoue.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_8.addWidget(self.lineEdit_reglage_RayonRoue)

        self.sendButton_reglage = QPushButton(self.centralwidget)
        self.sendButton_reglage.setObjectName(u"sendButton_reglage")
        self.sendButton_reglage.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_8.addWidget(self.sendButton_reglage)


        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_8)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(150, 0))
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_18)

        self.lineEdit_changment_ID_pamis = QLineEdit(self.centralwidget)
        self.lineEdit_changment_ID_pamis.setObjectName(u"lineEdit_changment_ID_pamis")
        self.lineEdit_changment_ID_pamis.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_18.addWidget(self.lineEdit_changment_ID_pamis)

        self.sendButton_changement_ID_pamis = QPushButton(self.centralwidget)
        self.sendButton_changement_ID_pamis.setObjectName(u"sendButton_changement_ID_pamis")
        self.sendButton_changement_ID_pamis.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_18.addWidget(self.sendButton_changement_ID_pamis)


        self.formLayout_3.setLayout(2, QFormLayout.LabelRole, self.horizontalLayout_18)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

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
        self.lineEdit_XYT_x.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_3.addWidget(self.lineEdit_XYT_x)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(60, 0))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.lineEdit_XYT_y = QLineEdit(self.centralwidget)
        self.lineEdit_XYT_y.setObjectName(u"lineEdit_XYT_y")
        self.lineEdit_XYT_y.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_3.addWidget(self.lineEdit_XYT_y)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(60, 0))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.lineEdit_XYT_theta = QLineEdit(self.centralwidget)
        self.lineEdit_XYT_theta.setObjectName(u"lineEdit_XYT_theta")
        self.lineEdit_XYT_theta.setMinimumSize(QSize(90, 45))

        self.horizontalLayout_3.addWidget(self.lineEdit_XYT_theta)

        self.sendButton_XYT = QPushButton(self.centralwidget)
        self.sendButton_XYT.setObjectName(u"sendButton_XYT")
        self.sendButton_XYT.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_3.addWidget(self.sendButton_XYT)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

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
        self.lineEdit_recalage_distance.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_4.addWidget(self.lineEdit_recalage_distance)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.comboBox_recalage = QComboBox(self.centralwidget)
        self.comboBox_recalage.addItem("")
        self.comboBox_recalage.addItem("")
        self.comboBox_recalage.setObjectName(u"comboBox_recalage")
        self.comboBox_recalage.setMinimumSize(QSize(90, 45))

        self.horizontalLayout_4.addWidget(self.comboBox_recalage)

        self.sendButton_recalage = QPushButton(self.centralwidget)
        self.sendButton_recalage.setObjectName(u"sendButton_recalage")
        self.sendButton_recalage.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_4.addWidget(self.sendButton_recalage)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1106, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Ecriture de la Strategie :", None))
        self.ClearButton_strategie.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.sendButton_strategie.setText(QCoreApplication.translate("MainWindow", u"Send Strategie", None))
        self.sendButton_wait_for_jack.setText(QCoreApplication.translate("MainWindow", u"Attente du d\u00e9part Match", None))
        self.sendButton_jack.setText(QCoreApplication.translate("MainWindow", u"D\u00e9part Match", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Num\u00e9ro du Pamis", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Reglage de la couleur", None))
        self.comboBox_reglage_couleur.setItemText(0, QCoreApplication.translate("MainWindow", u"Bleu", None))
        self.comboBox_reglage_couleur.setItemText(1, QCoreApplication.translate("MainWindow", u"Jaune", None))

        self.sendButton_reglage_couleur.setText(QCoreApplication.translate("MainWindow", u"Send clr", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rotation (en deg \u00b0)", None))
        self.sendButton_rotation.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Changement Position", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"X (mm)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Y (mm)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"theta (\u00b0)", None))
        self.sendButton_XYT_2.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Translation (en mm)", None))
        self.sendButton_translation.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Reglage Coef", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Largeur Robot (mm)", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Rayon Roue (mm)", None))
        self.sendButton_reglage.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Changement de l'ID", None))
        self.sendButton_changement_ID_pamis.setText(QCoreApplication.translate("MainWindow", u"Send", None))
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

