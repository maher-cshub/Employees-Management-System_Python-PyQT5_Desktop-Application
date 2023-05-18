# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_v(object):
    def setupUi(self, v):
        if not v.objectName():
            v.setObjectName(u"v")
        v.setWindowModality(Qt.ApplicationModal)
        v.resize(847, 671)
        icon = QIcon()
        icon.addFile(u"../assets/company.png", QSize(), QIcon.Normal, QIcon.Off)
        v.setWindowIcon(icon)
        v.setStyleSheet(u"")
        v.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(v)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Body = QFrame(self.centralwidget)
        self.Body.setObjectName(u"Body")
        sizePolicy.setHeightForWidth(self.Body.sizePolicy().hasHeightForWidth())
        self.Body.setSizePolicy(sizePolicy)
        self.Body.setStyleSheet(u"QFrame{\n"
"background:rgb(25, 25, 25);\n"
"margin:0 0 0 0;\n"
"}")
        self.Body.setFrameShape(QFrame.StyledPanel)
        self.Body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.Body)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setMinimumSize(QSize(0, 100))
        self.header_frame.setMaximumSize(QSize(16777215, 100))
        self.header_frame.setStyleSheet(u".QFrame{\n"
"background:rgb(25, 25, 25);\n"
"margin: 0 0 0 0;\n"
"padding: 0 0 0 0;\n"
"}")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.today_label = QLabel(self.header_frame)
        self.today_label.setObjectName(u"today_label")
        self.today_label.setMinimumSize(QSize(0, 20))
        font = QFont()
        font.setPointSize(12)
        self.today_label.setFont(font)
        self.today_label.setStyleSheet(u".QLabel{\n"
"color:rgb(255, 234, 8);\n"
"}")

        self.horizontalLayout_2.addWidget(self.today_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.enterprise_name = QLabel(self.header_frame)
        self.enterprise_name.setObjectName(u"enterprise_name")
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(30)
        self.enterprise_name.setFont(font1)
        self.enterprise_name.setStyleSheet(u".QLabel{\n"
"color:white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.enterprise_name)

        self.organisation_name = QLabel(self.header_frame)
        self.organisation_name.setObjectName(u"organisation_name")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.organisation_name.setFont(font2)
        self.organisation_name.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 234, 8);\n"
"}")

        self.horizontalLayout_2.addWidget(self.organisation_name)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.header_frame)

        self.Container = QFrame(self.Body)
        self.Container.setObjectName(u"Container")
        sizePolicy.setHeightForWidth(self.Container.sizePolicy().hasHeightForWidth())
        self.Container.setSizePolicy(sizePolicy)
        self.Container.setStyleSheet(u".QFrame{\n"
"margin: 0px;\n"
"background: rgb(25, 25, 25);\n"
"padding: 0;\n"
"}")
        self.Container.setFrameShape(QFrame.StyledPanel)
        self.Container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.SideBar_Frame = QFrame(self.Container)
        self.SideBar_Frame.setObjectName(u"SideBar_Frame")
        sizePolicy.setHeightForWidth(self.SideBar_Frame.sizePolicy().hasHeightForWidth())
        self.SideBar_Frame.setSizePolicy(sizePolicy)
        self.SideBar_Frame.setMinimumSize(QSize(250, 0))
        self.SideBar_Frame.setMaximumSize(QSize(250, 16777215))
        self.SideBar_Frame.setStyleSheet(u".QFrame{\n"
"background:rgb(25, 25, 25);\n"
"}")
        self.SideBar_Frame.setFrameShape(QFrame.StyledPanel)
        self.SideBar_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.SideBar_Frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.SideBar_Frame_Buttons = QFrame(self.SideBar_Frame)
        self.SideBar_Frame_Buttons.setObjectName(u"SideBar_Frame_Buttons")
        sizePolicy.setHeightForWidth(self.SideBar_Frame_Buttons.sizePolicy().hasHeightForWidth())
        self.SideBar_Frame_Buttons.setSizePolicy(sizePolicy)
        self.SideBar_Frame_Buttons.setStyleSheet(u"")
        self.SideBar_Frame_Buttons.setFrameShape(QFrame.StyledPanel)
        self.SideBar_Frame_Buttons.setFrameShadow(QFrame.Raised)
        self.SideBar_Frame_Buttons.setLineWidth(1)
        self.verticalLayout_5 = QVBoxLayout(self.SideBar_Frame_Buttons)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.liste_employee_btn = QPushButton(self.SideBar_Frame_Buttons)
        self.liste_employee_btn.setObjectName(u"liste_employee_btn")
        sizePolicy.setHeightForWidth(self.liste_employee_btn.sizePolicy().hasHeightForWidth())
        self.liste_employee_btn.setSizePolicy(sizePolicy)
        self.liste_employee_btn.setMinimumSize(QSize(250, 50))
        self.liste_employee_btn.setMaximumSize(QSize(250, 50))
        self.liste_employee_btn.setSizeIncrement(QSize(0, 0))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(25, 25, 25, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.liste_employee_btn.setPalette(palette)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.liste_employee_btn.setFont(font3)
        self.liste_employee_btn.setMouseTracking(False)
        self.liste_employee_btn.setAutoFillBackground(False)
        self.liste_employee_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color:rgb(255, 234, 8);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	color:rgb(0,0,0);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color:  rgb(255, 234, 8);\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../assets/employee.png", QSize(), QIcon.Normal, QIcon.Off)
        self.liste_employee_btn.setIcon(icon1)
        self.liste_employee_btn.setIconSize(QSize(30, 30))
        self.liste_employee_btn.setAutoDefault(False)

        self.verticalLayout_5.addWidget(self.liste_employee_btn)

        self.liste_presence_btn = QPushButton(self.SideBar_Frame_Buttons)
        self.liste_presence_btn.setObjectName(u"liste_presence_btn")
        sizePolicy.setHeightForWidth(self.liste_presence_btn.sizePolicy().hasHeightForWidth())
        self.liste_presence_btn.setSizePolicy(sizePolicy)
        self.liste_presence_btn.setMinimumSize(QSize(250, 50))
        self.liste_presence_btn.setMaximumSize(QSize(250, 50))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.liste_presence_btn.setFont(font4)
        self.liste_presence_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color:rgb(255, 234, 8);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	color:rgb(0,0,0);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color:  rgb(255, 234, 8);\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../assets/schedule.png", QSize(), QIcon.Normal, QIcon.Off)
        self.liste_presence_btn.setIcon(icon2)
        self.liste_presence_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.liste_presence_btn)

        self.payements_en_cours_btn = QPushButton(self.SideBar_Frame_Buttons)
        self.payements_en_cours_btn.setObjectName(u"payements_en_cours_btn")
        sizePolicy.setHeightForWidth(self.payements_en_cours_btn.sizePolicy().hasHeightForWidth())
        self.payements_en_cours_btn.setSizePolicy(sizePolicy)
        self.payements_en_cours_btn.setMinimumSize(QSize(250, 50))
        self.payements_en_cours_btn.setMaximumSize(QSize(250, 50))
        self.payements_en_cours_btn.setFont(font4)
        self.payements_en_cours_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color:rgb(255, 234, 8);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	color:rgb(0,0,0);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color:  rgb(255, 234, 8);\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../assets/time-is-money.png", QSize(), QIcon.Normal, QIcon.Off)
        self.payements_en_cours_btn.setIcon(icon3)
        self.payements_en_cours_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.payements_en_cours_btn)

        self.payements_a_faire_btn = QPushButton(self.SideBar_Frame_Buttons)
        self.payements_a_faire_btn.setObjectName(u"payements_a_faire_btn")
        sizePolicy.setHeightForWidth(self.payements_a_faire_btn.sizePolicy().hasHeightForWidth())
        self.payements_a_faire_btn.setSizePolicy(sizePolicy)
        self.payements_a_faire_btn.setMinimumSize(QSize(250, 50))
        self.payements_a_faire_btn.setMaximumSize(QSize(250, 50))
        self.payements_a_faire_btn.setFont(font4)
        self.payements_a_faire_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color:rgb(255, 234, 8);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	color:rgb(0,0,0);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color:  rgb(255, 234, 8);\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"../assets/cash-payment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.payements_a_faire_btn.setIcon(icon4)
        self.payements_a_faire_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.payements_a_faire_btn)

        self.payements_reussis_btn = QPushButton(self.SideBar_Frame_Buttons)
        self.payements_reussis_btn.setObjectName(u"payements_reussis_btn")
        sizePolicy.setHeightForWidth(self.payements_reussis_btn.sizePolicy().hasHeightForWidth())
        self.payements_reussis_btn.setSizePolicy(sizePolicy)
        self.payements_reussis_btn.setMinimumSize(QSize(250, 50))
        self.payements_reussis_btn.setMaximumSize(QSize(250, 50))
        self.payements_reussis_btn.setFont(font4)
        self.payements_reussis_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color:rgb(255, 234, 8);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	color:rgb(0,0,0);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color:  rgb(255, 234, 8);\n"
"}\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"../assets/business.png", QSize(), QIcon.Normal, QIcon.Off)
        self.payements_reussis_btn.setIcon(icon5)
        self.payements_reussis_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.payements_reussis_btn)

        self.credits_btn = QPushButton(self.SideBar_Frame_Buttons)
        self.credits_btn.setObjectName(u"credits_btn")
        self.credits_btn.setMinimumSize(QSize(250, 50))
        self.credits_btn.setMaximumSize(QSize(250, 50))
        self.credits_btn.setFont(font4)
        self.credits_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color:rgb(255, 234, 8);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	color:rgb(0,0,0);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color:  rgb(255, 234, 8);\n"
"}\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"../assets/cashback.png", QSize(), QIcon.Normal, QIcon.Off)
        self.credits_btn.setIcon(icon6)
        self.credits_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.credits_btn)

        self.sync_date_btn = QPushButton(self.SideBar_Frame_Buttons)
        self.sync_date_btn.setObjectName(u"sync_date_btn")
        self.sync_date_btn.setMinimumSize(QSize(250, 50))
        self.sync_date_btn.setMaximumSize(QSize(250, 50))
        self.sync_date_btn.setFont(font4)
        self.sync_date_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color:rgb(255, 234, 8);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	color:rgb(0,0,0);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color:  rgb(255, 234, 8);\n"
"}\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"../assets/sync.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sync_date_btn.setIcon(icon7)
        self.sync_date_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.sync_date_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.contact_btn = QPushButton(self.SideBar_Frame_Buttons)
        self.contact_btn.setObjectName(u"contact_btn")
        self.contact_btn.setMinimumSize(QSize(250, 50))
        self.contact_btn.setMaximumSize(QSize(250, 50))
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.contact_btn.setFont(font5)
        self.contact_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color:rgb(255, 234, 8);\n"
"	border-left: 3px solid rgb(255, 234, 8);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"../assets/information.png", QSize(), QIcon.Normal, QIcon.Off)
        self.contact_btn.setIcon(icon8)
        self.contact_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.contact_btn)


        self.verticalLayout_3.addWidget(self.SideBar_Frame_Buttons)


        self.horizontalLayout.addWidget(self.SideBar_Frame)

        self.Content_Frame = QFrame(self.Container)
        self.Content_Frame.setObjectName(u"Content_Frame")
        sizePolicy.setHeightForWidth(self.Content_Frame.sizePolicy().hasHeightForWidth())
        self.Content_Frame.setSizePolicy(sizePolicy)
        self.Content_Frame.setStyleSheet(u"QFrame{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.Content_Frame.setFrameShape(QFrame.StyledPanel)
        self.Content_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Content_Frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.Content_Frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u".QTableWidget{\n"
"background: rgb(40, 40, 40);\n"
"color:rgb(188,255,54);\n"
"}\n"
".QTableView::section\n"
"{\n"
"	margin-top:0px;\n"
"	margin-left:0px;\n"
"	margin-right:0px;\n"
"	margin-bottom:0px;\n"
"	padding-top:0;\n"
"	padding-left:0;\n"
"	padding-right:0;\n"
"	padding-bottom:0;\n"
"	border: 2px solid white;   \n"
"    color:rgb(188,255,54);    \n"
"}\n"
"\n"
"QTableView::item \n"
"{\n"
"	margin-top:0px;\n"
"	margin-left:0px;\n"
"	margin-right:0px;\n"
"	margin-bottom:0px;\n"
"	padding-top:0;\n"
"	padding-left:0;\n"
"	padding-right:0;\n"
"	padding-bottom:0;\n"
"	border: 2px solid white;   \n"
"    color:rgb(255, 234, 8);\n"
"}\n"
"\n"
".QTableView::item::focus\n"
"{   \n"
"    color: #000000;\n"
"   background: #ddddaa;           \n"
"}        \n"
"QTableView::item::selected\n"
"{   \n"
"    color: #000000;\n"
"    background: #ddddaa;         \n"
"}\n"
".QHeaderView::section {\n"
"    background-color:rgb(255, 234, 8); \n"
"	color:black;\n"
"    padding: 2px;\n"
"    border-style: none;\n"
"    border-"
                        "bottom: 0px solid #fffff8;\n"
"    border-right: 3px solid #fffff8;\n"
"}\n"
".QLineEdit{\n"
"background: rgb(40, 40, 40);\n"
"color: rgb(255, 234, 8);\n"
"border-radius: 10px;\n"
"}")
        self.stackedWidget.setFrameShadow(QFrame.Sunken)
        self.liste_employees_page = QWidget()
        self.liste_employees_page.setObjectName(u"liste_employees_page")
        self.liste_employees_page.setMinimumSize(QSize(40, 0))
        self.liste_employees_page.setSizeIncrement(QSize(2, 2))
        self.liste_employees_page.setBaseSize(QSize(50, 50))
        self.liste_employees_page.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.liste_employees_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.employee_frame_header = QWidget(self.liste_employees_page)
        self.employee_frame_header.setObjectName(u"employee_frame_header")
        self.employee_frame_header.setMinimumSize(QSize(0, 70))
        self.employee_frame_header.setMaximumSize(QSize(16777215, 70))
        self.employee_frame_header.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.employee_frame_header)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_2 = QWidget(self.employee_frame_header)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(250, 40))
        self.widget_2.setMaximumSize(QSize(250, 40))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"color:rgb(255, 234, 8);\n"
"}")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_19.setSpacing(2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.total_results_text_employee = QLabel(self.widget_2)
        self.total_results_text_employee.setObjectName(u"total_results_text_employee")
        self.total_results_text_employee.setMinimumSize(QSize(0, 40))
        self.total_results_text_employee.setMaximumSize(QSize(40, 40))
        self.total_results_text_employee.setSizeIncrement(QSize(2, 2))
        self.total_results_text_employee.setBaseSize(QSize(2, 2))
        font6 = QFont()
        font6.setBold(True)
        font6.setItalic(False)
        font6.setUnderline(True)
        font6.setWeight(75)
        font6.setStrikeOut(False)
        self.total_results_text_employee.setFont(font6)
        self.total_results_text_employee.setStyleSheet(u".QLabel{\n"
"color:yellow;\n"
"font-size:15px;\n"
"}")
        self.total_results_text_employee.setTextFormat(Qt.MarkdownText)
        self.total_results_text_employee.setPixmap(QPixmap(u"../assets/employee.png"))
        self.total_results_text_employee.setScaledContents(True)
        self.total_results_text_employee.setAlignment(Qt.AlignCenter)
        self.total_results_text_employee.setIndent(1)

        self.horizontalLayout_19.addWidget(self.total_results_text_employee)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        font7 = QFont()
        font7.setFamily(u"Lucida Sans")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_2.setFont(font7)

        self.horizontalLayout_19.addWidget(self.label_2)


        self.horizontalLayout_4.addWidget(self.widget_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.widget_9 = QWidget(self.employee_frame_header)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(80, 0))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.liste_employee_search_field = QLineEdit(self.widget_9)
        self.liste_employee_search_field.setObjectName(u"liste_employee_search_field")
        self.liste_employee_search_field.setMinimumSize(QSize(40, 40))
        self.liste_employee_search_field.setMaximumSize(QSize(300, 16777215))
        font8 = QFont()
        font8.setPointSize(10)
        self.liste_employee_search_field.setFont(font8)
        self.liste_employee_search_field.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.liste_employee_search_field)

        self.liste_employee_search_btn = QPushButton(self.widget_9)
        self.liste_employee_search_btn.setObjectName(u"liste_employee_search_btn")
        self.liste_employee_search_btn.setMinimumSize(QSize(0, 40))
        font9 = QFont()
        font9.setPointSize(9)
        self.liste_employee_search_btn.setFont(font9)
        self.liste_employee_search_btn.setStyleSheet(u".QPushButton{\n"
"background: rgb(200, 150, 200);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background: rgb(220, 120, 220);\n"
"}\n"
"\n"
".QPushButton:clicked{\n"
"background: rgb(250, 100, 250);\n"
"}")

        self.horizontalLayout_5.addWidget(self.liste_employee_search_btn)


        self.horizontalLayout_4.addWidget(self.widget_9)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addWidget(self.employee_frame_header)

        self.employee_frame_content = QWidget(self.liste_employees_page)
        self.employee_frame_content.setObjectName(u"employee_frame_content")
        self.employee_frame_content.setMinimumSize(QSize(0, 0))
        self.employee_frame_content.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.employee_frame_content)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.liste_employee_table = QTableWidget(self.employee_frame_content)
        if (self.liste_employee_table.columnCount() < 10):
            self.liste_employee_table.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.liste_employee_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font5);
        self.liste_employee_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font5);
        self.liste_employee_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.liste_employee_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.liste_employee_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font5);
        self.liste_employee_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font5);
        self.liste_employee_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font5);
        self.liste_employee_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font5);
        self.liste_employee_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font5);
        self.liste_employee_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.liste_employee_table.setObjectName(u"liste_employee_table")
        self.liste_employee_table.setFont(font4)
        self.liste_employee_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.liste_employee_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.liste_employee_table.horizontalHeader().setMinimumSectionSize(250)
        self.liste_employee_table.horizontalHeader().setDefaultSectionSize(250)
        self.liste_employee_table.verticalHeader().setMinimumSectionSize(80)
        self.liste_employee_table.verticalHeader().setDefaultSectionSize(80)

        self.verticalLayout_11.addWidget(self.liste_employee_table)


        self.verticalLayout_6.addWidget(self.employee_frame_content)

        self.employee_frame_actions = QWidget(self.liste_employees_page)
        self.employee_frame_actions.setObjectName(u"employee_frame_actions")
        self.employee_frame_actions.setMinimumSize(QSize(0, 80))
        self.employee_frame_actions.setMaximumSize(QSize(16777215, 80))
        self.employee_frame_actions.setSizeIncrement(QSize(0, 100))
        self.employee_frame_actions.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.employee_frame_actions)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.actions_list = QWidget(self.employee_frame_actions)
        self.actions_list.setObjectName(u"actions_list")
        self.actions_list.setMinimumSize(QSize(0, 80))
        self.actions_list.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.actions_list)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_6 = QWidget(self.actions_list)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(100, 0))
        self.widget_6.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.widget_6)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.add_employee_btn = QPushButton(self.widget_6)
        self.add_employee_btn.setObjectName(u"add_employee_btn")
        self.add_employee_btn.setMinimumSize(QSize(110, 50))
        font10 = QFont()
        font10.setFamily(u"Segoe UI Black")
        font10.setPointSize(8)
        font10.setBold(True)
        font10.setWeight(75)
        self.add_employee_btn.setFont(font10)
        self.add_employee_btn.setStyleSheet(u".QPushButton{\n"
"background: rgb(212, 250, 150);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton::hover{\n"
"background: rgb(197, 253, 89);\n"
"}\n"
"\n"
".QPushButton::pressed{\n"
"background: rgb(188, 255, 54);\n"
"}")

        self.verticalLayout_8.addWidget(self.add_employee_btn)


        self.horizontalLayout_3.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.actions_list)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(100, 0))
        self.widget_7.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.widget_7)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.update_employee_btn = QPushButton(self.widget_7)
        self.update_employee_btn.setObjectName(u"update_employee_btn")
        self.update_employee_btn.setMinimumSize(QSize(110, 50))
        font11 = QFont()
        font11.setFamily(u"Segoe UI Black")
        font11.setBold(True)
        font11.setWeight(75)
        self.update_employee_btn.setFont(font11)
        self.update_employee_btn.setStyleSheet(u".QPushButton{\n"
"background: rgb(100, 180, 250);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton::hover{\n"
"background:  rgb(90, 200, 250);\n"
"}\n"
"\n"
".QPushButton::pressed{\n"
"background: rgb(50, 220, 250);\n"
"}")

        self.verticalLayout_9.addWidget(self.update_employee_btn)


        self.horizontalLayout_3.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.actions_list)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(100, 0))
        self.widget_8.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.widget_8)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.delete_employee_btn = QPushButton(self.widget_8)
        self.delete_employee_btn.setObjectName(u"delete_employee_btn")
        self.delete_employee_btn.setMinimumSize(QSize(110, 50))
        self.delete_employee_btn.setFont(font11)
        self.delete_employee_btn.setStyleSheet(u".QPushButton{\n"
"background:rgb(255, 109, 109);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton::hover{\n"
"background:rgb(255, 90, 90);\n"
"}\n"
"\n"
".QPushButton::pressed{\n"
"background: rgb(255, 45, 45);\n"
"}")
        self.delete_employee_btn.setFlat(False)

        self.verticalLayout_10.addWidget(self.delete_employee_btn)


        self.horizontalLayout_3.addWidget(self.widget_8)


        self.verticalLayout_7.addWidget(self.actions_list)


        self.verticalLayout_6.addWidget(self.employee_frame_actions)

        self.stackedWidget.addWidget(self.liste_employees_page)
        self.liste_presence_page = QWidget()
        self.liste_presence_page.setObjectName(u"liste_presence_page")
        self.liste_presence_page.setSizeIncrement(QSize(2, 2))
        self.liste_presence_page.setBaseSize(QSize(50, 50))
        self.liste_presence_page.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.verticalLayout_22 = QVBoxLayout(self.liste_presence_page)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.liste_presence_frame_header = QWidget(self.liste_presence_page)
        self.liste_presence_frame_header.setObjectName(u"liste_presence_frame_header")
        self.liste_presence_frame_header.setMinimumSize(QSize(0, 70))
        self.liste_presence_frame_header.setMaximumSize(QSize(16777215, 70))
        self.liste_presence_frame_header.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.liste_presence_frame_header)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_3 = QWidget(self.liste_presence_frame_header)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(250, 40))
        self.widget_3.setMaximumSize(QSize(250, 40))
        self.widget_3.setStyleSheet(u"QWidget{\n"
"color:rgb(255, 234, 8);\n"
"}")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_20.setSpacing(2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.total_results_text_presence = QLabel(self.widget_3)
        self.total_results_text_presence.setObjectName(u"total_results_text_presence")
        self.total_results_text_presence.setMinimumSize(QSize(40, 40))
        self.total_results_text_presence.setMaximumSize(QSize(40, 40))
        self.total_results_text_presence.setSizeIncrement(QSize(2, 2))
        self.total_results_text_presence.setBaseSize(QSize(2, 2))
        font12 = QFont()
        font12.setBold(False)
        font12.setWeight(50)
        self.total_results_text_presence.setFont(font12)
        self.total_results_text_presence.setStyleSheet(u".QLabel{\n"
"color:yellow;\n"
"font-size:15px;\n"
"}")
        self.total_results_text_presence.setPixmap(QPixmap(u"../assets/schedule.png"))
        self.total_results_text_presence.setScaledContents(True)
        self.total_results_text_presence.setAlignment(Qt.AlignCenter)
        self.total_results_text_presence.setIndent(1)
        self.total_results_text_presence.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout_20.addWidget(self.total_results_text_presence)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font7)

        self.horizontalLayout_20.addWidget(self.label_3)


        self.horizontalLayout_10.addWidget(self.widget_3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.widget_17 = QWidget(self.liste_presence_frame_header)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.liste_presence_search_field = QLineEdit(self.widget_17)
        self.liste_presence_search_field.setObjectName(u"liste_presence_search_field")
        self.liste_presence_search_field.setMinimumSize(QSize(40, 40))
        self.liste_presence_search_field.setMaximumSize(QSize(300, 16777215))
        self.liste_presence_search_field.setFont(font8)
        self.liste_presence_search_field.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.liste_presence_search_field)

        self.liste_presence_search_btn = QPushButton(self.widget_17)
        self.liste_presence_search_btn.setObjectName(u"liste_presence_search_btn")
        self.liste_presence_search_btn.setMinimumSize(QSize(0, 40))
        self.liste_presence_search_btn.setFont(font9)
        self.liste_presence_search_btn.setStyleSheet(u".QPushButton{\n"
"background: rgb(200, 150, 200);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background: rgb(220, 120, 220);\n"
"}\n"
"\n"
".QPushButton:clicked{\n"
"background: rgb(250, 100, 250);\n"
"}")

        self.horizontalLayout_11.addWidget(self.liste_presence_search_btn)


        self.horizontalLayout_10.addWidget(self.widget_17)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_22.addWidget(self.liste_presence_frame_header)

        self.liste_presence_frame_content = QWidget(self.liste_presence_page)
        self.liste_presence_frame_content.setObjectName(u"liste_presence_frame_content")
        self.liste_presence_frame_content.setMinimumSize(QSize(0, 0))
        self.liste_presence_frame_content.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"color:white;\n"
"}")
        self.verticalLayout_17 = QVBoxLayout(self.liste_presence_frame_content)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.liste_presence_table = QTableWidget(self.liste_presence_frame_content)
        if (self.liste_presence_table.columnCount() < 6):
            self.liste_presence_table.setColumnCount(6)
        brush5 = QBrush(QColor(255, 255, 255, 255))
        brush5.setStyle(Qt.NoBrush)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font5);
        __qtablewidgetitem10.setForeground(brush5);
        self.liste_presence_table.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font5);
        self.liste_presence_table.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font5);
        self.liste_presence_table.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font5);
        self.liste_presence_table.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font5);
        self.liste_presence_table.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font5);
        self.liste_presence_table.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        self.liste_presence_table.setObjectName(u"liste_presence_table")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.liste_presence_table.sizePolicy().hasHeightForWidth())
        self.liste_presence_table.setSizePolicy(sizePolicy1)
        self.liste_presence_table.setMinimumSize(QSize(0, 0))
        self.liste_presence_table.setSizeIncrement(QSize(0, 0))
        self.liste_presence_table.setBaseSize(QSize(50, 50))
        font13 = QFont()
        font13.setPointSize(11)
        font13.setBold(True)
        font13.setWeight(75)
        self.liste_presence_table.setFont(font13)
        self.liste_presence_table.setStyleSheet(u".QTableWidget{\n"
"background: rgb(40, 40, 40);\n"
"color:rgb(188,255,54);\n"
"}")
        self.liste_presence_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.liste_presence_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.liste_presence_table.setSortingEnabled(False)
        self.liste_presence_table.setCornerButtonEnabled(False)
        self.liste_presence_table.horizontalHeader().setMinimumSectionSize(250)
        self.liste_presence_table.horizontalHeader().setDefaultSectionSize(250)
        self.liste_presence_table.verticalHeader().setMinimumSectionSize(80)
        self.liste_presence_table.verticalHeader().setDefaultSectionSize(80)

        self.verticalLayout_17.addWidget(self.liste_presence_table)


        self.verticalLayout_22.addWidget(self.liste_presence_frame_content)

        self.liste_presence_frame_actions = QWidget(self.liste_presence_page)
        self.liste_presence_frame_actions.setObjectName(u"liste_presence_frame_actions")
        self.liste_presence_frame_actions.setMinimumSize(QSize(0, 80))
        self.liste_presence_frame_actions.setMaximumSize(QSize(16777215, 80))
        self.liste_presence_frame_actions.setSizeIncrement(QSize(0, 80))
        self.liste_presence_frame_actions.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.liste_presence_frame_actions)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.actions_list_3 = QWidget(self.liste_presence_frame_actions)
        self.actions_list_3.setObjectName(u"actions_list_3")
        self.actions_list_3.setMinimumSize(QSize(0, 80))
        self.actions_list_3.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_9 = QHBoxLayout(self.actions_list_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_14 = QWidget(self.actions_list_3)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(100, 0))
        self.widget_14.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_19 = QVBoxLayout(self.widget_14)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.faire_presence_btn = QPushButton(self.widget_14)
        self.faire_presence_btn.setObjectName(u"faire_presence_btn")
        self.faire_presence_btn.setMinimumSize(QSize(100, 50))
        self.faire_presence_btn.setFont(font11)
        self.faire_presence_btn.setStyleSheet(u".QPushButton{\n"
"background: rgb(100, 180, 250);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton::hover{\n"
"background:  rgb(90, 200, 250);\n"
"}\n"
"\n"
".QPushButton::pressed{\n"
"background: rgb(50, 220, 250);\n"
"}")

        self.verticalLayout_19.addWidget(self.faire_presence_btn)


        self.horizontalLayout_9.addWidget(self.widget_14)


        self.verticalLayout_18.addWidget(self.actions_list_3)


        self.verticalLayout_22.addWidget(self.liste_presence_frame_actions)

        self.stackedWidget.addWidget(self.liste_presence_page)
        self.credit_page = QWidget()
        self.credit_page.setObjectName(u"credit_page")
        self.credit_page.setSizeIncrement(QSize(2, 2))
        self.credit_page.setBaseSize(QSize(50, 50))
        self.verticalLayout_14 = QVBoxLayout(self.credit_page)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.credit_frame_header = QWidget(self.credit_page)
        self.credit_frame_header.setObjectName(u"credit_frame_header")
        self.credit_frame_header.setMinimumSize(QSize(0, 70))
        self.credit_frame_header.setMaximumSize(QSize(16777215, 70))
        self.credit_frame_header.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.horizontalLayout_21 = QHBoxLayout(self.credit_frame_header)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.widget_4 = QWidget(self.credit_frame_header)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(250, 40))
        self.widget_4.setMaximumSize(QSize(250, 40))
        self.widget_4.setStyleSheet(u"QWidget{\n"
"color:rgb(255, 234, 8);\n"
"}")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_24.setSpacing(2)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.total_results_credit = QLabel(self.widget_4)
        self.total_results_credit.setObjectName(u"total_results_credit")
        self.total_results_credit.setMinimumSize(QSize(40, 40))
        self.total_results_credit.setMaximumSize(QSize(40, 40))
        self.total_results_credit.setSizeIncrement(QSize(2, 2))
        self.total_results_credit.setBaseSize(QSize(2, 2))
        font14 = QFont()
        self.total_results_credit.setFont(font14)
        self.total_results_credit.setStyleSheet(u".QLabel{\n"
"color:yellow;\n"
"font-size:15px;\n"
"}")
        self.total_results_credit.setPixmap(QPixmap(u"../assets/cashback.png"))
        self.total_results_credit.setScaledContents(True)
        self.total_results_credit.setAlignment(Qt.AlignCenter)
        self.total_results_credit.setWordWrap(False)
        self.total_results_credit.setIndent(1)

        self.horizontalLayout_24.addWidget(self.total_results_credit)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font7)

        self.horizontalLayout_24.addWidget(self.label_4)


        self.horizontalLayout_21.addWidget(self.widget_4)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_15)

        self.widget_28 = QWidget(self.credit_frame_header)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.credit_recherche_field = QLineEdit(self.widget_28)
        self.credit_recherche_field.setObjectName(u"credit_recherche_field")
        self.credit_recherche_field.setMinimumSize(QSize(40, 40))
        self.credit_recherche_field.setMaximumSize(QSize(300, 16777215))
        self.credit_recherche_field.setFont(font8)
        self.credit_recherche_field.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.credit_recherche_field)

        self.credit_recherche_btn = QPushButton(self.widget_28)
        self.credit_recherche_btn.setObjectName(u"credit_recherche_btn")
        self.credit_recherche_btn.setMinimumSize(QSize(0, 40))
        self.credit_recherche_btn.setFont(font9)
        self.credit_recherche_btn.setStyleSheet(u".QPushButton{\n"
"background: rgb(200, 150, 200);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background: rgb(220, 120, 220);\n"
"}\n"
"\n"
".QPushButton:clicked{\n"
"background: rgb(250, 100, 250);\n"
"}")

        self.horizontalLayout_22.addWidget(self.credit_recherche_btn)


        self.horizontalLayout_21.addWidget(self.widget_28)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_16)


        self.verticalLayout_14.addWidget(self.credit_frame_header)

        self.credit_frame_content = QWidget(self.credit_page)
        self.credit_frame_content.setObjectName(u"credit_frame_content")
        self.credit_frame_content.setMinimumSize(QSize(0, 0))
        self.credit_frame_content.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.verticalLayout_39 = QVBoxLayout(self.credit_frame_content)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.credit_table = QTableWidget(self.credit_frame_content)
        if (self.credit_table.columnCount() < 6):
            self.credit_table.setColumnCount(6)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font5);
        self.credit_table.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font5);
        self.credit_table.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font5);
        self.credit_table.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font5);
        self.credit_table.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font5);
        self.credit_table.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font5);
        self.credit_table.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        self.credit_table.setObjectName(u"credit_table")
        self.credit_table.setSizeIncrement(QSize(0, 0))
        self.credit_table.setBaseSize(QSize(50, 50))
        font15 = QFont()
        font15.setFamily(u"Segoe UI")
        font15.setPointSize(11)
        font15.setBold(True)
        font15.setWeight(75)
        self.credit_table.setFont(font15)
        self.credit_table.setStyleSheet(u".QTableWidget{\n"
"background: rgb(40, 40, 40);\n"
"color:rgb(188,255,54);\n"
"}")
        self.credit_table.setAutoScrollMargin(10)
        self.credit_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.credit_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.credit_table.horizontalHeader().setMinimumSectionSize(250)
        self.credit_table.horizontalHeader().setDefaultSectionSize(250)
        self.credit_table.verticalHeader().setMinimumSectionSize(80)
        self.credit_table.verticalHeader().setDefaultSectionSize(80)

        self.verticalLayout_39.addWidget(self.credit_table)


        self.verticalLayout_14.addWidget(self.credit_frame_content)

        self.credit_frame_actions = QWidget(self.credit_page)
        self.credit_frame_actions.setObjectName(u"credit_frame_actions")
        self.credit_frame_actions.setMinimumSize(QSize(0, 80))
        self.credit_frame_actions.setMaximumSize(QSize(16777215, 80))
        self.credit_frame_actions.setSizeIncrement(QSize(0, 80))
        self.credit_frame_actions.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.verticalLayout_40 = QVBoxLayout(self.credit_frame_actions)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.actions_list_7 = QWidget(self.credit_frame_actions)
        self.actions_list_7.setObjectName(u"actions_list_7")
        self.actions_list_7.setMinimumSize(QSize(0, 80))
        self.actions_list_7.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_23 = QHBoxLayout(self.actions_list_7)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.widget_29 = QWidget(self.actions_list_7)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMinimumSize(QSize(100, 0))
        self.widget_29.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_41 = QVBoxLayout(self.widget_29)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_23.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.actions_list_7)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMinimumSize(QSize(100, 0))
        self.widget_30.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_42 = QVBoxLayout(self.widget_30)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.payer_credit_btn = QPushButton(self.widget_30)
        self.payer_credit_btn.setObjectName(u"payer_credit_btn")
        self.payer_credit_btn.setMinimumSize(QSize(100, 50))
        self.payer_credit_btn.setFont(font11)
        self.payer_credit_btn.setStyleSheet(u".QPushButton{\n"
"background: rgb(100, 180, 250);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton::hover{\n"
"background:  rgb(90, 200, 250);\n"
"}\n"
"\n"
".QPushButton::pressed{\n"
"background: rgb(50, 220, 250);\n"
"}")

        self.verticalLayout_42.addWidget(self.payer_credit_btn)


        self.horizontalLayout_23.addWidget(self.widget_30)

        self.widget_31 = QWidget(self.actions_list_7)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMinimumSize(QSize(100, 0))
        self.widget_31.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_43 = QVBoxLayout(self.widget_31)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_23.addWidget(self.widget_31)


        self.verticalLayout_40.addWidget(self.actions_list_7)


        self.verticalLayout_14.addWidget(self.credit_frame_actions)

        self.stackedWidget.addWidget(self.credit_page)
        self.payements_en_cours_page = QWidget()
        self.payements_en_cours_page.setObjectName(u"payements_en_cours_page")
        self.payements_en_cours_page.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.payements_en_cours_page)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.payements_en_cours_frame_header = QWidget(self.payements_en_cours_page)
        self.payements_en_cours_frame_header.setObjectName(u"payements_en_cours_frame_header")
        self.payements_en_cours_frame_header.setMinimumSize(QSize(0, 70))
        self.payements_en_cours_frame_header.setMaximumSize(QSize(16777215, 70))
        self.payements_en_cours_frame_header.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.payements_en_cours_frame_header)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_5 = QWidget(self.payements_en_cours_frame_header)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(250, 40))
        self.widget_5.setMaximumSize(QSize(250, 40))
        self.widget_5.setStyleSheet(u"QWidget{\n"
"color:rgb(255, 234, 8);\n"
"}")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_25.setSpacing(2)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.total_results_text_payements_en_cours = QLabel(self.widget_5)
        self.total_results_text_payements_en_cours.setObjectName(u"total_results_text_payements_en_cours")
        self.total_results_text_payements_en_cours.setMinimumSize(QSize(40, 40))
        self.total_results_text_payements_en_cours.setMaximumSize(QSize(40, 40))
        self.total_results_text_payements_en_cours.setSizeIncrement(QSize(2, 2))
        self.total_results_text_payements_en_cours.setBaseSize(QSize(2, 2))
        self.total_results_text_payements_en_cours.setFont(font14)
        self.total_results_text_payements_en_cours.setStyleSheet(u".QLabel{\n"
"color:yellow;\n"
"font-size:15px;\n"
"}")
        self.total_results_text_payements_en_cours.setPixmap(QPixmap(u"../assets/time-is-money.png"))
        self.total_results_text_payements_en_cours.setScaledContents(True)
        self.total_results_text_payements_en_cours.setAlignment(Qt.AlignCenter)
        self.total_results_text_payements_en_cours.setIndent(1)

        self.horizontalLayout_25.addWidget(self.total_results_text_payements_en_cours)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)

        self.horizontalLayout_25.addWidget(self.label_5)


        self.horizontalLayout_6.addWidget(self.widget_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.widget_10 = QWidget(self.payements_en_cours_frame_header)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.payements_en_cours__search_field = QLineEdit(self.widget_10)
        self.payements_en_cours__search_field.setObjectName(u"payements_en_cours__search_field")
        self.payements_en_cours__search_field.setMinimumSize(QSize(40, 40))
        self.payements_en_cours__search_field.setMaximumSize(QSize(300, 16777215))
        self.payements_en_cours__search_field.setFont(font8)
        self.payements_en_cours__search_field.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.payements_en_cours__search_field)

        self.payements_en_cours_search_btn = QPushButton(self.widget_10)
        self.payements_en_cours_search_btn.setObjectName(u"payements_en_cours_search_btn")
        self.payements_en_cours_search_btn.setMinimumSize(QSize(0, 40))
        self.payements_en_cours_search_btn.setFont(font9)
        self.payements_en_cours_search_btn.setStyleSheet(u".QPushButton{\n"
"background: rgb(200, 150, 200);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background: rgb(220, 120, 220);\n"
"}\n"
"\n"
".QPushButton:clicked{\n"
"background: rgb(250, 100, 250);\n"
"}")

        self.horizontalLayout_7.addWidget(self.payements_en_cours_search_btn)


        self.horizontalLayout_6.addWidget(self.widget_10)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_20.addWidget(self.payements_en_cours_frame_header)

        self.payements_en_cours_frame_content = QWidget(self.payements_en_cours_page)
        self.payements_en_cours_frame_content.setObjectName(u"payements_en_cours_frame_content")
        self.payements_en_cours_frame_content.setMinimumSize(QSize(0, 0))
        self.payements_en_cours_frame_content.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.payements_en_cours_frame_content)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.payements_en_cours_table = QTableWidget(self.payements_en_cours_frame_content)
        if (self.payements_en_cours_table.columnCount() < 10):
            self.payements_en_cours_table.setColumnCount(10)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font5);
        __qtablewidgetitem22.setBackground(QColor(255, 255, 255));
        self.payements_en_cours_table.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font5);
        self.payements_en_cours_table.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font5);
        self.payements_en_cours_table.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font5);
        self.payements_en_cours_table.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font5);
        self.payements_en_cours_table.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font5);
        self.payements_en_cours_table.setHorizontalHeaderItem(5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font5);
        self.payements_en_cours_table.setHorizontalHeaderItem(6, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font5);
        self.payements_en_cours_table.setHorizontalHeaderItem(7, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font5);
        self.payements_en_cours_table.setHorizontalHeaderItem(8, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font5);
        self.payements_en_cours_table.setHorizontalHeaderItem(9, __qtablewidgetitem31)
        self.payements_en_cours_table.setObjectName(u"payements_en_cours_table")
        self.payements_en_cours_table.setFont(font13)
        self.payements_en_cours_table.setStyleSheet(u".QTableWidget{\n"
"background: rgb(40, 40, 40);\n"
"color:rgb(188,255,54);\n"
"}")
        self.payements_en_cours_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.payements_en_cours_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.payements_en_cours_table.horizontalHeader().setMinimumSectionSize(250)
        self.payements_en_cours_table.horizontalHeader().setDefaultSectionSize(250)
        self.payements_en_cours_table.verticalHeader().setMinimumSectionSize(80)
        self.payements_en_cours_table.verticalHeader().setDefaultSectionSize(80)

        self.verticalLayout_12.addWidget(self.payements_en_cours_table)


        self.verticalLayout_20.addWidget(self.payements_en_cours_frame_content)

        self.payements_en_cours_frame_actions = QWidget(self.payements_en_cours_page)
        self.payements_en_cours_frame_actions.setObjectName(u"payements_en_cours_frame_actions")
        self.payements_en_cours_frame_actions.setMinimumSize(QSize(0, 80))
        self.payements_en_cours_frame_actions.setMaximumSize(QSize(16777215, 80))
        self.payements_en_cours_frame_actions.setSizeIncrement(QSize(0, 80))
        self.payements_en_cours_frame_actions.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.payements_en_cours_frame_actions)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.actions_list_2 = QWidget(self.payements_en_cours_frame_actions)
        self.actions_list_2.setObjectName(u"actions_list_2")
        self.actions_list_2.setMinimumSize(QSize(0, 80))
        self.actions_list_2.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_8 = QHBoxLayout(self.actions_list_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_12 = QWidget(self.actions_list_2)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(100, 0))
        self.widget_12.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_15 = QVBoxLayout(self.widget_12)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.demander_avance_btn = QPushButton(self.widget_12)
        self.demander_avance_btn.setObjectName(u"demander_avance_btn")
        self.demander_avance_btn.setMinimumSize(QSize(100, 50))
        self.demander_avance_btn.setFont(font11)
        self.demander_avance_btn.setStyleSheet(u".QPushButton{\n"
"background: rgb(100, 180, 250);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton::hover{\n"
"background:  rgb(90, 200, 250);\n"
"}\n"
"\n"
".QPushButton::pressed{\n"
"background: rgb(50, 220, 250);\n"
"}")

        self.verticalLayout_15.addWidget(self.demander_avance_btn)


        self.horizontalLayout_8.addWidget(self.widget_12)


        self.verticalLayout_13.addWidget(self.actions_list_2)


        self.verticalLayout_20.addWidget(self.payements_en_cours_frame_actions)

        self.stackedWidget.addWidget(self.payements_en_cours_page)
        self.payements_a_faire_page = QWidget()
        self.payements_a_faire_page.setObjectName(u"payements_a_faire_page")
        self.payements_a_faire_page.setMinimumSize(QSize(0, 40))
        self.payements_a_faire_page.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.payements_a_faire_page)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.payements_a_faire_frame_header = QWidget(self.payements_a_faire_page)
        self.payements_a_faire_frame_header.setObjectName(u"payements_a_faire_frame_header")
        self.payements_a_faire_frame_header.setMinimumSize(QSize(0, 70))
        self.payements_a_faire_frame_header.setMaximumSize(QSize(16777215, 70))
        self.payements_a_faire_frame_header.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.payements_a_faire_frame_header)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_11 = QWidget(self.payements_a_faire_frame_header)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(250, 40))
        self.widget_11.setMaximumSize(QSize(250, 40))
        self.widget_11.setStyleSheet(u"QWidget{\n"
"color:rgb(255, 234, 8);\n"
"}")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_26.setSpacing(2)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.total_results_text_payements_a_faire = QLabel(self.widget_11)
        self.total_results_text_payements_a_faire.setObjectName(u"total_results_text_payements_a_faire")
        self.total_results_text_payements_a_faire.setMinimumSize(QSize(40, 40))
        self.total_results_text_payements_a_faire.setMaximumSize(QSize(40, 40))
        self.total_results_text_payements_a_faire.setSizeIncrement(QSize(2, 2))
        self.total_results_text_payements_a_faire.setBaseSize(QSize(2, 2))
        self.total_results_text_payements_a_faire.setFont(font14)
        self.total_results_text_payements_a_faire.setStyleSheet(u".QLabel{\n"
"color:yellow;\n"
"font-size:15px;\n"
"}")
        self.total_results_text_payements_a_faire.setPixmap(QPixmap(u"../assets/cash-payment.png"))
        self.total_results_text_payements_a_faire.setScaledContents(True)
        self.total_results_text_payements_a_faire.setAlignment(Qt.AlignCenter)
        self.total_results_text_payements_a_faire.setIndent(1)

        self.horizontalLayout_26.addWidget(self.total_results_text_payements_a_faire)

        self.label_6 = QLabel(self.widget_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font7)

        self.horizontalLayout_26.addWidget(self.label_6)


        self.horizontalLayout_12.addWidget(self.widget_11)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)

        self.widget_15 = QWidget(self.payements_a_faire_frame_header)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.payements_a_faire_search_field = QLineEdit(self.widget_15)
        self.payements_a_faire_search_field.setObjectName(u"payements_a_faire_search_field")
        self.payements_a_faire_search_field.setMinimumSize(QSize(40, 40))
        self.payements_a_faire_search_field.setMaximumSize(QSize(300, 16777215))
        self.payements_a_faire_search_field.setFont(font8)
        self.payements_a_faire_search_field.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.payements_a_faire_search_field)

        self.payements_a_faire_search_btn = QPushButton(self.widget_15)
        self.payements_a_faire_search_btn.setObjectName(u"payements_a_faire_search_btn")
        self.payements_a_faire_search_btn.setMinimumSize(QSize(0, 40))
        self.payements_a_faire_search_btn.setFont(font9)
        self.payements_a_faire_search_btn.setStyleSheet(u".QPushButton{\n"
"background: rgb(200, 150, 200);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background: rgb(220, 120, 220);\n"
"}\n"
"\n"
".QPushButton:clicked{\n"
"background: rgb(250, 100, 250);\n"
"}")

        self.horizontalLayout_13.addWidget(self.payements_a_faire_search_btn)


        self.horizontalLayout_12.addWidget(self.widget_15)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)


        self.verticalLayout_27.addWidget(self.payements_a_faire_frame_header)

        self.payements_a_faire_frame_content = QWidget(self.payements_a_faire_page)
        self.payements_a_faire_frame_content.setObjectName(u"payements_a_faire_frame_content")
        self.payements_a_faire_frame_content.setMinimumSize(QSize(0, 0))
        self.payements_a_faire_frame_content.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.verticalLayout_21 = QVBoxLayout(self.payements_a_faire_frame_content)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.payements_a_faire_table = QTableWidget(self.payements_a_faire_frame_content)
        if (self.payements_a_faire_table.columnCount() < 10):
            self.payements_a_faire_table.setColumnCount(10)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font5);
        self.payements_a_faire_table.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font5);
        self.payements_a_faire_table.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font5);
        self.payements_a_faire_table.setHorizontalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font5);
        self.payements_a_faire_table.setHorizontalHeaderItem(3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font5);
        self.payements_a_faire_table.setHorizontalHeaderItem(4, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font5);
        self.payements_a_faire_table.setHorizontalHeaderItem(5, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font5);
        self.payements_a_faire_table.setHorizontalHeaderItem(6, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font5);
        self.payements_a_faire_table.setHorizontalHeaderItem(7, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font5);
        self.payements_a_faire_table.setHorizontalHeaderItem(8, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font5);
        self.payements_a_faire_table.setHorizontalHeaderItem(9, __qtablewidgetitem41)
        self.payements_a_faire_table.setObjectName(u"payements_a_faire_table")
        self.payements_a_faire_table.setFont(font13)
        self.payements_a_faire_table.setStyleSheet(u".QTableWidget{\n"
"background: rgb(40, 40, 40);\n"
"color:rgb(188,255,54);\n"
"}")
        self.payements_a_faire_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.payements_a_faire_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.payements_a_faire_table.horizontalHeader().setMinimumSectionSize(250)
        self.payements_a_faire_table.horizontalHeader().setDefaultSectionSize(250)
        self.payements_a_faire_table.verticalHeader().setMinimumSectionSize(80)
        self.payements_a_faire_table.verticalHeader().setDefaultSectionSize(80)

        self.verticalLayout_21.addWidget(self.payements_a_faire_table)


        self.verticalLayout_27.addWidget(self.payements_a_faire_frame_content)

        self.payements_a_faire_frame_actions = QWidget(self.payements_a_faire_page)
        self.payements_a_faire_frame_actions.setObjectName(u"payements_a_faire_frame_actions")
        self.payements_a_faire_frame_actions.setMinimumSize(QSize(0, 80))
        self.payements_a_faire_frame_actions.setMaximumSize(QSize(16777215, 80))
        self.payements_a_faire_frame_actions.setSizeIncrement(QSize(0, 100))
        self.payements_a_faire_frame_actions.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.verticalLayout_23 = QVBoxLayout(self.payements_a_faire_frame_actions)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.actions_list_4 = QWidget(self.payements_a_faire_frame_actions)
        self.actions_list_4.setObjectName(u"actions_list_4")
        self.actions_list_4.setMinimumSize(QSize(0, 80))
        self.actions_list_4.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_14 = QHBoxLayout(self.actions_list_4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_16 = QWidget(self.actions_list_4)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(100, 0))
        self.widget_16.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_24 = QVBoxLayout(self.widget_16)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_14.addWidget(self.widget_16)

        self.widget_18 = QWidget(self.actions_list_4)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(100, 0))
        self.widget_18.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_25 = QVBoxLayout(self.widget_18)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.payer_payement_a_faire_btn = QPushButton(self.widget_18)
        self.payer_payement_a_faire_btn.setObjectName(u"payer_payement_a_faire_btn")
        self.payer_payement_a_faire_btn.setMinimumSize(QSize(100, 50))
        self.payer_payement_a_faire_btn.setFont(font11)
        self.payer_payement_a_faire_btn.setStyleSheet(u".QPushButton{\n"
"background: rgb(100, 180, 250);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton::hover{\n"
"background:  rgb(90, 200, 250);\n"
"}\n"
"\n"
".QPushButton::pressed{\n"
"background: rgb(50, 220, 250);\n"
"}")

        self.verticalLayout_25.addWidget(self.payer_payement_a_faire_btn)


        self.horizontalLayout_14.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.actions_list_4)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(100, 0))
        self.widget_19.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_26 = QVBoxLayout(self.widget_19)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_14.addWidget(self.widget_19)


        self.verticalLayout_23.addWidget(self.actions_list_4)


        self.verticalLayout_27.addWidget(self.payements_a_faire_frame_actions)

        self.stackedWidget.addWidget(self.payements_a_faire_page)
        self.payements_reussis_page = QWidget()
        self.payements_reussis_page.setObjectName(u"payements_reussis_page")
        self.payements_reussis_page.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.verticalLayout_33 = QVBoxLayout(self.payements_reussis_page)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.payements_reussis_frame_header = QWidget(self.payements_reussis_page)
        self.payements_reussis_frame_header.setObjectName(u"payements_reussis_frame_header")
        self.payements_reussis_frame_header.setMinimumSize(QSize(0, 70))
        self.payements_reussis_frame_header.setMaximumSize(QSize(16777215, 70))
        self.payements_reussis_frame_header.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.horizontalLayout_15 = QHBoxLayout(self.payements_reussis_frame_header)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.widget = QWidget(self.payements_reussis_frame_header)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 40))
        self.widget.setMaximumSize(QSize(250, 40))
        self.widget.setStyleSheet(u"QWidget{\n"
"color:rgb(255, 234, 8);\n"
"}")
        self.horizontalLayout_18 = QHBoxLayout(self.widget)
        self.horizontalLayout_18.setSpacing(2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.total_results_text_payements_reussis = QLabel(self.widget)
        self.total_results_text_payements_reussis.setObjectName(u"total_results_text_payements_reussis")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.total_results_text_payements_reussis.sizePolicy().hasHeightForWidth())
        self.total_results_text_payements_reussis.setSizePolicy(sizePolicy2)
        self.total_results_text_payements_reussis.setMinimumSize(QSize(40, 40))
        self.total_results_text_payements_reussis.setMaximumSize(QSize(40, 40))
        self.total_results_text_payements_reussis.setSizeIncrement(QSize(2, 2))
        self.total_results_text_payements_reussis.setBaseSize(QSize(2, 2))
        self.total_results_text_payements_reussis.setFont(font14)
        self.total_results_text_payements_reussis.setStyleSheet(u".QLabel{\n"
"color:yellow;\n"
"font-size:15px;\n"
"}")
        self.total_results_text_payements_reussis.setPixmap(QPixmap(u"../assets/business.png"))
        self.total_results_text_payements_reussis.setScaledContents(True)
        self.total_results_text_payements_reussis.setAlignment(Qt.AlignCenter)
        self.total_results_text_payements_reussis.setIndent(1)

        self.horizontalLayout_18.addWidget(self.total_results_text_payements_reussis)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(16777215, 40))
        font16 = QFont()
        font16.setFamily(u"Lucida Sans")
        font16.setPointSize(10)
        font16.setBold(True)
        font16.setItalic(False)
        font16.setWeight(75)
        self.label.setFont(font16)

        self.horizontalLayout_18.addWidget(self.label)


        self.horizontalLayout_15.addWidget(self.widget)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_11)

        self.widget_20 = QWidget(self.payements_reussis_frame_header)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.payements_reussis_search_field = QLineEdit(self.widget_20)
        self.payements_reussis_search_field.setObjectName(u"payements_reussis_search_field")
        self.payements_reussis_search_field.setMinimumSize(QSize(40, 40))
        self.payements_reussis_search_field.setMaximumSize(QSize(300, 16777215))
        self.payements_reussis_search_field.setFont(font8)
        self.payements_reussis_search_field.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.payements_reussis_search_field)

        self.payements_reussis_search_btn = QPushButton(self.widget_20)
        self.payements_reussis_search_btn.setObjectName(u"payements_reussis_search_btn")
        self.payements_reussis_search_btn.setMinimumSize(QSize(0, 40))
        self.payements_reussis_search_btn.setFont(font9)
        self.payements_reussis_search_btn.setStyleSheet(u".QPushButton{\n"
"background: rgb(200, 150, 200);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background: rgb(220, 120, 220);\n"
"}\n"
"\n"
".QPushButton:clicked{\n"
"background: rgb(250, 100, 250);\n"
"}")

        self.horizontalLayout_16.addWidget(self.payements_reussis_search_btn)


        self.horizontalLayout_15.addWidget(self.widget_20)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_12)


        self.verticalLayout_33.addWidget(self.payements_reussis_frame_header)

        self.payements_reussis_frame_content = QWidget(self.payements_reussis_page)
        self.payements_reussis_frame_content.setObjectName(u"payements_reussis_frame_content")
        self.payements_reussis_frame_content.setMinimumSize(QSize(0, 0))
        self.payements_reussis_frame_content.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.verticalLayout_28 = QVBoxLayout(self.payements_reussis_frame_content)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.payements_reussis_table = QTableWidget(self.payements_reussis_frame_content)
        if (self.payements_reussis_table.columnCount() < 5):
            self.payements_reussis_table.setColumnCount(5)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font5);
        self.payements_reussis_table.setHorizontalHeaderItem(0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFont(font5);
        self.payements_reussis_table.setHorizontalHeaderItem(1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setFont(font5);
        self.payements_reussis_table.setHorizontalHeaderItem(2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setFont(font5);
        self.payements_reussis_table.setHorizontalHeaderItem(3, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setFont(font5);
        self.payements_reussis_table.setHorizontalHeaderItem(4, __qtablewidgetitem46)
        self.payements_reussis_table.setObjectName(u"payements_reussis_table")
        self.payements_reussis_table.setFont(font13)
        self.payements_reussis_table.setStyleSheet(u"")
        self.payements_reussis_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.payements_reussis_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.payements_reussis_table.horizontalHeader().setMinimumSectionSize(250)
        self.payements_reussis_table.horizontalHeader().setDefaultSectionSize(250)
        self.payements_reussis_table.verticalHeader().setMinimumSectionSize(80)
        self.payements_reussis_table.verticalHeader().setDefaultSectionSize(80)

        self.verticalLayout_28.addWidget(self.payements_reussis_table)


        self.verticalLayout_33.addWidget(self.payements_reussis_frame_content)

        self.payements_reussis_frame_actions = QWidget(self.payements_reussis_page)
        self.payements_reussis_frame_actions.setObjectName(u"payements_reussis_frame_actions")
        self.payements_reussis_frame_actions.setMinimumSize(QSize(0, 80))
        self.payements_reussis_frame_actions.setMaximumSize(QSize(16777215, 80))
        self.payements_reussis_frame_actions.setSizeIncrement(QSize(0, 100))
        self.payements_reussis_frame_actions.setStyleSheet(u".QWidget{\n"
"background: rgb(60, 60, 60);\n"
"}")
        self.verticalLayout_29 = QVBoxLayout(self.payements_reussis_frame_actions)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.actions_list_5 = QWidget(self.payements_reussis_frame_actions)
        self.actions_list_5.setObjectName(u"actions_list_5")
        self.actions_list_5.setMinimumSize(QSize(0, 80))
        self.actions_list_5.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_17 = QHBoxLayout(self.actions_list_5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.widget_21 = QWidget(self.actions_list_5)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(100, 0))
        self.widget_21.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_30 = QVBoxLayout(self.widget_21)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_17.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.actions_list_5)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMinimumSize(QSize(100, 0))
        self.widget_22.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_31 = QVBoxLayout(self.widget_22)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.export_payements_reussis_btn = QPushButton(self.widget_22)
        self.export_payements_reussis_btn.setObjectName(u"export_payements_reussis_btn")
        self.export_payements_reussis_btn.setMinimumSize(QSize(100, 50))
        self.export_payements_reussis_btn.setFont(font11)
        self.export_payements_reussis_btn.setStyleSheet(u".QPushButton{\n"
"background: rgb(100, 180, 250);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton::hover{\n"
"background:  rgb(90, 200, 250);\n"
"}\n"
"\n"
".QPushButton::pressed{\n"
"background: rgb(50, 220, 250);\n"
"}")

        self.verticalLayout_31.addWidget(self.export_payements_reussis_btn)


        self.horizontalLayout_17.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.actions_list_5)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMinimumSize(QSize(100, 0))
        self.widget_23.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_32 = QVBoxLayout(self.widget_23)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_17.addWidget(self.widget_23)


        self.verticalLayout_29.addWidget(self.actions_list_5)


        self.verticalLayout_33.addWidget(self.payements_reussis_frame_actions)

        self.stackedWidget.addWidget(self.payements_reussis_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.Content_Frame)


        self.verticalLayout.addWidget(self.Container)


        self.verticalLayout_2.addWidget(self.Body)

        v.setCentralWidget(self.centralwidget)

        self.retranslateUi(v)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(v)
    # setupUi

    def retranslateUi(self, v):
        v.setWindowTitle(QCoreApplication.translate("v", u"Gestion Des Employees", None))
        self.today_label.setText(QCoreApplication.translate("v", u"<html><head/><body><p>FEWFEW</p></body></html>", None))
        self.enterprise_name.setText(QCoreApplication.translate("v", u"<html><head/><body><p/></body></html>", None))
        self.organisation_name.setText(QCoreApplication.translate("v", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffff00;\">TextLabel</span></p></body></html>", None))
        self.liste_employee_btn.setText(QCoreApplication.translate("v", u"LISTE EMPLOYEES", None))
        self.liste_presence_btn.setText(QCoreApplication.translate("v", u"LISTE PRESENCE", None))
        self.payements_en_cours_btn.setText(QCoreApplication.translate("v", u"PAYEMENTS EN COURS", None))
        self.payements_a_faire_btn.setText(QCoreApplication.translate("v", u"PAYEMENTS A FAIRE", None))
        self.payements_reussis_btn.setText(QCoreApplication.translate("v", u"PAYEMENTS REUSSIS", None))
        self.credits_btn.setText(QCoreApplication.translate("v", u"CREDITS ", None))
        self.sync_date_btn.setText(QCoreApplication.translate("v", u"SYNC LA PRESENCE", None))
        self.contact_btn.setText(QCoreApplication.translate("v", u"ABOUT DEVELOPPER", None))
        self.total_results_text_employee.setText("")
        self.label_2.setText(QCoreApplication.translate("v", u"LISTE EMPLOYEES", None))
        self.liste_employee_search_btn.setText(QCoreApplication.translate("v", u"RECHERCHER", None))
        ___qtablewidgetitem = self.liste_employee_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("v", u"NOM", None));
        ___qtablewidgetitem1 = self.liste_employee_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("v", u"PRENOM", None));
        ___qtablewidgetitem2 = self.liste_employee_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("v", u"NUM_TELEPHONE", None));
        ___qtablewidgetitem3 = self.liste_employee_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("v", u"DATE NAISSANCE", None));
        ___qtablewidgetitem4 = self.liste_employee_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("v", u"ADDRESSE", None));
        ___qtablewidgetitem5 = self.liste_employee_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("v", u"NUMERO CARTE NAT", None));
        ___qtablewidgetitem6 = self.liste_employee_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("v", u"DATE DEBUT TRAVAIL", None));
        ___qtablewidgetitem7 = self.liste_employee_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("v", u"DATE FIN TRAVAIL", None));
        ___qtablewidgetitem8 = self.liste_employee_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("v", u"SALAIRE (DA)", None));
        ___qtablewidgetitem9 = self.liste_employee_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("v", u"OBSERVATION", None));
        self.add_employee_btn.setText(QCoreApplication.translate("v", u"AJOUTER UN EMPLOYEE", None))
        self.update_employee_btn.setText(QCoreApplication.translate("v", u"MAJ UN EMPLOYEE", None))
        self.delete_employee_btn.setText(QCoreApplication.translate("v", u"SUPPRIMER UN EMPLOYEE", None))
        self.total_results_text_presence.setText("")
        self.label_3.setText(QCoreApplication.translate("v", u"LISTE PRESENCE", None))
        self.liste_presence_search_btn.setText(QCoreApplication.translate("v", u"RECHERCHER", None))
        ___qtablewidgetitem10 = self.liste_presence_table.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("v", u"NUMERO CARTE NAT", None));
        ___qtablewidgetitem11 = self.liste_presence_table.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("v", u"NOM", None));
        ___qtablewidgetitem12 = self.liste_presence_table.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("v", u"PRENOM", None));
        ___qtablewidgetitem13 = self.liste_presence_table.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("v", u"PRESENCE VALIDE", None));
        ___qtablewidgetitem14 = self.liste_presence_table.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("v", u"PRESENT ", None));
        ___qtablewidgetitem15 = self.liste_presence_table.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("v", u"TRAVAIL TOTAL (Journee)", None));
        self.faire_presence_btn.setText(QCoreApplication.translate("v", u"FAIRE LA PRESENCE", None))
        self.total_results_credit.setText("")
        self.label_4.setText(QCoreApplication.translate("v", u"CREDITS", None))
        self.credit_recherche_btn.setText(QCoreApplication.translate("v", u"RECHERCHER", None))
        ___qtablewidgetitem16 = self.credit_table.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("v", u"NUMERO CARTE NAT", None));
        ___qtablewidgetitem17 = self.credit_table.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("v", u"NOM", None));
        ___qtablewidgetitem18 = self.credit_table.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("v", u"PRENOM", None));
        ___qtablewidgetitem19 = self.credit_table.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("v", u"CREDIT (DA)", None));
        ___qtablewidgetitem20 = self.credit_table.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("v", u"EN_JOURS_DE_TRAVAIL", None));
        ___qtablewidgetitem21 = self.credit_table.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("v", u"DATE_CREDITS", None));
        self.payer_credit_btn.setText(QCoreApplication.translate("v", u"PAYER", None))
        self.total_results_text_payements_en_cours.setText("")
        self.label_5.setText(QCoreApplication.translate("v", u"PAYEMENTS EN COURS", None))
        self.payements_en_cours_search_btn.setText(QCoreApplication.translate("v", u"RECHERCHER", None))
        ___qtablewidgetitem22 = self.payements_en_cours_table.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("v", u"NUMERO CARTE NAT", None));
        ___qtablewidgetitem23 = self.payements_en_cours_table.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("v", u"NOM", None));
        ___qtablewidgetitem24 = self.payements_en_cours_table.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("v", u"PRENOM", None));
        ___qtablewidgetitem25 = self.payements_en_cours_table.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("v", u"DATE PROCHAIN PAYEMENT", None));
        ___qtablewidgetitem26 = self.payements_en_cours_table.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("v", u"ABSENCE (JOUR)", None));
        ___qtablewidgetitem27 = self.payements_en_cours_table.horizontalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("v", u"TOTAL JOURS TRAVAIL", None));
        ___qtablewidgetitem28 = self.payements_en_cours_table.horizontalHeaderItem(6)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("v", u"SALAIRE (DA)", None));
        ___qtablewidgetitem29 = self.payements_en_cours_table.horizontalHeaderItem(7)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("v", u"AVANCE (DA)", None));
        ___qtablewidgetitem30 = self.payements_en_cours_table.horizontalHeaderItem(8)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("v", u"TOTAL A PAYER (DA)", None));
        ___qtablewidgetitem31 = self.payements_en_cours_table.horizontalHeaderItem(9)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("v", u"PRESENCE AUJOURDHUI VALIDE ?", None));
        self.demander_avance_btn.setText(QCoreApplication.translate("v", u"DEMANDER AVANCE", None))
        self.total_results_text_payements_a_faire.setText("")
        self.label_6.setText(QCoreApplication.translate("v", u"PAYEEMNTS A FAIRE", None))
        self.payements_a_faire_search_btn.setText(QCoreApplication.translate("v", u"RECHERCHER", None))
        ___qtablewidgetitem32 = self.payements_a_faire_table.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("v", u"NUMERO CARTE NAT", None));
        ___qtablewidgetitem33 = self.payements_a_faire_table.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("v", u"NOM", None));
        ___qtablewidgetitem34 = self.payements_a_faire_table.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("v", u"PRENOME", None));
        ___qtablewidgetitem35 = self.payements_a_faire_table.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("v", u"DATE DU PAYEMENT", None));
        ___qtablewidgetitem36 = self.payements_a_faire_table.horizontalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("v", u"RETARD DU PAYEMENT (JOUR)", None));
        ___qtablewidgetitem37 = self.payements_a_faire_table.horizontalHeaderItem(5)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("v", u"SALAIRE (DA)", None));
        ___qtablewidgetitem38 = self.payements_a_faire_table.horizontalHeaderItem(6)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("v", u"ABSENCE (JOUR)", None));
        ___qtablewidgetitem39 = self.payements_a_faire_table.horizontalHeaderItem(7)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("v", u"TOTAL JOURS TRAVAIL", None));
        ___qtablewidgetitem40 = self.payements_a_faire_table.horizontalHeaderItem(8)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("v", u"AVANCE (DA)", None));
        ___qtablewidgetitem41 = self.payements_a_faire_table.horizontalHeaderItem(9)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("v", u"PAYEMENT A PAYER (DA)", None));
        self.payer_payement_a_faire_btn.setText(QCoreApplication.translate("v", u"PAYER", None))
        self.total_results_text_payements_reussis.setText("")
        self.label.setText(QCoreApplication.translate("v", u"PAYEMENTS REUSSIS", None))
        self.payements_reussis_search_btn.setText(QCoreApplication.translate("v", u"RECHERCHER", None))
        ___qtablewidgetitem42 = self.payements_reussis_table.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("v", u"NUMERO CARTE NAT", None));
        ___qtablewidgetitem43 = self.payements_reussis_table.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("v", u"NOM", None));
        ___qtablewidgetitem44 = self.payements_reussis_table.horizontalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("v", u"PRENOM", None));
        ___qtablewidgetitem45 = self.payements_reussis_table.horizontalHeaderItem(3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("v", u"DATE DU PAYEMENT", None));
        ___qtablewidgetitem46 = self.payements_reussis_table.horizontalHeaderItem(4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("v", u"PAYEMENT (DA)", None));
        self.export_payements_reussis_btn.setText(QCoreApplication.translate("v", u"EXPORTER", None))
    # retranslateUi

