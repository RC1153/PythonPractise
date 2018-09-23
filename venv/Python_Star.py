from turtle import *


def draw_star(length,angle):
    count = 1
    while count <= 5:
        forward(length)
        right(angle)
        count += 1

def draw_tree():
    left(90)
    forward(100)
    right(45)
    forward(100)




def main():

    draw_tree()
    exitonclick()


if __name__=='__main__':
    main()

