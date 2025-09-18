import math

a = float(input("Введіть довжину сторони основи a: "))
h = float(input("Введіть висоту піраміди h: "))

S_base = (3 * math.sqrt(3) / 2) * a**2

r = (a * math.sqrt(3)) / 2

l = math.sqrt(h**2 + r**2)

S_side = 0.5 * a * l

V = (1/3) * S_base * h

print(f"Площа основи: {S_base}")
print(f"Площа однієї бічної грані: {S_side}")
print(f"Об'єм піраміди: {V}")
