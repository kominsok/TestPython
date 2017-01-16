
#search(),match()
import re
telcheck =re.compile(r'(\d{2,3})-(\d{3,4})-(\d{4})')
print(bool(telcheck.match(('02-123-4567')))) #True
print(bool(telcheck.match(('02-가123-4567')))) #False
print(bool(telcheck.match(('3402-123-4567')))) #false
print(bool(telcheck.match(('032-123-4567')))) # true
print(telcheck.match(('02-123-4567')))

phone=re.compile('(\d{3})-(\d{3,4})-(\d{4})')
m=phone.match('010-123-4567')
m.group() #매칭된 문자열 집합을 튜플로 반환
print(m.groups())
print(m.group())
print(m.group(2,3))
print(m.start())
print(m.end())
print(m.start(2))
print(m.end(2))
print(m.end(2))
print(m.string[m.start(2):m.end(3)])

#findall()
s='matches the start of a string.'
result=re.findall('[a-z]+',s)
print(result) #['matches', 'the', 'start', 'of', 'a', 'string']

p=re.compile('\d+')
res=p.findall('12 AM, 24 allday, 10 pm')
print(res) #['12', '24', '10']

my_str="My mobile phone number is 010-2701-3604"
MPattern = re.compile('(\d{3})-(\d{3})-(\d{4})$')
Mres = re.search(MPattern, my_str).groups()
print(Mres)

MPattern02 = re.compile('[-,:\s]]')
print(re.sub(MPattern02,':',my_str,5))
