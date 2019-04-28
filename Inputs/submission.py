import sys

if __name__ == "__main__":
    inputFile = sys.argv[1]
    photoBase = sys.argv[2]
    fileOpen = open(inputFile, "r")
    photoBase = open(photoBase, "r")
    for line in fileOpen: