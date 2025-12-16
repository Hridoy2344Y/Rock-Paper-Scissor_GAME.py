import random #This line imports the random module
opt=('Rock','Paper','Scissor')
x=random.choice(opt) #This choose a option between the opt

i_user=input("Enter your move: ").capitalize()
print(f"{x} is given by opp. ")
match (i_user,x):
    case("Rock","Rock"):
        print("Tie") 
    case("Rock","Paper"):
        print("Opp. wins 😞")
    case("Rock","Scissor"):
        print("You won 😇")

    case("Paper","Paper"):
        print("Tie")
    case("Paper","Rock"):
        print("You won 😇")
    case("Paper","Scissor"):
        print('Opp wins 😞')

    case("Scissor","Scissor"):
        print("Tie")
    case("Scissor","Rock"):
        print("Opp wins 😞")
    case("Scissor","Paper"):
        print("You won 😇")