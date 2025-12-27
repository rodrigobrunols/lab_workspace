from collections import defaultdict, OrderedDict


class TimeMap:
    """
    void set(String key, String value, int timestamp)

    with timestamp_prev <= timestamp.
    If multiple values exist, return the value for the largest timestamp_prev. If no values, return ""

    """
    def __init__(self):
        self.name = "TimeMap"
        self.time_map = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int):
        self.time_map[key].append((timestamp, value))


    def get(self, key: str, timestamp: int):
        if key not in self.time_map:
            return ""

        time_values = self.time_map[key]
        left, right = 0, len(time_values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            mid_time, mid_value = time_values[mid]

            if mid_time <= timestamp:
                result = mid_value
                left = mid + 1
            else:
                right = mid - 1

        return result







time_map = TimeMap()

# Set values for the key "foo" at different times
time_map.set("foo", "bar", 1)
time_map.set("foo", "bar2", 4)

# Now let's query for "foo" at different timestamps
print(time_map.get("foo", 1))   # Output: "bar"  (exact match)
print(time_map.get("foo", 3))   # Output: "bar"  (timestamp 3 is between 1 and 4, so we get the value at time 1)
print(time_map.get("foo", 4))   # Output: "bar2" (exact match)
print(time_map.get("foo", 5))   # Output: "bar2" (timestamp 5 is after the last set, so we get the most
# recent value, from time 4)


