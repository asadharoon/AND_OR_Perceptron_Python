# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:06:36 2020

@author: Asad
"""

import random as rnd
class Neuron:

    def __init__(self):
        self.bias=0
        a=rnd.uniform(0,1)
        b=rnd.uniform(0,1)
        print("Weights are :"+str([a,b]))
        self.weights=[a,b] # assign random weights between 0 and 1 for both facts

    def predict_OR(self,fact1,fact2):
        sum=fact1*self.weights[0]+fact2*self.weights[1]+self.bias
        return sum
    
    def predict_AND(self,fact1,fact2):
        sum=fact1*self.weights[0]*fact2*self.weights[1]+self.bias
        return sum
print("For Decision 1:")
a=Neuron()
decision1=a.predict_AND(fact1=0.65,fact2=0.90)
print("For Decision 2:")
b=Neuron()
decision2=b.predict_OR(fact1=0.5,fact2=0.7)
print("For Final Decision:")
c=Neuron()
final_decision=c.predict_AND(fact1=decision1,fact2=decision2)
print("Final Decision is "+str(final_decision))

