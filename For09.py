def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    result = []

    for i in range(1, 11):
        result += [i * price]
    return result


print(main(2.25))
