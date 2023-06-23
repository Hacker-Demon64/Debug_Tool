try:
    from ILK import Specs
    from colorama import Fore

    print("Hi There, Welcome To The Iphone Shop!")
    ask = input("Please Tell Us Your Name!: ")
    asker = input("Hi There " + ask + " Have You Come Here To Buy Something?: ")
    if asker == "yes":
        print("Alright Sir We'll Show You Our Best Iphones!")
    elif asker == "no":
        print("Alright Sir You Can Leave!")
        quit()
    else:
        print("I Didn't Quite Get That?")
        quit()
    
    addr = input("Sir What's Your Address?: ")

    iPhone13ProMax = Specs("iPhone 13 Pro Max", "Apple", "₹1,17,900", ask, addr, "A15 Bionic chip", " Triple 12MP rear cameras, 12MP front camera" , "1TB")
    Iphone13Pro = Specs("Iphone 13 Pro", "Apple", "₹1,07,900", ask, addr, "A15 Bionic Chip", "Triple 12MP rear cameras, 12MP front camera", "1TB")
    IphoneSE = Specs("Iphone SE", "Apple", "₹37,900", ask, addr, "A13 Bionic chip", "12MP rear camera, 7MP front camera","512GB")
    IphoneXR = Specs("iPhone XR", "Apple", "₹47,900", ask, addr, "A12 Bionic chip", "Single 12MP rear camera, 7MP front camera", "128GB")
    Iphone12ProMax = Specs("iPhone 12 Pro Max", "Apple", "₹1,29,900", ask, addr, "A14 Bionic chip", "Triple 12MP rear cameras, 12MP front camera", "128GB")

    print("Here You Go Pick A Number You Will Get That Phone For Free")

    OpB = input("Pick A Number: ")
    if OpB == "1":
        print("Alright Here You Go")
        print(Fore.CYAN + "Specs: " + IphoneSE.name)
        print(Fore.CYAN + "Specs: " + IphoneSE.brand)
        print(Fore.CYAN + "Specs: " + IphoneSE.price)
        print(Fore.CYAN + "Specs: " + IphoneSE.buyer)
        print(Fore.CYAN + "Specs: " + IphoneSE.address)
        print(Fore.CYAN + "Specs: " + IphoneSE.CPU)
        print(Fore.CYAN + "Specs: " + IphoneSE.CameraQuality)
        print(Fore.CYAN + "Specs: " + IphoneSE.Storage)
    elif OpB == "2":
        print("Alright Here You Go")
        print(Fore.LIGHTRED_EX + "Specs: " + IphoneXR.name)
        print(Fore.LIGHTRED_EX + "Specs: " + IphoneXR.brand)
        print(Fore.LIGHTRED_EX + "Specs: " + IphoneXR.price)
        print(Fore.LIGHTRED_EX + "Specs: " + IphoneXR.buyer)
        print(Fore.LIGHTRED_EX + "Specs: " + IphoneXR.address)
        print(Fore.LIGHTRED_EX + "Specs: " + IphoneXR.CPU)
        print(Fore.LIGHTRED_EX + "Specs: " + IphoneXR.CameraQuality)
        print(Fore.LIGHTRED_EX + "Specs: " + IphoneXR.Storage)
    elif OpB == "3":
        print("Alright Here You Go")
        print(Fore.GREEN + "Specs: " + iPhone13ProMax.name)
        print(Fore.GREEN + "Specs: " + iPhone13ProMax.brand)
        print(Fore.GREEN + "Specs: " + iPhone13ProMax.price)
        print(Fore.GREEN + "Specs: " + iPhone13ProMax.buyer)
        print(Fore.GREEN + "Specs: " + iPhone13ProMax.address)
        print(Fore.GREEN + "Specs: " + iPhone13ProMax.CPU)
        print(Fore.GREEN + "Specs: " + iPhone13ProMax.CameraQuality)
        print(Fore.GREEN + "Specs: " + iPhone13ProMax.Storage)
    elif OpB == "4":
        print("Okay There Ya Go")
        print(Fore.LIGHTMAGENTA_EX + "Specs: " + Iphone12ProMax.name)
        print(Fore.LIGHTMAGENTA_EX + "Specs: " + Iphone12ProMax.brand)
        print(Fore.LIGHTMAGENTA_EX + "Specs: " + Iphone12ProMax.price)
        print(Fore.LIGHTMAGENTA_EX + "Specs: " + Iphone12ProMax.buyer)
        print(Fore.LIGHTMAGENTA_EX + "Specs: " + Iphone12ProMax.address)
        print(Fore.LIGHTMAGENTA_EX + "Specs: " + Iphone12ProMax.CPU)
        print(Fore.LIGHTMAGENTA_EX + "Specs: " + Iphone12ProMax.CameraQuality)
        print(Fore.LIGHTMAGENTA_EX + "Specs: " + Iphone12ProMax.Storage)
    elif OpB == "5":
        print("Alrighty You Won't Like It") 
        print(Fore.LIGHTWHITE_EX + "Specs: " + Iphone13Pro.name)
        print(Fore.LIGHTWHITE_EX + "Specs: " + Iphone13Pro.brand)
        print(Fore.LIGHTWHITE_EX + "Specs: " + Iphone13Pro.price)
        print(Fore.LIGHTWHITE_EX + "Specs: " + Iphone13Pro.buyer)
        print(Fore.LIGHTWHITE_EX + "Specs: " + Iphone13Pro.address)
        print(Fore.LIGHTWHITE_EX + "Specs: " + Iphone13Pro.CPU)
        print(Fore.LIGHTWHITE_EX + "Specs: " + Iphone13Pro.CameraQuality)
        print(Fore.LIGHTWHITE_EX + "Specs: " + Iphone13Pro.Storage)
    else:
        print(Fore.RED + "Sorry Guy No More Phones I'll Have To Buy Them")
    
    buyme = input("Hey Which One Of These Phones Do You Wanna Buy?: ")

    if buyme == "Iphone13Pro":
        print(Fore.GREEN + "Alright Pay Me Please Give Me Your Card Details: ")
        card_num = input("What Card Number: ")
        Expiration = input("What Expiration Date: ")
        cvv = input("What CVV Number: ")
        card_holder = input(Fore.RED + "Under Whose Name Is The Card Registered To?: ")
        print("Please Verify Your Card Details:")
        print(card_num)
        print(Expiration)
        print(cvv)
        print(card_holder)
        ilycg = input("Is This Correct Info?:")
        if ilycg == "No":
            print("Sorry Well Retry It Again Work In Progress For This Store!")
        elif ilycg == "yes":
            print(Fore.YELLOW + "Alright Payment Maid! Enjoy Your Phone First Look At It")
            print("Congratulations On Your First Purchase From The Banana Store!")
    elif buyme == "IphoneXR":
        print("Alright Fill in the Card Details")
        print(Fore.GREEN + "Alright Pay Me Please Give Me Your Card Details: ")
        card_num = input("What Card Number: ")
        Expiration = input("What Expiration Date: ")
        cvv = input("What CVV Number: ")
        card_holder = input(Fore.RED + "Under Whose Name Is The Card Registered To?: ")
        print("Please Verify Your Card Details:")
        print(card_num)
        print(Expiration)
        print(cvv)
        print(card_holder)
        ilycg = input("Is This Correct Info?:")
        if ilycg == "No":
            print("Sorry Well Retry It Again Work In Progress For This Store!")
        elif ilycg == "yes":
            print(Fore.YELLOW + "Alright Payment Maid! Enjoy Your Phone First Look At It")
            print("Congratulation On Your IphoneXR From The Dark Web!")
    elif buyme == "Iphone SE":
        print("Alright Fill in the Card Details")
        print(Fore.GREEN + "Alright Pay Me Please Give Me Your Card Details: ")
        card_num = input("What Card Number: ")
        Expiration = input("What Expiration Date: ")
        cvv = input("What Is Your CVV Number: ")
        card_holder = input(Fore.RED + "Under Whose Name Is The Card Registered To?: ")
        print("Please Verify Your Card Details:")
        print(card_num)
        print(Expiration)
        print(cvv)
        print(card_holder)
        ilycg = input("Is This Correct Info?:")
        if ilycg == "No":
            print("Sorry Well Retry It Again Work In Progress For This Store!")
        elif ilycg == "yes":
            print(Fore.YELLOW + "Alright Payment Maid! Enjoy Your Phone First Look At It")
            print("Congratulations On Your Purchase!")
        elif buyme == "Iphone12ProMax":
            print("Alright Fill in the Card Details")
        print(Fore.GREEN + "Alright Pay Me Please Give Me Your Card Details: ")
        card_num = input("What Card Number: ")
        Expiration = input("What Expiration Date: ")
        cvv = input("What Is Your CVV Number: ")
        card_holder = input(Fore.RED + "Under Whose Name Is The Card Registered To?: ")
        print("Please Verify Your Card Details:")
        print(card_num)
        print(Expiration)
        print(cvv)
        print(card_holder)
        ilycg = input("Is This Correct Info?:")
        if ilycg == "No":
            print("Sorry Well Retry It Again Work In Progress For This Store!")
        elif ilycg == "yes":
            print(Fore.YELLOW + "Alright Payment Maid! Enjoy Your Phone First Look At It")
            print("Congratulations On Your Purchase!")
    elif buyme == "Iphone13ProMax":
        print("Alright Fill in the Card Details")
        print(Fore.GREEN + "Alright Pay Me Please Give Me Your Card Details: ")
        card_num = input("What Card Number: ")
        Expiration = input("What Expiration Date: ")
        cvv = input("What Is Your CVV Number: ")
        card_holder = input(Fore.RED + "Under Whose Name Is The Card Registered To?: ")
        print("Please Verify Your Card Details:")
        print(card_num)
        print(Expiration)
        print(cvv)
        print(card_holder)
        ilycg = input("Is This Correct Info?:")
        if ilycg == "No":
            print("Sorry Well Retry It Again Work In Progress For This Store!")
        elif ilycg == "yes":
            print(Fore.YELLOW + "Alright Payment Maid! Enjoy Your Phone First Look At It")
            print("Congratulations On Your iPhone")
        else:
            print("Sorry Not Available!:(")
except:
    print("Sorry Not Available")
