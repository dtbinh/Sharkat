from ps6 import Position
from ps6 import RectangularRoom
from ps6 import Robot
from ps6 import StandardRobot
from ps6 import runSimulation
from ps6 import RandomWalkRobot

p = Position(2.1,5.4)
print p.getX()
print p.getY()

r = RectangularRoom(5, 6)

#print r.getNumCleanedTiles()


d = RandomWalkRobot(r, 5)
#print d.getRobotPosition()

g = Position(3,4)
#print g
#d.setRobotPosition(g)
#print d.getRobotPosition()


s = StandardRobot(r, 3)


print runSimulation(1, 1, 10, 10, 1, 100, StandardRobot)
