class MoneyNotEnoughError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class PINCodeError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass


info = input().split(', ')

pin_code, balance, age = info[0], int(info[1]), int(info[2])

while True:
    line = input()

    if line == 'End':
        break

    line = line.split("#")

    # Handle command 'Send Money':
    if line[0] == 'Send Money':
        money, pin_code_entered = float(line[1]), line[2]
        # Check for insufficient balance
        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        # PIN check
        if pin_code_entered != pin_code:
            raise PINCodeError("Invalid PIN code")

        # Age check
        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        # Transaction is successful
        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif line[0] == 'Receive Money':
        salary = float(line[1])

        # Check to see if amount is negative:
        if salary < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        # Perform operations and deposit:
        salary_after_investing = salary / 2
        balance += salary_after_investing
        print(f"{salary_after_investing:.2f} money went straight into the bank account")
