people = [
    {"name": "foo", "age": 12},
    {"name": "bar", "age": 34},
    {"name": "boo", "age": 99}
]


# def f(person):
#   return person["name"]


people.sort(key=lambda person: person["name"])
print(people)
