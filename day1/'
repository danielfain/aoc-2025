file = open("input.txt", "r")

password = 0
dial_position = 50
total_positions = 100

for line in file.readlines():
    direction = line[:1]
    distance = int(line[1:].strip())

    if distance > total_positions:
        password += distance // total_positions
        distance %= total_positions

    if direction == "L":
        new_position = dial_position - distance
    else:
        new_position = dial_position + distance

    if dial_position != 0 and (new_position >= total_positions or new_position <= 0):
        password += 1

    if new_position >= total_positions:
        new_position -= total_positions
    elif new_position < 0:
        new_position += total_positions

    dial_position = new_position


print(f"Password is {password}")
