import rumps


class PomodoroApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Pomodoro",
            "start": "Start Pomodoro",
            "pause": "Pause Pomodoro",
            "continue": "Continue Pomodoro",
            "stop": "Stop Timer",
            "reset": "Reset Pomodoros",
            "break_message": "Time is up! Take a 5 minute break 👍",
            "completed_message": "Four Pomodoros completed! Take a 20 minute break 😇",
            "interval": 10,
        }
        self.completed = 0
        self.app = rumps.App(self.config["app_name"])
        self.timer = rumps.Timer(self.on_tick, 1)
        self.interval = self.config["interval"]
        self.set_up_menu()
        self.start_stop_button = rumps.MenuItem(
            title=self.config["start"], callback=self.start_timer
        )
        self.reset_button = rumps.MenuItem(
            title=self.config["reset"], callback=self.reset_count
        )
        self.app.menu = [self.start_stop_button, self.reset_button]

    def set_up_menu(self):
        self.timer.stop()
        self.timer.count = 0
        self.app.title = "🍅" if self.completed == 0 else "🍅" * self.completed

    def on_tick(self, sender):
        time_left = sender.end - sender.count
        mins = time_left // 60 if time_left >= 0 else time_left // 60 + 1
        secs = time_left % 60 if time_left >= 0 else (-1 * time_left) % 60
        if mins == 0 and time_left < 0:
            self.completed += 1
            if self.completed < 4:
                message = self.config["break_message"]
            else:
                message = self.config["completed_message"]
                self.completed = 0
            rumps.notification(
                title=self.config["app_name"], subtitle=message, message=message
            )
            self.stop_timer(None)
        else:
            self.app.title = "{:2d}:{:02d}".format(mins, secs)
        sender.count += 1

    def start_timer(self, sender):
        assert sender.title.lower().startswith("start")
        self.timer.count = 0
        self.timer.end = self.interval
        sender.title = self.config["stop"]
        self.timer.start()
        self.start_stop_button.set_callback(self.stop_timer)

    def stop_timer(self, sender):
        assert sender is None or sender.title.lower().startswith("stop")
        self.timer.stop()
        self.set_up_menu()
        self.timer.count = 0
        self.start_stop_button.set_callback(self.start_timer)
        self.start_stop_button.title = self.config["start"]

    def reset_count(self, sender):
        self.completed = 0
        self.timer.stop()
        self.set_up_menu()
        self.timer.count = 0
        self.start_stop_button.title = self.config["start"]

    def run(self):
        self.app.run()


if __name__ == "__main__":
    app = PomodoroApp()
    app.run()
