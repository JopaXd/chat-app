from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QAction
import re
import socket
import threading
import json
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1091, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.mainPage = QtWidgets.QWidget()
        self.mainPage.setObjectName("mainPage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.mainPage)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.mainPageContainer = QtWidgets.QWidget(self.mainPage)
        self.mainPageContainer.setObjectName("mainPageContainer")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.mainPageContainer)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.mainPageTitle = QtWidgets.QLabel(self.mainPageContainer)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.mainPageTitle.setFont(font)
        self.mainPageTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.mainPageTitle.setObjectName("mainPageTitle")
        self.verticalLayout_8.addWidget(self.mainPageTitle)
        self.mainPageVerticalContainer = QtWidgets.QWidget(self.mainPageContainer)
        self.mainPageVerticalContainer.setObjectName("mainPageVerticalContainer")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.mainPageVerticalContainer)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.ipAddressContainer = QtWidgets.QHBoxLayout()
        self.ipAddressContainer.setObjectName("ipAddressContainer")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ipAddressContainer.addItem(spacerItem1)
        self.ipAddressLbl = QtWidgets.QLabel(self.mainPageVerticalContainer)
        self.ipAddressLbl.setObjectName("ipAddressLbl")
        self.ipAddressContainer.addWidget(self.ipAddressLbl)
        self.ipAddressField = QtWidgets.QLineEdit(self.mainPageVerticalContainer)
        self.ipAddressField.setObjectName("ipAddressField")
        self.ipAddressContainer.addWidget(self.ipAddressField)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ipAddressContainer.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.ipAddressContainer)
        self.usernameContainer = QtWidgets.QHBoxLayout()
        self.usernameContainer.setObjectName("usernameContainer")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.usernameContainer.addItem(spacerItem3)
        self.usernameLbl = QtWidgets.QLabel(self.mainPageVerticalContainer)
        self.usernameLbl.setObjectName("usernameLbl")
        self.usernameContainer.addWidget(self.usernameLbl)
        self.usernameField = QtWidgets.QLineEdit(self.mainPageVerticalContainer)
        self.usernameField.setObjectName("usernameField")
        self.usernameContainer.addWidget(self.usernameField)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.usernameContainer.addItem(spacerItem4)
        self.verticalLayout_9.addLayout(self.usernameContainer)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem5)
        self.connectBtnContainer = QtWidgets.QHBoxLayout()
        self.connectBtnContainer.setObjectName("connectBtnContainer")
        self.connectBtn = QtWidgets.QPushButton(self.mainPageVerticalContainer)
        self.connectBtn.setMaximumSize(QtCore.QSize(450, 16777215))
        self.connectBtn.setObjectName("connectBtn")
        self.connectBtnContainer.addWidget(self.connectBtn)
        self.verticalLayout_9.addLayout(self.connectBtnContainer)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem6)
        self.verticalLayout_8.addWidget(self.mainPageVerticalContainer)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 2)
        self.verticalLayout_6.addWidget(self.mainPageContainer)
        self.stackedWidget.addWidget(self.mainPage)
        self.chatPage = QtWidgets.QWidget()
        self.chatPage.setObjectName("chatPage")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.chatPage)
        self.hboxlayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(0)
        self.hboxlayout.setObjectName("hboxlayout")
        self.chatWidget = QtWidgets.QWidget(self.chatPage)
        self.chatWidget.setStyleSheet("background-color:white;")
        self.chatWidget.setObjectName("chatWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.chatWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chatVerticalContainer = QtWidgets.QVBoxLayout()
        self.chatVerticalContainer.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.chatVerticalContainer.setSpacing(0)
        self.chatVerticalContainer.setObjectName("chatVerticalContainer")
        self.messagesScrollArea = QtWidgets.QScrollArea(self.chatWidget)
        self.messagesScrollArea.setStyleSheet("background:white;\n"
"border-color:white;\n"
"border:solid;")
        self.messagesScrollArea.setWidgetResizable(True)
        self.messagesScrollArea.setObjectName("messagesScrollArea")
        self.messagesScrollAreaContent = QtWidgets.QWidget()
        self.messagesScrollAreaContent.setGeometry(QtCore.QRect(0, 0, 871, 509))
        self.messagesScrollAreaContent.setObjectName("messagesScrollAreaContent")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.messagesScrollAreaContent)
        self.verticalLayout.setObjectName("verticalLayout")
        self.messagesScrollArea.setWidget(self.messagesScrollAreaContent)
        self.chatVerticalContainer.addWidget(self.messagesScrollArea)
        self.chatFieldContainer = QtWidgets.QHBoxLayout()
        self.chatFieldContainer.setSpacing(0)
        self.chatFieldContainer.setObjectName("chatFieldContainer")
        self.messageTextEdit = QtWidgets.QTextEdit(self.chatWidget)
        self.messageTextEdit.setMaximumSize(QtCore.QSize(16777215, 75))
        self.messageTextEdit.setStyleSheet("background-color:#eeeeee;\n"
"border: solid;\n"
"border-color: #eeeeee;\n"
"border-radius:5px;\n"
"border-width:3px;\n"
"margin-bottom:10px;\n"
"margin-right:20px;\n"
"margin-left:20px;\n"
"margin-top:20px;")
        self.messageTextEdit.setObjectName("messageTextEdit")
        self.chatFieldContainer.addWidget(self.messageTextEdit)
        self.sendBtn = QtWidgets.QPushButton(self.chatWidget)
        self.sendBtn.setMinimumSize(QtCore.QSize(70, 20))
        self.sendBtn.setMaximumSize(QtCore.QSize(16000000, 55))
        self.sendBtn.setStyleSheet("border:none;\n"
"background:#eeeeee;\n"
"margin-top:9px;")
        self.sendBtn.setObjectName("sendBtn")
        self.chatFieldContainer.addWidget(self.sendBtn)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.chatFieldContainer.addItem(spacerItem7)
        self.chatVerticalContainer.addLayout(self.chatFieldContainer)
        self.chatVerticalContainer.setStretch(0, 9)
        self.chatVerticalContainer.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.chatVerticalContainer)
        self.hboxlayout.addWidget(self.chatWidget)
        self.membersWidget = QtWidgets.QWidget(self.chatPage)
        self.membersWidget.setStyleSheet("background-color:#00A5FF;")
        self.membersWidget.setObjectName("membersWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.membersWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.membersContainer = QtWidgets.QVBoxLayout()
        self.membersContainer.setObjectName("membersContainer")
        self.membersLbl = QtWidgets.QLabel(self.membersWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.membersLbl.setFont(font)
        self.membersLbl.setStyleSheet("color:white;")
        self.membersLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.membersLbl.setObjectName("membersLbl")
        self.membersContainer.addWidget(self.membersLbl)
        self.membersListWidget = QtWidgets.QListWidget(self.membersWidget)
        self.membersListWidget.setStyleSheet("border-color:#00A5FF;\n"
"border:solid;\n"
"color:white;")
        self.membersListWidget.setObjectName("membersListWidget")
        self.membersContainer.addWidget(self.membersListWidget)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.membersContainer.addItem(spacerItem8)
        self.disconnectBtn = QtWidgets.QPushButton(self.membersWidget)
        self.disconnectBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.disconnectBtn.setStyleSheet("border:none;\n"
"color:white;\n"
"background:#dd0000;")
        self.disconnectBtn.setObjectName("disconnectBtn")
        self.membersContainer.addWidget(self.disconnectBtn)
        self.verticalLayout_5.addLayout(self.membersContainer)
        self.hboxlayout.addWidget(self.membersWidget)
        self.hboxlayout.setStretch(0, 4)
        self.hboxlayout.setStretch(1, 1)
        self.stackedWidget.addWidget(self.chatPage)
        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat App"))
        self.mainPageTitle.setText(_translate("MainWindow", "Chat App"))
        self.ipAddressLbl.setText(_translate("MainWindow", "IP Address:"))
        self.usernameLbl.setText(_translate("MainWindow", "Username:"))
        self.connectBtn.setText(_translate("MainWindow", "Connect!"))
        self.sendBtn.setText(_translate("MainWindow", "Send!"))
        self.membersLbl.setText(_translate("MainWindow", "Members (3):"))
        self.disconnectBtn.setText(_translate("MainWindow", "Disconnect"))

class mainAppWindow(QMainWindow, Ui_MainWindow):
    newMessage = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super(mainAppWindow, self).__init__(parent)
        self.setupUi(self)
        self.sendBtn.clicked.connect(self.send_message)
        self.disconnectBtn.clicked.connect(self.disconnect)
        self.connectBtn.clicked.connect(self.connect)
        self.newMessage.connect(self.new_msg)
        self.client = socket.socket()

    def new_msg(self, msg):
        msg_text = msg["text"]
        msg_sender = msg["sender"]
        new_msg_lbl = QtWidgets.QLabel("msgLabel")
        new_msg_lbl.setText(f"  {msg_sender}:\n  {msg_text}")
        #TODO: try to find a bettter formula to calculate the size of the message box/label.
        new_msg_lbl.setMinimumSize(len(msg_sender) * 10, 45)
        new_msg_lbl.setMaximumSize(len(f"  {msg_text}") * 5, len(f"  {msg_text}") * 5)
        new_msg_lbl.setStyleSheet("background:#eeeeee;")
        self.verticalLayout.addWidget(new_msg_lbl)

    def _client_connection(self, host, port, username):
        self.client.send(str.encode(username))
        while True:
            try:
                msg_size = int(self.client.recv(2048).decode("utf-8"))
                msg = self.client.recv(msg_size)
                msg_data = json.loads(msg.decode("utf-8"))
                if (msg_type := msg_data["data_type"]) == "user_data":
                    users = msg_data["value"]
                    self.membersLbl.setText(f"Members ({len(users)}):")
                    self.membersListWidget.clear()
                    for user in users:
                        self.membersListWidget.addItem(user)
                elif msg_type == "message_data":
                    sender = msg_data["sender"]
                    text = msg_data["value"]
                    #All of the spaces are just for a slight margin on the ui...
                    self.newMessage.emit({"text": text, "sender": sender})
            except:
                break

    def connect(self):
        #Address format ip:port
        regex = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?::[0-9]{1,4})?\b"
        address = self.ipAddressField.text()
        username = self.usernameField.text()
        if address == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("The address field is empty!")
            msg.setWindowTitle("Error!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        elif username == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("The username field is empty!")
            msg.setWindowTitle("Error!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        if re.match(regex, address):
            addressSplit = address.split(":")
            host = addressSplit[0]
            port = int(addressSplit[1])
            self.client = socket.socket()
            try:
                self.client.connect((host, port))
                #Load the chat screen.
                self.stackedWidget.setCurrentIndex(1)
                c_thread = threading.Thread(target=self._client_connection, args=(host, port, username,))
                c_thread.start()
            except Exception as e:
                print(e)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Failed to connect to this server!")
                msg.setWindowTitle("Error!")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("This address is invalid, the format should be: ip:port.")
            msg.setWindowTitle("Error!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def _disconnect_client(self):
        disconnect_msg = "!disconnect"
        d_msg = disconnect_msg.encode("utf-8")
        d_msg_len = str(len(d_msg)).encode("utf-8")
        try:
            self.client.send(d_msg_len)
            self.client.send(d_msg)
        except ConnectionResetError:
            #Meaning the server already closed the connection.
            #Do nothing.
            pass

    def disconnect(self):
        disconenct_msg_box = QMessageBox()
        disconenct_msg_box.setText("Are you sure you want to disconnect from this server?")
        disconenct_msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        disconenct_msg_box = disconenct_msg_box.exec_()
        if disconenct_msg_box == QMessageBox.Yes:
            #Disconnect
            self._disconnect_client()
            #Return to the home page.
            self.stackedWidget.setCurrentIndex(0)
        else:
            pass

    def send_message(self):
        message = self.messageTextEdit.toPlainText()
        if message != "":
            msg = message.encode("utf-8")
            msg_len = str(len(msg)).encode("utf-8")
            #Send the amount of data first
            try:
                self.client.send(msg_len)
                #Then send the actual data
                self.client.send(msg)
            except ConnectionResetError:
                connectionWarning = QMessageBox()
                connectionWarning.setText("Lost connection to the server.")
                connectionWarning.setIcon(QMessageBox.Critical)
                connectionWarning.setStandardButtons(QMessageBox.Ok)
                #Waiting for the user to click ok.
                connectionWarning = connectionWarning.exec_()
                self.stackedWidget.setCurrentIndex(0)
            self.messageTextEdit.clear()
        else:
            pass

    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("Are you sure you want to exit?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec_()
        if close == QMessageBox.Yes:
            try:
                self._disconnect_client()
                event.accept()
            except OSError:
                #Meaning the client is not connected.
                pass
        else:
            event.ignore()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = mainAppWindow()
    MainWindow.show()
    sys.exit(app.exec_())