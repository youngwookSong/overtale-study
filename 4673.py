# -*- coding: utf-8 -*-
#위에꺼 #쓰기 위해서는 써줘야됨
arr_1=set() 
i=1
#set은 집합. 중복되는걸 없애줌 그대신 index 사용 불가

while(i<=10000) :
   ii=map(int, list(str(i)))
   arr_1.add(i+sum(ii))
   i=i+1

arr_1=list(arr_1)

k=0
p=1
while(p<10000):
   if(p==arr_1[k]):
      k=k+1
      p=p+1
   else:
      print(p)
      p=p+1



   