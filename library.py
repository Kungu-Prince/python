from datetime import datetime

def calculate_fine(bookID, dueDate, returnDate):
    due_date = datetime.strptime(dueDate, '%Y-%m-%d')
    return_date = datetime.strptime(returnDate, '%Y-%m-%d')
    days_overdue = (return_date - due_date).days
    #Fine rate based on days overdue
    if days_overdue <= 7:
        fine_rate = 20
    elif 8 <= days_overdue <= 14:
        fine_rate = 50
    else:
        fine_rate = 100
    # Calculate fine amount
    fine_amount = days_overdue * fine_rate

    print("bookID:", bookID)
    print("due Date:", dueDate)
    print("returnDate:", returnDate)
    print("daysOverdue:", days_overdue)
    print("fine Rate:", f"Ksh. {fine_rate}")
    print("fine Amount:", f"Ksh. {fine_amount}")


bookID = input("Enter bookID: ")
dueDate = input("Enter due Date (YYYY-MM-DD): ")
returnDate = input("Enter returnDate (YYYY-MM-DD): ")


calculate_fine(bookID, dueDate, returnDate)
