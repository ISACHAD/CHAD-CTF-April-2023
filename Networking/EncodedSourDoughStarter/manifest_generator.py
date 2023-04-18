import random 
import string 
import json
import base64
import os

'''
Generates a manifest to annoy players 

Container number, container location, container ISO, container color, owner, items present, claimed weight, measured weight, valuation, insurance, security lock number 
'''

number_of_containers = 40
number_of_ships = 20
number_of_convoys = 5
container_weight = 15000
width = 32
length = 60

colors = ["red", "blue", "green", "red", "blue", "green", "red", "blue", "green", "purple", "tan", "orange"]

ISO_lookup = {
    "A":10, "B":12, "C":13, "D":14, "E":15, "F":16, "G":17, "H":18, "I":19, "J":20, "K":21, "L":23, "M":24, "N":25, "O":26, "P":27, "Q":28, "R":29, "S":30, "T":31, "U":32, "V":34, "W":35, "X":36, "Y":37, "Z":38 
    }



items = {
    "electronics" : 750,
    "weapons" : 200,
    "food" : 50,
    "toys" : 75,
    "chemicals" : 500,
    "furniture" : 30,
    "machine_parts" : 300,
    "entertainment" : 100
}

owner_name_part = ["stock", "CHAD", "orient", "occident", "Flag", "Flagstaff", "Flagged","{F....}","{", "eastern", "western", "East", "West", "North", "import", "export", "prime", "essential", "service", "offering", "marketing", "digital", "Japan", "India", "United", "States", "American", "Euro", "European", "Pan", "Trans", "Inter", "Intra", "South", "Shipping", "factory", "site", "contractors", "contracting", "office", "park", "Swift", "Hustle", "Alliance", "}"]

final = ["ltd", "co", "LLC", "Conglomerate", "Corp", "soft", "Shipping", "contractors", "inc", "co-op", "cooperative", "Alliance", "subsidiary", "}"]

#https://www.container-xchange.com/blog/container-number/


def random_char(y):
    return ''.join(random.choice(string.ascii_letters).upper() for x in range(y))
       

def random_num(y):
    return ''.join(random.choice(string.digits) for x in range(y))
       

def calculate_check(three, u, six):
    ret = 0;
    part_1 = 0;
    part_2 = 0;
    mult = 1;

    storage = []
    data = f"{three}{u}"
    
    for i in data:
        storage.append(ISO_lookup[i])
    for i in six:
        storage.append(int(i))

    for i in storage:
        part_1 += i * mult 
        part_2 += i * mult 
        mult = mult * 2

    part_2 = int(part_2/11)
    part_2 = part_2 * 11

    res = part_1-part_2

    return res
    

def generate_name():

    ret = ""

    for i in range(0, random.randint(2,5)):
        ret += f"{random.choice(owner_name_part).upper()} "
    ret += f"{random.choice(final).upper()}"
    
    new = ""

    while new != ret:
        new = ret.replace("  ", " ")
        ret = new
        new = ret.replace("  ", " ")

    return ret
    

def generate_actual_weight(weight):
    rang = weight * .05 
    return random.gauss(weight, rang)


def generate_estimated_weight(weight):
    rang = weight * .15 
    return random.gauss(weight*.85, rang)
    

def generate_value(weight, item):
    rang = weight*items[item] * .05 
    med = weight*items[item]
    return random.gauss(med, rang)


def get_insurance(price):
    return price * random.uniform(1.0,1.2)


def generate_lock():
    return random.randbytes(4)


def shipping_iso_number():
    three = random_char(3)
    u = 'U'
    six = random_num(6) 
    check = calculate_check(three, u, six)
    return f"{three}{u}{six}{check}"


def container_location(number, width, length):
    curr = 0 
    curr_height = 0
    curr_width = 0
    curr_length = 0
    while curr < number:
        curr += 1
        curr_width+=1
        if(curr_width == width):
            curr_width = 0
            curr_length += 1
        if(curr_length == length):
            curr_length = 0
            curr_height += 1

    return {"height":curr_height, "width":curr_width, "length":curr_length}


def generate_line_item(number):
    #Container number, container location, container ISO, container color, owner, items present, claimed weight, measured weight, valuation, insurance, security lock number 
    locl = container_location(number, width, length)
    iso = shipping_iso_number()
    color = random.choice(colors)
    owner = generate_name()
    item = random.choice(list(items.keys()))
    claimed_weight = generate_estimated_weight(container_weight)
    actual_weight = generate_actual_weight(container_weight)
    valuation = generate_value(claimed_weight, item)
    insurance = get_insurance(valuation)
    lock = generate_lock()

    ret = {"number":f"{number}",
    "location":f"{locl}",
    "iso":f"{iso}",
    "color":f"{color}",
    "owner":f"{owner}",
    "item":f"{item}",
    "claimed_weight":f"{int(claimed_weight)}",
    "actual_weight":f"{int(actual_weight)}",
    "valuation":f"{int(valuation)}",
    "insurance":f"{int(insurance)}",
    "lock_number":f"{str(hex(lock[0])).upper()[2:]}{str(hex(lock[1])).upper()[2:]}{str(hex(lock[2])).upper()[2:]}{str(hex(lock[3])).upper()[2:]}"}

    #return f"{number}\t{locl}\t{iso}\t{color}\t{owner}\t{item}\t{int(claimed_weight)}\t{int(actual_weight)}\t{int(valuation)}\t{int(insurance)}\t{str(hex(lock[0])).upper()[2:]}{str(hex(lock[1])).upper()[2:]}{str(hex(lock[2])).upper()[2:]}{str(hex(lock[3])).upper()[2:]}\t\n"

    return f"{base64.b32encode(json.dumps(ret).encode())}"


def generate_manifest(containers, ships, convoys):

    stor = {}

    curr_num = 0

    target = random.randint(0,convoys*ships*containers)

    flag = {"flag":"CHAD{L4yersUp0nL4yers}"}
    
    encoded_flag = f"{base64.b32encode(json.dumps(flag).encode())}"

    for i in range(0, convoys):
        ship_stor = {}
        for j in range(0, ships):
            temp_stor = []
            for k in range(0, containers):
                temp_stor.append(generate_line_item(i))
                if curr_num == target:
                    print(f"inserting flag at {curr_num}")
                    temp_stor.append(encoded_flag)
                    random.shuffle(temp_stor)
                curr_num += 1
            ship_stor["Ship{j}"] = f"{base64.b16encode(json.dumps(temp_stor).encode())}"

        stor[f"Convoy{i}"] = f"{base64.b64encode(json.dumps(ship_stor).encode())}"

        print(f"{i} Complete")

    with open("./manifest.txt", "w+") as manifest:
        manifest.write(f"{base64.b64encode(json.dumps(stor).encode())}")
        print(f"manifest written {os.getcwd()}")
            

print("Starting b64")
generate_manifest(number_of_containers, number_of_ships, number_of_convoys)
print("finished")
input()
exit(0)
