from graphics import *
from random import randint

class QTree:
    def __init__(self,Left,Right):
        self.topLeftTree=None
        self.topRightTree=None
        self.botLeftTree=None
        self.botRightTree=None
        self.topLeft=Left
        self.botRight=Right
        tempA = Point(self.botRight.getX()/2,self.topLeft.getY())
        tempB = Point(self.botRight.getX()/2,0)
        tempC = Point(self.botRight.getX(),self.topLeft.getY()/2)
        tempD = Point(0,self.topLeft.getY()/2)
        self.vertLine = Line(tempA,tempB)
        self.horzLine = Line(tempC,tempD)

    def showTree(self,win):
        self.vertLine.draw(win)
        self.horzLine.draw(win)

def fillDataPoints(pointArr):
    for x in range(512):
        a = Point(randint(0,512),randint(0,512))
        pointArr.append(a)

def showDataPoints(pointArr,win):
    for a in pointArr:
        a.draw(win)

def main():
    win = GraphWin("Quadtree Example",512,512)
    pointArr = []

    fillDataPoints(pointArr)
    showDataPoints(pointArr,win)
    
    myQTree = QTree(Point(0,512),Point(512,0))
    myQTree.showTree(win)


if __name__=="__main__":
    main()
