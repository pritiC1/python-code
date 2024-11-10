class owner():
    def product(self):
        print("our product")

class sales_man(owner):
    def launch(self):
        print("New product")

class customer(sales_man):
    def new(self):
        print("new one added")

c1=customer()
c1.product()
c1.launch()
c1.new()



 