print("mathhomework.py")
problem = input("Enter a math sum,or 'q' to quit:")
while (problem != "q"):
    print("The answer to",problem,"is:",eval(problem) )
    problem = input("Enter another math sum,or 'q' to quit: ")