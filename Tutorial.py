class human:
    def __init__(self,height):
        self.height = height

    def initialize_head(self):
        print("head initialized")

    def initialize_body(self):
        print("body initialized")

class female(human):
    def __init__(height):
        super().__init__(10)

    def initialize_long_hair(self):
        print("female was created with a height",self.height)

Shades = female()
Shades.initialize_head()
Shades.initialize_body()
Shades.initialize_long_hair()
