# Movie cinema ticketing system

ADULT = 12.50
CHILD = 7.00
STUDENT = 9.00
GIFT = 0


def main_routine():
    adult_tickets = 0
    child_tickets = 0
    student_tickets = 0
    gift_tickets = 0
    tickets_sold = 0
    ticket_wanted = input("Do you want to sell a ticket? (Y/N): ").upper()
    if ticket_wanted != "Y" or "N":
        ticket_wanted = input("Please enter Y or N (Y/N): ").upper()
    else:
        while ticket_wanted == "Y":
            ticket = sell_ticket()
        num_tickets = int(input("How many of these tickets do you want?: "))
        confirm = input("confirm purchase of tickets?: (Y/N)").upper()
        while confirm != "Y" or "N":
            confirm = input("Please enter Y or N (Y/N): ").upper()
            if confirm == "Y":
                tickets_sold += num_tickets
                if ticket == "adult":
                    num_tickets += adult_tickets
                elif ticket == "student":
                    num_tickets += student_tickets
                elif ticket == "child":
                    num_tickets += child_tickets
                else:
                    num_tickets += gift_tickets
            ticket_wanted = input("Do you want to sell another ticket? (Y/N): ").upper()
            while ticket_wanted != "Y" or "N":
                ticket_wanted = input("Please enter Y or N (Y/N): ").upper
        total_sales = (adult_tickets * ADULT) + (child_tickets * CHILD) + (student_tickets * STUDENT) + (gift_tickets * GIFT)
        print(f"tickets sold: {tickets_sold} ")
        print(f"adult tickets: {adult_tickets}")
        print(f"child tickets: {child_tickets}")
        print(f"student tickets: {student_tickets}")
        print(f"gift tickets: {gift_tickets}")
        print(f"sales for the day came to: {total_sales}")


def sell_ticket():
    ticket_type_ = input("what kind of ticket do you want?: \n"
                         "\tadult for adult\n"
                         "\tstudent for student \n"
                         "\tchild for child \n"
                         "\tgift for gift \n"
                         "\t>>").lower()
    return ticket_type_

print("*****My movie theatre ticketing system*****")
main_routine()

