Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> re.search(r'FishC', 'I love FishC.com!')
<_sre.SRE_Match object; span=(7, 12), match='FishC'>
>>> "I love FishC.com!".find('FishC')
7
>>> re,search(r'.','I love FishC.com!')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    re,search(r'.','I love FishC.com!')
NameError: name 'search' is not defined
>>> re.search(r'.','I love FishC.com!')
<_sre.SRE_Match object; span=(0, 1), match='I'>
>>> re.search(r'Fish.', 'I love FishC.com!') #'.'为正则表达式的通配符
<_sre.SRE_Match object; span=(7, 12), match='FishC'>
>>> re.search(r'\.', 'I love FishC.com!')
<_sre.SRE_Match object; span=(12, 13), match='.'>
>>> re.search(r'\d', 'I love 123 FishC.com!')
<_sre.SRE_Match object; span=(7, 8), match='1'>
>>>  re.search(r'\d\d\d', 'I love 123 FishC.com!')
SyntaxError: unexpected indent
>>> re.search(r'\d\d\d', 'I love 123 FishC.com!')
<_sre.SRE_Match object; span=(7, 10), match='123'>
>>> re.search(r'\d\d\d.\d\d\d.\d\d\d.\d\d\d', '192.117.132.209')
<_sre.SRE_Match object; span=(0, 15), match='192.117.132.209'>
>>> re.search(r'[aeiou]','I love FishC.com!')
<_sre.SRE_Match object; span=(3, 4), match='o'>
>>> re.search(r'[aeiouAEIOU]','I love FishC.com!')
<_sre.SRE_Match object; span=(0, 1), match='I'>
>>> re.search(r'ab[3]','abbbc')
>>> re.search(r'ab[3]c','abbbc')
>>> 
>>> re.search(r'ab{3}','abbbc')
<_sre.SRE_Match object; span=(0, 4), match='abbb'>
>>> re.search(r'[01]\d\d|2[0-4]\d|25[0-5]','188')
<_sre.SRE_Match object; span=(0, 3), match='188'>
>>> #匹配IP地址
>>> re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])','192.168.1.1')
<_sre.SRE_Match object; span=(0, 11), match='192.168.1.1'>
>>> #ip地址范围为0-255
