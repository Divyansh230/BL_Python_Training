import random

n=int(input('Enter the number of times the coin is flipped:'))
head,tail=0,0
for i in range(n):
    x=random.random()
    if x>0.5:
        head+=1
    else:
        tail+=1

percentage=head/n*100
print(f'Percentage of heads occurence:{percentage}%')