#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
messages_array =[]
alphabet = string.ascii_uppercase
fa = {'a':9.2,'b':1.02,'c':2.64,'d':3.39,'e':15.87,'f':0.95,'g':1.04,\
               'h':0.77,'i':8.41,'j':0.89,'k':0.00,'l':5.34,'m':3.24,'n':7.15,\
               'o':5.14,'p':2.86,'q':1.06,'r':6.46,'s':7.90,'t':7.26,'u':6.24,\
               'v':2.15,'w':0.00,'x':0.30,'y':0.24,'z':0.32}


def dechiffrement(message,cle):
    message = message.upper()
    text_dechiffre = ""
    for i in message:
        if i==" " or i=="\t" or i=="\n":
             text_dechiffre = text_dechiffre+i
        else:
            position = alphabet.find(i)
            if position>=0:
                text_dechiffre = text_dechiffre + alphabet[(position-cle)%26]
            else:
                text_dechiffre = text_dechiffre + i
    return text_dechiffre
    
    
if __name__=="__main__":
    message=input("Veillez saisir le text \n ")
    message.lower()
    nombre=int(input("Veillez specifier le nombre d'iteration\n"))
    ponderation_array={}
    for i in range(26):
        
        dechiffre=''
        dechiffre=dechiffrement(message, i)
        messages_array .append(dechiffre)
        ponderation=0
        for j in alphabet:
            ponderation+=dechiffre.count(j)*fa[j.lower()]
        ponderation_array[i]=ponderation
    result = sorted(ponderation_array.items(), key=lambda x: x[1])   
    

    #nous inversons maintenant les resultats pour que la plus grande ponderation se retrouve au dessus
    result.reverse()
    #on affiche en triant par rapport aux ponderations
    for cle, val in result[:nombre]:
        print("Clé [%2d] | ponderation [%4.2f]"% (cle, val))
        print(messages_array [cle])
