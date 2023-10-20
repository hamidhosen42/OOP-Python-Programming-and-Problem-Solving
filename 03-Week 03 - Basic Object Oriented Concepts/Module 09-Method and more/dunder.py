# dunder
# special method

class Person:

    def __init__(self,name,age,money) -> None:
        self.name = name
        self.age = age
        self.money = money

    def __add__(self,other):
        # return self.money + other.money
        return self.age + other.age


alim = Person("Hamid",12,4500)
dalim = Person("Dalim",16,715)

print(alim + dalim)

print(type(alim))

print(alim.name + dalim.name)
print(alim.age , dalim.age)
print(alim.money , dalim.money)


class my_defaultdict(dict):
    def __init__(self, default_factory, **kwargs):
        super().__init__(**kwargs)
        self.default_factory = default_factory

    def __missing__(self, key):
        """Populate the missing key and return its value."""
        self[key] = self.default_factory()
        return self[key]

olympic_medals = my_defaultdict(lambda: 0)  # Produce 0 by default
olympic_medals["Phelps"] = 28

print(olympic_medals["Phelps"])  # 28
print(olympic_medals["me"])  # 0