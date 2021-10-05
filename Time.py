class Time:
    def __init__(self, h, m, s):
        self.__hours = h
        self.__minutes = m
        self.__seconds = s
    def getHours(self):
        return self.__hours
    def getMinutes(self):
        return self.__minutes
    def getSeconds(self):
        return self.__seconds
    def __str__(self):
        return str(self.__hours) + ":" + str(self.__minutes) + ":" + str(self.__seconds)
    """
    timeInSeconds
    returns self object converted to seconds
    """
    def timeInSeconds(self):
        return (self.__hours*24 + self.__minutes)*60 + self.__seconds
    """
    changeTheTime
    param   h   int hours
    param   m   int minutes
    param   s   int seconds
    assigns inputted values to self object
    """
    def changeTheTime(self,h,m,s):
        self.__hours = h
        self.__minutes = m
        self.__seconds = s
    """
    twelveHourClock
    returns self object as a 12-hour time
    """
    def twelveHourClock(self):
        if self.__hours > 12: # if time is past noon
            self.changeTheTime(self.__hours-12,self.__minutes,self.__seconds)
            return str(self) + " pm"
        else: # if time is noon or before
            return str(self) + " am"
    """
    whatTimeIsIt
    returns what time of day self object is
    """
    def whatTimeIsIt(self):
        if self.__hours >= 6 and self.__hours < 12: # if time is during morning
            return "morning"
        elif self.__hours >= 12 and self.__hours < 17: # if time is during afternoon
            return "afternoon"
        elif self.__hours >= 17 and self.__hours < 22: # if time is during evening
            return "evening"
        else: # if time is during nighttime
            return "nighttime"
    """
    compareTo
    param   t   time object
    returns the number of seconds in between t and self
    """
    def compareTo(self,t):
        return abs(self.timeInSeconds()-t.timeInSeconds())
    """
    timeTill
    param   t   time object
    returns amount of time until t from self
    """
    def timeTill(self,t):
        if self.__hours > t.getHours(): # if t is day after
            t.changeTheTime(t.getHours()+24,t.getMinutes(),t.getSeconds())
        if self.__minutes > t.getMinutes(): # if t minutes are less than self's
            t.changeTheTime(t.getHours()-1,t.getMinutes()+60,t.getSeconds())
        if self.__seconds > t.getSeconds(): # if t seconds are less than self's
            t.changeTheTime(t.getHours(),t.getMinutes()-1,t.getSeconds()+60)
        t0 = Time(t.getHours()-self.__hours,t.getMinutes()-self.__minutes,t.getSeconds()-self.__seconds)
        return t0