def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    for i in range(len(list1)):
        list1[i] = list1[i].capitalize()
    return list1


print(main(['rustam', 'diyor', 'alisher', 'bektosh']))
