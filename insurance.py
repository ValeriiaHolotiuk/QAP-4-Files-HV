import datetime
import time
from FormatValues import to_title_case, to_upper_case, format_currency, calculate_hst_and_total

def load_constants():
    with open('Const.txt', 'r') as file:
        return [line.strip() for line in file]

def validate_province(province):
    valid_provinces = ['ON', 'QC', 'NS', 'NB', 'MB', 'BC', 'PE', 'SK', 'AB', 'NL', 'NT', 'YT', 'NU']
    return province in valid_provinces

def validate_payment_method(method):
    valid_methods = ['Full', 'Monthly', 'Down Pay']
    return method in valid_methods

def calculate_premium(num_cars, liability, glass, loaner, constants):
    basic_premium = float(constants[1])
    discount = float(constants[2])
    liability_cost = float(constants[3])
    glass_cost = float(constants[4])
    loaner_cost = float(constants[5])

    premium = basic_premium + (num_cars - 1) * (basic_premium * (1 - discount))

    extra_costs = 0
    if liability == 'Y':
        extra_costs += liability_cost * num_cars
    if glass == 'Y':
        extra_costs += glass_cost * num_cars
    if loaner == 'Y':
        extra_costs += loaner_cost * num_cars

    total_premium = premium + extra_costs
    return total_premium

def process_customer():
    constants = load_constants()
    next_policy_number = int(constants[0])
    hst_rate = float(constants[6])
    processing_fee = float(constants[7])

    first_name = to_title_case(input("Enter customer's first name: "))
    last_name = to_title_case(input("Enter customer's last name: "))
    address = input("Enter customer's address: ")
    city = to_title_case(input("Enter customer's city: "))
    province = to_upper_case(input("Enter customer's province (abbreviation): "))
    while not validate_province(province):
        province = to_upper_case(input("Invalid province. Enter again: "))
    postal_code = input("Enter customer's postal code: ")
    phone_number = input("Enter customer's phone number: ")

    num_cars = int(input("Enter number of cars being insured: "))
    liability = to_upper_case(input("Extra liability coverage (Y/N): "))
    glass = to_upper_case(input("Glass coverage (Y/N): "))
    loaner = to_upper_case(input("Loaner car coverage (Y/N): "))
    payment_method = to_title_case(input("Payment method (Full/Monthly/Down Pay): "))
    while not validate_payment_method(payment_method):
        payment_method = to_title_case(input("Invalid payment method. Enter again: "))

    if payment_method == 'Down Pay':
        down_payment = float(input("Enter the down payment amount: "))
    else:
        down_payment = 0.0

    claims = []
    while True:
        claim_number = input("Enter claim number (or 'done' to finish): ")
        if claim_number.lower() == 'done':
            break
        claim_date = input("Enter claim date (YYYY-MM-DD): ")
        claim_amount = float(input("Enter claim amount: "))
        claims.append((claim_number, claim_date, claim_amount))

    total_premium = calculate_premium(num_cars, liability, glass, loaner, constants)
    hst, total_cost = calculate_hst_and_total(total_premium, hst_rate)

    if payment_method == 'Monthly':
        monthly_payment = (total_cost + processing_fee) / 8
    elif payment_method == 'Down Pay':
        monthly_payment = (total_cost - down_payment + processing_fee) / 8
    else:
        monthly_payment = 0

    invoice_date = datetime.date.today()
    first_payment_date = invoice_date.replace(day=1) + datetime.timedelta(days=32)
    first_payment_date = first_payment_date.replace(day=1)

    print("\n--- Receipt ---")
    print(f"Policy Number: {next_policy_number}")
    print(f"Customer: {first_name} {last_name}")
    print(f"Address: {address}, {city}, {province}, {postal_code}")
    print(f"Phone: {phone_number}")
    print(f"Number of cars: {num_cars}")
    print(f"Extra liability coverage: {liability}")
    print(f"Glass coverage: {glass}")
    print(f"Loaner car coverage: {loaner}")
    print(f"Payment method: {payment_method}")
    print(f"Basic Premium: {format_currency(float(constants[1]))}")
    print(f"Total Premium: {format_currency(total_premium)}")
    print(f"HST: {format_currency(hst)}")
    print(f"Total Cost: {format_currency(total_cost)}")
    if payment_method != 'Full':
        print(f"Monthly Payment: {format_currency(monthly_payment)}")
    print(f"Invoice Date: {invoice_date}")
    print(f"First Payment Date: {first_payment_date}")

    print("\nPrevious Claims:")
    print("Claim #  Claim Date  Amount")
    print("-" * 30)
    for claim in claims:
        print(f"{claim[0]:<8} {claim[1]:<12} {format_currency(claim[2])}")

    print("\nSaving policy data...")

    time.sleep(1)  # Simulate saving data

    with open('policy_data.txt', 'a') as file:
        file.write(f"{next_policy_number},{first_name},{last_name},{address},{city},{province},{postal_code},{phone_number},{num_cars},{liability},{glass},{loaner},{payment_method},{total_premium}\n")

    print("Policy data saved successfully.")
    next_policy_number += 1

def main():
    while True:
        process_customer()
        more_customers = input("Do you want to enter another customer? (Y/N): ").upper()
        if more_customers != 'Y':
            break

if __name__ == "__main__":
    main()