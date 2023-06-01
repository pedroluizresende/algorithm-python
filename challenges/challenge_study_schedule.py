def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    number_of_students = 0

    for start, end in permanence_period:
        if (
            start is None
            or not isinstance(start, int)
            or end is None
            or not isinstance(end, int)
        ):
            return None
        if start <= target_time <= end:
            number_of_students += 1

    return number_of_students


permanence_period = [
    (2, 2),
    (1, 2),
    (2, 3),
    (1, 5),
    (4, 5),
    (4, 5),
]

target_time1 = 5  # 3
target_time2 = 4  # 3
target_time3 = 3  # 2

# print(study_schedule(permanence_period), 0)  # None
print(study_schedule([(1, 2), (1, 3), (2, 3)], 2))
print(
    study_schedule(
        [(2, None), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), (6, 7)], 5
    )
)  # 2
print(study_schedule(permanence_period, target_time2))  # 3
# print(study_schedule(permanence_period, target_time3))  # 2
