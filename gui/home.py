from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
)


class Home(QWidget):
    def __init__(self, accountID):
        super().__init__()
        self.setWindowTitle("Finance Manager")

        self.setStyleSheet("""
            QWidget {
                background-color: #dddddd;
            }
        """)

        layout = QVBoxLayout()

        self.setLayout(layout)
        self.showMaximized()