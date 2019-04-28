import sys
import pprint

def pictureIndexer(pictureBase):
    pictureIndex = {}
    numPic = 0
    f = open(pictureBase, "r")
    f.readline()
    for line in f:
        pictureIndex[numPic]=line.rstrip()
        numPic+=1
    return pictureIndex

def tagsFromPicture(pictureNumber, pictureIndex):
    pictureDescription = pictureIndex[int(pictureNumber)]
    return(pictureDescription[4:].split())

def verticalTags(pic1number, pic2number, pictureIndex):
    picture1Tags = tagsFromPicture(pic1number, pictureIndex)
    picture2Tags = tagsFromPicture(pic1number, pictureIndex)
    totalTags = list(set.union(set(picture1Tags), set(picture2Tags)))
    return totalTags

def puntuateSlides(submissionFile, pictureIndex):
    tagsRepresentation = []
    punctuation = 0
    f = open(submissionFile, "r")
    f.readline()
    for line in f:
        pictures = line.split()
        if len(pictures) > 1:
            tagsRepresentation.append(verticalTags(pictures[0],pictures[1],pictureIndex))
        else:
            tagsRepresentation.append(tagsFromPicture(pictures[0], pictureIndex))

    for i in range(len(tagsRepresentation)-1):
        setTags1 = set(tagsRepresentation[i])
        setTags2 = set(tagsRepresentation[i+1])
        pprint.pprint(setTags1)
        pprint.pprint(setTags2)
        intersection = len(setTags1.intersection(setTags2))
        leftDif = len(setTags1.difference(setTags2))
        rightDif = len(setTags2.difference(setTags1)) 
        print(intersection, leftDif, rightDif)
        pprint.pprint("")

        points = min(intersection, leftDif, rightDif)
        punctuation += points

    return punctuation

if __name__ == "__main__":
    inputFile = sys.argv[1]
    pictureBase = sys.argv[2]
    fileOpen = open(inputFile, "r")
    
    pictureIndex = pictureIndexer(pictureBase)
    pprint.pprint(pictureIndex)
    print(puntuateSlides(inputFile, pictureIndex))