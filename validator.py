import re
def validate(string):
    top_level = ["com","net","org","tech"]
    ctr = string.count('@')
    if ctr == 1:
        name = string[:string.index("@")]
        pattern = r'^(?![_.])(?!.*\.$)[A-Za-z0-9._-]{3,24}$'
        if re.match(pattern, name):
            pattern2 = r'^[A-Za-z0-9.-]{3,12}$'
            domain = string[string.index('@')+1:string.rfind('.')]
            if re.match(pattern2,domain):
                top = string[string.rfind('.')+1:]
                if top in top_level:
                    return True 
    return False

if __name__ == "__main__":
    email = input("Enter email:\n")
    output = validate(email)
    if(output):
        print("Email is valid")
    else:
        print("Email is invalid")