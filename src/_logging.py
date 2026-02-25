
class Log:
        def __init__(self):
                self.INFO = 0
                self.ERROR = 1
                self.WARNING = 2
                self.DEBUG = 3

        def log(self,level = 0 , text = "") -> None:
                if level == self.INFO:
                        print("[INFO] " + text)
                elif level == self.ERROR:
                        print("[ERROR] " + text)
                elif level == self.WARNING:
                        print("[WARNING] " + text)
                elif level == self.DEBUG:
                        print("[DEBUG] " + text)

if __name__ == "__main__":
        log = Log()
        log.log()
        log.log(level = log.ERROR, text = "This is a test")