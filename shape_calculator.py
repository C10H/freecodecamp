class Rectangle:
    def __init__(self,width,height):
        # 使用width和height属性对Rectangle对象进行初始化
        self.width = width
        self.height = height
    def set_width(self,width):
        self.width = width
    def set_height(self,height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture"
        str = ''
        for i in range(self.height):
            str += '*' * self.width + '\n'
        return str
    def get_amount_inside(self,square:object):
        if self.width < square.width:
            return 0
        if self.height < square.height:
            return 0
        return (self.width // square.width) * (self.height // square.height)
    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width,self.height)

class Square(Rectangle):
    def __init__(self,side_length):
        # 使用side_length属性对Rectangle对象进行初始化
        self.width = side_length
        self.height = side_length
    def set_side(self,side_length):
        self.width = side_length
        self.height = side_length
    def __str__(self):
        return 'Square(side={})'.format(self.width)


