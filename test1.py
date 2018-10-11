# import matplotlib.pylab as plt
# import numpy as np
import collections

# Исходные данные
# vList1 = [1, 0]
# IndexList = [1, 2]

# Начальные значения весов

# wList1 = [[1,1,0.45],[1,2,0.78],[2,1,-0.12], [2,2,0.13], [1.5, -2.3]
# wList2 = [0,   0,    0,    0,    0,    0]


class Neuron:
    def __init__(self, pLayerType, pLayer, pIndex, pGlobalIndex):
        self.index = pIndex
        self.globalIndex=pGlobalIndex
        self.layer = pLayer
        self.layerType = pLayerType
        self.inputValue = 0
        self.outputValue = 0
        self.activated = 0

    def __SwichActivated__(self):
        if self.activated == 0:
            self.activated = 1
        else:
            self.activated = 0

    def __SetInputValue__(self, pInputValue):
        if ((self.layer == 'Output') or (self.layer == 'Internal')):
            self.inputValue = pInputValue
        else:
            raise ('Для данного типа уровня, входные значения, не вычисляются')

    def __SetOutputValue__(self, pOutputValue):
        self.outputValue = pOutputValue

    def __Print__(self):
        print('globalIndex='+str(self.globalIndex)+' inputValue='+str(self.inputValue)+' outputValue='+str(self.outputValue))


class Weight:
    leftLayer=0
    indexInLayerL=0
    indexInLayerR=0
    value=0
    def __init__(self, pLeftlayer, pIndexInLayerL, pIndexInLayerR, plGlobalIndex, prGlobalIndex):
        self.leftLayer = pLeftlayer
        self.indexInLayerL = pIndexInLayerL
        self.indexInLayerR = pIndexInLayerR
        self.lGlobalIndex=plGlobalIndex
        self.rGlobalIndex=prGlobalIndex
        self.value = 0

    def __SetValue__(self, pValue):
        self.value = pValue

    def __Print__(self):
        print('Leftlayer='+str(self.leftLayer)+' pIndexInLayerL='+str(self.indexInLayerL)+' pIndexInLayerR='+str(self.indexInLayerR))


def indexing_decorator(func):

    def decorated(self, index, *args):
        if index == 0:
            raise IndexError('Indices start from 1')
        elif index > 0:
            index -= 1

        return func(self, index, *args)

    return decorated


class NeuronList:
    #Создаим
    list=[]
    count = 0
    def __init__(self, pCountIndexInLayer, nCountInternalLayer, bHaveMovNeuron):
        pGlobalIndex=0
        print('Начало циклов')
        for nvIndex in range(nCountInternalLayer+2): #Это цикл по слоям (0...N)
            if nvIndex ==0:
                layerType='Input'
            elif nvIndex==nCountInternalLayer+1: #Это выходной слой
                layerType='Output'
            else:
                layerType ='Internal'

            vStr='  Слой № '+str(nvIndex)+' ' + str(layerType)

            for i in range(pCountIndexInLayer): #1..3 d нашем случае
                    print(vStr+' '+str(nvIndex) +' Индекс № ' + str(i)+ ' globaIndex='+str(pGlobalIndex))
                    neuron = Neuron(layerType, nvIndex, i, pGlobalIndex)
                    #-->
                    neuron.inputValue=10*pGlobalIndex
                    #--<
                    self.list.append(neuron)
                    pGlobalIndex = pGlobalIndex + 1
                    if layerType=='Output':
                        break
        self.count=pGlobalIndex

    def getFirstGlobalIndexInLayer(self, pLayer):
        for globalIndex in range(self.count):
            if self.list[globalIndex].layer==pLayer:
                return globalIndex


class WeightList:
    list=[]
    def __init__(self, pCountIndexInLayer, nCountInternalLayer, bHaveMovNeuron):
        # Создаем веса
        for nvIndex in range(nCountInternalLayer + 2):  # Это цикл по слоям (0...N)
            for j in range(pCountIndexInLayer):  # Цикл по "всем" узлам внутри слоя
                # #Для получения глобального номера используем слудующую формулу globalInxex=(№Слой-1)*Коичество узлов в слое+№ узла в текущем слое
                currentGlobalIndex=((nvIndex-1)*pCountIndexInLayer+j)
                # Если для сети задан нейрон смещения и - это он (последний на слое, то обрабатываем по особенному
                if bHaveMovNeuron == False or j < pCountIndexInLayer:
                    # Пробегаем по всем нейронам слоя текущий +1 для создания связий текущего нейрона со всеми нейронами следующего слоя
                    for k in range(pCountIndexInLayer):
                        if bHaveMovNeuron == False or k < pCountIndexInLayer:
                            kGlobalIndex=(nvIndex  * pCountIndexInLayer + k)

                            weight = Weight(nvIndex, j, k, currentGlobalIndex, kGlobalIndex)
                            # ->
                            # weight.__Print__()
                            # -<
                            self.list.append(weight)
                            print(weight.indexInLayerL)

##Поиск индекса по списку значений с условиями отбора
     def findIndexByParams(self, pLeftGlobalIndex, pGlobalIndex, pLayer):
         if pLayer is None:
             #Если начальный уровень не задан, то ищем по всему диапозону значений
             for index in range(pCountIndexInLayer, self.nl.count):
                 if self.wl.list[index]



    def __print__(self):
        for __index__  in range(1,self.__len__()):
            print('leftLayer='+str(self.__getitem__(__index__).leftLayer)+' indexInLayerL='+str(self.__getitem__(__index__).indexInLayerL)+' indexInLayerR='+str(self.__getitem__(__index__).indexInLayerR)+' value='+str(self.__getitem__(__index__).value))


class NeuralNetwork:
    def __init__(self, pCountIndexInLayer, nCountInternalLayer, bHaveMovNeuron):
        self.nl = NeuronList(pCountIndexInLayer, nCountInternalLayer, bHaveMovNeuron)
        self.wl = WeightList(pCountIndexInLayer, nCountInternalLayer, bHaveMovNeuron)

    def __calcValue(self, pGlobalIndex):
        firstGlobalIndexInLayer=getFirstGlobalIndexInLayer(self.nl.list[pGlobalIndex].layer - 1)
        for index in range(getFirstGlobalIndexInLayer(firstGlobalIndexInLayer, firstGlobalIndexInLayer+pCountIndexInLayer)):
            value= self.nl.list[index].inputValue*self.wl.list[index].value


    def __runCalc__(self, pCountIndexInLayer, nCountInternalLayer, bHaveMovNeuron):
        #функция расчета
        for vGlobalIndex in range(pCountIndexInLayer, self.nl.count):
           print( " Глобальный индекс=" + str(vGlobalIndex))
           print(self.nl.list[vGlobalIndex].inputValue)

        #  for nvIndex in range(1, nCountInternalLayer + 2):  #Это цикл по слоям (1...N), те не включая входной слой
        #      vStr ="Слой="+str(nvIndex)
        #      for j in range(pCountIndexInLayer): #Цикл по "всем" узлам внутри слоя
        #          vGlobalIndex=pCountIndexInLayer+(nvIndex)*(j+1)
        #          print(vStr + " узел=" + str(j)+" Глобальный индекс="+str(vGlobalIndex))
        #          #print("глобальный индекс"+str(vGlobalIndex))
        #          print(self.nl.list[vGlobalIndex].inputValue)#Привели к глобальному индексу и нашли значение
        #          if nvIndex == nCountInternalLayer+1:
        #              break
                #print(self.neuronList.__getitem__((nvIndex+1)*(j+1)))
                #print(self.neuronList.)






nn=NeuralNetwork(3, 1, False)
print('-----------------------')
nn.__runCalc__(3, 1, False)
#nn.neuronList.__print__()
#print(nn.neuronList.__len__())
#nn.weightList.__print__()
# Попытаемся залить новые значения
#collections.OrderedDict(sorted(nn.neuronList, key=lambda t: t[0]))
#print('-----------------------')
#nn.neuronList.__print__()