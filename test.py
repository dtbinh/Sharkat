from ps6_utils import Position
from ps6_room import RectangularRoom
from ps6 import Robot, StandardRobot, RandomWalkRobot

from test_robot_movement import testRobotMovement

testRobotMovement(RandomWalkRobot, RectangularRoom)

# from Tkinter import *
# from PIL import Image, ImageTk

# # Initialize a drawing surface
# master = Tk()
# w = Canvas(master, width=500, height=500)
# w.pack()
# master.update()


# image = Image.open("sharkat_small.jpg")
# photo = ImageTk.PhotoImage(image)
# print photo.height(), photo.width()

# w.create_image(0 + photo.width()/2, 0 + photo.height()/2, image = photo)
# w.pack()
# master.update()

# while (True):
# 	pass