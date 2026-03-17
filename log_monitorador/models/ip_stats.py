class IPStats:

    def __init__(self, failed, success, timestamps, risk):
        self.failed = 0
        self.success = 0
        self.timestamps = []
        self.risk = "LOW"

    def add_failure(self, timestamp):
        self.failed += 1
        if timestamp is not None:
            self.timestamps.append(timestamp)
    
    def add_success(self):
        self.success += 1

    def failure_rate(self):
        total_attempts = self.failed + self.success
        if total_attempts == 0:
            return 0
        return (self.failed / total_attempts) * 100
    
    def update_risk(self):
        rate = self.failure_rate()
        if rate > 80:
            self.risk = "CRITICAL"
        elif rate > 60:
            self.risk = "HIGH"
        elif rate > 40:
            self.risk = "MEDIUM"
        else:
            self.risk = "LOW"

    def behavior(self):
        self.update_risk()
        return {
            "failed": self.failed,
            "success": self.success,
            "timestamps": self.timestamps,
            "risk": self.risk
        }
    
    def to_dict(self):
        return {
            "failed": self.failed,
            "success": self.success,
            "failure_rate": self.failure_rate(),
            "timestamps": self.timestamps,
            "risk": self.risk
        }