from tkinter import *  # for the gui
import pygame  # for the music
import os  # used to get filepaths
import time # for the time delay between playing musical notes

class piano:
    def __init__(self):
        self.chordTime = 0.25 # seconds used to determine if multiple notes together are a chord
        self.past = time.time() # initializes time check
        self.localPath = "/musicalNotes/"
        self.root = Tk()  # the root window
        self.root.title('Piano')
        self.topFrame = Frame(self.root)  # we'll use this frame for the piano keys
        self.topFrame.pack()  # put the frame on the window
        
        self.script_dir = os.path.dirname(
        os.path.abspath(__file__))  # filepath for the directory that this file exists in. (this file is piano.py)

        pygame.init()  # initialize pygame

        # buttons for each of the musical musicalNotes

        Cbutton = Button(self.topFrame, text="C", fg="black", bg="white", height=8, width=3, command=self.soundForC)
        Cbutton.pack(side=LEFT)
        Dbutton = Button(self.topFrame, text="D", fg="black", bg="white", height=8, width=3, command=self.soundForD)
        Dbutton.pack(side=LEFT)
        Ebutton = Button(self.topFrame, text="E", fg="black", bg="white", height=8, width=3, command=self.soundForE)
        Ebutton.pack(side=LEFT)
        Fbutton = Button(self.topFrame, text="F", fg="black", bg="white", height=8, width=3, command=self.soundForF)
        Fbutton.pack(side=LEFT)
        Gbutton = Button(self.topFrame, text="G", fg="black", bg="white", height=8, width=3, command=self.soundForG)
        Gbutton.pack(side=LEFT)
        Abutton = Button(self.topFrame, text="A", fg="black", bg="white", height=8, width=3, command=self.soundForA)
        Abutton.pack(side=LEFT)
        Bbutton = Button(self.topFrame, text="B", fg="black", bg="white", height=8, width=3, command=self.soundForB)
        Bbutton.pack(side=LEFT)
        HighCbutton = Button(self.topFrame, text="High\nC", fg="black", bg="white", height=8, width=3,
                             command=self.soundForHighC)
        HighCbutton.pack(side=LEFT)
        EmptyBeatbutton = Button(self.topFrame, text="Empty\nBeat", fg="black", bg="white", height=8, width=5, command=self.emptyBeat)
        EmptyBeatbutton.pack(side=LEFT)
        
        self.root.bind('q',self.soundForC)
        self.root.bind('w', self.soundForD)
        self.root.bind('e', self.soundForE)
        self.root.bind('r', self.soundForF)
        self.root.bind('t', self.soundForG)
        self.root.bind('y', self.soundForA)
        self.root.bind('u', self.soundForB)
        self.root.bind('i', self.soundForHighC)
        self.root.bind('o', self.emptyBeat)

        self.chords = []

        self.root.mainloop()  # keep gui on screen until user closes window

    # functions to play the sound for each musical note
    
    def soundForC(self,event=None):
        if self.checkTime():
            self.chords.append("C")
        else:
            self.chords[len(self.chords)-1] = self.chords[len(self.chords)-1] + "C"
        relativePath = "C.wav"
        absolutePath = self.script_dir + self.localPath + relativePath
        sound = pygame.mixer.Sound(absolutePath)
        sound.play()
        return


    def soundForD(self,event=None):
        if self.checkTime():
            self.chords.append("D")
        else:
            self.chords[len(self.chords)-1] = self.chords[len(self.chords)-1] + "D"
        relativePath = "D.wav"
        absolutePath = self.script_dir + self.localPath + relativePath
        sound = pygame.mixer.Sound(absolutePath)
        sound.play()
        return


    def soundForE(self,event=None):
        if self.checkTime():
            self.chords.append("E")
        else:
            self.chords[len(self.chords)-1] = self.chords[len(self.chords)-1] + "E"
        relativePath = "E.wav"
        absolutePath = self.script_dir + self.localPath + relativePath
        sound = pygame.mixer.Sound(absolutePath)
        sound.play()
        return


    def soundForF(self,event=None):
        if self.checkTime():
            self.chords.append("F")
        else:
            self.chords[len(self.chords)-1] = self.chords[len(self.chords)-1] + "F"
        relativePath = "F.wav"
        absolutePath = self.script_dir + self.localPath + relativePath
        sound = pygame.mixer.Sound(absolutePath)
        sound.play()
        return


    def soundForG(self,event=None):
        if self.checkTime():
            self.chords.append("G")
        else:
            self.chords[len(self.chords)-1] = self.chords[len(self.chords)-1] + "G"
        relativePath = "G.wav"
        absolutePath = self.script_dir + self.localPath + relativePath
        sound = pygame.mixer.Sound(absolutePath)
        sound.play()
        return


    def soundForA(self,event=None):
        if self.checkTime():
            self.chords.append("A")
        else:
            self.chords[len(self.chords)-1] = self.chords[len(self.chords)-1] + "A"
        relativePath = "A.wav"
        absolutePath = self.script_dir + self.localPath + relativePath
        sound = pygame.mixer.Sound(absolutePath)
        sound.play()
        return


    def soundForB(self,event=None):
        if self.checkTime():
            self.chords.append("B")
        else:
            self.chords[len(self.chords)-1] = self.chords[len(self.chords)-1] + "B"
        relativePath = "B.wav"
        absolutePath = self.script_dir + self.localPath + relativePath
        sound = pygame.mixer.Sound(absolutePath)
        sound.play()
        return


    def soundForHighC(self,event=None):
        if self.checkTime():
            self.chords.append("^C")
        else:
            self.chords[len(self.chords)-1] = self.chords[len(self.chords)-1] + "^C"
        relativePath = "HighC.wav"
        absolutePath = self.script_dir + self.localPath + relativePath
        sound = pygame.mixer.Sound(absolutePath)
        sound.play()
        return
        
    def emptyBeat(self,event=None):
        self.chords.append("?")
        return
        
    def playCompleteSong(self, song):
        for i in range(len(song)):
            time.sleep(1) #sleep for 1 second (to allow time between each musical note)

            for j, note in enumerate(song[i]):
                #play each note in the completed song
                if j>0 and song[i][j-1] == "^" and note == "C":
                    pass
                elif note == "C":
                    relativePath = "\musicalNotes\C.wav"
                    absolutePath = self.script_dir + relativePath
                    sound = pygame.mixer.Sound(absolutePath)
                    sound.play()
                elif note == "D":
                    relativePath = "\musicalNotes\D.wav"
                    absolutePath = self.script_dir + relativePath
                    sound = pygame.mixer.Sound(absolutePath)
                    sound.play()
                elif note == "E":
                    relativePath = "\musicalNotes\E.wav"
                    absolutePath = self.script_dir + relativePath
                    sound = pygame.mixer.Sound(absolutePath)
                    sound.play()
                elif note == "F":
                    relativePath = "\musicalNotes\F.wav"
                    absolutePath = self.script_dir + relativePath
                    sound = pygame.mixer.Sound(absolutePath)
                    sound.play()
                elif note == "G":
                    relativePath = "\musicalNotes\G.wav"
                    absolutePath = self.script_dir + relativePath
                    sound = pygame.mixer.Sound(absolutePath)
                    sound.play()
                elif note == "A":
                    relativePath = "\musicalNotes\A.wav"
                    absolutePath = self.script_dir + relativePath
                    sound = pygame.mixer.Sound(absolutePath)
                    sound.play()
                elif note == "B":
                    relativePath = "\musicalNotes\B.wav"
                    absolutePath = self.script_dir + relativePath
                    sound = pygame.mixer.Sound(absolutePath)
                    sound.play()
                elif note == "^":
                    relativePath = "\musicalNotes\HighC.wav"
                    absolutePath = self.script_dir + relativePath
                    sound = pygame.mixer.Sound(absolutePath)
                    sound.play()
                elif note == "?":
                    pass
                else:
                    print(note," is an invalid note")

    # checks to see if the time threshold has been reached
    # if the threshold is reached, returns true. otherwise, false
    def checkTime(self):
        currentTime = time.time()
        if currentTime - self.past >= self.chordTime:
            self.past = currentTime
            return True
        else:
            return False