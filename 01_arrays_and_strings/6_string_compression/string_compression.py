"""
Implement a method to perform basic string compression using the counts of
repeated characters. If the "compressed" string would not become smaller
than the original string, your method should return the original string.
You can assume the string has ony uppercase and lowercase letters(a-z).
"""


def compress(orig_str):
    """
    Runtime is O(p + k^2), where p is the size of the original string,
    and k is the number of character sequences. It's slow because string
    concatenation is O(n^2) time.
    """

    str_len = len(orig_str)

    letter = None
    count = 1
    comp_str = ''

    for char in orig_str:
        if letter is None:
            letter = char
        elif letter is char:
            count += 1
        else:
            append = letter + str(count)
            comp_str += append

            letter = char
            count = 1

    # after the for loop is done, append the last set
    append = letter + str(count)
    comp_str += append

    if str_len < len(comp_str):
        return orig_str
    else:
        return comp_str





