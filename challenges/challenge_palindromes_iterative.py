def is_palindrome_iterative(word):
    if word == "":
        return False
    end = len(word) - 1
    # start = 0

    for index in range(len(word)):
        if index >= end:
            return True
        curr_char = word[index]
        last_char = word[end]
        if curr_char != last_char:
            return False
        end -= 1


print(is_palindrome_iterative("i"))
