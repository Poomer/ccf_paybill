income = [500, 600, 600]

for money in income:
    print(money)

# Add a function to calculate the mean of salary
def calculate_mean(income_list):
    return sum(income_list) / len(income_list)


print(calculate_mean(income))