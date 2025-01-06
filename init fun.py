class laptop:


    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("configurations are " , self.cpu , self.ram)


com1 = laptop('i5',16)
com2 = laptop('Ryzen 3' , 8)

com1.config()
com2.config()