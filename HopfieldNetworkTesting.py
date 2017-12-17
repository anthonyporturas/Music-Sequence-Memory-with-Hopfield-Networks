import numpy as np
import random
import LIF

class HopfieldMusic:
    def __init__(self, numNotes, numBeats, numMeasures):
        self.numNotes = numNotes  # number of musicalNotes
        self.numBeats = numBeats  # number of beats per measure
        self.numMeasures = numMeasures  # number of measures
        self.numNeurons = self.numNotes * self.numBeats * self.numMeasures  # number of neurons
        self.weights = np.zeros(shape=(self.numNeurons, self.numNeurons))  # initial weights (all 0)

        self.snn = [] #spiking neural net
        self.snn.append(LIF.main(5, 20, "C"))
        self.snn.append(LIF.main(5, 20, "D"))
        self.snn.append(LIF.main(5, 20, "E"))
        self.snn.append(LIF.main(5, 20, "F"))
        self.snn.append(LIF.main(5, 20, "G"))
        self.snn.append(LIF.main(5, 20, "A"))
        self.snn.append(LIF.main(5, 20, "B"))
        self.snn.append(LIF.main(5, 20, "^C"))
        self.snn.append(LIF.main(5, 20, "?")) #"?" represents the empty beat i.e silence or the unknown note which the remembered state will fill in
       
        self.noteSet = set()
        
        #noteState is the collection of states for all notes (i.e the 8 bit state of the system showing which neurons are spiking based on the given musical note)
        self.noteState = dict(
            [('C', self.snn[0]), 
             ('D', self.snn[1]), 
             ('E', self.snn[2]),
             ('F', self.snn[3]),
             ('G', self.snn[4]), 
             ('A', self.snn[5]), 
             ('B', self.snn[6]),
             ('^C', self.snn[7]),
             ('?', self.snn[8])])
        
        self.randomOrderArray = []
        for i in range(self.numNeurons):
            self.randomOrderArray.append(i)

    # add new state to memory
    # generally hebbian learning, except with a small change to not remember inverse states
    # neuron weights don't increase if both neurons don't fire
    def addState(self, state):
        newWeights = []
        for i in range(len(state)):
            newWeights.append([])
            for j, neuron in enumerate(state):
                weight = 0
                if i != j:
                    if state[i] == neuron and state[i] == 1:
                        weight = 7
                        #weight = 1
                    elif state[i] == neuron and state[i] == 0:
                        weight = 0
                    else:
                        weight = -1
                newWeights[i].append(weight)
        self.weights += newWeights

    # calculate energy of system
    # weights are added to total if the two connecting neurons are both on
    def countEnergy(self, state):
        energy = 0
        for i, neuron in enumerate(state):
            if neuron == 1:
                for j, neuron2 in enumerate(state):
                    if i != j and neuron2 == 1:
                        energy += self.weights[i][j]
        return energy

    # recalls saved states
    # states are randomly selected to turn on or off to test overall system energy
    # the way that the system is created, higher energy values in the code are actually lower energy values theoretically
    def rememberState(self, state):
        totalEnergy = self.countEnergy(state)
        random.shuffle(self.randomOrderArray)
        for i in self.randomOrderArray:
            flip = state[i]
            if flip == 1:
                state[i] = 0
            else:
                state[i] = 1
            currentEnergy = self.countEnergy(state)
            if currentEnergy > totalEnergy:
                totalEnergy = currentEnergy
                return self.rememberState(state)
            else:
                state[i] = flip

        return state


    # saves a song
    # function breaks down each chord and converts the input to a state [x,x,x,x,x,x,x,x]
    # where each x represents whether or not a specific note is played

    def enterSongToSave(self,userInput):
        userSong = userInput
        songState = []
        for note in userSong:
            self.noteSet.add(note)
            chord = [0 for j in range(self.numNotes)]
            highC = False
            for i in range(len(note)):
                if note[i] == '^':
                    highC = True
                    continue

                if highC:
                    chord = map(lambda x, y: x + y, self.noteState['^C'], chord)
                    highC = False
                else:
                    chord = map(lambda x, y: x + y, self.noteState[note[i]], chord)

            songState.extend(chord)

        songState.extend([0 for j in range(self.numNeurons - len(songState))])
        self.addState(songState)

    # remembers a song
    # works similarly to enterSongToSave, except it prints the results
    def enterSongToRemember(self, userInput):
        userSong = []
        userSong.extend(userInput)
        songState = []
        for note in userSong:
            chord = [0 for j in range(self.numNotes)]
            highC = False
            for i in range(len(note)):
                if note[i] == '^':
                    highC = True
                    continue

                if highC:
                    chord = map(lambda x, y: x + y, self.noteState['^C'], chord)
                    highC = False
                else:
                    chord = map(lambda x, y: x + y, self.noteState[note[i]], chord)

            songState.extend(chord)

        songState.extend([0 for j in range(self.numNeurons - len(songState))])
        rememberedState = self.rememberState(songState)
        #print()
        #print("Remembered song:")
        out = []
        for i in range(0, len(rememberedState), self.numNotes):
            #print(self.parseStates(rememberedState[i:(i + self.numNotes)]), sep=' ', end=' ', flush=True)
            out.append(self.parseStates(rememberedState[i:(i + self.numNotes)]))

        return out
   
    
    #get song completion
    # plays the notes you've entered and completes the sequence from memory of previous songs
    def getSongCompletion(self, userInput):
        userSong = userInput
        songState = []
        for note in userSong:
            chord = [0 for j in range(self.numNotes)]
            highC = False
            for i in range(len(note)):
                if note[i] == '^':
                    highC = True
                    continue

                if highC:
                    chord = map(lambda x, y: x + y, self.noteState['^C'], chord)
                    highC = False
                else:
                    chord = map(lambda x, y: x + y, self.noteState[note[i]], chord)

            songState.extend(chord)

        songState.extend([0 for j in range(self.numNeurons - len(songState))])
        rememberedState = self.rememberState(songState)
        
        songCompletion = [] #when user wants to complete a song we play this
        
        for i in range(0, len(rememberedState), self.numNotes):
            songCompletion.append(self.parseStates(rememberedState[i:(i + self.numNotes)]))
            
        return songCompletion
        
    # separates neurons for musicalNotes
    # takes [x,x,x,x,x,x,x,x] and converts it to a chord like "EFG"
    def parseStates(self, state):
        notes = ''
        #silenceCheck = True
        for i in range(len(state)):
            if state[i] == 1:
                #silenceCheck = False
                note = [0 for j in range(self.numNotes)]
                note[i] = 1
                notes += self.statesToNotes(note)

        #if silenceCheck:
         #   notes += "?"
        return notes

    # converts states to musicalNotes
    # reverse dictionary lookup
    def statesToNotes(self, state):
        return list(self.noteState.keys())[list(self.noteState.values()).index(state)]