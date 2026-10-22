"""Business rules and calculations for software license orders."""

def calculate_license_cost(seat_price: float, seats: int) -> float: 
    """Returns the license cost before any discount"""
    return seat_price * seats

def get_seat_discount(seats: int, education: bool = False) -> float:
    """Returns the discount rate as a decimal"""
    if seats < 10:
        return 0.0
    else:
        if seats < 50:
            discount = 0.07
        else: 
            if education:
                discount = 0.16
            else:
                discount = 0.07
        return discount

def calculate_license_total(seat_price: float, seats: int, education: bool = False) -> float:
    """Returns the license total for one order: the discounted cost, plus the onboarding fee when it applies"""
    cost = calculate_license_cost(seat_price, seats)
    discount_rate = get_seat_discount(seats, education)
    discounted_cost = cost * (1 - discount_rate)

    if discounted_cost < 50.0:
        discounted_cost += 25.0

    return discounted_cost

def needs_contract_review(total: float) -> bool:
    """Reterns Ture when the license total needs a contract review, otherwise False"""
    return total > 300.0

def gets_trainer(seats: int, total: float) -> bool: 
    """Returns Ture when the order gets a dedicated trainer, otherwise False"""
    return seats > 50 or total > 400.0

def total_licensed(orders: list) ->float:
    """Returns the sum of the license totals for every order in the list"""
    sum_total = 0.0
    for order in orders:
        sum_total += calculate_license_total(order["seat_price"], order["seats"], order["education"])
    return sum_total

def largest_license( orders: list) -> str:
    """Returns the company of the order with the largest license total"""
    if not orders:
        return ""

    largest_company = ""
    max_total = -1.0

    for order in orders:
        company = order["company"]
        seat_price = order["seat_price"]
        seats = order["seats"]
        education = order["education"]
        
        total = calculate_license_total(seat_price, seats, education)
        if total > max_total:
            max_total = total
            max_company = company
            
    return max_company

    return largest_company

def format_license_line(company: str, total: float, contract_review: bool, trainer: bool) -> str:
    """Returns one line of the report with two decimal places and yes/no values."""
    cr_str = "yes" if contract_review else "no"
    tr_str = "yes" if trainer else "no"
    return f"{company}: ${total:.2f} | contract review: {cr_str} | trainer {tr_str}"


    


    

