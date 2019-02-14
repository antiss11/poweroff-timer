import gui
import sys
import os
from PyQt5 import QtWidgets
import time
import threading
from PyQt5.Qt import QTime, QWidget, QEvent
import datetime

SLEEP = "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
POWEROFF = "shutdown /s"
RESTART = "shutdown /r"

class Timer(QtWidgets.QMainWindow, gui.Ui_MainWindow, QWidget):
    def __init__(self):
        QWidget.__init__(self)
        super().__init__()
        self.setupUi(self)
        self.radioButton_sleep.setChecked(True)
        self.action_time = 0
        self.radioButton_in.setChecked(True)
        self.centralwidget.setFocus()
        self.pushButton_start.clicked.connect(self.start_button)
        self.pushButton_stop.clicked.connect(self.stop_button)
        self.time_thread_kill = False
        self.action_time_thread_kill = False
        self.timeEdit.installEventFilter(self)
        # self.pushButton_start.installEventFilter(self)

    def eventFilter(self, watched, event):
        if watched == self.timeEdit and event.type() == QEvent.FocusIn:
            self.time_thread_kill = True
        if watched == self.pushButton_stop and event.type() == QEvent.MouseButtonPress:
            self.action_time_thread_kill = True

        return QWidget.eventFilter(self, watched, event)

    def _update(self):
        while self.time_thread_kill is False:
            time_now = QTime.currentTime()
            self.timeEdit.setTime(time_now)
            time.sleep(1)

    def time_thread(self):
        threading.Thread(target=self._update).start()

    def get_timer_type(self):
        if self.radioButton_after.isChecked():
            return "after"
        elif self.radioButton_in.isChecked():
            return "in"

    def get_action_type(self):
        if self.radioButton_off.isChecked():
            return "off"
        elif self.radioButton_restart.isChecked():
            return "restart"
        elif self.radioButton_sleep.isChecked():
            return "sleep"

    def get_action_time(self):
        time = self.timeEdit.time()
        return time

    def start_action(self, timer_type, action_type, action_time):
        if timer_type == "in":
            if action_type == "sleep":
                self.in_timer(action_time, SLEEP)
            elif action_type == "off":
                self.in_timer(action_time, POWEROFF)
            elif action_type == "restart":
                self.in_timer(action_time, RESTART)
        elif timer_type == "after":
            if action_type == "sleep":
                self.after_timer(action_time, SLEEP)
            elif action_type == "off":
                self.after_timer(action_time, POWEROFF)
            elif action_type == "restart":
                self.in_timer(action_time, RESTART)

    def start_button(self):
        timer_type = self.get_timer_type()
        action_type = self.get_action_type()
        action_time = self.get_action_time().toString()
        self.pushButton_start.setDisabled(True)
        threading.Thread(target=self.start_action, args=(timer_type, action_type, action_time)).start()

    def stop_button(self):
        self.action_time_thread_kill = True
        self.restore()

    def restore(self):
        self.action_time_thread_kill = False
        self.time_thread_kill = False
        self.pushButton_start.setEnabled(True)

    def restore_after_action(self):
        self.action_time_thread_kill = False
        self.time_thread_kill = False
        self.pushButton_start.setEnabled(True)
        self.time_thread()

    def in_timer(self, action_time, action_type):
        try:
            while True:
                now = QTime.currentTime().toString()
                if now == action_time:
                    print(123)
                    os.system(action_type)
                    raise StopIteration
                    break
                elif self.action_time_thread_kill is True:
                    print("Stop")
                    self.restore()
                    break
        except StopIteration:
            self.restore()

    def after_timer(self, action_time, action_type):
        seconds_to_start = int(action_time[0:2]) * 3600 + int(action_time[3:5]) * 60 + int(action_time[6:8])
        for i in range(seconds_to_start + 1):
            if self.action_time_thread_kill is False:
                time.sleep(1)
            elif self.action_time_thread_kill is True:
                print("break")
                self.restore()
                break
        else:
            os.system(action_type)
            self.restore_after_action()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Timer()
    window.show()
    window.time_thread()

    app.exec_()

if __name__ == "__main__":
    main()