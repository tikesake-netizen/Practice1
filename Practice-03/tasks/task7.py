def grams_to_ounces(grams):
    return grams / 28.3405231


grams = float(input("Enter grams: "))

ounces = grams_to_ounces(grams)

print("Ounces:", ounces)