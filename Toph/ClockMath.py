class Clock:
    def __init__(self, h, m):
        self.hour = h
        self.min = m
        self.totalDegree = 360
        self.angle = 0
        self.perHour = 30
        self.perMin = 6
        self.perHourMin = 1/2

    def calculate(self):
        self.angle = abs((self.hour * self.perHour + self.min * self.perHourMin) - self.min * self.perMin)
        return self.angle

    def maxAngle(self):
        if self.angle > self.totalDegree//2:
            return self.angle
        return self.totalDegree - self.angle

    def minAngle(self):
        if self.angle > self.totalDegree//2:
            return self.totalDegree - self.angle
        return self.angle

hour, min = map(int, input().split())
clock = Clock(hour, min)
clock.calculate()
print(clock.minAngle())



