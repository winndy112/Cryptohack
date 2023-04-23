flag_starter1=(pow(101,17,22663)) # tính 101^17 mod 22663
flag_starter2=(pow(12,65537, 17*23)) 
# tính 12^65537 mod (17*23) theo công thức m^e mod n và n=p*q
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
flag_starter3 = (p-1)*(q-1) # phi(n)=phi(pq)=phi(p).phi(q)=(p-1)*(q-1)
phi_n=(p-1)*(q-1)
flag_starter4= pow(e,-1,phi_n) 
N = 882564595536224140639625987659416029426239230804614613279163
c = 77578995801157823671636298847186723593814843845525223303932
pri_key =pow(e,-1,phi_n)
flag_starter5= pow(c,pri_key, N)
print(flag_starter5)