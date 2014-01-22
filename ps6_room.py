import random
import math
from ps6_utils import Position

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

    def dirtyTileAtPosition(self, pos):
        raise NotImplementedError

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