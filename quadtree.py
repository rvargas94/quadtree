from graphics import *
from random import randint

class Node:
    def __init__(self,Position,Data):
        self.Position = Position
        self.Data = Data
    def get_Position():
        return self.Position
    def get_Data():
        return self.Data

class QTree:
    def __init__(self,Left,Right):
        self.topLeftTree=None
        self.topRightTree=None
        self.botLeftTree=None
        self.botRightTree=None
        self.tNode = None
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

    #Create insert(Node *) return void
    def insert(self, N):
        if(N == None):
            return

        if(not inBoundary(N.position)):
            return

        if(abs(self.topLeft.getX() - self.botRight.getX()) <= 1 and
           abs(self.topLeft.getY() - self.botRight.getY()) <= 1):
            if(tNode == None):
                tNode = N
            return

        if((self.topLeft.getX()+self.botRight.getX())/2 >= N.position.getX()):
            #Indicates topLeftTree
            if((self.topLeft.getY() + self.botRight.getY()) / 2 >= N.position.getY()):
                if(self.topLeftTree == None):
                    self.topLeftTree = QTree(
                        Point(self.topLeft.getX(),self.topLeft.getY()),
                        Point((self.topLeft.getX()+self.botRight.getX())/2,
                              (self.topLeft.getY()+self.botRight.getY())/2))
                    self.topLeftTree.insert(N)
            #Indicates botLeftTree
            else:
                    if(self.botLeftTree == None):
                        self.botLeftTree = QTree(
                            Point(self.topLeft.getX(),(self.topLeft.getY()+botRight.getY())/2),
                            Point((self.topLeft.getX()+self.botRight.getX())/2,self.botRight.getY()))
                        self.botLeftTree.insert(N)
        else:
            #Indicates topRightTree
            if((self.topLeft.getY()+self.botRight.getY())/2 >= N.position.getY()):
                if(self.topRightTree == None):
                    self.topRightTree = QTree(
                        Point((self.topLeft.getX()+self.botRight.getX())/2,self.topLeft.getY()),
                        Point(self.botRight.getX(),(self.topLeft.getY()+self.botRight.getX())/2))
                    self.topRightTree.insert(N)
            #Indicates botRightTree
            else:
                if(self.botRightTree == None):
                    self.botRightTree = QTree(
                        Point((self.topLeft.getX()+self.botRight.getX())/2,(self.topLeft.getY()+self.botRight.getY())/2),
                        Point(self.botRight.getX(),self.botRight.getY()))
                self.botRightTree.insert(N)
                    
        
    #Create search(Point)return Node*
        
    #Create inBoundary(Point) return bool
    def inBoundary(self,p):
        return (p.getX() >= self.topLeft.getX() and
                p.getX() <= self.botRight.getX() and
                p.getY() <= self.topLeft.getY() and
                p.getY() >= self.botRight.getY())

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
