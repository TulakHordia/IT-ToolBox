import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox, QTreeWidget, \
    QTreeWidgetItem, QHBoxLayout, QSplitter
from PyQt5.QtCore import Qt
import subprocess


def run_script(script_command):
    try:
        result = subprocess.run(["powershell", "-Command", script_command], capture_output=True, text=True)
        QMessageBox.information(window, "Script output", result.stdout)
    except Exception as e:
        QMessageBox.information(window, "Error", f"Failed to run script: {e}")

def on_item_click(item, column):
    script_command = item.data(0, 0)
    if script_command:
        run_script(script_command)

def screen_resolution(window, main_content_label, splitter):
    screen_res = app.primaryScreen().availableGeometry()
    screen_width = screen_res.width()
    screen_height = screen_res.height()
    initial_width = int(screen_width * 0.6)
    initial_height = int(screen_height * 0.6)

    window.resize(initial_width, initial_height)
    window.setFixedSize(initial_width, initial_height)

    main_content_label.setFixedWidth(int(initial_width * 0.7))
    splitter.setSizes([int(initial_width * 0.2), main_content_label.width()])



app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("IT ToolBox")
window.setWindowIcon(QIcon("title-robot-icon.png"))
window.setGeometry(100, 100, 600, 400)

tree_widget = QTreeWidget()
tree_widget.setHeaderLabel("Scripts")

categories = {
    "Exchange PS Scripts": [
        {"name": "Import Exchange Module", "command": "Import-Module ExchangeOnlineManagement"},
        {"name": "Connect to Exchange", "command": "Connect-ExchangeOnline"}
    ],
    "Microsoft Graph": [
        {"name": "Import Graph Module", "command": "Import-Module Microsoft.Graph"},
        {"name": "Connect to Audit", "command": "Connect-MgGraph -Scopes 'AuditLog.Read.All'"}
    ],
    "Windows Registry": [
        {"name": "Something", "command": "something"}
    ]
}

for category_name, scripts in categories.items():
    category_item = QTreeWidgetItem([category_name])
    for script in scripts:
        script_item = QTreeWidgetItem([script["name"]])
        script_item.setData(0, 0, script["command"])
        category_item.addChild(script_item)
    tree_widget.addTopLevelItem(category_item)

tree_widget.itemClicked.connect(on_item_click)

splitter = QSplitter(Qt.Horizontal)
splitter.addWidget(tree_widget)

main_content_label = QLabel("Main Content")
main_content_label.setAlignment(Qt.AlignCenter)
splitter.addWidget(main_content_label)
splitter.setSizes([200, 600])

main_layout = QHBoxLayout(window)
# main_layout = QVBoxLayout(window)
main_layout.addWidget(splitter)
window.setLayout(main_layout)

screen_resolution(window, main_content_label, splitter)
window.show()
sys.exit(app.exec_())