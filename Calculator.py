print(''' ________          ________          ___               ________          ___  ___          ___               ________          _________        ________          ________     
|\   ____\        |\   __  \        |\  \             |\   ____\        |\  \|\  \        |\  \             |\   __  \        |\___   ___\     |\   __  \        |\   __  \    
\ \  \___|        \ \  \|\  \       \ \  \            \ \  \___|        \ \  \\\  \       \ \  \            \ \  \|\  \       \|___ \  \_|     \ \  \|\  \       \ \  \|\  \   
 \ \  \            \ \   __  \       \ \  \            \ \  \            \ \  \\\  \       \ \  \            \ \   __  \           \ \  \       \ \  \\\  \       \ \   _  _\  
  \ \  \____        \ \  \ \  \       \ \  \____        \ \  \____        \ \  \\\  \       \ \  \____        \ \  \ \  \           \ \  \       \ \  \\\  \       \ \  \\  \| 
   \ \_______\       \ \__\ \__\       \ \_______\       \ \_______\       \ \_______\       \ \_______\       \ \__\ \__\           \ \__\       \ \_______\       \ \__\\ _\ 
    \|_______|        \|__|\|__|        \|_______|        \|_______|        \|_______|        \|_______|        \|__|\|__|            \|__|        \|_______|        \|__|\|__|''')


def expressions():
    try:
        while True:
            num = input("Enter an expression: ")
            print("The answer is: ", eval(num))
    except KeyboardInterrupt:
        print('\n')
        print("Exiting...")

    
def calc():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            firstnum = int(input("What is your first number?: "))
            secondnum = int(input("What is your second number?: "))
            symbol = input("Would you like to multiply or divide or add or subtract?: ")
            multiply = "*"
            divide = "/"
            add = "+"
            subtract = "-"

            if symbol == multiply:
                print("The answer is: " + str(firstnum * secondnum))

            if symbol == divide:
                print("The answer is: " + str(firstnum / secondnum))
    
            if symbol == add:
                print("The answer is: " + str(firstnum + secondnum))
    
            if symbol == subtract:
                print("The answer is: " + str(firstnum - secondnum))

    except KeyboardInterrupt:
        print('\n')
        print("Exiting...")

print("What type of calculator would you like to use?")
calctype = input('''1. Expressions
2. Normal (type Expressions or Normal): ''')
 
if calctype in ["Normal", "normal"]:
    calc()
elif calctype in ["Expressions", "expressions"]:
    expressions()
