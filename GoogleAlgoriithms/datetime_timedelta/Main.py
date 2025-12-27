from datetime import datetime, timedelta


def calculate_business_days(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    #   payday = datetime(year, month, 15)

    if start > end:
        return 0  # edge case: invalid date range

    business_days = 0
    current = start
    while current <= end:
        if current.weekday() < 5:  # 0=Monday, 4=Friday
            business_days += 1
        current += timedelta(days=1)
    return business_days


def next_payday(current_date, payday_rule):
    current = datetime.strptime(current_date, '%Y-%m-%d')
    year, month = current.year, current.month

    if payday_rule == 'last_friday':
        # Find the last day of the month
        next_month = month + 1 if month < 12 else 1
        next_year = year if month < 12 else year + 1
        last_day = datetime(next_year, next_month, 1) - timedelta(days=1)

        # Iterate backward to find the last Friday
        payday = last_day
        while payday.weekday() != 4:  # 4=Friday
            payday -= timedelta(days=1)

        # If payday is before current_date, move to next month
        if payday < current:
            month = month + 1 if month < 12 else 1
            year = year if month < 12 else year + 1
            return next_payday(f"{year}-{month:02d}-01", 'last_friday')
        return payday.strftime('%Y-%m-%d')

    elif payday_rule == '15th':
        # Check 15th of current month
        payday = datetime(year, month, 15)

        # Adjust if 15th is weekend (Saturday=5, Sunday=6)
        if payday.weekday() >= 5:
            payday += timedelta(days=(7 - payday.weekday()))

        # If payday is before current_date, move to next month
        if payday < current:
            month = month + 1 if month < 12 else 1
            year = year if month < 12 else year + 1
            return next_payday(f"{year}-{month:02d}-01", '15th')
        return payday.strftime('%Y-%m-%d')

# Tests

import uuid
print(uuid.uuid4())

today = datetime.today()
today2 = today.replace(year=1000)
# today.year
print(today2)
print(today)



print(next_payday('2023-09-14', '15th'))        # Output: '2023-09-15'
print(next_payday('2023-10-14', '15th'))        # Output: '2023-10-16'
start_date = '2023-10-01'  # Sunday
end_date = '2023-10-08'    # Sunday
print(calculate_business_days(start_date, end_date))  # Output: 5
current_date = '2023-09-28'  # Thursday
print(next_payday(current_date, 'last_friday'))  # Output: '2023-09-29'
current_date = '2023-09-14'
print(next_payday(current_date, '15th'))  # Output: '2023-09-15'
