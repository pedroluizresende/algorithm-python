def is_anagram(first_string, second_string):
    word_1 = list(first_string.lower())
    merge_sort(word_1)
    word_2 = list(second_string.lower())
    merge_sort(word_2)
    result = ("".join(word_1), "".join(word_2), (word_1 == word_2))
    if len(word_1) <= 0 or len(word_2) <= 0:
        result = ("".join(word_1), "".join(word_2), False)
    return result


def merge_sort(caracters, start=0, end=None):
    if end is None:
        end = len(caracters)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(caracters, start, mid)
        merge_sort(caracters, mid, end)
        merge(caracters, start, mid, end)


def merge(caracters, start, mid, end):
    left = caracters[start:mid]
    right = caracters[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            caracters[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            caracters[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            caracters[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            caracters[general_index] = right[right_index]
            right_index = right_index + 1


first_string_1 = "amor"
second_string_1 = "roMa"

first_string_2 = "Coxinha"
second_string_2 = "empadinha"

print(is_anagram(first_string_1, second_string_1))
print(is_anagram(first_string_2, second_string_2))
