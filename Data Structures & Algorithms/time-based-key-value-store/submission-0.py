# my solution
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self._entries = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._entries[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if not self._entries[key] or timestamp < self._entries[key][0][0]:
            return ""

        candidates = self._entries[key]

        start, end = 0, len(candidates) - 1

        while start <= end:
            mid = start + (end - start) // 2
            time_entry, value = candidates[mid]

            if time_entry == timestamp:
                return value
            
            if time_entry > timestamp:
                end = mid - 1
            else:
                start = mid + 1

        return candidates[end][1]
        """
        early checks we can make
            entries[key] is empty or entries[key][0][0] > timestamp -> return ""
            example input: key = a and timestamp = 3
            a = [(0,blue),(2,red), (3,purple)]
            binary search
                start | end | mid, a[mid][0] |
                0,2,1, 2
                    2 < timestamp
                    search right, start = mid + 1 = 2
                2,2,2,3
                    timestamps = return a[mid][1]
            -- asuming timestamp is 4 for the same key
                start | end | mid, a[mid][0] |
                0,2,1, 2
                    2 < 4
                    search right, start = mid + 1 = 2
                2,2,2,3
                    3 < 4
                    search right, start = mid + 1 = 3
                3,2,
                    start > end since end is the last valid index we return a[end][1]
            -- asuming timestamp is 1 for the same key
                start | end | mid, a[mid][0] |
                0,2,1, 2
                    2 > 1, search left, end = mid - 1 = 0
                0,0,0,0
                    0 < 1, searh right, start = mid + 1 = 1
                1,0
                    start > end
                    start and end are valid indices but end is the smaller so we return a[end][1]
        """