import os
from random import randint
import sys

def setup():
    number = randint(0, 15)
    for i in range(number):
        os.mkdir(f"dir_{i}")
        num_of_files = randint(0, 10)
        for j in range(num_of_files):
            with open(f"dir_{i}/file_{j}.txt", "w") as file:
                num_to_write = randint(0, 100)
                file.write(f"Hello from file_{i}.txt\n")
                file.write(f"Random number: {num_to_write}\n")

def delete():
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            name = os.path.join(root, name)
            if name.find("git") == -1 and name.find("main") == -1 and name.find("READ") == -1 and name.find("Output") == -1:
                #print(f"Deleting {name}")
                os.remove(name)

        for name in dirs:
            name = os.path.join(root, name)
            if name.find("git") == -1:
                #print(f"Deleting {name}")
                os.rmdir(os.path.join(root, name))

def print_file_contents(file):
    with open(file, "r") as f:
        print(f.read())

def print_dir_contents(dir):
    for root, dirs, files in os.walk(dir):
        for name in files:
            name = os.path.join(root, name)
            print_file_contents(name)

        for name in dirs:
            name = os.path.join(root, name)
            print(f"Dir: {name}")

def print_files():
    for root, dirs, files in os.walk("."):
        for name in files:
            name = os.path.join(root, name)
            if name.find("git") == -1:
                print(f"File: {name}")

        for name in dirs:
            name = os.path.join(root, name)
            if name.find("git") == -1:
                print(f"Dir: {name}")
    
def main():
    sys.stdout = open("Output.txt", "w")
    print("Files created.")
    setup()

    print_files()

    print("Deleting files...")
    delete()

    print_files()
    sys.stdout.close()

if __name__ == "__main__":
    main()