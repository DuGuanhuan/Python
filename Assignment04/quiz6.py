class Player:
    def __init__(self, name, number, height, dob, position):
        self.name = name
        self.number = number
        self.height = height
        self.dob = dob
        self.position = position

    def __str__(self):
        return f'Player[name="{self.name}", number="{self.number}", height="{self.height}", dob="{self.dob}", position="{self.position}"]'

# Test the implementation
playerObj1 = Player("Steven Gerrard", "8", "183 cm", "30 May 1980", "Midfielder")
playerObj2 = Player("Michael Owen", "10/11", "1.73 m", "14 December 1979", "Striker")
print(playerObj1)
print(playerObj2)

playerObj3 = Player("Cristiano Ronaldo", "7", "1.87 m", "5 February 1985", "Forward")
playerObj4 = Player("Kylian Mbappé", "7", "1.78 m", "20 December 1998", "Forward")
print(playerObj3)
print(playerObj4)
