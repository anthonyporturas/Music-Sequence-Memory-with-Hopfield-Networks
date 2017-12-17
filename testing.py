import HopfieldNetworkTesting
import random
import time
noteArray = ['C','D','E','F','G','A','B','^C']

def createRandomStates(beats,measures,numTests):
    output = []
    for testNumber in range(numTests):
        test = []
        for i in range(beats*measures):
            test.append(random.choice(noteArray))
        output.append(test)
    return output

def randomlyAlter(savedStates, numTests, numChange):
    output = []
    original = []
    for testNumber in range(numTests):
        ref = random.choice(savedStates)
        test = []
        test.extend(ref)

        original.append(list(ref))
        posSet = set()
        for i in range(numChange):
            pos = random.randint(0, len(test)-1)

            while pos in posSet:
                pos = random.randint(0, len(test)-1)

            posSet.add(pos)
            note = test[pos]
            randNote = random.choice(noteArray)
            while (randNote == note):
                randNote = random.choice(noteArray)

            test[pos] = randNote

        output.append(test)

    return output, original

beats = 4
measures = 8
numTests = 20
numChanges = 1
numRuns = 10
totalCorrect = 0
total = numRuns * numTests

hf = HopfieldNetworkTesting.HopfieldMusic(8,beats,measures)
saved = createRandomStates(beats,measures,numTests)
results = [0] * (beats*measures+1)
for i in range(numTests):
    hf.enterSongToSave(saved[i])

start = time.time()
for i in range(numRuns):
    #print(i)
    [tests, originals] = randomlyAlter(saved,numTests,numChanges)
    for j, test in enumerate(tests):

        remembered = hf.enterSongToRemember(test)
        if remembered == originals[j]:

            results[0] += 1
        else:
            count = 0
            for i in range(len(remembered)):
                #if remembered[i] == '':
                 #   continue
                if remembered[i] != originals[j][i]:
                    count += 1
            results[count] += 1

end = time.time()
print("num of incorrect results percentage")
for i in range(len(results)):
    print(results[i] / total * 100)

print()
print("total time:", end-start)