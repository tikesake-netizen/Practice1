def show_numbers(*args):
    print(args)


def show_person(**kwargs):
    print(kwargs)


show_numbers(1, 2, 3, 4)
show_person(name="Alex", age=18, country="Kazakhstan")