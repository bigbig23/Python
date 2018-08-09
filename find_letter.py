import random
import collections

#une foctione que retourne la lettre suviante
def alphabet(val = 1):
    s = input("Enter a letter: ") 
    if len(s) <= 1:
        t = ord(s) + val
        if t in range(97,122,1):
           
            b = chr(t)
        elif t == 123:
            t = 97
            b = chr(t)
    print("the next letter is : ",b)
alphabet()



#fonctione que retourne l'alpahbets en LOWERCASE
alphabet = []

for letters in range(97,123):
    alphabet.append(chr(letters))
    
print(alphabet)



#une fonction que retourne l'alphabet en UPPERCASE
alphabet = []

for letters in range(65,91):
    alphabet.append(chr(letters))
    
print(alphabet)



#une fonction que compt l'occurence des lettre
text = "je souhaite compter l'occurence des lettres dans cettes phrase"
d_empty = {}
e = text.lower().split()
e = text.replace('','')
e = ''.join(text)
for item in e:
    d_empty[item] = d_empty.get(item, 0) + 1
print(d_empty)


#une fonction que retourne l'occurence des mots
l = "je souhaite compter l'occurence des lettres dans cettes  phrase"
d  = l.split()
em_dict = {}
for item in d:
    em[item] = em_dict.get(item,0)+1 
print(em)

 
 
#
import random
for myC in range(10):
    myC = chr(myC)
    randomN = random.randint(33,126)
    print(randomN)
    print(myC)
    



















    
    
    
