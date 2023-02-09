import datetime

def workdayweek2daterange(year, weekno):
    offset = datetime.timedelta(days=3)
    try:
        start_date = datetime.date.fromisocalendar(year, weekno, 1) - offset
        end_date = datetime.date.fromisocalendar(year, weekno, 7) - offset
        return start_date, end_date
    except ValueError:
        return None, None

def print_weeks_in_year(year):
    print('\\begin{table}[H]')
    print('\\centering')
    print('\\begin{tabular}{|r|ccc|r|ccc|}')
    print('\\hline')
    print('\\multicolumn{1}{|c|}{\\textbf{No.}} & \multicolumn{3}{c|}{\\textbf{Week}} & \\multicolumn{1}{c|}{\\textbf{No.}} & \multicolumn{3}{c|}{\\textbf{Week}} \\\\')
    print('\\hline')
    for weekno in range(1, 27):
        weekno2 = weekno + 26
        start_date1, end_date1 = workdayweek2daterange(year, weekno)
        start_date2, end_date2 = workdayweek2daterange(year, weekno2)
        print('%2d & \\texttt{%s} & -- & \\texttt{%s} & %2d & \\texttt{%s} & -- & \\texttt{%s} \\\\' %
              (weekno, start_date1, end_date1,
               weekno2, start_date2, end_date2))
    start_date, end_date = workdayweek2daterange(year, 53)
    if start_date:
        print(' & & & & 53 & %s & -- & %s \\\\' % (start_date, end_date))
    print('\\hline')
    print('\\end{tabular}')
    print('\\caption{Workday weeks for year %d}' % year)
    print('\\end{table}')


if __name__ == '__main__':
    for year in range(2020, 2041):
        print_weeks_in_year(year)

