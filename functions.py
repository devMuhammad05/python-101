def greet(first_name, last_name):
    print("Hi there")
    print(f"Welcome aboard {first_name} {last_name}")

greet("Muhammad", "Yahaya")


def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Starman")
print(message)


def increment(number, by):
    return number + by

result = increment(2, by=5)
print(result)