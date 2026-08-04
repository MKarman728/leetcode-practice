class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.store:
            return ""
        time_values = self.store[key]
        l, r = 0, len(time_values) - 1
        while l <= r:
            m = (l + r ) // 2
            if timestamp == time_values[m][1]:
                return time_values[m][0]
            elif timestamp > time_values[m][1]:
                res = time_values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
