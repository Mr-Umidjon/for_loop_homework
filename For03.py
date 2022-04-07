def main(k, n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    ans = []

    for _ in range(n):
        ans.append(k)
    return ans


print(main(5, 3))
