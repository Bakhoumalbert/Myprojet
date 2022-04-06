def factorielle:
	if n==1 or n==0:
		return 1
	else
		return n**factorielle(n-1)

int(input("Entrer un  entier : "))
print("La valeur de factorielle de ",n," est :",factorielle(n))