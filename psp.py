# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'psp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CompanyService(object):
    def setupUi(self, CompanyService):
        CompanyService.setObjectName("CompanyService")
        CompanyService.resize(400, 300)
        CompanyService.setMaximumSize(QtCore.QSize(400, 300))
        self.pushButton = QtWidgets.QPushButton(CompanyService)
        self.pushButton.setGeometry(QtCore.QRect(0, 80, 121, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(CompanyService)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 100, 151, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit = QtWidgets.QTextEdit(CompanyService)
        self.textEdit.setGeometry(QtCore.QRect(70, 0, 181, 31))
        self.textEdit.setObjectName("textEdit")
        self.timeEdit = QtWidgets.QTimeEdit(CompanyService)
        self.timeEdit.setGeometry(QtCore.QRect(0, 20, 71, 22))
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(17, 0, 0)))
        self.timeEdit.setMaximumDate(QtCore.QDate(2020, 1, 1))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(CompanyService)
        self.dateEdit.setGeometry(QtCore.QRect(0, 0, 71, 22))
        self.dateEdit.setStyleSheet("color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 6, 11), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.tabWidget = QtWidgets.QTabWidget(CompanyService)
        self.tabWidget.setGeometry(QtCore.QRect(250, 0, 150, 300))
        self.tabWidget.setMaximumSize(QtCore.QSize(150, 300))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 90, 131, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(0, 150, 151, 131))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(16, 69, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 120, 141, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_3.setGeometry(QtCore.QRect(13, 0, 131, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listView = QtWidgets.QListView(self.tab_2)
        self.listView.setGeometry(QtCore.QRect(0, 30, 151, 141))
        self.listView.setObjectName("listView")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 0, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.lineEdit = QtWidgets.QLineEdit(CompanyService)
        self.lineEdit.setGeometry(QtCore.QRect(10, 120, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.frame = QtWidgets.QFrame(CompanyService)
        self.frame.setGeometry(QtCore.QRect(19, 149, 221, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit_4 = QtWidgets.QTextEdit(CompanyService)
        self.textEdit_4.setGeometry(QtCore.QRect(70, 30, 181, 41))
        self.textEdit_4.setObjectName("textEdit_4")

        self.retranslateUi(CompanyService)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CompanyService)

    def retranslateUi(self, CompanyService):
        _translate = QtCore.QCoreApplication.translate
        CompanyService.setWindowTitle(_translate("CompanyService", "Form"))
        self.pushButton.setText(_translate("CompanyService", "Company registration"))
        self.pushButton_4.setText(_translate("CompanyService", "Withdrawal from cooperation"))
        self.textEdit.setHtml(_translate("CompanyService", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#0000ff;\">In The name of good</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"><br /></span></p></body></html>"))
        self.pushButton_2.setText(_translate("CompanyService", "PushButton"))
        self.label.setText(_translate("CompanyService", "None"))
        self.textEdit_2.setHtml(_translate("CompanyService", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic; text-decoration: underline;\">Corona News</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-style:italic; text-decoration: underline;\"><br /></p></body></html>"))
        self.textEdit_3.setHtml(_translate("CompanyService", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Weather </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("CompanyService", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("CompanyService", "Tab 2"))
        self.textEdit_4.setHtml(_translate("CompanyService", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline;\">ServiceProvider</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CompanyService = QtWidgets.QWidget()
    ui = Ui_CompanyService()
    ui.setupUi(CompanyService)
    CompanyService.show()
    sys.exit(app.exec_())
