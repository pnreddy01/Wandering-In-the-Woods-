from tkinter import *
import random
import tkinter as tk
import pygame


def mov():
    global p1_x, p1_y ,p2_x, p2_y,p3_x, p3_y, p4_y,p4_x, num_moves,grid_size
    direction = random.choice([1, 2, 3, 4])
    cor1 = my_canvas.bbox(cir1)


    if direction == 1:  # left

        if (cor1[0] - 10 > 0  and cor1[0]-10 < grid_size-10):
            x = -10
            y = 0
            my_canvas.move(cir1, x, y)
    if direction == 2:  # right
        if (cor1[0] + 10 < grid_size-10 and cor1[0]+10>0 ):
            x = 10
            y = 0
            my_canvas.move(cir1, x, y)
    if direction == 3:  # up
        if (cor1[1] - 10 < grid_size-10  and cor1[1] -10 >0):
            x = 0
            y = -10
            my_canvas.move(cir1, x, y)
    if direction == 4:  # Right
        if (cor1[1] + 10 < grid_size-10 and   cor1[1] +10>0):
            x = 0
            y = 10
            my_canvas.move(cir1, x, y)
    direction = random.choice([1, 2, 3, 4])
    cor2 = my_canvas.bbox(cir2)

    if direction == 1:  # left

        if (cor2[0] - 10 > 0  and cor2[0]-10 <= grid_size-10):
            x = -10
            y = 0
            my_canvas.move(cir2, x, y)
    if direction == 2:  # right
        if (cor2[0] + 10 <= grid_size-10 and cor2[0]+10>0):
            x = 10
            y = 0
            my_canvas.move(cir2, x, y)
    if direction == 3:  # up
        if (cor2[1] - 10 <= grid_size-10 and cor2[1] -10 >0):
            x = 0
            y = -10
            my_canvas.move(cir2, x, y)
    if direction == 4:  # down
        if (cor2[1] + 10 <= grid_size-10 and   cor2[1] +10>0):
            x = 0
            y = 10
            my_canvas.move(cir2, x, y)


    if((cor1[0] != cor2[0]) and cor1[1]!=cor2[1]):
        num_moves+=1
        root.after(100, mov)
        pygame.mixer.music.load("game_mix.mp3")
        pygame.mixer.music.play(loops=0)
    else:
        my_canvas.delete(cir1)
        pygame.mixer.music.stop()
        img = PhotoImage(file="c:\\Users\\pnith\\PycharmProjects\\pythonProject\\ghost_one.png")
        my_canvas.create_image(0, 0, anchor=NW, image=img)
        pygame.mixer.music.play(loops=0, fade_ms=20)

        pygame.mixer.music.stop()

        print(num_moves)
def mov1():
    global p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_y, p4_x, num_moves, grid_size,width,height, num_people
    global first,second, third

    direction = random.choice([1, 2, 3, 4])
    cor1 = my_canvas.bbox(cir1)

    if direction == 1:  # left

        if (cor1[0] - 10 > 0 and cor1[0] - 10 < width - 10):
            x = -10
            y = 0
            my_canvas.move(cir1, x, y)
            num_moves += 1
    if direction == 2:  # right
        if (cor1[0] + 10 < width - 10 and cor1[0] + 10 > 0):
            x = 10
            y = 0
            my_canvas.move(cir1, x, y)
    if direction == 3:  # up
        if (cor1[1] - 10 < height - 10 and cor1[1] - 10 > 0):
            x = 0
            y = -10
            my_canvas.move(cir1, x, y)
    if direction == 4:  # Right
        if (cor1[1] + 10 < height - 10 and cor1[1] + 10 > 0):
            x = 0
            y = 10
            my_canvas.move(cir1, x, y)
    direction = random.choice([1, 2, 3, 4])
    cor2 = my_canvas.bbox(cir2)

    if direction == 1:  # left

        if (cor2[0] - 10 > 0 and cor2[0] - 10 <= width - 10):
            x = -10
            y = 0
            my_canvas.move(cir2, x, y)
    if direction == 2:  # right
        if (cor2[0] + 10 <= width - 10 and cor2[0] + 10 > 0):
            x = 10
            y = 0
            my_canvas.move(cir2, x, y)
    if direction == 3:  # up
        if (cor2[1] - 10 <= height - 10 and cor2[1] - 10 > 0):
            x = 0
            y = -10
            my_canvas.move(cir2, x, y)
    if direction == 4:  # down
        if (cor2[1] + 10 <= height - 10 and cor2[1] + 10 > 0):
            x = 0
            y = 10
            my_canvas.move(cir2, x, y)
    if ((cor1[0] != cor2[0]) and cor1[1] != cor2[1]):
        num_moves+=1
        root.after(100, mov1)
        pygame.mixer.music.load("game_mix.mp3")
        pygame.mixer.music.play(loops=0)
    else:
        my_canvas.delete(cir1)
        pygame.mixer.music.stop()
        img = PhotoImage(file="c:\\Users\\pnith\\PycharmProjects\\pythonProject\\ghost_one.png")
        my_canvas.create_image(0, 0, anchor=NW, image=img)
        pygame.mixer.music.play(loops=0, fade_ms=20)

        pygame.mixer.music.stop()
        print(num_moves)

def mov2():
    global p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_y, p4_x, num_moves, grid_size, width, height, num_people
    global first, second, third
    if(first== "True"):
        direction = random.choice([1, 2, 3, 4])
        cor1 = my_canvas.bbox(cir1)

        if direction == 1:  # left

            if (cor1[0] - 10 > 0 and cor1[0] - 10 < width - 10):
                num_moves += 1
                x = -10
                y = 0
                my_canvas.move(cir1, x, y)
                num_moves += 1
        if direction == 2:  # right
            if (cor1[0] + 10 < width - 10 and cor1[0] + 10 > 0):
                x = 10
                y = 0
                my_canvas.move(cir1, x, y)
                num_moves += 1
        if direction == 3:  # up
            if (cor1[1] - 10 < height - 10 and cor1[1] - 10 > 0):
                x = 0
                y = -10
                my_canvas.move(cir1, x, y)
                num_moves += 1
        if direction == 4:  # Right
            if (cor1[1] + 10 < height - 10 and cor1[1] + 10 > 0):
                x = 0
                y = 10
                my_canvas.move(cir1, x, y)
                num_moves += 1
    if(second=="True"):
        direction = random.choice([1, 2, 3, 4])
        cor2 = my_canvas.bbox(cir2)

        if direction == 1:  # left

            if (cor2[0] - 10 > 0 and cor2[0] - 10 <= width - 10):
                num_moves += 1
                x = -10
                y = 0
                my_canvas.move(cir2, x, y)
                num_moves += 1
        if direction == 2:  # right
            if (cor2[0] + 10 <= width - 10 and cor2[0] + 10 > 0):
                x = 10
                y = 0
                my_canvas.move(cir2, x, y)
                num_moves += 1
        if direction == 3:  # up
            if (cor2[1] - 10 <= height - 10 and cor2[1] - 10 > 0):
                x = 0
                y = -10
                my_canvas.move(cir2, x, y)
                num_moves += 1
        if direction == 4:  # down
            if (cor2[1] + 10 <= height - 10 and cor2[1] + 10 > 0):
                x = 0
                y = 10
                my_canvas.move(cir2, x, y)
                num_moves += 1
    if (third == "True"):
        if (num_people == 3):
            direction = random.choice([1, 2, 3, 4])
            cor3 = my_canvas.bbox(cir2)

            if direction == 1:  # left

                if (cor3[0] - 20 > 0 and cor3[0] - 20 <= width):
                    x = -20
                    y = 0
                    my_canvas.move(cir3, x, y)
            if direction == 2:  # right
                if (cor3[0] + 20 <= width and cor3[0] + 20 > 0):
                    x = 20
                    y = 0
                    my_canvas.move(cir3, x, y)
            if direction == 3:  # up
                if (cor3[1] - 20 <= height - 20 and cor3[1] - 20 > 0):
                    x = 0
                    y = -20
                    my_canvas.move(cir3, x, y)
            if direction == 4:  # down
                if (cor3[1] + 20 <= height + 20 and cor3[1] + 20 > 0):
                    x = 0
                    y = 20
                    my_canvas.move(cir3, x, y)
            cor3 = my_canvas.bbox(cir3)
    if (num_people == 4):
        direction = random.choice([1, 2, 3, 4])
        cor4 = my_canvas.bbox(cir2)

        if direction == 1:  # left

            if (cor4[0] - 20 > 0 and cor4[0] - 20 <= width - 20):
                num_moves += 1
                x = -20
                y = 0
                my_canvas.move(cir4, x, y)
        if direction == 2:  # right
            if (cor4[0] + 20 <= width - 10 and cor4[0] + 20 > 0):
                x = 20
                y = 0
                my_canvas.move(cir4, x, y)
        if direction == 3:  # up
            if (cor4[1] - 20 <= height - 20 and cor4[1] - 20 > 0):
                x = 0
                y = -20
                my_canvas.move(cir4, x, y)
        if direction == 4:  # down
            if (cor4[1] + 20 <= height - 20 and cor4[1] + 20 > 0):
                x = 0
                y = 20
                my_canvas.move(cir4, x, y)

        cor4 = my_canvas.bbox(cir4)
    cor2 = my_canvas.bbox(cir2)
    cor1 = my_canvas.bbox(cir1)

    if (num_people == 3):
        if (first == "True"):
            if (cor1[0] == cor2[0] and cor1[1] == cor2[1]):
                my_canvas.delete(cir1)
                first = "False"
        if ((first == "True") and (third == "True")):
            if (cor1[0] == cor3[0] and cor1[1] == cor3[1]):
                my_canvas.delete(cir1)
                first = "False"
        if (third == "True"):
            if (cor3[0] == cor2[0] and cor3[1] == cor2[1]):
                my_canvas.delete(cir3)
                third = "False"
        print(cor1, cor2, cor3)
        if (first == "True" and third == "True"):
            num_moves+=1
            root.after(100, mov1())
            pygame.mixer.music.play(loops=0, fade_ms=20)

            pygame.mixer.music.stop()
        else:
            my_canvas.delete(cir1)
            pygame.mixer.music.stop()
            img = PhotoImage(file="c:\\Users\\pnith\\PycharmProjects\\pythonProject\\ghost_one.png")
            my_canvas.create_image(0, 0, anchor=NW, image=img)
            pygame.mixer.music.play(loops=0, fade_ms=20)

            pygame.mixer.music.stop()


while 1:
    root = tk.Tk()
    root.geometry("500x500")
    K_2 = False
    pygame.mixer.init()
    global num_moves,num_people,first, second, third
    grades_3_5 = False
    grades_6_8 = False
    grade = int(input("Please enter your grade: "))
    if grade >= 0 and grade <= 2:
        K_2 = True
    elif grade >= 3 and grade <= 5:
        grades_3_5 = True
    elif grade >= 6 and grade <= 8:
        grades_6_8 = True
    if K_2:
        global grid_size
        grid_size = int(input("Please enter the size of the grid: "))
        global p1_x
        p1_x = 1
        global p1_y
        global p1_y
        p1_y = 1
        global p2_x
        p2_x = grid_size+1
        global p2_y
        p2_y = grid_size+1
        global num_moves
        num_moves = 0
        my_canvas = Canvas(root, width=700, heigh=700, bg="black")
        my_canvas.pack(pady=40)
        img=PhotoImage(file="c:\\Users\\pnith\\PycharmProjects\\pythonProject\\Screenshot (103).png")
        my_ima = my_canvas.create_image(0, 0,anchor = NW, image=img)
        cir2 = my_canvas.create_rectangle(p2_x, p2_y, p2_x + 10, p2_y + 10,fill='red')
        cir1 = my_canvas.create_rectangle(p1_x, p1_y, p1_x + 10, p1_y + 10,fill='blue')
        mov()
        root.mainloop()


    # For grades 3-5, students can set up the size of a grid, which can be rectangular
    elif grades_3_5:

        num_people=2
        first = "True"
        second = "True"
        third = "False"
        num_moves = 0
        width = int(input("Please enter the width of the grid: "))
        height = int(input("Please enter the height of the grid: "))
        p1_x = int(input("Please enter the x-coordinate of Person 1: "))
        p1_y = int(input("Please enter the y-coordinate of Person 1: "))
        p2_x = int(input("Please enter the x-coordinate of Person 2: "))
        p2_y = int(input("Please enter the y-coordinate of Person 2: "))
        my_canvas = Canvas(root, width=width, heigh=height, bg="white")
        my_canvas.pack(pady=40)
        img = PhotoImage(file="c:\\Users\\pnith\\PycharmProjects\\pythonProject\\Screenshot (103).png")
        my_ima = my_canvas.create_image(0, 0, anchor=NW, image=img)
        cir1 = my_canvas.create_rectangle(p1_x, p1_y, p1_x + 10, p1_y + 10, fill='red')
        cir2 = my_canvas.create_rectangle(p2_x, p2_y, p2_x + 10, p2_y + 10, fill='red')
        num_moves=0
        mov1()
        root.mainloop()
    # For grades 6-8, students can set up the size of a grid, which can be rectangular, and can include 2, 3, or 4 people
    elif grades_6_8:

        num_moves=0
        first = "True"
        second = "True"
        third = "True"
        width = int(input("Please enter the width of the grid: "))
        height = int(input("Please enter the height of the grid: "))
        num_people = int(input("Please enter the number of people: "))
        my_canvas = Canvas(root, width=width, heigh=height, bg="white")
        my_canvas.pack(pady=40)

        img = PhotoImage(file="c:\\Users\\pnith\\PycharmProjects\\pythonProject\\Screenshot (103).png")
        my_ima = my_canvas.create_image(0, 0, anchor=NW, image=img)
        p1_x = int(input("Please enter the x-coordinate of Person 1: "))
        p1_y = int(input("Please enter the y-coordinate of Person 1: "))

        if num_people > 2:
            p2_x = int(input("Please enter the x-coordinate of Person 2: "))
            p2_y = int(input("Please enter the y-coordinate of Person 2: "))

        if num_people >= 3:
            p3_x = int(input("Please enter the x-coordinate of Person 3: "))
            p3_y = int(input("Please enter the y-coordinate of Person 3: "))
            cir3 = my_canvas.create_rectangle(p3_x, p3_y, p3_x + 10, p3_y + 10,fill='green')

        if num_people == 4:
            p4_x = int(input("Please enter the x-coordinate of Person 4: "))
            p4_y = int(input("Please enter the y-coordinate of Person 4: "))
            cir4 = my_canvas.create_rectangle(p4_x, p4_y, p4_x + 10, p4_y + 10,fill = 'yellow')


        cir1 = my_canvas.create_rectangle(p1_x, p1_y, p1_x + 10, p1_y + 10,fill = 'red')
        cir2 = my_canvas.create_rectangle(p2_x, p2_y, p2_x + 10, p2_y + 10,fill ='blue')
        mov2()
        root.mainloop()
    num_moves = 0
    s1=input("enter yes to start again else no ")
    if(s1 == "no"):
        break




