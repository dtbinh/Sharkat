# Problem Set 6: Simulating robots
# Name: Alexandra Wrobel
# Collaborators: Minh-Tue Vo Thanh ('14, 6-3, helped me a with understanding/clarification what the pset was asking me to do for certain functions) 
# Time: 7 hours

import math
import random

import ps6_visualize
import pylab

# For python 2.6:
#from ps6_verify_movement26 import testRobotMovement

# If you get a "Bad magic number" ImportError, comment out what's above and
# uncomment this line (for python 2.7):
from ps6_verify_movement27 import testRobotMovement

# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """

        self.width = width
        self.height = height

        room = {}

        for w in xrange(self.width): #make a dictionary to store the information of each tile + whether it is dirty or clean
            for h in xrange(self.height):
                
                room[(w,h)] = 'dirty'

        self.room = room
            
        
        #raise NotImplementedError
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """

        w = Position.getX(pos) #shorter notation = pos.getX()
        h = Position.getY(pos)
                
        w = math.floor(w)
        h = math.floor(h)

        self.room[(w,h)] = 'clean'
         
        #raise NotImplementedError

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        
        if self.room[(m, n)] == 'clean':
            return True
        else:
            return False
        
        #raise NotImplementedError
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """

        numTiles = self.width*self.height

        return numTiles
    
        #raise NotImplementedError

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
       
        cleanTiles = 0
        for w in xrange(self.width):
            for h in xrange(self.height):
                if self.isTileCleaned(w, h):
                    cleanTiles = cleanTiles + 1
        return cleanTiles

        #raise NotImplementedError

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        w = random.uniform(0, self.width) #returns a random position, with decimal points
        h = random.uniform(0, self.height)

        return Position(w,h)
        
        #raise NotImplementedError

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        w = Position.getX(pos)
        h = Position.getY(pos)
        
        if w < self.width and h < self.height and w>=0 and h>=0:
            return True
        else:
            return False
        
        #raise NotImplementedError


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

# Uncomment this line to see your implementation of StandardRobot in action!
testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    
    timeSteps = []
    num_tiles_to_clean = min_coverage*RectangularRoom.getNumTiles(RectangularRoom(width,height))

    def make_robot(robot_type, room, speed): #need to make a list of robots to iterate through all robots later
        
        return robot_type(room, speed)

    for trial in xrange(num_trials):
        
        room = RectangularRoom(width,height)
        tot_timeSteps = 0

        n = 1

        robots = [] #making list of robots
        while n <= num_robots:
            new_robot = make_robot(robot_type, room, speed)
            robots.append(new_robot)
            n = n+1

        while RectangularRoom.getNumCleanedTiles(room) < num_tiles_to_clean:
            
            for robot in robots: #assume that at each time step, each robot is required to move and clean
                
                robot_type.updatePositionAndClean(robot)
            tot_timeSteps = tot_timeSteps + 1
                
        timeSteps.append(tot_timeSteps)

    avg_time_steps = sum(timeSteps)/num_trials

    return avg_time_steps 
    
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

testRobotMovement(RandomWalkRobot, RectangularRoom)



# === Problem 5
#
# 1a) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your comment here ...)
#       showPlot1('compare robot methods', 'number of robots', 'time')
#
# 1b) How does the performance of the two robot types compare when cleaning 80%
#       of a 20x20 room?
#
#       (... your comment here ...)
#       According to the plot, the random walk robot initially (with 3 or fewer robots take significantly more time to clean the room, compared to the standard robot; however, as the number of robots increases, the random walk robot becomes nearly as efficient as the standard robot
#
# 2a) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your comment here ...)
#       showPlot2('robot comparison', 'aspect ratio', 'time')
#
# 2b) How does the performance of the two robot types compare when two of each
#       robot cleans 80% of rooms with dimensions 
#       10x30, 20x15, 25x12, 50x6
#
#       (... your comment here ...)
#       as the room becomes more narrow, it takes the random walk robot significantly longer to clean the room, compared to the standard robot. the standard robot cleans the room in approximately the same size, regardless of the dimensions.
#




def showPlot1(title, x_label, y_label):
    """
    Produces a plot comparing the two robot strategies in a 20x20 room with 80%
    minimum coverage.
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


