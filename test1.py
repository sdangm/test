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
    def __init__(self, pLayerType, pLayer, pIndex):
        self.index = pIndex
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


class Weight:
    def __init__(self, pLeftlayer, pIndexInLayerL, pIndexInLayerR):
        self.leftLayer = pLeftlayer
        self.indexInLayerL = pIndexInLayerL
        self.indexInLayerR = pIndexInLayerR
        self.value = 0

    def __SetValue__(self, pValue):
        self.Value = pValue



def indexing_decorator(func):

    def decorated(self, index, *args):
        if index == 0:
            raise IndexError('Indices start from 1')
        elif index > 0:
            index -= 1

        return func(self, index, *args)

    return decorated


class NeuronList(collections.MutableSequence):
    def __init__(self):
        self._inner_list = list()

    def __len__(self):
        return len(self._inner_list)

    @indexing_decorator
    def __delitem__(self, index):
        self._inner_list.__delitem__(index)

    @indexing_decorator
    def insert(self, index, value):
        self._inner_list.insert(index, value)

    @indexing_decorator
    def __setitem__(self, index, value):
        self._inner_list.__setitem__(index, value)

    @indexing_decorator
    def __getitem__(self, index):
        return self._inner_list.__getitem__(index)

    def append(self, value):
        self.insert(len(self) + 1, value)

    def __print__(self):
        for __index__  in range(1,self.__len__()):
            print('InputValue='+str(self.__getitem__(__index__).inputValue)+' '+' OutputValue='+str(self.__getitem__(__index__).outputValue))



class WeightList(collections.MutableSequence):
    def __init__(self):
        self._inner_list = list()

    def __len__(self):
        return len(self._inner_list)

    @indexing_decorator
    def __delitem__(self, index):
        self._inner_list.__delitem__(index)

    @indexing_decorator
    def insert(self, index, value):
        self._inner_list.insert(index, value)

    @indexing_decorator
    def __setitem__(self, index, value):
        self._inner_list.__setitem__(index, value)

    @indexing_decorator
    def __getitem__(self, index):
        return self._inner_list.__getitem__(index)

    def append(self, value):
        self.insert(len(self) + 1, value)

    def __print__(self):
        for __index__  in range(1,self.__len__()):
            print('leftLayer='+str(self.__getitem__(__index__).leftLayer)+' indexInLayerL='+str(self.__getitem__(__index__).indexInLayerL)+' indexInLayerR='+str(self.__getitem__(__index__).indexInLayerR)+' value='+str(self.__getitem__(__index__).value))


class NeuralNetwork:
    neuronList = NeuronList()
    weightList = WeightList()
    def __init__(self, pCountIndexInLayer, nCountInternalLayer):

        print('Начало циклов')
        for nvIndex in range(nCountInternalLayer+2): #Это цикл по слоям
            if nvIndex ==0:
                layerType_1='Input'
                layerType_2 = 'Internal'
            elif nvIndex==nCountInternalLayer+1: #Это выходной слой
                layerType_1 ='Internal'
                layerType_2='Output'
            else:
                layerType_1 ='Internal'
                layerType_2='Internal'

            print('  Слой № '+str(nvIndex)+' ' + str(layerType_1) + ' ' + str(layerType_2))

            for i in range(pCountIndexInLayer): #1..3 d нашем случае
                print('     Индекс № ' + str(i))
                neuron_1 = Neuron(layerType_1, nvIndex, i)
                neuron_2 = Neuron(layerType_2, nvIndex+1, i)

                self.neuronList.append(neuron_1)
                self.neuronList.append(neuron_2)

                weight = Weight(nvIndex, i, i)
                self.weightList.append(weight)
                #Создаем не созданные веса

                for j in range(nCountInternalLayer+2-1):
                    if i!=j:
                        weight = Weight(nvIndex, i, j)
                        self.weightList.append(weight)
                # Это выходной слой, то после первой же итерации выходим
                if nvIndex == nCountInternalLayer + 1:
                    return



nn=NeuralNetwork(3, 1)

nn.neuronList.__print__()
nn.weightList.__print__()
# Попытаемся залить новые значения
nn.neuronList.__setitem__()
