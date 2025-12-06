# We need to find the largest digit (excluding last digit)
# We then need to look for largest digit that comes after the first largest digit

banks = [line.strip() for line in open("input.txt", "r").readlines()]

total_joltage = 0
bank_batteries = 12


def find_max_digit(bank, start, end):
    max_digit = 0
    max_digit_idx = 0

    for i in range(start, end):
        if int(bank[i]) > max_digit:
            max_digit = int(bank[i])
            max_digit_idx = i

    return (max_digit, max_digit_idx + 1)


def get_max_joltage(bank):
    stack = []

    batteries_remaining = len(bank) - bank_batteries

    for digit in bank:
        while stack and stack[-1] < digit and batteries_remaining > 0:
            stack.pop()
            batteries_remaining -= 1

        stack.append(digit)

    return int("".join(stack[:bank_batteries]))


for bank in banks:
    max_joltage = 0
    start = 0

    for i in range(1, bank_batteries + 1):
        end = len(bank) - (bank_batteries - i)

        digit, start = find_max_digit(bank, start, end)

        max_joltage += digit * (10 ** (bank_batteries - i))

    total_joltage += max_joltage

print(f"Total joltage: {total_joltage}")

total_joltage = 0

# Montonic stack approach
for bank in banks:
    total_joltage += get_max_joltage(bank)


print(f"Total joltage: {total_joltage}")
