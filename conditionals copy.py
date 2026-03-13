att = int(input("Enter your attendance: "))

if att >= 75:
    print("You are not Debarred.")
    mes = int(input("Your MES: "))
    A1 = int(input("Your Assignment 1 marks: "))
    A2 = int(input("Your Assignment 2 marks: "))

    if mes >= 12 and A1>=5 and A2>=5:
        print("You are Eligible for end term")
        math = int(input("Your Math mark: "))
        eng = int(input("Your English mark: "))
        phy = math = int(input("Your physics amrk: "))

        result = ((math+eng+phy)/300)*100

        if result >= 75:
            print("You got First Division with Distinction.", round(result,2))
        elif result >= 60 and result <75:
            print("First Division", round(result,2))
        elif result >= 50 and result <59:
            print("Second Division", round(result,2))
        elif result >= 30 and result <49:
            print("Third Division", round(result,2))
        else:
            print("Fail")
                        
    else:
        print("You are not Eligible for end term")
else:
    print("You are Debarred.")
