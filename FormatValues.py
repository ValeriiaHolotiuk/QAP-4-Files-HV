# FormatValues.py

def to_title_case(value):
    return value.title()

def to_upper_case(value):
    return value.upper()

def format_currency(value):
    return f"${value:,.2f}"

def format_percentage(value):
    return f"{value * 100:.2f}%"

# New function to calculate HST and total cost
def calculate_hst_and_total(premium, hst_rate):
    hst = premium * hst_rate
    total = premium + hst
    return hst, total