def calc_price(days):
    rate = days * 0.80
    if rate + 0.50 <= 30:
        answer = rate + 0.50
    else:
        answer = 30
    return answer


overdue = int(input("How many days overdue?: "))
print("${0:.2f}".format(calc_price(overdue)))
