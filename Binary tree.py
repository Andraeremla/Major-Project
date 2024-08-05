import csv
import numpy as np
import pandas as pd
import os

class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insertNodes(self, val):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left:
                self.left.insertNodes(val)
                return
            self.left = BSTNode(val)
        else:
            if self.right:
                self.right.insertNodes(val)
                return
            self.right = BSTNode(val)

    def printTree(self):
        return (self.left, self.right)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current

    def delete(self, val):
        if not self:
            return self
        
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left and self.right:
                temp = self.right.get_min()
                self.val = temp.val
                self.right = self.right.delete(temp.val)            
            elif not self.left:
                return self.right
            elif not self.right:
                return self.left

            temp = self.right.get_min()
            self.val = temp.val
            self.right = self.right.delete(temp.val)

        return self

    def exists(self, val):
        current = self
        while current:
            if val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            else:
                return True
        return False

    def preorder(self, vals, array=None):
        if array is None:
            array = []
        if vals:
            if isinstance(vals.val, Node):                
                array.append(vals.val.printNode())
            else:
                array.append(vals.val)
            self.preorder(vals.left, array)
            self.preorder(vals.right, array)
        return array

    def inorder(self, vals, array=None):
        if array is None:
            array = []
        if vals:
            self.inorder(vals.left, array)
            if isinstance(vals.val, Node):                
                array.append(vals.val.printNode())
            else:
                array.append(vals.val)
            self.inorder(vals.right, array)
        return array

    def postorder(self, vals, array=None):
        if array is None:
            array = []
        if vals:
            self.postorder(vals.left, array)
            self.postorder(vals.right, array)
            if isinstance(vals.val, Node):                
                array.append(vals.val.printNode())
            else:
                array.append(vals.val)
        return array

class Node:
    def __init__(self, year, film, boxOffice, budget):
        self.year = year
        self.film = film
        self.boxOffice = boxOffice
        self.budget = budget

    def __gt__(self, node2):
        return self.film > node2.film

    def __lt__(self, node2):
        return self.film < node2.film

    def printNode(self):
        try:
            return int(self.year), self.film, int(self.boxOffice), int(self.budget)
        except (AttributeError, ValueError):
            print("Something is wrong with your node")

def readDataFile(fileName, sheet_name):
    try:
        if os.path.exists(fileName):
            os.chmod(fileName, 0o666)
            df = pd.read_excel(fileName, sheet_name)
            return df
        else:
            print("File does not exist", fileName)
    except PermissionError:
        print("You cannot access this file")

def createTree():
    nodeList = []
    dataFrame = readDataFile(r"C:\Users\newli\Documents\School work\Discrete Maths 2\Major Project\Seagal_box_office.xlsx", 'Sheet1')
    for i in range(dataFrame.shape[0]):
        try:
            node = Node(dataFrame.iloc[i]['Year'], dataFrame.iloc[i]['Film'], dataFrame.iloc[i]['Box Office'], dataFrame.iloc[i]['Budget'])
            nodeList.append(node)
        except ValueError:
            print("There is something wrong with the data")

    bst = BSTNode()
    for node in nodeList:
        bst.insertNodes(node)

    print(bst.exists(nodeList[26]))
    print(nodeList[1].film)
    print("Max Value: ", bst.get_max().val.printNode())
    print("Minimum Value: ", bst.get_min().val.printNode())
    print("---------------------Pre Order ---------------")
    print(bst.preorder(bst))
    print("---------------------In Order ---------------")
    print(bst.inorder(bst))
    print("---------------------Post Order ---------------")
    print(bst.postorder(bst))
    print("--------------------- Deleted Node ---------------")
    bst.delete(nodeList[36])
    bst.delete(nodeList[1])
    print(bst.exists(nodeList[36]))
    print(bst.exists(nodeList[1]))
    print("--------------------- Updated Tree ---------------")
    print(bst.postorder(bst))
    print("Deleted Node: ",nodeList[36].film)
    print("Deleted Node: ",nodeList[1].film)

createTree()



