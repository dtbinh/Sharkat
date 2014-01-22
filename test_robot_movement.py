#Embedded file name: C:\Users\tkortz\Desktop\ps6_old\ps6_verify_movement.py
import ps6_visualize

def testRobotMovement(robot_type, room_type, delay = 0.4):
    """
    Runs a simulation of a single robot of type robot_type in a 5x5 room.
    """
    room = room_type(5, 5)
    robot = robot_type(room, 1)
    anim = ps6_visualize.RobotVisualization(1, 5, 5, delay)
    while room.getNumCleanedTiles() < room.getNumTiles():
        robot.updatePositionAndClean()
        anim.update(room, [robot])

    anim.done()
