#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:31:22 2018

@author: IBM-Watson
"""

#this program displays information 
#about a rectangle drawn by the user.


from graphics import *
import math
def main():
    
    win = GraphWin('Rectangle Information', 400 , 400)
    win.setCoords(-10, -10, 10, 10)
    
    # get user inputs(two points/mouse clciks) 
    # draw rectangle
    point1 = win.getMouse()
    point2 = win.getMouse()
    aRectangle = Rectangle(point1, point2)
    aRectangle.draw(win)
    
    
    #measuring length of a rectangle
    dx = point2.getX() - point1.getX()
    dy = point1.getY() - point1.getY()
    
    length = math.sqrt(dx * dx + dy * dy)
    
    
    #measuring width of a rectangle
    dxw = point1.getX() - point1.getX()
    dyw = point2.getY() - point1.getY()
    
    width = math.sqrt(dxw * dxw + dyw * dyw )
    
    #perimeter and area
    area = length * width
    perimeter = 2 * (length + width)
    
    
    #Display texts 
    Text(Point(-8.6,-7),'Perimeter: ').draw(win)
    Text(Point(-4,-7), perimeter).draw(win)
    Text(Point(-9,-8),'Area: '    ).draw(win)
    Text(Point(-5,-8), area).draw(win)
    
    win.getMouse()
    win.close()


main()
