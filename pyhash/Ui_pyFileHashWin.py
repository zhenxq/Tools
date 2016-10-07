# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\gitPtoject\pyhash\pyFileHashWin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(850, 420)
        MainWindow.setMinimumSize(QtCore.QSize(850, 420))
        MainWindow.setMaximumSize(QtCore.QSize(850, 420))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.textBrowser = QtGui.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 9, 850, 280))
        self.textBrowser.setMinimumSize(QtCore.QSize(850, 280))
        self.textBrowser.setMaximumSize(QtCore.QSize(850, 280))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton_openfile = QtGui.QPushButton(self.centralWidget)
        self.pushButton_openfile.setGeometry(QtCore.QRect(760, 330, 75, 23))
        self.pushButton_openfile.setObjectName(_fromUtf8("pushButton_openfile"))
        self.pushButton_clear = QtGui.QPushButton(self.centralWidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(570, 330, 75, 23))
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 290, 161, 91))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox_md5 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_md5.setChecked(True)
        self.checkBox_md5.setObjectName(_fromUtf8("checkBox_md5"))
        self.verticalLayout.addWidget(self.checkBox_md5)
        self.checkBox_sha1 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_sha1.setChecked(True)
        self.checkBox_sha1.setObjectName(_fromUtf8("checkBox_sha1"))
        self.verticalLayout.addWidget(self.checkBox_sha1)
        self.checkBox_sha224 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_sha224.setChecked(True)
        self.checkBox_sha224.setObjectName(_fromUtf8("checkBox_sha224"))
        self.verticalLayout.addWidget(self.checkBox_sha224)
        self.checkBox_sha256 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_sha256.setChecked(True)
        self.checkBox_sha256.setObjectName(_fromUtf8("checkBox_sha256"))
        self.verticalLayout.addWidget(self.checkBox_sha256)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 290, 160, 91))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.checkBox_atime = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_atime.setEnabled(True)
        self.checkBox_atime.setChecked(True)
        self.checkBox_atime.setObjectName(_fromUtf8("checkBox_atime"))
        self.verticalLayout_2.addWidget(self.checkBox_atime)
        self.checkBox_mtime = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_mtime.setChecked(True)
        self.checkBox_mtime.setObjectName(_fromUtf8("checkBox_mtime"))
        self.verticalLayout_2.addWidget(self.checkBox_mtime)
        self.checkBox_ctime = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_ctime.setChecked(True)
        self.checkBox_ctime.setObjectName(_fromUtf8("checkBox_ctime"))
        self.verticalLayout_2.addWidget(self.checkBox_ctime)
        self.checkBox_size = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_size.setChecked(True)
        self.checkBox_size.setObjectName(_fromUtf8("checkBox_size"))
        self.verticalLayout_2.addWidget(self.checkBox_size)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(320, 290, 160, 91))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.checkBox_sha384 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_sha384.setChecked(True)
        self.checkBox_sha384.setObjectName(_fromUtf8("checkBox_sha384"))
        self.verticalLayout_3.addWidget(self.checkBox_sha384)
        self.checkBox_sha512 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_sha512.setChecked(True)
        self.checkBox_sha512.setObjectName(_fromUtf8("checkBox_sha512"))
        self.verticalLayout_3.addWidget(self.checkBox_sha512)
        self.checkBox_crc32 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_crc32.setChecked(True)
        self.checkBox_crc32.setObjectName(_fromUtf8("checkBox_crc32"))
        self.verticalLayout_3.addWidget(self.checkBox_crc32)
        self.checkBox_adler32 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_adler32.setChecked(True)
        self.checkBox_adler32.setObjectName(_fromUtf8("checkBox_adler32"))
        self.verticalLayout_3.addWidget(self.checkBox_adler32)
        self.pushButton_save = QtGui.QPushButton(self.centralWidget)
        self.pushButton_save.setGeometry(QtCore.QRect(670, 330, 75, 23))
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 850, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu = QtGui.QMenu(self.menuBar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menuBar)
        self.action_openfile = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/photo/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_openfile.setIcon(icon)
        self.action_openfile.setObjectName(_fromUtf8("action_openfile"))
        self.action_save = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/photo/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save.setIcon(icon1)
        self.action_save.setObjectName(_fromUtf8("action_save"))
        self.action_close = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/photo/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_close.setIcon(icon2)
        self.action_close.setObjectName(_fromUtf8("action_close"))
        self.menu.addAction(self.action_openfile)
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_close)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "文件校验和", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1：点击Open File</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2：选择文件</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3：自动显示文件信息</p></body></html>", None))
        self.pushButton_openfile.setText(_translate("MainWindow", "Open File", None))
        self.pushButton_clear.setText(_translate("MainWindow", "clear", None))
        self.checkBox_md5.setText(_translate("MainWindow", "md5", None))
        self.checkBox_sha1.setText(_translate("MainWindow", "sha1", None))
        self.checkBox_sha224.setText(_translate("MainWindow", "sha224", None))
        self.checkBox_sha256.setText(_translate("MainWindow", "sha256", None))
        self.checkBox_atime.setText(_translate("MainWindow", "atime", None))
        self.checkBox_mtime.setText(_translate("MainWindow", "mtime", None))
        self.checkBox_ctime.setText(_translate("MainWindow", "ctime", None))
        self.checkBox_size.setText(_translate("MainWindow", "size", None))
        self.checkBox_sha384.setText(_translate("MainWindow", "sha384", None))
        self.checkBox_sha512.setText(_translate("MainWindow", "sha512", None))
        self.checkBox_crc32.setText(_translate("MainWindow", "crc32", None))
        self.checkBox_adler32.setText(_translate("MainWindow", "adler32", None))
        self.pushButton_save.setText(_translate("MainWindow", "save", None))
        self.menu.setTitle(_translate("MainWindow", "菜单", None))
        self.action_openfile.setText(_translate("MainWindow", "打开文件", None))
        self.action_save.setText(_translate("MainWindow", "保存记录", None))
        self.action_close.setText(_translate("MainWindow", "关闭窗口", None))

import photoes_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

