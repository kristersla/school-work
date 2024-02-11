
class CSDD:
    def __init__(self, mark, model, reg_num, full_weight, fuel_type):
        self.mark = mark
        self.model = model
        self.reg_num = reg_num
        self.full_weight = full_weight
        self.fuel_type = fuel_type
    
    def print(self):
        print(f"zimols: {car.mark}")
        print(f"modelis: {car.model}")
        print(f"registracijas datums: {car.reg_num}")
        print(f"pilna masa: {car.full_weight}")
        print(f"degvielas veids: {car.fuel_type}")

car = CSDD("BMW","E92","SH-1094","1800","benzins")

car.print()