from typing import List

def get_prime_number(lower: int, upper: int) -> List:
    """
    This function gets all the prime numbers within an interval.

    Args:
        lower: lower bound of the interval.
        upper: upper bound of the interval.

    Returns:
        prime_number_list: the prime numbers within an interval.
    """
    # Python program to display all the prime numbers within an interval
    print(f'Prime numbers between {lower} and {upper} are: ')
    prime_number_list = []
    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            prime_number_list.append(num)
    return prime_number_list
