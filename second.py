import matplotlib.pyplot as plt
plt.plot([8,10,13,15,16,18,20,20,20,23,24,26,27,28,29,30,30,30,33,34,35])  
plt.ylabel('Numero de primos y hermanos')
plt.xlabel('anos de mi vida')
plt.title('Mis primos y hermanos') 
plt.savefig('temp.png')
plt.show()
