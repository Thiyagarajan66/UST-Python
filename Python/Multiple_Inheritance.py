#Multiple Inheritance


class CurrentDate:
    def __init__(self, date):
        self.date = date

class CurrentTime:
    def __init__(self, time):
        self.time = time

class Timestamp(CurrentDate, CurrentTime):
    def __init__(self, date, time):
        CurrentDate.__init__(self, date)
        CurrentTime.__init__(self, time)
        DateTime = self.date + ' ' + self.time   #DateTime is a object
        print(DateTime)

datetime1 = Timestamp('2022-10-2' , '11:00:22')        
