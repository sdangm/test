#import matplotlib.pylab as plt
#import numpy as np

#Исходные данные
#vList1 = [1, 0]
#IndexList = [1, 2]

#Начальные значения весов

#wList1 = [[1,1,0.45],[1,2,0.78],[2,1,-0.12], [2,2,0.13], [1.5, -2.3]
#wList2 = [0,   0,    0,    0,    0,    0]


class Neuron:
    def __init__(self, pLayerType, pLayer, pIndex):
        self.index = pIndex
        self.layer = pLayer
        self.layerType = pLayerType
        self.inputValue=0
        self.outputValue=0
        self.activated=0

    def __SwichActivated__(self):
        if self.activated==0:
            self.activated=1
        else:
            self.activated = 0

    def __SetInputValue__(self, pInputValue):
        if ((self.layer=='Output') or (self.layer=='Internal')):
            self.inputValue=pInputValue
        else:
            raise ('Для данного типа уровня, входные значения, не вычисляются')

    def __SetOutputValue__(self, pOutputValue):
        self.outputValue=pOutputValue


class Weight:
    def __init__(self, pLeftlayer, pIndexInLayerL, pIndexInLayerR):
        self.leftLayer = pLeftlayer
        self.indexInLayerL = pIndexInLayerL
        self.indexInLayerR = pIndexInLayerR
        self.value=0
    def __SetValue__(self, pValue):
        self.Value=pValue


class NeuronList:
    def __init__(self):
        self.__list=list();

    def __iter__(self):
        self.__i=0
        return  self

    def __next__(self):
        if self.__i>len(self.__list)-1:
            raise StopIterration
        else:
            a= self.__list[self.__i]
            self.__i=self.__i+1
            return a
    def __len__(self):
        return len(self.__list)

    def __add__(self, pValue):
        self.__list[self.__i]=pValues
        self.__i=self.__i+1

class WeightList:
    def __init__(self):
        self.__list=list();

    def __iter__(self):
        self.__i=0
        return  self

    def __next__(self):
        if self.__i>len(self.__list)-1:
            raise StopIterration
        else:
            a= self.__list[self.__i]
            self.__i=self.__i+1
            return a
    def __len__(self):
        return len(self.__list)



class NeuralNetwork:
    def __init__(self, pCountIndexInLayer, nCountInternalLayer):
        neuronList=NeuronList()
        weightList=WeightList()

nn=NeuralNetwork(1,1)
print(nn)





