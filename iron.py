a = {"jerry":1, "musa":2, "scofield":3}
b = int(input("What is your password: "))


def new_file(f):
    '''w = open('exampl45.txt', 'w')
    w.write("this is a new project")
    w.close()'''

    wp= open('exampl45.txt', 'r')
    w = wp.read()
    w = w.splitlines()

    if f in w:
        return "the item is in the list"
    else:
        return "no new file found"

if b in a.values():
    ws = input("Enter the value: ")
    print(new_file(ws))
else:
    print("Password is Incorrect!!")
    print("Only the following people can access the code")
    for key in a.keys():
        print(key)


