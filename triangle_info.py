#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 19:36:20 2018

@author: IBM-Watson
"""


from graphics import *
import math
def main():
    
    win = GraphWin('Rectangle Information', 400 , 400)
    win.setCoords(0, 0, 10, 10)
    
    # get user inputs(two points/mouse clciks) 
    # draw rectangle
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    poligon = Polygon(point1, point2 , point3)
    poligon.draw(win)
    
    #need three lengths 
    #point1 to point2
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()
    
    a = math.sqrt(dx * dx + dy * dy )
    #point2 to point3
    dx = point3.getX() - point2.getX()
    dy = point3.getY() - point2.getY()
    
    b = math.sqrt(dx * dx + dy * dy )
    #point3 to point1
    dx = point1.getX() - point3.getX()
    dy = point1.getY() - point3.getY()
    
    c = math.sqrt(dx * dx + dy * dy )
    
    #perimeter and area
    perimeter = a + b + c
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))    
    
    
    #Display texts 
    Text(Point(5,0.7),'Perimeter: ').draw(win)
    Text(Point(7,0.7), perimeter).draw(win)
    Text(Point(5,1),'Area: '    ).draw(win)
    Text(Point(7,1), area).draw(win)
    
    win.getMouse()
    win.close()


main()