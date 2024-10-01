class Budget:
    def __init__(self, cost, date):
        self.cost = float(cost) 
        self.date = date
        
    def __repr__(self):
        return f'Budget({self.cost}, {self.date})'