#Yikai Wang
#Period 6 SoftDev

import random
from flask import Flask, render_template
app = Flask(__name__) #create Flask object

def importCSV(fileName):
    inStream = open(fileName, 'r')
    lines = inStream.readlines()
    inStream.close()
    return lines

def cleanUp(L):
    for w in range(len(L)):
        L[w] = L[w].strip()
        L[w] = L[w].strip( "\n" )
        L[w] = L[w].strip( "\r" )
        if ('"' in L[w][0]):
            L[w] = L[w].split( '"' )[1:]
            L[w][1] = L[w][1][1:]
        else:
            L[w] = L[w].split( ',' )
    return L

def convertToDictionary(L):
    #print L
    D = dict()
    for subL in L:
        #print subL
        #print ""
        D[subL[0]] = subL[1]
    return D

def randChooser(D):
    x = random.randrange(998)
    sumLast = 0
    
    for i in D:
        #print x
        #print float(D[i])*10
        #print sumLast
        sumLast = sumNow = sumLast + (float(D[i])*10)
        if ( x < sumNow ):
            return i

@app.route("/occupations")
def makeHTML():
    L = cleanUp(importCSV("data/occupations.csv"))
    h1 = L[0][0]
    h2 = L[0][1]
    D = convertToDictionary(L[1:len(L)-1])
    rj = randChooser(D).lower()
    return render_template( 'template.html', title="Occupations List", header1 = h1, header2 = h2, collection = L[1:], job = rj )

@app.route("/") #assign following fxn to run when root route requested
def intro():
    return "Hello, there is nothing here!"

if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
