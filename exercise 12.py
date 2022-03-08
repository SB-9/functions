# Movie cinema ticketing system

ADULT = 12.50
CHILD = 7.00
STUDENT = 9.00
GIFT = 0
adult_tickets = 0
child_tickets = 0
student_tickets = 0
gift_tickets = 0
adult_current_sale = 0
student_current_sale = 0
gift_current_sale = 0
child_current_sale = 0


def sales_calculations():
    adult_sales = adult_tickets * ADULT
    child_sales = child_tickets * CHILD
    student_sales = student_tickets * STUDENT
    gift_sales = gift_tickets * GIFT
    total_sales = adult_sales + child_sales + student_sales + gift_sales
    return total_sales


def ticket_calculations():
    total_tickets = adult_tickets + child_tickets + student_tickets + gift_tickets
    return total_tickets


ticket_wanted = input()
