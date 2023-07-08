# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:02:13 2023

@author: ULRICH_LUMENDO
"""

l5 = 16
l6 = 14
p = 6
n1 = 26

n2 = round(2*p*l6-n1)
n4 = round((2*p*l5)/(n2/n1*0.05+1))
n3 = round(2*l5*p-n4)

print("Le nombre de dents pour pour 1, 2, 3, 4 sont respectivement",
      n1, n2, n3, n4)

w1 = 1200
w4 = round(0.05 * w1)
w2 = round(-n1/n2*w1)
w3 = w2

print("Les vitesses de rotations pour 1, 2, 3, 4 sont respectivement",
      w1, w2, w3, w4)

hp = 20   #puissance en hp 

