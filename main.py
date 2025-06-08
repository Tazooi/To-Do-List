
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QProgressBar, QVBoxLayout, QWidget

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ჩემი To-Do List აპლიკაცია")
        self.setGeometry(100, 100, 400, 500)

        self.tasks = []
        self.completed_tasks = 0

        self.initUI()

    def initUI(self):
        self.label = QLabel("ჩემი დავალებების სია", self)
        self.line_edit = QLineEdit(self)
        self.add_button = QPushButton("დამატება", self)
        self.task_list = QListWidget(self)
        self.progress_bar = QProgressBar(self)

        self.add_button.clicked.connect(self.add_task)
        self.task_list.itemChanged.connect(self.update_progress)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.add_button)
        layout.addWidget(self.task_list)
        layout.addWidget(self.progress_bar)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_task(self):
        task_text = self.line_edit.text().strip()
        if task_text:
            item = QListWidgetItem(task_text)
            item.setFlags(item.flags() | 2)  # Enable checkbox
            item.setCheckState(0)  # Unchecked

            self.task_list.addItem(item)
            self.tasks.append(item)
            self.line_edit.clear()
            self.update_progress()

    def update_progress(self):
        if not self.tasks:
            self.progress_bar.setValue(0)
            return

        completed = sum(1 for task in self.tasks if task.checkState() == 2)
        progress = int((completed / len(self.tasks)) * 100)
        self.progress_bar.setValue(progress)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
