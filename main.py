from functions import *

def printChoices():
    print("============ CHOICES ===========")
    print("[1] Household's Profile")
    print("[2] B. Pag-unlad at pagbabago sa pamayanan")
    print("[3] ")
    print("================================")


if __name__ == "__main__":
    printChoices()
    choice = int(input("Choice: "))

    if choice == 1:
        my_dict = householdInfo()

        with open('output.txt', 'w') as file:
            for key, value in my_dict.items():
                file.write(f'{value}\t')
    elif choice == 2:
        pagbabagoSaPamayanan()
