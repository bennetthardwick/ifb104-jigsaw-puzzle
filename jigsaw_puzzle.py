
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9803572
#    Student name: Bennett Hardwick
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  FOUR PIECE JIGSAW PUZZLE
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_attempt".
#  You are required to complete this function so that when the
#  program is run it produces a picture of a jigsaw puzzle whose
#  state of completion is determined by data stored in a list which
#  specifies the locations of the pieces.  You are also required to
#  provide a solution to your particular puzzle.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

size_of_pieces = 300 # pixels (excluding any protruding "tabs")
half_piece_size = size_of_pieces / 2
max_tab_size = 100 # pixels
box_size = size_of_pieces + (max_tab_size * 2)
half_box_size = box_size / 2
left_border = max_tab_size
gap = max_tab_size
top_bottom_border = max_tab_size
canvas_height = (top_bottom_border + size_of_pieces) * 2
canvas_width = (size_of_pieces * 2 + left_border) * 2
template_centres = [[-(size_of_pieces + half_piece_size), -half_piece_size], # bottom left
                    [-half_piece_size, -half_piece_size], # bottom right
                    [-(size_of_pieces + half_piece_size), half_piece_size], # top left
                    [-half_piece_size, half_piece_size]] # top right
box_centre = [gap + (box_size / 2), 0]

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background for the puzzle, i.e., the template for the
# pieces and the box they're kept in.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up and at its standard width and colour.
#


# Draw the box that contains unused puzzle pieces.  (The box is
# larger than the puzzle pieces to allow for tabs sticking out on
# any of their four sides.)
def draw_box():

    # Determine the position of the box's bottom-left corner
    bottom_left = [box_centre[0] - half_box_size,
                   box_centre[1] - half_box_size]

    # Go to the bottom-left corner and get ready to draw
    penup()
    goto(bottom_left)
    width(5)
    color('black')
    pendown()
    
    # Walk around the box's perimeter
    setheading(0) # point east
    for side in [1, 2, 3, 4]:
        forward(box_size)
        left(90)

    # Reset the pen
    width(1)
    penup()
 

# Draw the individual squares of the jigsaw's template
def draw_template(show_template = False):

    # Only draw if the argument is True
    if show_template:

        # Set up the pen
        width(3)
        color('grey')

        # Draw a box for each centre coordinate
        for centre_x, centre_y in template_centres:
            
            # Determine the position of this square's bottom-left corner
            bottom_left = [centre_x - half_piece_size,
                           centre_y - half_piece_size]

            # Go to the bottom-left corner and get ready to draw
            penup()
            goto(bottom_left)
            pendown()
        
            # Walk around the square's perimeter
            setheading(0) # point east
            for side in [1, 2, 3, 4]:
                forward(size_of_pieces)
                left(90)

        # Reset the pen
        width(1)
        color('black')
        penup()


# As a debugging aid, mark the coordinates of the centres of
# the template squares and the box
def mark_coords(show_coords = False):

    # Only mark the coordinates if the argument is True
    if show_coords:

        # Don't draw lines between the coordinates
        penup()

        # Go to each coordinate, draw a dot and print the coordinate
        color('black')
        for x_coord, y_coord in template_centres + [box_centre]:
            goto(x_coord, y_coord)
            dot(4)
            write(str(x_coord) + ', ' + str(y_coord),
                  font = ('Arial', 12, 'normal'))

    # Reset the pen
    width(1)
    penup()
               
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the locations of
# jigsaw puzzle pieces:
#
# 1. The name of the piece, from 'Piece A' to 'Piece D'
# 2. The place to put the piece, either in the template, denoted
#    'Top left', 'Top right', 'Bottom left' or 'Bottom right', or
#    in the unused pieces box, denoted 'In box'
# 3. An optional mystery value, 'X', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily mention all pieces.  Also notice
# that several pieces may be in the box at the same time, in which
# case they should just be drawn on top of each other.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Most importantly, you must write your own data set at the end
# to provide the correct solution to your puzzle.
#

# The following data set doesn't require drawing any jigsaw pieces
# at all.  You may find it useful as a dummy argument when you
# first start developing your "draw_attempt" function.

attempt_00 = []

# Each of the following data sets put just one piece in the box.
# You may find them useful when creating your individual pieces.

attempt_01 = [['Piece A', 'In box']]
attempt_02 = [['Piece B', 'In box']]
attempt_03 = [['Piece C', 'In box']]
attempt_04 = [['Piece D', 'In box']]

# Each of the following data sets put just one piece in a
# location in the template.

attempt_05 = [['Piece A', 'Top left']]
attempt_06 = [['Piece B', 'Bottom right']]
wow = [['Piece B', 'Top right']]
attempt_07 = [['Piece C', 'Top right']]
attempt_08 = [['Piece D', 'Bottom left']]
attempt_09 = [['Piece A', 'Bottom left']]
attempt_10 = [['Piece B', 'Top left']]
attempt_11 = [['Piece C', 'Bottom right']]
attempt_12 = [['Piece D', 'Top right']]

# Each of the following data sets put all four pieces in the
# box, but in different orders.

attempt_13 = [['Piece A', 'In box'], ['Piece B', 'In box'],
              ['Piece C', 'In box'], ['Piece D', 'In box']]
attempt_14 = [['Piece D', 'In box'], ['Piece C', 'In box'],
              ['Piece B', 'In box'], ['Piece A', 'In box']]
attempt_15 = [['Piece C', 'In box'], ['Piece D', 'In box'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]

# Each of the following data sets uses between two and four pieces,
# either in the template or in the box

attempt_16 = [['Piece A', 'Top right'], ['Piece B', 'Bottom left']]
attempt_17 = [['Piece D', 'Bottom right'], ['Piece C', 'In box']]
attempt_18 = [['Piece C', 'Bottom right'], ['Piece A', 'Bottom right']]
attempt_19 = [['Piece B', 'In box'], ['Piece D', 'Top left'],
              ['Piece C', 'In box']]
attempt_20 = [['Piece C', 'Top left'], ['Piece D', 'Top right'],
              ['Piece A', 'Bottom left']]
attempt_21 = [['Piece A', 'In box'], ['Piece D', 'Bottom left'],
              ['Piece C', 'Top right']]
attempt_22 = [['Piece A', 'Bottom left'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom right'], ['Piece D', 'In box']]
attempt_23 = [['Piece D', 'Bottom right'], ['Piece C', 'In box'],
              ['Piece B', 'Top right'], ['Piece A', 'Top left']]
attempt_24 = [['Piece C', 'Bottom right'], ['Piece D', 'Top left'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]
attempt_25 = [['Piece D', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece C', 'Bottom right'], ['Piece A', 'Top right']]
attempt_26 = [['Piece C', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece A', 'Bottom right'], ['Piece D', 'Top right']]
attempt_27 = [['Piece C', 'Bottom left'], ['Piece D', 'In box'],
              ['Piece A', 'Top left'], ['Piece B', 'Top right']]

# Each of the following data sets is a complete attempt at solving
# the puzzle using all four pieces (so there are no pieces left in the box)

attempt_28 = [['Piece A', 'Bottom left'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Top right']]
attempt_29 = [['Piece A', 'Top right'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left']]
attempt_30 = [['Piece A', 'Bottom left'], ['Piece B', 'Top left', 'X'],
              ['Piece C', 'Bottom right'], ['Piece D', 'Top right']]
attempt_31 = [['Piece A', 'Bottom right'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom left', 'X'], ['Piece D', 'Top left']]
attempt_32 = [['Piece D', 'Top right', 'X'], ['Piece A', 'Bottom left', 'X'],
              ['Piece B', 'Top left'], ['Piece C', 'Bottom right']]
attempt_33 = [['Piece A', 'Top right', 'X'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left', 'X']]

# Here you must provide a list which is the correct solution to
# your puzzle.

# ***** Put the solution to your puzzle in this list
solution = [['Piece A', 'Top left'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom left'], ['Piece D', 'Bottom right']]

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_attempt" function.
#

# Declare variables and coordinates

#
#   Variables to control the quality of the drawing and
#   the size of the image strokes. By default, max_segments
#   should be set to about 20. This could be seen as "medium"
#   quality. "Low" qualilty would be anywhere from 0 - 10 and
#   "high" qualilty is 50+. Because of the low resolution of the
#   canvas, the differece between medium and low may not be much,
#   but the lines will take much longer to draw.
#
#   By defauly, the stroke width is set to 3.
#
max_segments = 20
stroke_width = 3

#
#   These lists are all the points required to draw each of the
#   pieces. They take the format piece[shape[curve[point]]].
#
#   Each curve is represented in the format
#   (x0, y0, x1, y1, x2, y2, x3, y3), where points xy0 and xy3
#   are the begining and end of the curve respectively, and xy1 and
#   xy2 are bezier anchor points.
#

piece_one = [
            [[0,274,-146,282,-220,119,-177,53],
             [-177,53,-177,53,-172,55,-163,59],
             [-163,59,-170,103,-169,141,-73,210],
             [-73,210,-74,247,-32,251,0,234],
             [0,234,0,234,0,234,0,274]],
            [[-123,90,-98,87,-60,114,0,107],
             [0,107,0,107,0,107,0,0],
             [0,0,0,0,0,0,-57,0],
             [-57,0,-57,0,-113,35,-123,90]],
            [[0,0,0,0,0,0,0,44],
             [-0,44,-20,65,-94,52,-77,16],
             [-77,16,-77,16,-82,16,-59,-1],
             [-59,0,-59,0,-59,0,0,0]],
            [[0,107,-39,111,-104,86,-123,90],
             [-123,90,-181,98,-164,187,-103,149]],
            [[-68,114,-68,114,-68,114,-160,89]],
            [[-67,136,-67,136,-67,136,-170,138]],
            [[-66,167,-66,167,-66,167,-154,193]],
            [[0,191,0,191,-16,192,-17,175],
             [-17,175,-17,175,-64,153,-73,210],
             [-73,210,-74,247,-32,251,0,234],
             [0, 234, 0, 234, 0, 234, 0, 191]],
            [[51,179,49,175,23,168,6,190]],
            
            [[0,0,0,0,0,0,-110,0], 
             [-110,0,-82,61,-200,36,-195,0],  
             [-195,0,-195,0,-195,0,-300,0],
             [-300,0,-300,0,-300,0,-300,300], 
             [-300,300,-300,300,-300,300,0,300], 
             [0,300,0,300,0,300,0,191], 
             [0,191,81,216,96,66,0,110], 
             [0,110,0,110,0,110,0,0]],

            [[-21,202,-21,202,-21,202,-21,219]]
        ]

piece_two = [
            [[110,-24,222,66,170,179,0,274],
             [0,274,0,274,0,274,0,234],
             [0,234,2,258,61,265,68,212],
             [68,212,150,201,211,99,110,-24]],
            [[67,213,68,199,59,192,54,180]],
            [[115,97,66,102,33,107,0,107],
             [0,107,0,107,0,107,0,48],
             [0,48,0,48,73,89,69,14],
             [69,14,69,14,97,40,115,97]],
            [[69,14,63,10,59,6,53,0],
             [53,0,53,0,53,0,0,0],
             [0,0,0,0,0,0,0,48],
             [0,48,0,48,73,89,69,14]],
            [[107,-26,121,-10,140,-14,161,13],
             [161,13,161,13,168,-17,192,-19],
             [192,-19,192,-19,194,-22,160,-60],
             [160,-60,165,-65,112,-70,107,-26]],
            [[228,0,254,50,165,26,163,13],
             [161,13,161,13,168,-17,192,-19],
             [192,-19,193,-19,196,-10,189,0],
             [189,0,189,0,189,0,228,0]],
            [[72,172,72,172,72,172,134,197]],
            [[72,145,72,145,72,145,153,147]],
            [[67,122,67,122,67,122,155,102]],
            [[105,159,153,200,176,53,110,96],
             [115,97,66,102,33,107,0,107]],
            
            [[0,0,0,0,0,0,110,0],
             [110,0,73,-71,218,-28,188,0],
             [188,0,188,0,188,0,300,0],
             [300,0,300,0,300,0,300,300],
             [300,300,300,300,300,300,0,300],
             [0,300,0,300,0,300,0,191], 
             [0,191,81,216,96,66,0,110], 
             [0,110,0,110,0,110,0,0]],

            [[17,202,17,202,17,202,17,219]]
        ]

piece_three = [
            [[-117,-31,-138,-19,-164,6,-176,50],
             [-176,50,-176,50,-172,56,-162,58],
             [-162,58,-162,58,-160,15,-112,-30],
             [-112,-30,-112,-30,-112,-30,-120,-29]],
            [[-124,-42,-124,-42,-165,-71,-183,-104],
             [-183,-104,-183,-104,-152,-99,-146,-140],
             [-146,-140,-146,-140,-146,-140,-123,-129],
             [-123,-129,-130,-143,-107,-174,-113,-216],
             [-113,-216,-113,-216,-85,-229,-14,-221],
             [-14,-221,-14,-221,-12,-201,-2,-200],
             [-2,-200,-2,-200,-2,-200,-2,-193],
             [-2,-193,-2,-193,-35,-201,-54,-183],
             [-54,-183,-54,-183,-134,-150,-75,-52],
             [-75,-52,-75,-52,-116,-56,-122,-42]],
            [[-117,-64,-117,-64,-127,-69,-122,-129]],
            [[-146,-140,-176,-222,-261,-43,-181,-104],
             [-181,-104,-183,-104,-152,-99,-146,-140]],
            [[-113,-209,-233,-280,43,-227,-14,-220],
             [-14,-220,-14,-220,-73,-232,-113,-209]],
            [[-122,-30,-87,-38,-39,-25,0,-35],
             [0,-35,0,-35,-8,-34,-18,-52],
             [-18,-52,-18,-52,-117,-61,-122,-42],
             [-122,-42,-122,-42,-127,-42,-122,-30]],
            [[0,-35,0,-35,-8,-34,-18,-52],
             [-18,-52,-18,-52,-28,-81,-2,-91],
             [0,-91,0,-91,0, -91,0,-35]],
            [[-48,-108,-48,-108,-48,-108,-72,-110],
             [-72,-110,-72,-110,-77,-119,-68,-144]],
            [[0,0,0,0,0,0,-59,0],
             [-59,1,-59,1,-42,-16,-1,-17],
             [-1,-17,-1,-17,-1,-17,-1,-1]], 
            
            [[0,0,0,0,0,0,-110,0], 
             [-110,0,-82,61,-200,36,-195,0],
             [-195,0,-195,0,-195,0,-300,0],
             [-300,0,-300,0,-300,0,-300,-300],
             [-300,-300,-300,-300,-300,-300,0,-300],
             [0,-300,0,-300,0,-300,0,-190],
             [0,-190,-90,-221,-92,-48,0,-106],
             [0,-106,0,-106,0,-106,0,0]]
          ]
piece_four = [
            [[111,-43,89,-45,101,-45,74,-49],
             [74,-49,108,-95,108,-147,1,-194],
             [1,-194,1,-194,1,-194,2,-199],
             [2,-199,2,-199,5,-199,8,-218],
             [8,-218,8,-218,90,-228,112,-209],
             [112,-209,102,-190,134,-110,111,-43]],
            [[111,-208,111,-208,71,-226,6,-220],
             [6,-220,6,-220,-34,-289,108,-261],
             [108,-261,133,-258,155,-224,111,-208]],
            [[0,-33,0,-33,18,-35,109,-24],
             [109,-24,109,-24,103,-26,111,-40],
             [111,-40,111,-40,114,-49,30,-52],
             [30,-52,30,-52,33,-34,0,-33]],
            [[0,0,0,0,0,0,55,0],
             [55,0,55,0,37,-14,0,-17],
             [0,-17,0,-17,0,-17,0,0]],
            [[228,1,228,1,222,-22,194,-20]],
            [[152,-67,152,-67,141,-78,118,-90],
             [118,-90,118,-90,118,-64,111,-44],
             [111,-44,111,-44,127,-68,152,-67]],
            [[0,-91,47,-103,54,-16,0,-37],
             [0,-37,0,-37,0,-37,0,-91]],
            [[-43,-109,-43,-109,18,-108,72,-104],
             [72,-104,83,-175,-28,-141,-67,-141]],

            [[0,0,0,0,0,0,110,0],
             [110,0,73,-71,218,-28,188,0],
             [188,0,188,0,188,0,300,0],
             [300,0,300,0,300,0,300, -300],
             [300, -300, 300, -300, 300, -300, 0, -300],
             [0,-300,0,-300,0,-300,0,-190],
             [0,-190,-90,-221,-92,-48,0,-106],
             [0,-106,0,-106,0,-106,0,0]]

         ]

missing_piece = [
                [[-89,24,-89,24,-89,24,-37,39],
                 [-37,39,-37,39,-37,39,-27,61],
                 [-27,61,-27,61,-27,61,23,62],
                 [23,62,23,62,23,62,36,37],
                 [36,37,36,37,36,37,75,36],
                 [75,36,75,36,75,36,75,-62],
                 [75,-62,75,-62,75,-62,-89,-62],
                 [-89,-62,-89,-62,-89,-62,-89,24]],
                [[-74,56,-74,56,-74,56,-53,56],
                 [-53,56,-53,56,-53,56,-53,47],
                 [-53,47,-53,47,-53,47,-78,41],
                 [-78,41,-78,41,-78,41,-74,56]],
                [[-90,-62,-90,-62,-90,-62,92,69]],
                [[90,-67,90,-67,90,-67,-91,72]] 
                ]

#
#   colourPalette is a list of the hex values for all the
#   colours used in the Doraemon image.
#
    
colourPalette = ["#218ec9", "#000000", "#5d000a",
                 "#ffffff", "#db301f", "#991113",
                 "#b0aeb7", "#fbb017", "#5d3f01",
                 "#d7d7d7"]

#
#   draw_attempt draws the Doraemon image based on a set of instructions
#   'arrangement.' Boolean logic is used to discern where each piece should
#   go and then drawPieceA - D or drawMissing is called
#

def draw_attempt(arrangement):
    for x in range(len(arrangement)):
        if (len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
            print 'Tried to draw', arrangement[x][0], 'at', arrangement[x][1], 'but piece was missing.'
        else:
            print 'Drawing', arrangement[x][0], 'at', arrangement[x][1]
        
        if (arrangement[x][0] == 'Piece A'):
            if (arrangement[x][1] == 'Top left'):
                pos = [-450, 150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceA([-300, 0])
            if (arrangement[x][1] == 'Top right'):
                pos = [-150, 150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceA([0, 0])
            if (arrangement[x][1] == 'Bottom left'):
                pos = [-450, -150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceA([-300, -300])
            if (arrangement[x][1] == 'Bottom right'):
                pos = [-150, -150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceA([0, -300])
            if (arrangement[x][1] == 'In box'):
                pos = [350, 0]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceA([500, -150])
        elif (arrangement[x][0] == 'Piece B'):
            if (arrangement[x][1] == 'Top left'):
                pos = [-450, 150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceB([-600, 0])
            if (arrangement[x][1] == 'Top right'):
                pos = [-150, 150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceB([-300, 0])
            if (arrangement[x][1] == 'Bottom left'):
                pos = [-450, -150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceB([-600, -300])
            if (arrangement[x][1] == 'Bottom right'):
                pos = [-150, -150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceB([-300, -300])
            if (arrangement[x][1] == 'In box'):
                pos = [350, 0]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceB([200, -150])
        elif (arrangement[x][0] == 'Piece C'):
            if (arrangement[x][1] == 'Top left'):
                pos = [-450, 150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceC([-300, 300])
            if (arrangement[x][1] == 'Top right'):
                pos = [-150, 150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceC([0, 300])
            if (arrangement[x][1] == 'Bottom left'):
                pos = [-450, -150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceC([-300, 0])
            if (arrangement[x][1] == 'Bottom right'):
                pos = [-150, -150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceC([0, 0])
            if (arrangement[x][1] == 'In box'):
                pos = [350, 0]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceC([500, 150])
        elif (arrangement[x][0] == 'Piece D'):
            if (arrangement[x][1] == 'Top left'):
                pos = [-450, 150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceD([-600, 300])
            if (arrangement[x][1] == 'Top right'):
                pos = [-150, 150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceD([-300, 300])
            if (arrangement[x][1] == 'Bottom left'):
                pos = [-450, -150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceD([-600, 0])
            if (arrangement[x][1] == 'Bottom right'):
                pos = [-150, -150]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X" and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceD([-300, 0])
            if (arrangement[x][1] == 'In box'):
                pos = [350, 0]
                if(len(arrangement[x]) > 2 and arrangement[x][2] == "X"):
                    drawMissing(pos)
                else:
                    drawPieceD([200, 150])
        else:
            print "Incorrect arrangement entered."

#
#   mathBezierCurve is a function that returns the x and y coordinate of
#   parametric curve
#       f(x) = axt^3 + bxt^2 + cxt + x0
#       f(y) = ayt^3 + byt^2 + cyt + y0
#   depending on t, a value between 0 and 1 expressing the completeness
#   of the curve (0 being the beginning and 1 the end.)
#
#   These functions have been rearranged to be in the format
#   (x0, y0, x1, y1, x2, y2, x3, y3, t) where points xy0 and xy3
#   are the begining and end of the curve respectively, and xy1 and
#   xy2 are the anchor points.
#

def mathBezierCurve(x0, y0, x1, y1, x2, y2, x3, y3, t):
    cx = 3*(x1 - x0)
    bx = 3*(x2 - x1) - cx
    ax = x3 - x0 - cx - bx

    cy = 3*(y1 - y0)
    by = 3*(y2 - y1)
    ay = y3 - y0 - cy - by

    return [ ax*(pow(t, 3)) + bx*(pow(t, 2)) + cx*t + x0, ay*(pow(t, 3)) + by*(pow(t, 2)) + cy*t + y0 ]

#
#   mathBezierCoords returns the values for x and y depending on t
#   where segments is the number of points to be used in the
#   curve
#

def mathBezierCoords(coords, segments, t):
    return mathBezierCurve(coords[0], coords[1], coords[2], coords[3], coords[4], coords[5], coords[6], coords[7], float(t)/float(segments))


#
#   Routines for drawing the bezier curves to the canvas based on 
#   an array "coords"
#

def drawBezierCurve(coords):
    segments = findSegmentSize(coords)
    if(findSegmentSize(coords) == 1):
        drawStraightLine(coords)
    else:
        for x in range(1, segments):
            goto(mathBezierCoords(coords, segments, x)[0], mathBezierCoords(coords, segments, x)[1])

def drawStraightLine(coords):
    goto(coords[0], coords[1])
    goto(coords[6], coords[7])

#
#   Logic for determining what segment size each line should use
#   to optimise and reduce the number of "goto" calls
#

def isStraightLine(coords):
    if(coords[0] == coords[2] and coords[0] == coords[4]):
        return True
    else:
        return False

def findSegmentSize(coords):
    totalDistance = 0
    segments = 20
    if(isStraightLine(coords)):
        totalDistance = 1
    else:
        for x in range(1, segments):
            if(x != 1):
                totalDistance += sqrt(pow(mathBezierCoords(coords, segments, x)[1] - mathBezierCoords(coords, segments, x - 1)[1], 2) \
                                      + pow(mathBezierCoords(coords, segments, x)[0] - mathBezierCoords(coords, segments, x - 1)[0], 2))             
    if(totalDistance > max_segments):
        return max_segments
    else:
        return int(ceil(totalDistance))
            


#
#   Routines for translating pieces so they can
#   be drawn at any location
#

def addToAllArrays(array, pos, add):
    for x in range(len(array)):
        addToArray(array[x], pos, add)

def addToArray(array, pos, add):
    if(add):
        for x in range(len(array)):
            for y in range(len(array[x])):
                if(y%2==0):
                    array[x][y] += pos[0]
                else:
                    array[x][y] += pos[1]
    else:
        for x in range(len(array)):
            for y in range(len(array[x])):
                if(y%2==0):
                    array[x][y] -= pos[0]
                else:
                    array[x][y] -= pos[1]        
    return array

#
#   Routines for using bezier curves or primitives
#   to draw sections of pieces
#

#   Draw the nose
def drawNose(pos):
    penup()
    goto(2 + pos[0], 148 + pos[1])
    pendown()
    color("Black", colourPalette[4])
    begin_fill()
    circle(22)
    end_fill()

#   Draw a section of the image based on
#   coords, colour and fill.
#   Each section is made up of several bezier
#   curves

def drawSection(coords, colour, fill=True):
    penup()
    goto(coords[0][0], coords[0][1])
    pendown()
    color("black", colour)
    if(fill): begin_fill()
    for coord in coords:
        goto(coord[0], coord[1])
        drawBezierCurve(coord)
        goto(coord[6], coord[7])
    if(fill): end_fill()

#   Similar to the drawSection sub-routine,
#   draw missing parts does exactly the same
#   but with "light grey" as the outline.

def drawMissingParts(coords, fill = True):
    penup()
    goto(coords[0][0], coords[0][1])
    pendown()
    color("light grey", "white")
    if(fill): begin_fill()
    for coord in coords:
        goto(coord[0], coord[1])
        drawBezierCurve(coord)
        goto(coord[6], coord[7])
    if(fill): end_fill()


#
#   Routines for drawing pieces A - D and missing pieces
#

def drawPieceA(pos):
    width(stroke_width)

    # Translate the shape so it's at a desired position
    addToAllArrays(piece_one, pos, True)

    # Draw the outline of the shape
    drawSection(piece_one[9], colourPalette[3]) 

    # Begin drawing the shape
    drawSection(piece_one[0], colourPalette[0])
    drawSection(piece_one[1], colourPalette[2])
    drawSection(piece_one[2], colourPalette[4])
    drawSection(piece_one[3], colourPalette[0], False)
    drawSection(piece_one[4], colourPalette[0], False)
    drawSection(piece_one[5], colourPalette[0], False)
    drawSection(piece_one[6], colourPalette[0], False)
    drawSection(piece_one[7], colourPalette[0], False)
    drawSection(piece_one[8], colourPalette[0], False)
    drawNose(pos)

    #Draw eye
    width(stroke_width * 4)
    drawSection(piece_one[10], colourPalette[0], False)

    #Outline the shape
    width(stroke_width * 2)
    drawSection(piece_one[9], colourPalette[3], False)
    width(stroke_width)

    # Change the array back to it's original values
    addToAllArrays(piece_one, pos, False)

def drawPieceB(pos):
    width(stroke_width)

    # Translate the shape so it's at a desired position
    addToAllArrays(piece_two, pos, True)
    
    # Draw the outline of the shape
    drawSection(piece_two[10], colourPalette[3])

    # Begin drawing the shape    
    drawSection(piece_two[0], colourPalette[0])
    drawSection(piece_two[1], colourPalette[0], False)
    drawSection(piece_two[2], colourPalette[2])
    drawSection(piece_two[3], colourPalette[4])
    drawSection(piece_two[4], colourPalette[0])
    drawSection(piece_two[5], colourPalette[3])
    drawSection(piece_two[6], colourPalette[0], False)
    drawSection(piece_two[7], colourPalette[0], False)
    drawSection(piece_two[8], colourPalette[0], False)
    drawSection(piece_two[9], colourPalette[0], False)

    # Draw eye
    width(stroke_width * 4)
    drawSection(piece_two[11], colourPalette[0], False)

    # Outline the shape
    width(stroke_width * 2)
    drawSection(piece_two[10], colourPalette[0], False)
    width(stroke_width)

    # Change the array back to it's original values
    addToAllArrays(piece_two, pos, False)

def drawPieceC(pos):
    width(stroke_width)

    # Translate the shape so it's at a desired position
    addToAllArrays(piece_three, pos, True)

    # Draw the outline of the shape
    drawSection(piece_three[9], colourPalette[3], pos)

    # Begin drawing the shape        
    drawSection(piece_three[0], colourPalette[0], pos)
    drawSection(piece_three[1], colourPalette[0], pos)
    drawSection(piece_three[2], colourPalette[0], False)
    drawSection(piece_three[3], colourPalette[3])
    drawSection(piece_three[4], colourPalette[3])
    drawSection(piece_three[5], colourPalette[4])
    drawSection(piece_three[6], colourPalette[7])
    drawSection(piece_three[7], colourPalette[0], False)
    drawSection(piece_three[8], colourPalette[4])

    # Outline the shape
    width(stroke_width * 2)
    drawSection(piece_three[9], colourPalette[0], False)
    width(stroke_width)
    
    # Change the array back to it's original values
    addToAllArrays(piece_three, pos, False)

def drawPieceD(pos):
    width(stroke_width)

    # Translate the shape so it's at a desired position
    addToAllArrays(piece_four, pos, True)

    # Draw the outline of the shape    
    drawSection(piece_four[8], colourPalette[3])

    # Begin drawing the shape            
    drawSection(piece_four[0], colourPalette[0])
    drawSection(piece_four[1], colourPalette[3])
    drawSection(piece_four[2], colourPalette[4])
    drawSection(piece_four[3], colourPalette[4])
    drawSection(piece_four[4], colourPalette[0], False)
    drawSection(piece_four[5], colourPalette[0])
    drawSection(piece_four[6], colourPalette[7])
    drawSection(piece_four[7], colourPalette[0], False)

    # Outline the shape
    width(stroke_width * 2)
    drawSection(piece_four[8], colourPalette[0], False)
    width(stroke_width)

    # Change the array back to it's original values
    addToAllArrays(piece_four, pos, False)

def drawMissing(pos):

    # Define camera variables
    outer_circle_radius = 40
    inner_circle_radius = 20

    # Translate the shape so it's at a desired position    
    addToAllArrays(missing_piece, pos, True)

    # Begin drawing the shape            
    drawMissingParts(missing_piece[0])
    drawMissingParts(missing_piece[1])
    color('white', 'light grey')
    penup()
    goto(pos[0], pos[1] - outer_circle_radius)
    pendown()
    begin_fill()
    circle(outer_circle_radius)
    end_fill()
    color('white', colourPalette[3])
    penup()
    goto(pos[0], pos[1] - inner_circle_radius)
    pendown()
    begin_fill()
    circle(inner_circle_radius)
    end_fill()

    # Draw the cross
    color('light grey')
    width(10)
    drawMissingParts(missing_piece[2], False)
    drawMissingParts(missing_piece[3], False)
    width(stroke_width)

    # Change the array back to it's original values
    addToAllArrays(missing_piece, pos, False)
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
    
# Set up the drawing canvas
setup(canvas_width, canvas_height)

# Give the canvas a neutral background colour
# ***** You can change the background colour if necessary to ensure
# ***** good contrast with your puzzle pieces
bgcolor('light grey')

# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by solving your puzzle
title('Four Piece Jigsaw Puzzle - Doraemon')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Draw the box that holds unused jigsaw puzzle pieces
draw_box()

# Draw the template that holds the jigsaw pieces
# ***** If you don't want to display the template change the
# ***** argument below to False
draw_template(True)

# Mark the centres of the places where jigsaw puzzle pieces must
# be drawn
# ***** If you don't want to display the coordinates change the
# ***** argument below to False
mark_coords(True)

# Call the student's function to display the attempted solution
# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_attempt(solution)

# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()

#
#--------------------------------------------------------------------#

