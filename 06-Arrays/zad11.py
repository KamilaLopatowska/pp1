def month(n):
    month_name = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    return month_name[int(n)-1]

number = input('Enter month number: ')
month(number)