def length_of_longest_substring_k_distinct(s: str, k: int) -> tuple:
    if k == 0:
        return 0, []

    n = len(s)
    left = 0
    right = 0
    max_length = 0
    max_substrings = []
    char_count = {}

    while right < n:
        # Add current character to the window
        if s[right] in char_count:
            char_count[s[right]] += 1
        else:
            char_count[s[right]] = 1

        # If the window contains more than k distinct characters, shrink it from the left
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        # Calculate the length of the current window
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            max_substrings = [s[left:right+1]]
        elif current_length == max_length:
            max_substrings.append(s[left:right+1])

        # Expand the window to the right
        right += 1

    return max_length, max_substrings

s1 = "eceba"
k1 = 2
print(length_of_longest_substring_k_distinct(s1, k1))  # เอาต์พุต: (3, ['ece'])

s2 = "aa"
k2 = 1
print(length_of_longest_substring_k_distinct(s2, k2))  # เอาต์พุต: (2, ['aa'])

s3 = "a"
k3 = 2
print(length_of_longest_substring_k_distinct(s3, k3))  # เอาต์พุต: (1, ['a'])

s4 = "abcadcacacaca"
k4 = 3
print(length_of_longest_substring_k_distinct(s4, k4))  # เอาต์พุต: (11, ['cadcacacaca'])