from graphics import *
from random import randint
import pdb 

class Node:
    def __init__(self,Position,Data):
        self.Position = Position
        self.Data = Data
    def get_Position():
        return self.Position
    def get_Data():
        return self.Data

class QTree:
    def __init__(self,Left=None,Right=None):

        self.topLeftTree=None
        self.topRightTree=None
        self.botLeftTree=None
        self.botRightTree=None
        self.tNode = None
        self.topLeft=Left
        self.botRight=Right

    
    def inBoundary(self,p):
        return (p.getX() >= self.topLeft.getX() and
                p.getX() <= self.botRight.getX() and
                p.getY() <= self.topLeft.getY() and
                p.getY() >= self.botRight.getY())

    def showTree(self,win):
        if(self.topLeftTree == None and
           self.topRightTree == None and
           self.botLeftTree == None and
           self.botRightTree == None):
            return
        else:
            tempA = Point((self.botRight.getX()+self.topLeft.getX())/2,self.topLeft.getY())
            tempB = Point((self.botRight.getX()+self.topLeft.getX())/2,self.botRight.getY())
            tempC = Point(self.botRight.getX(),(self.topLeft.getY()+self.botRight.getY())/2)
            tempD = Point(self.topLeft.getX(),(self.topLeft.getY()+self.botRight.getY())/2)
            vertLine = Line(tempA,tempB)
            horzLine = Line(tempC,tempD)
            vertLine.draw(win)
            horzLine.draw(win)
        if(self.topLeftTree != None):
            self.topLeftTree.showTree(win)
        if(self.topRightTree != None):
            self.topRightTree.showTree(win)
        if(self.botLeftTree != None):
            self.botLeftTree.showTree(win)
        if(self.botRightTree != None):
            self.botRightTree.showTree(win)
        return

    #Create insert(Node *) return void
    def insert(self,N):
        if(self.tNode == None):
            self.tNode = N
            return
        if(N == None):
            return

        #checks if 2 nodes are in same position
        if(abs(self.topLeft.getX() - self.botRight.getX()) <= 1 and
           abs(self.topLeft.getY() - self.botRight.getY()) <= 1):
            if(self.tNode == None):
                self.tNode = N
                self.showTree(win)
            return

        #left side
        if((self.topLeft.getX()+self.botRight.getX())/2 >= N.Position.getX()):
            #Indicates topLeftTree
            if((self.topLeft.getY() + self.botRight.getY()) / 2 >= N.Position.getY()):
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
                            Point(self.topLeft.getX(),(self.topLeft.getY()+self.botRight.getY())/2),
                            Point((self.topLeft.getX()+self.botRight.getX())/2,self.botRight.getY()))
                    self.botLeftTree.insert(N)
        else:
            #Indicates topRightTree
            if((self.topLeft.getY()+self.botRight.getY())/2 >= N.Position.getY()):
                if(self.topRightTree == None):
                    self.topRightTree = QTree(
                        Point((self.topLeft.getX()+self.botRight.getX())/2,self.topLeft.getY()),
                        Point(self.botRight.getX(),(self.topLeft.getY()+self.botRight.getY())/2))
                self.topRightTree.insert(N)
            #Indicates botRightTree
            else:
                if(self.botRightTree == None):
                    self.botRightTree = QTree(
                        Point((self.topLeft.getX()+self.botRight.getX())/2,(self.topLeft.getY()+self.botRight.getY())/2),
                        Point(self.botRight.getX(),self.botRight.getY()))
                self.botRightTree.insert(N)
                    
        
    #Create search(Point)return Node*
        


def fillDataPoints(pointArr):
    for x in range(256):
        a = Point(randint(0,512),randint(0,512))
        pointArr.append(a)
        

def showDataPoints(pointArr,win):
    for a in pointArr:
        a.draw(win)

def fillNodeArray(nodeArr,pointArr):
    for a in pointArr:
        nodeArr.append(Node(a,0))

def main():
    win = GraphWin("Quadtree Example",512,512)

    pointArr = []
    fillDataPoints(pointArr)

    myQTree = QTree(Point(0,0),Point(512,512))
    for a in pointArr:
        b = win.getMouse()
        temp = Node(b,1)
        b.draw(win)
        myQTree.insert(temp)
        myQTree.showTree(win)
        win.getMouse()

if __name__=="__main__":
    main()
