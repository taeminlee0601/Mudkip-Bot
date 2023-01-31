from datetime import date
import typing

class TimeTable:
    late_start_days = [date(2023, 2, 15), date(2023, 2, 22), date(2023, 3, 22), date(2023, 3, 29), date(2023, 4, 19), date(2023, 4, 26), date(2023, 5, 24), date(2023, 5, 31)]

    def __init__(self, user, p1, p2, p3, p4):
        self.user = user
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def set_period(self, per_num, period):
        if per_num == 1:
            self.p1 = period
        elif per_num == 2:
            self.p2 = period
        elif per_num == 3:
            self.p3 = period
        else:
            self.p4 = period

    def __str__(self):
        today = date.today()
        curDay = today.day
        day = curDay % 2 

        periods = []

        passed = []

        for i in range(len(self.late_start_days)):
           if today > self.late_start_days[i]:
                passed.append(i)

        for i in reversed(passed):
            self.late_start_days.pop(i)

        if today != self.late_start_days[0]:
            periods.append("9:00 - 10:20  Period 1: **" + self.p1 + "**")
            periods.append("10:25 - 11:40 Period 2: **" + self.p2 + "**")
            periods.append("11:40 - 12:40 **Lunch**")

            if day == 1:
                periods.append("12:40 - 1:55  Period 3: **" + self.p3 + "**")
                periods.append("2:00- 3:15    Period 4: **" + self.p4 + "**")
            else:
                periods.append("12:40 - 1:55  Period 3: **" + self.p4 + "**")
                periods.append("2:00 - 3:15   Period 4: **" + self.p3 + "**")
        else:
            periods.append("9:55 - 10:55  Period 1: **" + self.p1 + "**")
            periods.append("11:00 - 12:00 Period 2: **" + self.p2 + "**")
            periods.append("12:00 - 1:05  **Lunch**")

            if day == 1:
                periods.append("1:05 - 2:10  Period 3: **" + self.p3 + "**")
                periods.append("2:15 - 3:15  Period 4: **" + self.p4 + "**")
            else:
                periods.append("1:05 - 2:10  Period 3: **" + self.p4 + "**")
                periods.append("2:15 - 3:15  Period 4: **" + self.p3 + "**")

        return '\n'.join(periods)

class Periods:
    def __init__(self, per_num, course, room = 0, teacher = ""):
        self.per_num = per_num
        self.course = course
        self.room = room
        self.teacher = teacher

    def set_course(self, course):
        self.course = course

    def set_room(self, room):
        self.room = room

    def set_teacher(self, teacher):
        self.teacher = teacher

    def get_num(self):
        return self.per_num

    def __str__(self):
        period_info = []

        period_info.append("Period " + str(self.per_num) + ": **" + self.course + "**")
        
        if self.room != 0:
            period_info.append("Room: **" + str(self.room) + "**")
        
        if self.teacher == "":
            return '\n'.join(period_info)
        else:
            period_info.append("Teacher: **" + self.teacher + "**")

        return '\n'.join(period_info)

