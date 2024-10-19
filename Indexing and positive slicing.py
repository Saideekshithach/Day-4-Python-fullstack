Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="Vijayawada"
a[3]
'a'
a[5]
'a'
a[9]
'a'
a[8]
'd'
a[0]
'V'
a[1]
'i'
a[2]
'j'
a[3]
'a'
a[4]
'y'
a[5]
'a'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'Vijaya'
a="Simple is better than complex"
a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'complex'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]
'Simple '
a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
'better'
b="Now is better than never"
b[0]+b[1]+b[2]
'Now'
b[19]+b[20]+b[21]+b[22]+b[23]
'never'
b[4]+b[5]
'is'
b[14]+b[15]+b[16]+b[17]
'than'
a="Sun rises in the east"
a[-21]+a[-20]+a[-19]
'Sun'
a[-17]+a[-16]+a[-15]+a[-14]+a[-13]
'rises'
a[-4]+a[-3]+a[-2]+a[-1]
'east'
a="Work hard until you succeed"
>>> a[-27]+a[-26]+a[-25]+a[-24]
'Work'
>>> a[-22]+a[-21]+a[-20]+a[-19]
'hard'
>>> a[-17]+a[-16]+a[-15]+a[-14]+a[-13]
'until'
>>> a[-11]+a[-10]+a[-9]
'you'
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'succeed'
>>> #slicing
>>> a="Vijayawada is a royal city"
>>> a[16:21]
'royal'
>>> a[22:26]
'city'
>>> a[11:13]
'is'
>>> a="codegnan:
SyntaxError: unterminated string literal (detected at line 1)
>>> a="codegnan"
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> a="Quick brown fox"
>>> a[0:5]
'Quick'
>>> a[12:15'
...   
SyntaxError: unterminated string literal (detected at line 1)
>>> a[12:15]
...   
'fox'
>>> a[6:11]
...   
'brown'
