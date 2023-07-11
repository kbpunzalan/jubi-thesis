import os
os.system('cls')

def printCount(counter, line):
    print("============")
    print(counter)
    print(line)
    print("============")

def genderCheck(line, my_dict):
    if line == 1:
        my_dict['bilang_lalaki'] += 1
    elif line == 2:
        my_dict['bilang_babae'] += 1

def educationCheck(line, my_dict):
    if line == 1:
        my_dict['bilang_hindi_nakapagaral'] += 1
    elif line == 2:
        my_dict["bilang_elementarya"] += 1
    elif line == 3:
        my_dict["bilang_highschool"] += 1
    elif line == 4:
        my_dict["bilang_vocational"] += 1
    elif line == 5:
        my_dict["bilang_college"] += 1
    elif line == 6:
        my_dict["bilang_postgrad"] += 1

def personalProfile(my_dict):
    print("PERSONAL INFORMATION")
    
    gender = int(input("Enter Gender (1 or 2): "))
    genderCheck(gender, my_dict)

    education = int(input("Enter Education (1-6): "))
    educationCheck(education, my_dict)

    kabuhayan = input("Enter Kabuhayan: ")
    my_dict['kabuhayan'].append(kabuhayan)

    
    return my_dict
    
def householdInfo():
    my_dict = {
        "number_household": 1, # di kasama yung ininterview
        "bilang_lalaki": 0,
        "bilang_babae": 0,
        "bilang_hindi_nakapagaral": 0,
        "bilang_elementarya": 0,
        "bilang_highschool": 0,
        "bilang_vocational": 0,
        "bilang_college": 0,
        "bilang_postgrad": 0,
        "kabuhayan": []
    }

    counter = 0
    # my_dict = personalProfile(my_dict)
    with open('file.txt', 'r') as file:
        for line in file:
            if line == '\n':
                file.readline() # since dalawa yung lines, read ka pa ng isa  
            else:
                line = line.replace('\n', '') # just remove \n kasi readline ang gamit

                #! KASARIAN
                if counter == 0:
                    line = int(line)
                    genderCheck(line, my_dict)

                #! NATAPOS NA EDUKASYON
                elif counter == 2:
                    line = int(line)
                    my_dict['number_household'] += 1 # increment a family member
                    educationCheck(line, my_dict)

                elif counter == 3:
                    my_dict["kabuhayan"].append(line)


            printCount(counter, line)
                
            counter += 1

            if counter == 4:
                counter = 0

            # just remove all occurrences of "wala"
            my_dict["kabuhayan"] = [item for item in my_dict["kabuhayan"] if item.lower() != "wala"]
        

    for key, value in my_dict.items():
        print(f"{key}:{value}")
        print()

    return my_dict



def pagbabagoSaPamayanan():
    class CAF:
        def __init__(self, hamon, benepisyo, napakinabangan, satisfaction, katayuan, rason):
            self.hamon = hamon
            self.benepisyo = benepisyo
            self.napakinabangan = napakinabangan
            self.satisfaction = satisfaction
            self.katayuan = katayuan
            self.rason = rason

    
    with open("file.txt", 'r') as file:
        counter = 0
        
        for line in file:
            # line = line.replace('\n', '')

            if counter == 0:
                new_CAF = CAF(None, None, None, None, None, None)
                new_CAF.hamon = line
                counter += 1

            elif counter == 1:
                new_CAF.benepisyo = line
                counter += 1

            elif counter == 2:
                new_CAF.napakinabangan = line
                counter += 1

            elif counter == 3:
                print("LINEEEE", line)
                new_count = 0
                if line == "/":
                    new_count == 5

                while file.readline == "\n":
                    file.readline()

                # while line == "\n":
                #     file.readline


                # new_CAF.satisfaction = check_count * 20
                counter += 1
            elif counter == 5:
                for attribute, value in vars(new_CAF).items():
                    print(value)
                counter = 0
                print()

            else:
                counter += 1
