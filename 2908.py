# -*- coding: utf-8 -*-
"""2908.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vAkYb7ZhuxQDLAlPfIPIFD12-4Ng7x2J
"""

a, b = map(int, input().split())
a=list(map(int, list(str(a))))
b=list(map(int, list(str(b))))

def reverse(n):
  i=n[0]
  n[0]=n[2]
  n[2]=i
  p=n[0]*100 + n[1]*10 + n[2]
  return p

print(max(reverse(a),reverse(b)))

