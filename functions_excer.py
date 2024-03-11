
def find_area(base, height, shape='triangle'):
    if shape == 'triangle':
        return 0.5*base*height
    elif shape == 'rectangle':
        return base*height
    else:
        print("Invalid shape type: So taking triangle as default shape")
        return 0.5*base*height

def print_pattern(num):
    for i in range(1, num+1):
        print("* "*i)


if __name__ == '__main__':
    print("Enter the width: ")
    base = float(input())
    print("Enter the height: ")
    height = float(input())
    print("Enter the shape")
    shape = str(input())
    print("Enter pattern number: ")
    pattern_number = int(input())
    area = find_area(base, height, shape)
    print_pattern(pattern_number)
    print(area)