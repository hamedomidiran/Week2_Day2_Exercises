def square_footage():
    length = int(input('What is the lenght of the house?   '))
    width  = int(input('What is the width of the house?    '))
    unit  = input('What is the unit of measurement?   ')

    square_footage = length * width
    print(f'The square footage of the house is {square_footage:.2f} {unit}^2')


def circumference():
    radius = int(input('What is the radius of the circle?   '))
    unit  = input('What is the unit of measurement?    ')
    

    circumference = 2*3.14*radius
    
    print(f'The circumference of the circle is {circumference:.2f} {unit}')