# Python Scope: LEGB rule
# Python looks up names in this order:
#   L - Local      (inside the current function)
#   E - Enclosing  (inside outer functions, for nested functions)
#   G - Global     (top level of the module)
#   B - Built-in   (names Python provides, like print, len)

# ---------- Global scope ----------
enemies = 1


def increase_enemies():
    # Local scope: this 'enemies' is a different variable from the global one
    enemies = 2
    print(f"Inside function: enemies = {enemies}")


increase_enemies()
print(f"Outside function: enemies = {enemies}")  # still 1

print("-" * 40)

# ---------- Local scope ----------
def drink_potion():
    potion_strength = 2  # only exists inside this function
    print(f"Potion strength inside: {potion_strength}")


drink_potion()
# print(potion_strength)  # NameError: not defined outside the function

print("-" * 40)

# ---------- Reading vs modifying a global ----------
player_health = 10


def read_health():
    # Reading a global works without any special keyword
    print(f"Reading global health: {player_health}")


def reset_health_wrong():
    # Assigning creates a NEW local variable; the global is untouched
    player_health = 100
    print(f"Local health: {player_health}")


def reset_health_right():
    # 'global' tells Python to use the module-level variable
    global player_health
    player_health = 100
    print(f"Global health changed to: {player_health}")


read_health()
reset_health_wrong()
print(f"Global after wrong reset: {player_health}")  # still 10
reset_health_right()
print(f"Global after right reset: {player_health}")  # now 100

print("-" * 40)

# ---------- Enclosing scope (nested functions) ----------
def outer():
    message = "from outer"

    def inner():
        # inner can read 'message' from the enclosing function
        print(f"inner sees: {message}")

    inner()


outer()


def counter():
    count = 0

    def increment():
        # 'nonlocal' lets inner modify the enclosing variable
        nonlocal count
        count += 1
        return count

    print(increment())
    print(increment())
    print(increment())


counter()

print("-" * 40)

# ---------- No block scope in Python ----------
# Unlike many languages, if/for/while do NOT create a new scope.
if 3 > 1:
    game_level = 3
    new_enemies = ["Skeleton", "Zombie", "Alien"]

print(f"Still accessible after the if block: level {game_level}, {new_enemies}")

for i in range(3):
    loop_var = i

print(f"Loop variables leak out too: i = {i}, loop_var = {loop_var}")


def create_enemy():
    # But a function DOES create a scope
    boss = "Dragon"


create_enemy()
# print(boss)  # NameError

print("-" * 40)

# ---------- Built-in scope ----------
print(len("scope"))  # 'len' lives in the built-in scope


# Shadowing a built-in is legal but a bad idea:
def shadow_demo():
    len = 5  # hides the built-in len inside this function only
    print(f"Local 'len' is just a number: {len}")


shadow_demo()
print(len("still works outside"))

print("-" * 40)

# ---------- Global constants ----------
# Convention: UPPER_CASE names for globals that never change
PI = 3.14159


def circle_area(radius):
    return PI * radius**2


print(f"Area of circle with radius 2: {circle_area(2)}")
