class Bus:
    def __init__(self, Route, Company, Plate):
        self.Route = Route
        self.Company = Company
        self.Plate = Plate
    
    def printBus(self):
        print(f"Route: {self.Route}")
        print(f"Company: {self.Company}")
        print(f"Plate: {self.Plate}")

# TEST
# busObj1 = Bus("55A", "Premier Illawarra", "7440MO")
# busObj1.printBus()
