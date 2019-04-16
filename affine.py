# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import sys
import re
M = 26
letter_range = [chr(x) for x in range(ord('A'), ord('Z')+1)]
def gcd(a,b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a%b)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Инверсии не существует для пары (%d, %d)' % (a, m))
    else:
        return x % m

def findinvbymodule(t, m):
    dett = (t[0][0] * t[1][1] - t[1][0]*t[0][1]) % M
    minors = [[t[1][1], -t[1][0]], [-t[0][1], t[0][0]]]
    dett = modinv(dett, M)
    matrix = [[minors[0][0]*dett, minors[0][1]*dett], [minors[1][0]*dett, minors[1][1]*dett]]
    matrix = [[matrix[0][0]%M, matrix[0][1]%M], [matrix[1][0]%M, matrix[1][1]%M]]
    matrix = [[matrix[0][0], matrix[1][0]], [matrix[0][1], matrix[1][1]]]
    return matrix

def encrypt(text, k1, k2):
    if gcd(k1, M) != 1:
        raise Exception('k1 должен быть взаимнопростым с m')
    orig_text = text.upper()
    cipher_t = []
    for char in orig_text:
        if char in letter_range:
            cipher_t.append((((ord(char) - ord('A'))*k1 + k2) % M) + ord('A'))
        else:
            cipher_t.append(ord(char))
    cipher = "".join(chr(x) for x in cipher_t)
    intv = modinv(k1, M)
    return cipher, intv

def decrypt(text, k1, k2):
    ciph_t = text.upper()
    orig_t = []
    for char in ciph_t:
        if char in letter_range:
            orig_t.append((((((ord(char) - ord('A')) - k2) * k1) % M) + ord('A')))
    else:
        orig_t.append(ord(char))
    oup = "".join(chr(x) for x in orig_t)
    return oup

def multimtr(m1, m2):
    nm = [m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0], m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0]]
    return nm

def statistic(text):
    syms = {}
    for char in text:
        if char in syms:
            syms[char] +=1
        else:
            syms[char] = 1
    for x in syms:
        syms[x] = syms[x] / len(text)
    return syms

def f(o):
    return (o[1], o[0])

def attack(e1, e2, l1, l2):
    matrix = [[e1, 1], [l1, 1]]
    matrix = findinvbymodule(matrix, M)
    ml = [[e2], [l2]]
    mtrx = multimtr(matrix, ml)
    k1 = mtrx[0] % M
    k2 = mtrx[1] % M
    return k1, k2