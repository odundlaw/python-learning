class Flight():
    def __init__(self, capacity):
        self.capacity = capacity;
        self.passangers = [];
    
    def add_passangers(self, name):
        if not self.available_seats():
            return False;
        self.passangers.append(name);
        return True

    def available_seats(self):
        return self.capacity - len(self.passangers);

    def remove_passangers(self, name):
        self.passangers.remove(name);

flight = Flight(3);

names = ["odunayo", "Lekan", "Adebayo", "Olalekan"];

for name in names:
    if flight.add_passangers(name):
        print(f"passanger {name} was added successfully");
    else: 
        print(f"No available seat for {name} at the moment");

print(flight.passangers);