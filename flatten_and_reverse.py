
a=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def listeyap(x,sstr=[]):
  for i in x:
    if type(i) is list:
        listeyap(i)
    else:
      sstr.append(i)
  return sstr
print(listeyap(a))





b=[[1, 2], [3, 4], [5, 6, 7]]
def terscevir(b,sstr=[]):
  for i in b:
    if type(i)==list:
      sstr.append(list(reversed(i)))

  return(sstr)

print(terscevir(b))
