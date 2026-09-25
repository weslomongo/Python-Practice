import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QPushButton
)

from PyQt5.QtCore import QTimer, QTime, Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

        self.time = QTime(0, 0, 0, 0)

        self.time_label = QLabel("00:00:00.00")

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.reset_button = QPushButton("Reset")

        self.timer = QTimer(self)

        self.initUI()


    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setGeometry(700, 300, 850, 350)

        layout = QVBoxLayout()

        layout.addWidget(self.time_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.reset_button)

        self.setLayout(layout)

        # Center the stopwatch text
        self.time_label.setAlignment(Qt.AlignCenter)

        # Style the display
        self.time_label.setStyleSheet(
            "font-size: 150px;"
            "color: #00FF00;"
            "background-color: black;"
        )

        # Button connections
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        # Timer connection
        self.timer.timeout.connect(self.update_time)


    def start(self):
        self.timer.start(10)


    def stop(self):
        self.timer.stop()


    def reset(self):
        self.timer.stop()

        self.time = QTime(0, 0, 0, 0)

        self.time_label.setText("00:00:00.00")


    def update_time(self):
        self.time = self.time.addMSecs(10)

        formatted_time = self.format_time(self.time)

        self.time_label.setText(formatted_time)


    def format_time(self, time):
        time_text = time.toString("hh:mm:ss.zzz")

        # Removes the last millisecond digit
        # 00:00:00.000 -> 00:00:00.00
        return time_text[:-1]


if __name__ == "__main__":
    app = QApplication(sys.argv)

    stopwatch = Stopwatch()

    stopwatch.show()

    sys.exit(app.exec_())