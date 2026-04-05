"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        times = set()

        for interval in intervals:
            for i in range(interval.start, interval.end):
                interval.start += 1
                if interval.start in times:
                    return False
                times.add(interval.start)
        return True