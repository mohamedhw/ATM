class Card:
    def __init__(self, number, pin, total):
        self.number = number
        self.pin = pin
        self.total = total

    def get_total(self):
        return self.total
    
    def get_number(self):
        return self.number
    
    def get_pin(self):
        return self.pin
    
    def set_total(self, val1):
        self.total = val1
