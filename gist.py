# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 17:16:48 2021

python gist.py --inpfile <имя файла>

@author: chere
"""

from sys import argv
from collections import Counter
import matplotlib.pyplot as plt
import re

def main():
    for i in range(1, 2):
        if argv[i] == "--inpfile":
            inpfile = argv[i + 1]
            
    f = open(inpfile, 'r')
    text = f.read()
    newtext = sorted(re.sub(r'[^а-яë]+', "", text.lower()))
    count_text = Counter(newtext)
    plt.bar(count_text.keys(), count_text.values())
    plt.show()
    f.close()

if __name__ == "__main__":
    main()
