
class FirstDayFinder:

    def __init__(self, transist_h, transit_m):
        self.transit = self.hh_mm_to_minutes(transist_h, transit_m)

    @staticmethod
    def hh_mm_to_minutes(h, m):
        return 60 * h + m

    @staticmethod
    def minutes_to_hh_mm(minutes):
        h = int(minutes / 60)
        m = minutes - h * 60
        return h, m

    @staticmethod
    def minutes_to_hh_mm_str(minutes):
        h, m = FirstDayFinder.minutes_to_hh_mm(minutes)
        return '%dh %dm' % (h, int(m))

    @staticmethod
    def minutes_to_time_str(minutes):
        h, m = FirstDayFinder.minutes_to_hh_mm(minutes)
        hh = h - 12 if h > 12 else h
        am_pm = 'pm' if h > 11 else 'am'
        return '%02d:%02d %s' % (hh, int(m), am_pm)


    def report_first(self, place, rise_h, rise_m, set_h, set_m):
        rise = self.hh_mm_to_minutes(rise_h, rise_m)
        set = self.hh_mm_to_minutes(set_h, set_m)
        day_length = set - rise
        three_fifths = int(0.6 * day_length)
        three_fifth_time = rise + three_fifths
        day = 'Next day' if three_fifth_time < self.transit else 'Same day'

        print('%-20s & \\texttt{%s} & \\texttt{%s} & \\texttt{%sm (%s)}  & \\texttt{%sm (%s)} & \\texttt{%s} & %s \\\\' % (
            place, self.minutes_to_time_str(rise), self.minutes_to_time_str(set),
            day_length, self.minutes_to_hh_mm_str(day_length),
            three_fifths, self.minutes_to_hh_mm_str(three_fifths),
            self.minutes_to_time_str(three_fifth_time), day))

if __name__ == '__main__':
    times = [
        ('Kanjangatu', 6, 21, 18, 26),
        ('Kozhikode', 6, 19, 18, 23),
        ('Trichur', 6, 18, 18, 21),
        ('Kochi', 6, 18, 18, 21),
        ('Kottayam', 6, 17, 18, 20),
        ('Kollam', 6, 16, 18, 19),
        ('Palakkadu', 6, 16, 18, 19),
        ('Pathanamthitta', 6, 16, 18, 18),
        ('Trivandrum', 6, 15, 18, 18)
    ]

    fdf = FirstDayFinder(13, 30)
    for t in times:
        fdf.report_first(t[0], t[1], t[2], t[3], t[4])