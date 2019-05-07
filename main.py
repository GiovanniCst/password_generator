#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Semplice script che genera una password composta da enne parole concatenate e prese da un
dizionario. E' possibile selezionare la lunghezza delle parole da utilizzare per 
la generazione della password modificando i parametri passati alla funzione new_list(x, min_len, max_len)

Esercizio, Maggio 2019
di Giovanni J. Costantini

licenza d'uso: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
'''

# Trova un dizionario
# Ok provo con questo: "1000 Parole italiane comuni" -->
# https://github.com/napolux/paroleitaliane/blob/master/paroleitaliane/1000_parole_italiane_comuni.txt

import os
import random

NUMERO_PAROLE = 3
DICT = 'dict.txt'

# le parole del dizionario vengono caricate in una lista e mescolate
with open(DICT) as f:
   lines = [line.strip() for line in f]
   random.shuffle(lines)

# funzione che estrae dal dizionario le parole più lunghe di min_len e più corte di max_len

def new_list(x, min_len, max_len):
    '''Estrae dal dizionario le parole più lunghe di min_len e più corte di max_len '''
    return [item for item in x if len(item) > min_len and len(item) < max_len]

# prendi dal dizionario solamente le parole più lunghe di 2 caratteri e più corte di 8
# caratteri 

short_words = new_list(lines, 2, 8)
random.shuffle(short_words)

def gen_pass(passLen, aList):
    ''' Returns a password. Pass the length of the password and the list to choose from '''
    password_list = []
    for x in range(passLen):
        password_list.append(random.choice(aList))
    password = '-'.join(password_list)
    
    return password

# Genero una passowrd composta da quattro parole concatenate da un '-'

your_password = gen_pass(NUMERO_PAROLE, short_words)

print("Ecco la tua nuova password creata da una lista di " + str(len(short_words)) + " parole: "  + your_password)

