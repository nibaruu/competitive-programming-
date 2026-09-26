s=input()
if s[1:].isupper() and s[0].islower(): 
  s=s[0].upper()+s[1:].lower()
elif  s.isupper():
  s=s.lower()  
elif len(s)==1 and s.islower():
  s=s.upper()  
print(s)
