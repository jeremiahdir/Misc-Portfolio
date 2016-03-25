from tkinter import *
import csv
class HW7:
    def __init__(self):
        self.win = Tk()  # Sets up windows
        self.guiSetup()  # sets up GUI in window
        self.win.mainloop()
    def guiSetup(self):
        self.fileRetrieval() # retrieves, processes and spits out data
        f0 = Frame(self.win) # Sets up frame for shit to go in
        f0.pack(side=TOP)

        titles = Label(f0,text= 'Company,Average Daily High, Average Daily Low, Average Share Volume, Average Share Value, Annual Target')
        titles.pack(side = TOP)

        f1 = Frame ( f0)
        f1.pack(side = TOP)
        f2 = Frame(f0)
        f2.pack(side=TOP)
        f3 = Frame(f0)
        f3.pack(side=TOP)
        f4 = Frame(f0)
        f4.pack(side=TOP)
        f5 = Frame(f0)
        f5.pack(side=TOP)



        l1 =Label(f1,text = self.outputs[0][0])
        l2= Label(f1,text = self.outputs[0][1::])

        l3 = Label(f2,text = self.outputs[1][0])
        l4 = Label(f2,text = self.outputs[1][1::])

        l5 =Label(f3,text = self.outputs[2][0])
        l6= Label(f3,text = self.outputs[2][1::])

        l7 =Label(f4,text = self.outputs[3][0])
        l8= Label(f4,text= self.outputs[3][1::])

        l9= Label(f5,text = self.outputs[4][0])
        l10= Label(f5,text = self.outputs[4][1::])

        l1.pack(side = LEFT)
        l2.pack(side = RIGHT)

        l3.pack(side = LEFT)
        l4.pack(side = RIGHT)

        l5.pack(side = LEFT)
        l6.pack(side = RIGHT)

        l7.pack(side = LEFT)
        l8.pack(side = RIGHT)

        l9.pack(side = LEFT)
        l10.pack(side = RIGHT)


    def fileRetrieval(self):
        file1 = open('stockData.csv')
        CSVReader = csv.reader(file1)
        #print ( CSVReader )
        rows = []
        for rawRow in CSVReader:  # Retrieves row from csv file
            rows.append(rawRow)
            #print ( ' done ')
        file1.close()

        symbols = {}
        #print ( rows )
        for row in rows[1:]:
            #print( row )
            if row[1] not in symbols.keys():
                symbols[row[1]] = [0,0,0,0,0]  # if company row hasn't been encountered, add zero values
            values = []
            for item in row: # Iterates through items in the row
                pos = row.index(item)
                if pos > 1: # If it's one of the values
                   values.append(item) # add to value list
            #print ( symbols )
            symbols[row[1]][0] += float( values[0] )
            symbols[row[1]][1] += float(values[1])   # Adds up the four first values for each company
            symbols[row[1]][2] += float(values[2])
            if row[1] != 'sum':
                symbols[row[1]][3] += float(values[3])
            elif row[1] == 'sum':
                symbols['sum'][3] = 'N/A'
            #symbols[row[1][4]] += float(values[4])
        self.outputs = []
        companies = symbols.keys()
        x = 1# retrieves all five companies
        for company in companies:
            avgHigh = symbols[company][0] / (len(rows) // 5)  # calculates averages and target for each company
            avgLow = symbols[company][1] / (len(rows) // 5)
            avgShareVol = symbols[company][2] / (len(rows) // 5)
            if company != 'sum':

                avgShareVal = symbols[company][3] / (len(rows) // 5)
            elif company == 'sum':
                avgShareVal = 'N/A'
            target = float(rows[x][6])
            x += 1
            #print ( avgHigh)
            output = [company,avgHigh,avgLow,avgShareVol,avgShareVol,target]
            self.outputs.append(output)

rootWin = HW7()

