def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    ans = ''
    for i in range(n):
        ans += str(i) + ","
    return ans[:-1]


print(main(5))
