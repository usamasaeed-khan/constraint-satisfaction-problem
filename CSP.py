# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:27:36 2019

@author: Usama Saeed
"""
stack=[]
board=[]
backTracks=0
def backTrack(board,row,col):
    global backTracks
    backTracks+=1
    print("\nBack Track At => Row: "+str(row)+" Column: "+str(col))
    board[row][col]=0
    right=col+1
    while(right<8):
        board[row][right]+=1
        right+=1
    left=col-1
    while(left>=0):
        board[row][left]+=1
        left-=1
    down=row+1
    while(down<8):
        board[down][col]+=1
        down+=1
    up=row-1
    while(up>=0):
        board[up][col]+=1
        up-=1
    upDig=row-1
    leftDig=col-1
    while(upDig>=0 and leftDig>=0):
        board[upDig][leftDig]+=1
        upDig-=1
        leftDig-=1
    downDig=row+1
    leftDig=col-1
    while(downDig<8 and leftDig>=0):
        board[downDig][leftDig]+=1
        downDig+=1
        leftDig-=1
    upDig=row-1
    rightDig=col+1
    while(upDig>=0 and rightDig<=7):
        board[upDig][rightDig]+=1
        upDig-=1
        rightDig+=1
    downDig=row+1
    rightDig=col+1
    while(downDig<=7 and rightDig<=7):
        board[downDig][rightDig]+=1
        downDig+=1
        rightDig+=1
    print("\nAfter Back Track==>\n\n")
    printBoard(board)
    return col+1
    
def printBoard(board):
    print("========================================================================")
    for i in range(8):
        print("\t"+str(i+1),end="")
    print("\t||")
    for i in range(8):
        print("_________",end="")
    print()
    for i in range(8):
        print(str(i+1)+" |",end="")
        for j in range(8):
            if board[i][j]==1:
                print("\tQ",end="")
            elif board[i][j]==0:
                print("\t ",end="")
            else:
                print("\t-",end="")
        print("",end="\t||\n")
    print("========================================================================")
def initializeBoard():
    for i in range(8):
        array=[]
        for j in range(8):
            array.append(0)
        board.append(array)
    return board
import random
board=initializeBoard()
j=random.randint(0,7)
i=0
while i!=8:
    while board[i][j]<0 and j<=7:
        if j==7:
            i-=1
            j=backTrack(board,i,stack.pop())
            if j==8:
                i-=1
                j=backTrack(board,i,stack.pop())
        if j<7:
            j+=1
    board[i][j]=1
    stack.append(j)
    print("\n")
    print("Placing Queen At Row: "+str(i+1)+" And Column: "+str(j+1)+"\n")
    col=j+1
    while(col<8):
        board[i][col]-=1
        col+=1
    col=j-1
    while(col>=0):
        board[i][col]-=1
        col-=1
    row=i+1
    while(row<8):
        board[row][j]-=1
        row+=1
    row=i-1
    while(row>=0):
        board[row][j]-=1
        row-=1
    row=i-1
    col=j-1
    while(row>=0 and col>=0):
        board[row][col]-=1
        row-=1
        col-=1
    row=i+1
    col=j+1
    while(row<=7 and col<=7):
        board[row][col]-=1
        row+=1
        col+=1 
    row=i+1
    col=j-1
    while(row<=7 and col>=0):
        board[row][col]-=1
        row+=1
        col-=1
    row=i-1
    col=j+1
    while(row>=0 and col<=7):
        board[row][col]-=1
        row-=1
        col+=1
    printBoard(board)
    i+=1
    j=0
print("\nAll Queens Placed Successfully.")
print("\nTotal No. of BackTracks: "+str(backTracks))