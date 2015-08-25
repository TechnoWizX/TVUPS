import time
import sys

version = "1.0.0"

print("****************************************")
print("*         Hello, I am 'TVUPS'          *")
print("*   (The Very Usefull Python Script)   *")
print("*                                      *")
print("*            Version ", version,"           *")
print("****************************************")

print("\nType help for a list of commnands")

while True:
    command = input(">>")

    #HELP
    if command.lower() == "help":
        print("Displays the help pages")
        print("Usage: help <command type>\n")
        print("Viable options for <command type>:")
        print("Basic\nMath")

    elif command.lower().split()[0] == "help":
        if command.lower().split()[1] == "basic":
            print("Help      Documentation")
            
        elif command.lower().split()[1] == "math":
            print("Math")
            
        else:
            print("That is not a valid help page")
	
    #ABOUT
    elif command.lower() == "about":
        print("This program was brought to you by me.")

    #EXIT
    elif command.lower() == "exit":
        print("Goodbye!")
        time.sleep(2)
        sys.exit()

    #VERSION
    elif command.lower() == "version":
        print(version)

    #ADD
    elif command.lower() == "add":
        print("Adds two numbers together")
        print("Usage: add <number> <number>")

    elif command.lower().split(" ")[0] == "add":
        numa = "NO"
        numb = "NO"
        
        try:
            numa = command.split(" ")[1]
            numb = command.split(" ")[2]

        except:
            print("Adds two numbers together")
            print("Usage: add <number> <number>")
        
        if numa == "NO":
            print("Adds two numbers together")
            print("Usage: add <number> <number>")
                
        else:
            if numb == "NO":
                print("Adds two numbers together")
                print("Usage: add <number> <number>")
            else:
                try:
                    numa = float(numa)
                    try:
                        numb = float(numb)
                        ans = numa+numb
                        if str(ans).split(".")[1] == "0":
                            print(str(ans).split(".")[0])

                        else:
                            print(ans)

                    except ValueError:
                        print("That is not a valid number")
                        
                except ValueError:
                    print("That is not a valid number")

    #SUBTRACT
    elif command.lower() == "sub":
        print("Subtracts two numbers")
        print("Usage: sub <number> <number>")

    elif command.lower().split(" ")[0] == "sub":
        numa = "NO"
        numb = "NO"
        
        try:
            numa = command.split(" ")[1]
            numb = command.split(" ")[2]

        except:
            print("Subtracts two numbers")
            print("Usage: sub <number> <number>")
        
        if numa == "NO":
            print("Subtracts two numbers")
            print("Usage: sub <number> <number>")
                
        else:
            if numb == "NO":
                print("Subtracts two numbers")
                print("Usage: sub <number> <number>")
            else:
                try:
                    numa = float(numa)
                    try:
                        numb = float(numb)
                        ans = numa-numb
                        if str(ans).split(".")[1] == "0":
                            print(str(ans).split(".")[0])

                        else:
                            print(ans)

                    except ValueError:
                        print("That is not a valid number")
                        
                except ValueError:
                    print("That is not a valid number")

    #MULTIPLY
    elif command.lower() == "sub":
        print("Multiplys two numbers together")
        print("Usage: mult <number> <number>")

    elif command.lower().split(" ")[0] == "mult":
        numa = "NO"
        numb = "NO"
        
        try:
            numa = command.split(" ")[1]
            numb = command.split(" ")[2]

        except:
            print("Multiplys two numbers together")
            print("Usage: mult <number> <number>")
        
        if numa == "NO":
            print("Multiplys two numbers together")
            print("Usage: mult <number> <number>")
                
        else:
            if numb == "NO":
                print("Multiplys two numbers together")
                print("Usage: mult <number> <number>")
            else:
                try:
                    numa = float(numa)
                    try:
                        numb = float(numb)
                        ans = numa*numb
                        if str(ans).split(".")[1] == "0":
                            print(str(ans).split(".")[0])

                        else:
                            print(ans)

                    except ValueError:
                        print("That is not a valid number")
                        
                except ValueError:
                    print("That is not a valid number")


    #DIVIDE
    elif command.lower() == "div":
        print("Divides two numbers")
        print("Usage: sub <number> <number>")

    elif command.lower().split(" ")[0] == "div":
        numa = "NO"
        numb = "NO"
        
        try:
            numa = command.split(" ")[1]
            numb = command.split(" ")[2]

        except:
            print("Divides two numbers")
            print("Usage: div <number> <number>")
        
        if numa == "NO":
            print("Divides two numbers")
            print("Usage: sub <number> <number>")
                
        else:
            if numb == "NO":
                print("Divides two numbers")
                print("Usage: sub <number> <number>")
            else:
                try:
                    numa = float(numa)
                    try:
                        numb = float(numb)
                        ans = numa/numb
                        if str(ans).split(".")[1] == "0":
                            print(str(ans).split(".")[0])

                        else:
                            print(ans)

                    except ValueError:
                        print("That is not a valid number")
                        
                except ValueError:
                    print("That is not a valid number")

    #NOT VALID
    else:
        print("That is not a valid command")


            
