#Jeremiah Dir
#jdir@gatech.edu
# I worked on this project alone, using only course approved materials

from tkinter import *
from tkinter import filedialog
from tkinter import Entry
from tkinter import messagebox
import csv


class HW6:
    def __init__(self):
        self.win = Tk()
        self.guiSetup()
        self.win.mainloop()

    def guiSetup(self):    # Setups GUI
        self.counter = 0
        self.searched = []
        self.counter2 = 0

        self.f1 = Frame(self.win)  # Top frame
        self.f1.grid(row=0,column=1)

        l1 = Label(self.f1, text = 'Number Search File')
        l1.grid(row=0,column=0)                                 # Search Labels
        l2 = Label(self.f1,text = 'Number Bank File    ')
        l2.grid(row = 1, column = 0)

        self.e1 = Entry(self.f1,state = 'readonly')   # Num Search File Display
        self.e1.grid(row = 0, column =1,columnspan = 6 )

        self.e2 = Entry(self.f1,state = 'readonly')  # Num Bank File Display
        self.e2.grid(row=1,column=1,columnspan = 6)

        self.f2 = Frame(self.win)  # Bottom Frame, holds grid
        self.f2.grid(row = 2, column = 1)

        self.f3 = Frame(self.win, relief = 'raised', border = 4) # Holds num bank numbers
        self.f3.grid(row = 2, column = 2)

        b1 = Button(self.f1,text = 'Select File',command = self.openNSClicked) # Search file open
        b1.grid(row = 0, column = 8)

        b2 = Button(self.f1,text = 'Select File', command=self.openNBClicked)  # Bank file open
        b2.grid(row = 1, column = 8)

        b3 = Button(self.f1,text = 'Generate Number Search',command=self.generate) # generates grid
        b3.grid(row=2,column=0)

        self.functionRan = [False,False] # shows if both files have been selected

    def openNSClicked(self):  # Opens num search file
        self.fileName = filedialog.askopenfilename(title = 'Select a number search file')
        self.e1.configure(state = 'normal')
        self.e1.insert(0,self.fileName) # sets display to file path
        self.e1.configure(state = 'readonly')

        self.functionRan[0] = True # shows it has been ran

    def openNBClicked(self): # Opens num bank file
        self.fileName1 = filedialog.askopenfilename(title = 'Select a number bank file')

        self.e2.configure(state = 'normal')
        self.e2.insert(0,self.fileName1)  # Sets display to file path
        self.e2.configure(state = 'readonly')

        self.functionRan[1] = True # shows it has been ran

    def readFile(self): # Takes in search file and creates dict of labels of values
        f1 = open(self.fileName,'r')
        CSVReader = csv.reader(f1)
        rawRows = []
        for row in CSVReader:
            rawRows.append(row) # converts csv file rows to normal raw rows in nested list
        f1.close()

        length = len(rawRows)
        # self.rows = []
        # if self.fileName[-1:-4:-1] != 'vsc':
        #     messagebox.showwarning(title = 'Excuse me!', message = 'Invalid file! >:(')
        #     self.openNSClicked() # re open file dialog and re try
        #     if self.readFileBool == True:
        #         self.readFile()
        #         self.readFileBool = False
        #
        # if self.fileName1[-1:-4:-1] != 'vsc':
        #     messagebox.showwarning(title = 'Excuse me!', message = 'Invalid file! >:(')
        #     self.openNBClicked() # re open file dialog and re try
        #     if self.readFileBool == True and self.counter2 == 0:
        #         self.readFile()
        #         self.readFileBool = False
        #         self.counter2 += 1
        # if self.fileName1[-1:-4:-1] == 'vsc' and self.fileName[-1:-4:-1] == 'vsc':
        #     self.readFileBool == False

        self.rows = []
        for rawRow in rawRows:
            pos = rawRows.index(rawRow) # y value
            row = []
            self.rows.append(row) # creates empty lists at each y value in final rows list
            for item in rawRow:
                item = item.strip() # gets rid of white space

                try:
                    ['-','=','+','*','/','0','1','2','3','4','5','6','7','8','9'].index(item)
                    self.rows[pos].append(item) #appends y value in rows with item in x value

                except: # if there is an item not acceptable
                    messagebox.showwarning(title = 'Excuse me!', message = 'Invalid file! >:(')
                    self.win.destroy()
                    return None

    def generate(self): # generates gen dict and bank dict, these are all labels so it gens GUI as well

        if self.functionRan[0] == False or self.functionRan[1] == False : # if the files haven't been selected
            messagebox.showwarning(title = 'Not Ran!',message = "You haven't selected files, baka!")
            return None

        self.readFile() # converts raw csv to readable rows
        def gridGen(): # generates grid dictionary
            rows = self.rows # the final, checked rows of the csv file

            self.aDict = {}
            x=0
            y=0
            for row in rows:
                x = 0 # reset x value at beginning of y list
                for item in row:
                    label = Label(self.f2,text =' ' + item + ' ' )
                    label.grid(row= y, column = x)
                    self.aDict[y,x] = label

                    x += 1
                y += 1


        def bankGen(): # gens bank on right in a dict
            f = open(self.fileName1) # takes in bank file
            CSVReader = csv.reader(f)
            self.rows2 = []
            self.booleans = []
            for rawRow in CSVReader:
                if len(rawRow[0]) == 2:
                    self.rows2.append(rawRow)
                else:
                    try:

                        ['0','1','2','3','4','5','6','7','8','9'].index(rawRow[0])
                        self.rows2.append(rawRow) #appends y value in rows with item in x value

                    except: # if there is an item not acceptable
                        print ( rawRow[0])
                        messagebox.showwarning(title = 'Excuse me!', message = 'Invalid file! >:(')
                        self.win.destroy()
                        return None
                self  # takes rows from bank file, which is a array with x value one
                self.booleans.append(False)
            self.searchables = {}
            y = 0
            for item in self.rows2:  # goes through and creates label of each num and assigns to dict
                #print ( item )
                label = Label(self.f3, text = item)
                self.searchables[y] = label
                label.grid(row = y, column = 0 )
                y += 1

        def guiGen():  # Generates label of grid and bottom find entry and button
            f4 = Frame(self.win)
            f4.grid(row = 3,column = 1) # bottom frame

            self.e3 = Entry(f4,state = 'normal') # search criteria entry
            self.e3.grid(row = 0, column = 0)

            l1 = Label(self.win, text = 'Have Fun With Math!')
            l1.grid(row = 1, column = 1) # grid label

            b1 = Button(f4,text= 'Find',command = self.updateGUI) # find button
            b1.grid(row = 0, column = 1)

        gridGen()
        bankGen()
        guiGen()

    def findStartingCoords(self): # finds all coordinates with the first num in them
        entry = self.e3.get()
        number = entry[0]
        coors = []
        rows = self.rows
        x = 0
        y = 0
        for row in rows:
            x = 0
            for item in row:
                #print ( item )
                coordinate = (y,x)
                if str(item) == number:
                    try:
                        a = coors.index(coordinate)
                    except:
                        coors.append(coordinate)
                x+= 1
            y += 1
        #print ( coors )
        return coors # returns the list of coordinates as tuples

    def find(self):

        startingCoors = self.findStartingCoords()
        outsideComboList = []
        outsideComboCoorList = []  # creates all emptpy lists to append to
        coordList = []

        if len(startingCoors) == 0: # If there are no coordinates with that num in it
            messagebox.showwarning(title = 'Warning',message = 'Check your Math! >:(')

        else:
            print ( 'you have coords') # Tells me it works

        maxY = len(self.rows) - 1  # Max x and y index they can be without being out of range
        maxX = len(self.rows[0])-1

        coordinates = []
        z = 0
        for coor1 in startingCoors:
            x = coor1[1]  # sets as int coordinates
            y = coor1[0]


            pointCoor = [y,x]
            point = self.rows[y][x]
            # Checks where the coordinate is

            # Checks y boundaries
            if y == 0:
                above = False
                above2 = False   # Sets actual text at that coor as false
                aboveCoor = False
                above2Coor = False # sets coors as false

                belowCoor = [1,x]
                below2Coor = [2,x] # sets as text value at that coor
                below = self.rows[1][x]
                below2 = self.rows[2][x] # sets as coor at that point

            elif y == 8:
                below = False
                #print ( below )
                below2 = False
                above = self.rows[7][x]
                above2 = self.rows[6][x]

                aboveCoor = [7,x]
                above2Coor = [6,x]

                belowCoor = False
                below2Coor = False


            elif y == 1:
                above2 = False
                above = self.rows[0][x]
                below = self.rows[2][x]
                below2 = self.rows[3][x]

                aboveCoor = [0,x]
                above2Coor = False
                belowCoor = [2,x]
                below2Coor = [3,x]


            elif y == 7: # If on 2nd to last row
                below2 = False
                below = self.rows[8][x]
                above = self.rows[6][x]
                above2 = self.rows[5][x]

                aboveCoor = [6,x]
                above2Coor = [5,x]
                belowCoor = [8,x]
                below2Coor = False


            else:  # If its not on any edge or not 1 away from any edge
                above = self.rows[y-1][x]
                above2 = self.rows[y-2][x]
                below = self.rows[y+1][x]
                below2 = self.rows[y+2][x]

                aboveCoor = [y-1,x]
                above2Coor = [y-2,x]
                belowCoor = [y+1,x]
                below2Coor = [y+2,x]
                #print ( below2Coor )

            # Checks x coordinate boundaries
            if x < 1:
                left = False
                left2 = False
                right = self.rows[y][x+1]
                right2 = self.rows[y][x+2]


                leftCoor = False
                left2Coor = False
                rightCoor = [y,x+1]
                right2Coor = [y,x+2]

            elif x == 8:
                right = False
                right2 = False
                left = self.rows[y][x-1]
                left2 = self.rows[y][x-2]


                leftCoor = [y,x-2]
                left2Coor = [y,x-1]
                rightCoor = False
                right2Coor = False


            elif x == 7:
                right2 = False
                right = self.rows[y][x+1]
                left = self.rows[y][x-1]
                left2 = self.rows[y][x-2]

                leftCoor = [y,x-1]
                left2Coor = [y,x-2]
                rightCoor = [y,x+1]
                right2Coor = False


            elif x == 1:
                left2 = False
                left = self.rows[y][x-1]
                right = self.rows[y][x+1]
                right2 = self.rows[y][x+2]

                leftCoor = [y,x-1]
                left2Coor = False
                rightCoor = [y,x+1]
                right2Coor = [y,x+2]


            else:
                left = self.rows[y][x-1]
                left2 = self.rows[y][x-2]
                right = self.rows[y][x+1]
                right2 = self.rows[y][x+2]

                leftCoor = [y,x-1]
                left2Coor = [y,x-2]
                rightCoor = [y,x+1]
                right2Coor = [y,x+2]

            upRight = False
            upRight2 = False

            upLeft = False
            upLeft2 = False

            downRight = False
            downRight2 = False

            downLeft = False
            downLeft2 = False   # Sets up diagonals

            upRightCoor = False
            upRight2Coor = False

            upLeftCoor = False
            upLeft2Coor = False

            downRightCoor = False
            downRight2Coor = False

            downLeft2Coor = False
            downLeftCoor = False


            if x < 7 and y > 1:
                upRight = self.rows[y-1][x+1]
                upRight2 = self.rows[y-2][x+2]

                upRightCoor = [y-1,x+1]
                upRight2Coor = [y-2,x+2]

            if x > 1 and y > 1:
                upLeft = self.rows[y-1][x-1]
                upLeft2 = self.rows[y-2][x-2]

                upLeftCoor = [y-1,x-1]    # Tests coordinates if these directions arepossible
                upLeft2Coor = [y-2,x-2]

            if x < 7 and y < 7:
                downRight = self.rows[y+1][x+1]
                downRight2 = self.rows[y+2][x+2]

                downRightCoor = [y+1,x+1]
                downRight2Coor = [y+2,x+2]

            if x > 1 and y < 7:
                downLeft = self.rows[y+1][x-1]
                downLeft2 = self.rows[y+2][x-2]

                downLeft2Coor = [y+2,x-2]
                downLeftCoor = [y+1,x-1]



            # Sets combo values
            if above2 == False:
                MU = False
                MUCoor = False
            else:
                MU = point + above + above2
                MUCoor = [pointCoor,aboveCoor,above2Coor]

            if below2 == False:
                MD = False
                MDCoor = False
            else:
                MD = point + below + below2
                MDCoor = [pointCoor,belowCoor,below2Coor]

            if left2 == False:
                ML = False
                MLCoor = False
            else:
                ML = point + left + left2
                MLCoor = [pointCoor,leftCoor,left2Coor]

            if right2 == False:
                MR = False
                MRCoor = False
            else:
                MR = point + right + right2
                MRCoor = [pointCoor,rightCoor,right2Coor]

            if downRight == False:
                DR = False
                DRcoor = False
            else:
                DR = point + downRight + downRight2
                DRcoor = [pointCoor,downRightCoor,downRight2Coor]

            if downLeft == False:
                DL = False
                DLcoor = False
            else:
                DL = point + downLeft + downLeft2
                DLcoor = [pointCoor,downLeftCoor,downLeft2Coor]

            if upRight == False:
                UR = False
                URcoor = False
            else:
                UR = point + upRight + upRight2
                URcoor = [pointCoor,upRightCoor,upRight2Coor]

            if upLeft == False:
                UL = False
                ULcoor = False
            else:
                UL = point + upLeft + upLeft2
                ULcoor = [pointCoor,upLeftCoor,upLeft2Coor]

            comboCoors = [MLCoor,MRCoor,MUCoor, MDCoor,ULcoor,URcoor,DLcoor,DRcoor] # makes list of adjacent coordinate combos next to this coor
            combos = [ML,MR,MU,MD,UL,UR,DL,DR]  # Makes list of text values for that starting coordinate

            outsideComboList.append(combos) # adds both to outside lists
            outsideComboCoorList.append(comboCoors)

        for coor in startingCoors:
            i1 = startingCoors.index(coor)
            combos = outsideComboList[i1]   # Iterates through starting coords
            k = 0
            for combo in combos:   # for each directional combo
                i2 = combos.index(combo)
                entry = self.e3.get()
                if combo != False: # If the combo exists
                    if combo == entry or combo[::-1] == entry:  # if the combo matches the search entry
                        for coor in outsideComboCoorList[i1][i2]:
                            coordList.append(coor) # add all the individual values' coors to the highlight list
        return coordList

    def updateGUI(self):

        list2 = self.find()
        for item in list2:
            y = item[0]
            x = item[1]
            tuple = (y,x)

            label = self.aDict[tuple]
            label.configure(background = 'yellow')
            label.configure(fg ='grey')

        entry = self.e3.get()
        if len(entry) == 3:
            if '=-+*/'.find(entry[0]) == -1 and '=-+*/'.find(entry[2]) == -1:
                value = eval(entry)
            else:
                value = False
        else:
            messagebox.showwarning(title = 'Invalid input', message = 'Invalid Input')
            value = False
        y = 0
        counter = 0
        for x in self.rows2:
            if value == False:
                searchNum = True
            else:
                searchNum = int(x[0])

            print ( searchNum , 'SearchNum')
            print ( counter, 'Counter')
            if value == searchNum:
                label = self.searchables[counter]
                label.configure(fg = 'grey')
                print ( 'label changed!')
                if self.booleans[counter] == False:
                    self.booleans[counter] = True
                    y += 1
                if y == 8:
                    messagebox._show(title = 'congrats', message = ' You have found all the nums!' )
                if counter != 9:
                    counter += 1
            else:
                print ('not a match!')
                counter += 1




rootWin = HW6()

