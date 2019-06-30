#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Auteur : Netmme


from iter.mergeSort import mergeSort
from math import log
from os import urandom
import sys


if __name__ == "__main__":
    # Initiate variables for stats
    win, loose = 0, 0
    lenFail = []

    # Initiate tests
    if len(sys.argv) > 1 and sys.argv[1].isnumeric() and int(sys.argv[1]) > 0:
        nByte = int(sys.argv[1])
    else:
        nByte = 1
    nbrTests = pow(2, nByte*8)-1
    for length in range(nbrTests):
        l = [int.from_bytes(urandom(nByte), 'big') for i in range(length)]
        lSorted = mergeSort(l)
        l.sort()
        if l == lSorted:
            win += 1
        else:
            loose += 1
            lenFail.append(length)

    # Results
    print("Nbr de tests: {}".format(nbrTests))
    print("Nbr de succes: {}".format(win))
    print("Nbr d'echec: {}".format(loose))
    if win == nbrTests:
        print("C'est un parfait!")
    else:
        print("Les tailles suivantes ont échouées: {}".format(lenFail))
