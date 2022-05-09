import replit
from misc.prime_number import get_prime_number


def run_test_case():
    replit.clear()
    lower = 1
    upper = 100
    prime_number_list = get_prime_number(lower, upper)
    print(prime_number_list)
