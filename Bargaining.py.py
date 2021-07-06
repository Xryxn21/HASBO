#intro and start
from responses import too_much, Fine
print("PLEASE SPEAK TO TO THE BOT IN SIMPLE LANGUAGE")
print("Hello I am ARIB and I am here to solve your queries and negotitae prices of products")
print("Would You like to solve your queries or bargain")
a=str(input("press b to bargain and q to solve your query"))
if a=="b":
      b1=str(input("please specify your product Id"))
value=0
d=0
#Product details
if b1=="100":
    print("Is your product samsung galaxy a5")
    d= int(input("Specify your price"))
    while value==1:
        if d>=3000 and b1=="100":
            print()
            value=1
        elif d<3000 and b1=="100":
            d=print("This is quite out man, enter something more reasnable ")
            value=1
        elif d1>=3000 and b1=="100":
            print("This price is a bit too much but i can do it", "SHOULD I LOCK THE PRICE")
            value=1
        else:
            d=int(input("I know you can do better come on"))
else:
    print("sad")

if b1=="103":
    print("Is your product samsung galaxy m31s")
if b1=="105":
    print("Is your product iphone 11")
if b1=="104":
    print("Is your product samsung galaxy a5")
if b1=="101":
    print("Is your product iphone 11 pro max")
if b1=="102":
    print("Is your product iphone 10 max")
if b1=="106":
    print("Is your product samsung note 10 lite  ")
if b1=="107":
    print("Is your product samsung note 10 ultra")
if b1=="108":
    print("Is your product one note 10s ")
if b1=="109":
    print("Is your product remdi note 5 ")
if b1=="110":
    print("Is your product mi note 10")
if b1=="111":
  print("Is your product Dell aprion 2020")
if b1=="112":
    print("Is your product hp ryzen 5 ultra")
if b1=="113":
    print("Is your product ryzen 7 dell 2k20")
if b1=="114":
    print("Is your product asus vivobook 14")
if b1=="115":
    print("Is your  dell aspirination 12")
#check bot
c=str(input("Please answer in a yes or a no"))
if c=="no":
    print("Please check your product details again")
if c=="yes":
   print("Now proceeding with barging of product",b1)
#bargaining
if c=="yes":
    print("Please tell the price which you prefer")
d=int(input(""))
#100
if d>=3000 and b1=="100":
    print("This price is a bit too much but i can do it", "SHOULD I LOCK THE PRICE")
elif d<3000 and b1=="100":
    d1=int(input("This is quite out man, enter something more reasnable "))
    
elif d1>=3000 and b1=="100":
    print("This price is a bit too much but i can do it", "SHOULD I LOCK THE PRICE")
else:
   d2=int(input("I know you can do better come on"))
    

if d2>=3000 and b1=="100":
    print("This price is a bit too much but i can do it", "SHOULD I LOCK THE PRICE")
else:
    d3=int(input("this has no margin in me, Please type a more suitable price"))

if d3>3000 and b1=="100":
    print("This price is a bit too much but i can do it", "SHOULD I LOCK THE PRICE")
else:
    str(input("the best I can do is 3200,Should I lock it"))
#101
if d>=5000 and b1=="101":
        print("This price is a bit too much but i can do it", "SHOULD I LOCK THE PRICE")
if d<5000 and b1=="101":
    e1=int(input("This is quite out man, enter something more reasnable "))
    
if e1>=5000 and b1=="101":
    print("This price is a bit too much but i can do it", "SHOULD I LOCK THE PRICE")
else:
   e2=int(input("I know you can do better come on"))
    

if e2>=5000 and b1=="101":
    print("This price is a bit too much but i can do it", "SHOULD I LOCK THE PRICE")
else:
    e3=int(input("this has no margin in me, Please type a more suitable price"))

if d3>5000 and b1=="101":
    print("This price is a bit too much but i can do it", "SHOULD I LOCK THE PRICE")
else:
    str(input("the best I can do is 3200,Should I lock it"))
if a=="q":
   q1=str(input("If your query is about a product type p , If it is about anything else type c"))
#Query coding
if q1=="p":
      q2=int(input("Please specify your product ID"))
if q1=="c":
      q3=str(input("Please write your query down"))
s

    #Query coding
if q1=="p":
      q2=str(input("Please specify your product ID"))
if q1=="c":
      q3=str(input("Please write your query down"))


if q2=="100":
    print("Is your product samsung galaxy a5")
if q2=="103":
    print("Is your product samsung galaxy m31s")
if q2=="105":
    print("Is your product iphone 11")
if q2=="104":
    print("Is your product samsung galaxy a5")
if q2=="101":
    print("Is your product iphone 11 pro max")
if q2=="102":
    print("Is your product iphone 10 max")
if q2=="106":
    print("Is your product samsung note 10 lite  ")
if q2=="107":
    print("Is your product samsung note 10 ultra")
if q2=="108":
    print("Is your product one note 10s ")
if q2=="109":
    print("Is your product remdi note 5 ")
if q2=="110":
    print("Is your product mi note 10")
if q2=="111":
  print("Is your product Dell aprion 2020")
if q2=="112":
    print("Is your product hp ryzen 5 ultra")
if q2=="113":
    print("Is your product ryzen 7 dell 2k20")
if q2=="114":
    print("Is your product asus vivobook 14")
if q2=="115":
    print("Is your  dell aspirination 12")
else:
 q2=str(input("Please check your product again and  specify your product ID"))
 







    

    

