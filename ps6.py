# Problem Set 6: Simulating robots
# Name: Alexandra Wrobel
# Collaborators: Minh-Tue Vo Thanh ('14, 6-3, helped me a with understanding/clarification what the pset was asking me to do for certain functions) 
# Time: 7 hours

import math
import random
from ps6_utils import Position
from ps6_room import RectangularRoom

class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """

        self.room = room
        self.speed = speed

        self.robotPosition = RectangularRoom.getRandomPosition(room)

        direction = random.randrange(0,360) #initializes the robot with a random direction
        self.robotDirection = direction
        
        #raise NotImplementedError

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """

        return self.robotPosition
        
        #raise NotImplementedError
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """

        return self.robotDirection

        #raise NotImplementedError

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """

        posW = Position.getX(position)
        posH = Position.getY(position)

        self.robotPosition = Position(posW,posH)
        
        #raise NotImplementedError

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """

        self.robotDirection = direction
        
        #raise NotImplementedError

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
        raise NotImplementedError # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        self.robotPosition = Position.getNewPosition(self.robotPosition, Robot.getRobotDirection(self), self.speed) #make the robot get a new position

        
        while RectangularRoom.isPositionInRoom(self.room, self.robotPosition) == False: #ensures that the new robot position is inside the room
            direction = Robot.getRobotDirection(self) #if the new position is not inside the room, make the robot go back to where it started and pick a new random direction
            direction = direction + 180
            if direction > 360:
                direction = direction = direction-360

            self.robotPosition = Position.getNewPosition(self.robotPosition, direction, self.speed)

            direction = random.randrange(0,360)
            self.robotDirection = direction 
            self.robotPosition = Position.getNewPosition(self.robotPosition, self.robotDirection, self.speed)


        RectangularRoom.cleanTileAtPosition(self.room, self.robotPosition)
        
        #raise NotImplementedError

# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """

    def __init__(self, room, speed): #pset states that robot changes direction after *every other step* however, this code says every step...i decided to do every other step

        self.room = room
        self.speed = speed

        self.robotPosition = RectangularRoom.getRandomPosition(room)

        direction = random.randrange(0,360)
        self.robotDirection = direction

        self.time_step = 0 #initializes a timestep to keep track of
       
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        def checkpos(robotPosition): #checks to see if new position is in the room, if not in the room, it moves robot back to original position and re-calculates a new position until the new position is inside the room
            while RectangularRoom.isPositionInRoom(self.room, self.robotPosition) == False:
                direction = Robot.getRobotDirection(self)
                direction = direction + 180
                if direction > 360:
                    direction = direction = direction-360
                self.robotPosition = Position.getNewPosition(self.robotPosition, direction, self.speed)

                direction = random.randrange(0,360) #calculates a new random direction, once robot hits a wall and moves back to original location
                self.robotDirection = direction 
                self.robotPosition = Position.getNewPosition(self.robotPosition, self.robotDirection, self.speed)

        if self.time_step%2 == 0: # on time steps 0, 2, 4, 6...
            self.robotPosition = Position.getNewPosition(self.robotPosition, Robot.getRobotDirection(self), self.speed)
            
            checkpos(self.robotPosition)
            
            RectangularRoom.cleanTileAtPosition(self.room, self.robotPosition)

        else: #on time steps 1, 2, 3... after this one, the robot will randomly change directions (regardless of whether it hit a wall)
            self.robotPosition = Position.getNewPosition(self.robotPosition, Robot.getRobotDirection(self), self.speed)
           
            checkpos(self.robotPosition)
           

            RectangularRoom.cleanTileAtPosition(self.room, self.robotPosition)

            direction = random.randrange(0,360) #calculates a new random direction
            self.robotDirection = direction
            

        self.time_step = self.time_step+1


        #raise NotImplementedError

