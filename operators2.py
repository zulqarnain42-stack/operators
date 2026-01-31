print("notes of different  divisions")
amount=int(input("enter the amount"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50) //10
note4=(((amount%100)%50)%10)//5
print("notes of 100 pounds",note1)
print("notes of 50 pounds",note2)
print("notes of 10 pounds",note3)
print("notes of 5 pounds",note4)








