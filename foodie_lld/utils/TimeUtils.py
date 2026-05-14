from datetime import datetime

class TimeUtils:
    @staticmethod
    def get_current_time():
        return datetime.now().strftime("%a %b %d %H:%M:%S %Y")