print("THIS IS ALSO BASED ON MULTIPLE INHERITANCE")
class dad:
    basketball = 1

class son(dad):
    dance = 1
    def classical_dance(self):
        return f"Yes! I dance {self.dance} no of times"

class grandson(son):
    dance = 6
    def classical_dance(self):
         return f"Jackson Yeah!" \
                 f"Yesss I dance in an awesome manner {self.dance} no of times"

darry = dad()
larry = son()
harry = grandson()

print(harry.classical_dance())
print(harry.basketball)



print("THIS IS MY PRACTICE")

class electronic_device:
    games = 4

class pocket_gadjet(electronic_device):
    games = 10
    def more_games(self):
        return f"yooo! I have {self.games} games with me...."


class phone(pocket_gadjet):
    games = 15
    def more_games(self):
        return f"yeahh! I have {self.games} games with me!"


vivo = electronic_device()
oppo = pocket_gadjet()
realme = phone()

print(realme.more_games())
print(oppo.more_games())
