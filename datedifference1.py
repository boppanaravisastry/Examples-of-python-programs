from datetime import datetime # import datetime Module
starting_date=input('enter date in YYYY-MM-DD:').strip()
ending_date=input('enter date in YYYY-MM-DD:').strip()
format= "%Y-%m-%d" # date format

def datedifference(date1, date2): 
        try:
                starting_date = datetime.strptime(date1,format)
                ending_date = datetime.strptime(date2, format)
        except Exception as e:
                print(e)
                return e
        return (ending_date - starting_date)
print(datedifference(starting_date,ending_date))



