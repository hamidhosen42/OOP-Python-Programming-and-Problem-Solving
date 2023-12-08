
# !All about mankind

class Human:
    def __init__(self,gender,height,weight):
        self.gender = gender
        self.height = height
        self.weight = weight

class Police(Human):
    def __init__(self, gender, height, weight):
        super().__init__(gender, height, weight)

    def __init__(self,cases,nationality,gender, height, weight):
        super().__init__(gender, height, weight)
        self.cases = cases
        self.nationality = nationality

class CsEngineer(Human):
    def __init__(self,love_to_code,has_gf, gender, height, weight):
        super().__init__(gender, height, weight)
        self.love_to_code = love_to_code
        self.has_gf =has_gf

if __name__ == '__main__':
    police = Police(True,"Bangladesh","Male",23,45)
    print(police.height)

    print("---------------------------------")

    eng = CsEngineer(True,False,'Male',"84","64")
    print(eng.has_gf)