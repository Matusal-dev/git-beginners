def calculate_health(health, damage):
    remaining_health = health - damage

    if remaining_health < 0:
        return 0
    else:
        return remaining_health


assert calculate_health(100, 20) == 80
assert calculate_health(50, 30) == 20
assert calculate_health(30, 50) == 0
assert calculate_health(100, 0) == 100

print("All 4 tests passed!")
