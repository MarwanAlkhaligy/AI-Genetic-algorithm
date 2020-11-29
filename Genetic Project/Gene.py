import random

GenSize = 9
Iteration = 3
def FitnessFunction(gen):               # to Calculate the Fitness of each  gen

    subString = "010"
    fitness =  sum(1 for i in range(len(gen)) if gen.startswith(subString, i))

    return fitness


def CheckGenes(gen):                  # to check if the gen is true

    check = True
    if(len(gen) < GenSize or len(gen)  > GenSize):
        check = False
    elif(len(gen) == GenSize):
        for sub in gen:
          if(sub != "0" and sub != "1"):
            check = False
            break

    return check


def generateListOfFitness(GensList):    #to  generate a list of fitness of the gens

    fitnesslist = []

    for element in GensList:
        x = FitnessFunction(element)
        fitnesslist.append( x)
    return fitnesslist

def duplicates(lst, item):              #to get the index of the element

  return [index for index, element in enumerate(lst) if element == item]


def MaxElementFunction(list):          # to get the maxmium elements

    element = list[0]
    for el in list:
        if(element < el):
            element = el

    return element

def bestGenFunction(Genes):           #to arrange gens according to fitness

    count = 0
    Gen = []
    listOffitness = generateListOfFitness(Genes)
    copylistOffitness = generateListOfFitness(Genes)
    while (Genes):
        maxElement = max(listOffitness)
        IndexOfMaxElement = listOffitness.index(maxElement)
        realIndex = duplicates(copylistOffitness, maxElement)
        if(len(realIndex) > 1):
            for el in realIndex:
                Gen.append([Genes[IndexOfMaxElement], el, maxElement])
                listOffitness.remove(maxElement)
                Genes.remove(Genes[IndexOfMaxElement])
        else:
            Gen.append([Genes[IndexOfMaxElement],realIndex[0] , maxElement])
            listOffitness.remove(maxElement)
            Genes.remove(Genes[IndexOfMaxElement])

    return Gen

def CrossOver( firstElement , secondElement):

    firstElement = list(firstElement)
    secondElement = list(secondElement)
    strLen = len(firstElement)
    #randomIndex = random.randrange(1,strLen-2 )
    randomIndex = 4
    for i  in range(randomIndex,strLen):
      temp =  firstElement[i]
      firstElement[i] = secondElement[i]
      secondElement[i] = temp
    firstElement = "".join(firstElement)
    secondElement = "".join(secondElement)

    return [firstElement , secondElement]

def Mutation(firstElement):

    strLen = len(firstElement)
    randomIndex = random.randrange(0, strLen -1)
    firstElement = list(firstElement)
    if (firstElement[randomIndex] == "0"):
        firstElement[randomIndex] = "1"
    elif (firstElement[randomIndex] == "1"):
        firstElement[randomIndex] = "0"
    firstElement = "".join(firstElement)

    return firstElement

def ArrangeList(listOGenes, len):    #to arrange the list

    list = []
    count = 0
    index = 0
    while(count < len):
        for i in range(0,len):
            if(listOGenes[i][1] == count):
                index = i
                count +=1
                list.append(listOGenes[index][0])
                break

    return list

def printGeneration(list , num):

    if(num == 0):
        print("Parents" +  "\n")
        for i in range(len(list)):
            print("Gen: " + list[i][0] + " , parent : " + str(list[i][1] + 1) + " ,Fitness: " + str(list[i][2]))
    else:
        print("Generation " + str(num) + "\n")
        for i in range(len(list)):
         print("Gen: " + list[i][0] + " , parent : " + str(list[i][1] +1) + " ,Fitness: " + str(list[i][2]) )
    print("\n")






try:
    print("Enter the number Genes")
    numberOfGenes = input()
    noG = int(numberOfGenes)
    print("Please enter the Genes  with size " + str(GenSize))
    listOfGenes = []


    for i in range(0, noG):
        x = input()
        if (CheckGenes(x) != True):
            while (CheckGenes(x) != True):
                print("Please enter a correct one")
                x = input()
        listOfGenes.append(x)


except:
    print("An exception occurred you entered uncorrect value")
    quit()
Count = 0
while(Count < Iteration):

    length = len(listOfGenes)
    BestGenList = bestGenFunction(listOfGenes)
    printGeneration(BestGenList, Count)

    firstBestGen = BestGenList[0][0]
    secondBestGen = BestGenList[1][0]
    bestGens = CrossOver(firstBestGen, secondBestGen)
    BestGenList[0][0] = bestGens[0]
    BestGenList[1][0] = bestGens[1]
    min = BestGenList[0][2]
    index = 0
    for i in range(0, length):
        if (min > BestGenList[i][2] and BestGenList[i][0] != secondBestGen and BestGenList[i][0] !=firstBestGen):
            min = BestGenList[i][2]
            index = i

    worstGen = Mutation(BestGenList[index][0])
    BestGenList[index][0] = worstGen

    listOfGenes = ArrangeList(BestGenList, length)
    Count +=1



















