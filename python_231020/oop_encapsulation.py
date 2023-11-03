class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_perimeter(self):
        return 2 * (self.__get_width_plus_height__())
    def __get_width_plus_height__(self): # __이 앞뒤로 붙어서 private method가 된다.
        return self.width + self.height
    
rect1 = Rectangle(3, 4) # 14
rect2 = Rectangle(5, 3) # 16

rect1_peri = rect1.get_perimeter()
rect2_peri = rect2.get_perimeter()

print(rect1_peri, rect2_peri)