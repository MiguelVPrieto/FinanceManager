import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QFrame, QPushButton, QLabel,
)
from PyQt5.QtCore import Qt
import hashlib
from database import loginAuth
from signup import SignUp
from home import Home


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance Manager")

        self.setStyleSheet("""
            QMainWindow {
                background-color: #dddddd;
            }
        """)

        layout = QVBoxLayout()

        self.card = QFrame()
        self.card.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border-radius: 10px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                padding: 20px;
            }
        """)
        self.card.setFixedSize(350, 235)

        cardLayout = QVBoxLayout()

        self.fullNameInput = QLineEdit()
        self.fullNameInput.setPlaceholderText("Full Name")
        self.fullNameInput.setStyleSheet("""
            QLineEdit {
                margin-bottom: 10px;
                padding: 8px;
                border: 1px solid #cccccc;
                border-radius: 5px;
            }
        """)
        cardLayout.addWidget(self.fullNameInput)

        self.passwordInput = QLineEdit()
        self.passwordInput.setPlaceholderText("Password")
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setStyleSheet("""
            QLineEdit {
                margin-top: 10px;
                padding: 8px;
                border: 1px solid #cccccc;
                border-radius: 5px;
            }
        """)
        cardLayout.addWidget(self.passwordInput)

        self.errorLabel = QLabel()
        self.errorLabel.setStyleSheet("""
            QLabel {
                color: #ff0000;
                border: 0px;
            }
        """)
        self.errorLabel.setFixedSize(300, 15)
        cardLayout.addWidget(self.errorLabel, alignment=Qt.AlignCenter)

        self.loginButton = QPushButton("Login")
        self.loginButton.clicked.connect(self.login)
        self.loginButton.setStyleSheet("""
            QPushButton {
            }
        """)
        cardLayout.addWidget(self.loginButton)

        self.signupLink = QPushButton("Don't have an account?")
        self.signupLink.clicked.connect(self.loadSignUp)
        self.signupLink.setStyleSheet("""
            QPushButton {
                border: 0px;
                text-decoration: none;
            }
            
            QPushButton:hover {
                text-decoration: underline;
            }
        """)
        cardLayout.addWidget(self.signupLink)

        self.card.setLayout(cardLayout)

        layout.addWidget(self.card, alignment=Qt.AlignCenter)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.showMaximized()

    def login(self):
        fullName = self.fullNameInput.text()
        password = self.passwordInput.text()

        hashedPassword = hashlib.sha256(password.encode()).hexdigest()

        res = loginAuth(fullName, hashedPassword)

        if res == -1:
            self.errorLabel.setText("Invalid username or password")
        else:
            self.loadHome(res)

    def loadHome(self, accountID):
        home = Home(accountID)
        self.setCentralWidget(home)

    def loadSignUp(self):
        signup = SignUp()
        self.setCentralWidget(signup)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
