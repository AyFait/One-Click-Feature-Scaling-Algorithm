#THIS IS A PREPROCESSING STAGE/STEP 
#CAN BE USED BEFORE OF AFTER PRINCIPAL COMPONENT ANALYSIS (PCA): which reduces number of features
#It advised to use this before PCA though

import pandas as pd
import numpy as np


print('Welcome To FSA by @AyFait')
#Copy your csv filepaths here
inputFilePath = '/home/a0x0bc1/Downloads/TitanictrainCleaned.csv'
outputFilePath = '/home/a0x0bc1/Downloads/TitanicCleanedScaled.csv'
print('Selected File: ', inputFilePath)
csvFile = pd.read_csv(inputFilePath)
print(csvFile.dtypes)#Data type of each col

uniqueIdCol = csvFile.columns[0]#Col to identify each traning examples
yTrainCol = csvFile.columns[1]#Result col; can put 'None' if not available 
yTrain = csvFile[yTrainCol]
#print(yTrain)
#csvFile.drop(yTrainCol, axis=1, inplace=True) #Seperating yTrain not neccessary since you can just skip the col during col loop
xTrain = csvFile
#print(xTrain)
m, n = xTrain.shape
print(f'Num of training examples, m: {m}')
print(f'Num of training features, n: {n - 2}')#Col for each feature unique id  and also yTrain col is ommited
#print(xTrain)
#print(yTrain)



#To ceck for a categorical col
def isCategorical(workingCol):
    numValues = len(workingCol)#Total num of values
    numUniks = workingCol.nunique()#Total num of unique vals
    numTwiceUniques = sum(workingCol.value_counts() >= 2)#Total num of vals that reapeat atb least twice
    #print(workingCol.value_counts()) # To get a view of the freq of each val

    if (numTwiceUniques / numUniks) >= 0.4:#Other categorical threshold can also be used instead
        return True
    
    else:
        return None #This col is not categorical

#To check for a col with close range of values
def closeRange(workingCol):
    if workingCol.max() <= 1:#Threshold can be changed to suit
        return True

    else:
        return None

#Dividing each value by maximum method
def divByMax(workingCol):
    maxNum = workingCol.max()
    #workingCol = workingCol.apply(lambda elmt: elmt / maxNum)
    #OR
    workingCol = workingCol / maxNum #Using vectoriztion

    return workingCol

#Subtracting the each col avg from each value then div by the (max - min)
def meanNorm(workingCol):#elmt = (elmt - avg) / (max - min)
    rng = workingCol.max() - workingCol.min()
    avg = workingCol.mean()
    avgDiff = workingCol - avg
    workingCol = avgDiff / rng

    return workingCol

#Subtracting the each col avg from each value then div by the standard deviatiom im each col
def zScoreNorm(workingCol):#elmt = (elmt - avg) / stdDev
    #Calc for the stdDev
    avg = workingCol.mean()
    devFrmMean = workingCol - avg
    squrdUp = devFrmMean ** 2
    #varnc = sum(squrdUp) / len(squrdUp)
    varnc = squrdUp.mean()
    stdDev = varnc ** 0.5 #sqdr(varnc)

    workingCol = devFrmMean / stdDev
    #OR just
    #(workingCol - workingCol.mean()) / workingCol.std()

    return workingCol


def mainProg(csvFile, selection):
    #Main Prog
    #Main Operation
    normalizedCol = []
    skippedCol = []
    for col in csvFile.columns:
        minNum1 = csvFile[col].min()
        maxNum1 = csvFile[col].max()
        #workingCol = csvFile[csvFile.columns]
        if col == uniqueIdCol or col == yTrainCol:# or isCategorical(csvFile[col])
            skippedCol.append(col)
            continue#Skips the id col and yTrain col
        
        #elif isCategorical(csvFile[col]):#This should be optional as it is not neccessary, some cat col also have laerge range of values
        #   skippedCol.append(col) 
        #   continue
        elif closeRange(csvFile[col]):#This might be a better option if col has close/small range of vals already
            skippedCol.append(col)
            continue
        
        else:
            csvFile[col] = selection(csvFile[col])#Insert desired funtion to be used here
            normalizedCol.append(col)
        minNum2 = csvFile[col].min()
        maxNum2 = csvFile[col].max()
        #print(csvFile[col])
        print(f'{col} from {minNum1} to {maxNum1} now is {minNum2} to {maxNum2}')
    print(f'Skipped: {skippedCol}\nNormalized: {normalizedCol}')
    print(f'{len(skippedCol)} skipped, {len(normalizedCol)} normalized')
    print()
    csvFile.to_csv(outputFilePath, index=False)
    print(f'Cleaned Data Exported Successfully To {outputFilePath}')

    #return csvFile #Not neccessary



while True:
    #Alternatively
    '''normDict = {
    1: divByMax,
    2: meanNorm,
    3: zScoreNorm
}

try:
    choice = int(input(f"Select: \n 1: For Divide by max normalization \n 2: For Mean normalization (Recommended) \n 3: For Z-Score normalization \n"))
    if choice in normDict:
        selection = normDict[choice]
        csvFile = mainProg(csvFile, selection)
'''
    try:
        choice = int(input(f"Select: \n 1: For Divide by max normalization \n 2: For Mean normalization (Recommended) \n 3: For Z-Score normalization \n"))

        if choice == 1:
            csvFile = mainProg(csvFile, divByMax)
            break
            
        elif choice == 2:
            csvFile = mainProg(csvFile, meanNorm)
            break
                       
        elif choice == 3:
            csvFile = mainProg(csvFile, zScoreNorm)
            break
            
        else:
            print('Wrong input, only input 1, 2 or 3 as your selection!')


    except ValueError:
        print('Wrong input, only input 1, 2 or 3 as your selection!')
