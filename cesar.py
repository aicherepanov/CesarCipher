# -*- coding: utf-8 -*-
"""
Шифр Цезаря 
    
python cesar.py --inpfile <имя файла> --outfile <имя файла> --shift <число> [-еnс | -dec]

@author: chere
"""

from sys import argv
import string

class CesarCipher(object):

    def __init__(self, inpfile, outfile, shift):
        self.inpfile = inpfile
        self.outfile = outfile
        self.shift = shift
        self.ru_lc_alphabet = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
        self.ru_uc_alphabet = list('абвгдежзийклмнопрстуфхцчшщъыьэюя'.upper())
        self.en_lc_alphabet = list(string.ascii_lowercase)
        self.en_uc_alphabet = list(string.ascii_uppercase)
        
    def encrypt(self):
        result = ""
        f = open(self.inpfile, 'r')
        text = f.read()
        f.close()
        for symbol in text:
            if symbol in self.ru_lc_alphabet:
                ind =  self.ru_lc_alphabet.index(symbol)
                result += self.ru_lc_alphabet[(ind + self.shift) % len(self.ru_lc_alphabet)]
            elif symbol in self.ru_uc_alphabet:
                ind = self.ru_uc_alphabet.index(symbol)
                result += self.ru_uc_alphabet[(ind + self.shift) % len(self.ru_uc_alphabet)]
            elif symbol in self.en_lc_alphabet:
                ind = self.en_lc_alphabet.index(symbol)
                result += self.en_lc_alphabet[(ind + self.shift) % len(self.en_lc_alphabet)]
            elif symbol in self.en_uc_alphabet:
                ind = self.en_uc_alphabet.index(symbol)
                result += self.en_uc_alphabet[(ind + self.shift) % len(self.en_uc_alphabet)]
            else:
                result += symbol
        return result

    def decrypt(self):
        result = ""
        f = open(self.inpfile, 'r')
        text = f.read()
        f.close()
        for symbol in text:
            if symbol in self.ru_lc_alphabet:
                ind = self.ru_lc_alphabet.index(symbol)
                result += self.ru_lc_alphabet[(ind - self.shift + len(self.ru_lc_alphabet)) % len(self.ru_lc_alphabet)]
            elif symbol in self.ru_uc_alphabet:
                ind = self.ru_uc_alphabet.index(symbol)
                result += self.ru_uc_alphabet[(ind - self.shift + len(self.ru_uc_alphabet)) % len(self.ru_uc_alphabet)]
            elif symbol in self.en_lc_alphabet:
                ind = self.en_lc_alphabet.index(symbol)
                result += self.en_lc_alphabet[(ind - self.shift + len(self.en_lc_alphabet)) % len(self.en_lc_alphabet)]
            elif symbol in self.en_uc_alphabet:
                ind = self.en_uc_alphabet.index(symbol)
                result += self.en_uc_alphabet[(ind - self.shift + len(self.en_uc_alphabet)) % len(self.en_uc_alphabet)]
            else:
                result += symbol
        return result

def main():
    result = ""
    for i in range(1, 8):
        if argv[i] == "--inpfile":
            inpfile = argv[i + 1]
        if argv[i] == "--outfile":
            outfile = argv[i + 1]
        if argv[i] == "--shift":
            shift = int(argv[i + 1])
        if argv[i] == "-enc":
            cs = CesarCipher(inpfile, outfile, shift)
            result = cs.encrypt()
        if argv[i] == "-dec":
            cs = CesarCipher(inpfile, outfile, shift)
            result = cs.decrypt()    
    f = open(outfile, 'w')
    f.write(result)
    f.close()

if __name__ == "__main__":
    main()
