fortune_500_companies = ['Walmart', 'Amazon', 'Apple', 'Apple', 'CVS Health', 'Meta', 'Meta', 'UnitedHealth Group', 'Berkshire Hathaway', 'McKesson', 'AmerisourceBergen', 'Alphabet', 'Exxon Mobil']
fortune_500_companies[2:2] = ['Meta']
meta_index = fortune_500_companies.index('Meta')
unique = set(fortune_500_companies)
print(unique)
print(meta_index)
print(fortune_500_companies)

top_company = []
for company in fortune_500_companies:
    top_company.append(company)
print(top_company)
for company in range(len(fortune_500_companies)):
    top_company.append(fortune_500_companies[company])
print(top_company)
number_of_list = 0
while number_of_list < len(fortune_500_companies):
    top_company.append(fortune_500_companies[number_of_list])
    number_of_list += 1
print(top_company)
while fortune_500_companies:
    top_company.append(fortune_500_companies[0])
    fortune_500_companies.remove(fortune_500_companies[0])
print(top_company)

day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
string_day = list(map(str, day_in_month))
string_day.sort()
print(string_day)
def filters(day):
    if day < 30:
        return True
    else:
        return False
filtered_day = list(filter(filters, day_in_month))
print(filtered_day)
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
def montly(month):
    return month.upper() if month == 'March' or month == 'May' else month.lower()
new_year = list(map(montly, month))
print(new_year)
new_month = list(filter(lambda month: month == 'March' or month == 'May', month))
print(new_month)