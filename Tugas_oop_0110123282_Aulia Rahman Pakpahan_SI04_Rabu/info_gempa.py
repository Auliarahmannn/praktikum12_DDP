from Gempa import *
garut = Gempa ("Garut", 4.0)
jayapura = Gempa ("Jayapura", 3.3)
cianjur = Gempa ("Cianjur", 5.6) 
banten = Gempa ("Banten",1.2)
palu = Gempa ("Palu", 6.1)

print(banten.dampak())
print(palu.dampak())
print(cianjur.dampak())
print(jayapura.dampak()) 
print(garut.dampak())

