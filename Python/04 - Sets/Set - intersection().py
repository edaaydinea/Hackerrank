number_of_students_english = int(input())
roll_numbers_english = set(map(int, input().split()))

number_of_students_french = int(input())
roll_numbers_french = set(map(int, input().split()))

at_least_one_subscription = roll_numbers_english.intersection(roll_numbers_french)
print(len(at_least_one_subscription))
