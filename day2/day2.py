# There are ranges of numbers. Within these ranges, we need to find any number 
# that is entirely comprised of a repeating sequence. Print the sum of all these numbers.

file = open('input.txt', 'r')
line = file.readline().strip()

num_ranges = line.split(',')

invalid_nums = []

for num_range in num_ranges:
    start, end = num_range.split('-')

    for num in range(int(start), int(end) + 1):
        num_str = str(num)

        if (num_str * 2).find(num_str, 1) != len(num_str):
            invalid_nums.append(num)

print(sum(invalid_nums))

