from functools import reduce

# Sample data
num = 4
str_input = "Hello"
nums_list = [1, 2, 3, 4, 5, 6, -7, -8]
strings_list = ["apple", "Orange", "banana", "umbrella", "Elephant", "Ink", "cat"]

# 1
square = lambda x: x ** 2
print("1:", square(num))

# 2
strlen = lambda s: len(s)
print("2:", strlen(str_input))

# 3
add = lambda a, b: a + b
print("3:", add(5, 7))

# 4
average = lambda lst: sum(lst) / len(lst)
print("4:", average(nums_list))

# 5
to_upper = lambda s: s.upper()
print("5:", to_upper("hello"))

# 6
longest = lambda lst: max(lst, key=len)
print("6:", longest(strings_list))

# 7
is_even = lambda x: x % 2 == 0
print("7:", is_even(4))

# 8
largest = lambda lst: max(lst)
print("8:", largest(nums_list))

# 9
to_lower = lambda s: s.lower()
print("9:", to_lower("HELLO"))

# 10
shortest = lambda lst: min(lst, key=len)
print("10:", shortest(strings_list))

# 11
even_numbers = list(filter(lambda x: x % 2 == 0, nums_list))
print("11:", even_numbers)

# 12
vowels = 'aeiou'
start_with_vowel = list(filter(lambda s: s[0].lower() in vowels, strings_list))
print("12:", start_with_vowel)

# 13
non_negative = list(filter(lambda x: x >= 0, nums_list))
print("13:", non_negative)

# 14
squared_nums = list(map(lambda x: x ** 2, nums_list))
print("14:", squared_nums)

# 15
upper_strings = list(map(lambda s: s.upper(), strings_list))
print("15:", upper_strings)

# 16
add_two = list(map(lambda x: x + 2, nums_list))
print("16:", add_two)

# 17
sum_all = reduce(lambda x, y: x + y, nums_list)
print("17:", sum_all)

# 18
multiply_all = reduce(lambda x, y: x * y, nums_list)
print("18:", multiply_all)

# 19
max_value = reduce(lambda x, y: x if x > y else y, nums_list)
print("19:", max_value)

# 20
even_square = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums_list)))
print("20:", even_square)

# 21
sum_of_squares = reduce(lambda x, y: x + y, map(lambda x: x ** 2, nums_list))
print("21:", sum_of_squares)

# 22
max_len_vowel = reduce(
    lambda x, y: x if x > y else y,
    map(lambda s: len(s), filter(lambda s: s[0].lower() in vowels, strings_list))
)
print("22:", max_len_vowel)
