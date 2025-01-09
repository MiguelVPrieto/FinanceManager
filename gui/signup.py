from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget, QLineEdit, QFrame, QPushButton, QLabel, QMainWindow,
)
from PyQt5.QtCore import Qt


class SignUp(QMainWindow):
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

        self.balanceInput = QLineEdit()
        self.balanceInput.setPlaceholderText("Balance")
        self.balanceInput.setStyleSheet("""
            QLineEdit {
                margin-bottom: 10px;
                padding: 8px;
                border: 1px solid #cccccc;
                border-radius: 5px;
            }
        """)
        cardLayout.addWidget(self.balanceInput)

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

        self.cPasswordInput = QLineEdit()
        self.cPasswordInput.setPlaceholderText("Confirm Password")
        self.cPasswordInput.setEchoMode(QLineEdit.Password)
        self.cPasswordInput.setStyleSheet("""
            QLineEdit {
                margin-top: 10px;
                padding: 8px;
                border: 1px solid #cccccc;
                border-radius: 5px;
            }
        """)
        cardLayout.addWidget(self.cPasswordInput)

        self.errorLabel = QLabel()
        self.errorLabel.setStyleSheet("""
            QLabel {
                color: #ff0000;
                border: 0px;
            }
        """)
        self.errorLabel.setFixedSize(300, 15)
        cardLayout.addWidget(self.errorLabel, alignment=Qt.AlignCenter)

        self.loginButton = QPushButton("Create Account")
        self.loginButton.clicked.connect(self.createAccount)
        self.loginButton.setStyleSheet("""
            QPushButton {
            }
        """)
        cardLayout.addWidget(self.loginButton)

        self.signupLink = QPushButton("Already have an account?")
        self.signupLink.clicked.connect(self.loadLogin)
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

    def loadLogin(self):
        from login import MainWindow
        login = MainWindow()
        self.setCentralWidget(login)

    def createAccount(self):
        print("Creating Account")