year=2020

if (year % 4==0 and year % 100!=0)or (year % 400==0):
    leap_year=True
else:
    leap_year=False
print(f"{year} is {leap_year}")