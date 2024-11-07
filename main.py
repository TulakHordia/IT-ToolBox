import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox, QTreeWidget, QTreeWidgetItem
import subprocess


def run_script():
    try:
        result = subprocess.run(["powershell", "-Command", "echo 'Hello, IT team!'"], capture_output=True, text=True)
        QMessageBox.information(window, "Script output", result.stdout)
    except Exception as e:
        QMessageBox.information(window, "Error", f"Failed to run script: {e}")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("IT ToolBox")
window.setWindowIcon(QIcon("title-robot-icon.png"))
window.setGeometry(100, 100, 500, 300)


layout = QVBoxLayout()


label = QLabel("Welcome to the IT ToolBox", window)
label.setStyleSheet("font-size: 16px; margin: 20px;")
layout.addWidget(label)


run_button = QPushButton("Run", window)
run_button.setFixedWidth(100)
run_button.setStyleSheet("font-size: 14px; padding: 10px; background-color: #4CAF50; color: white;")
run_button.clicked.connect(run_script)
layout.addWidget(run_button)


window.setLayout(layout)


window.show()
sys.exit(app.exec_())