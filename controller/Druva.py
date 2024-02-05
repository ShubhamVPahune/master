

def get_next_date(input_date):
    "Format of date should be 01Jul2024"
    date = input_date[0:2]
    month = input_date[2:5]
    year = int(input_date[5:len(input_date)])
    months = ["Jan","Feb","Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    if month in ["Jan","Mar", "May", "Jul", "Sep", "Nov", "Dec"]:
        last_date=31
    elif month == "Feb":
        if year%4 == 0:
            last_date=29
        else:
            last_date=28
    else:
        last_date=30

    next_date = int(date)+1
    if next_date > last_date:
        if month == "Dec":
            next_date = 1
            month = months[0]
            year = year + 1
        else:
            next_date = 1
            month_inex = months.index(month)
            month = months[month_inex+1]

    new_date = f"{next_date}{month}{year}"
    print(new_date)


get_next_date("29Feb2020")
