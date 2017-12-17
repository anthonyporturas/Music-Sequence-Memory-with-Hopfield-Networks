import HopfieldNetwork
import piano

measure = 1 #measure #NOTE TO USER: IF YOU WANT SONGS TO BE LONGER THAN ONE MEASURE, CHANGE THIS VALUE
beatsPerMeasure = 4 #number of beats per measure
# hopfield network to save, remember and complete song sequences
# 8 notes (i.e. one octave), 4 beats per measure, 1 measure
# notes must be 8, other values can vary
# the user should not play more notes than beatsPerMeasure * measure
hf = HopfieldNetwork.HopfieldMusic(8,beatsPerMeasure, measure)


#save the song that the user plays
def saveSongs():
    pi = piano.piano()
    print()
    print("The song you played is:")
    print(pi.chords)
    hf.enterSongToSave(pi.chords)

#remember the saved song that most closely resembles what the user plays
def rememberSong():
    pi = piano.piano()
    print()
    print("The song you played is:")
    print(pi.chords)
    hf.enterSongToRemember(pi.chords)
    print()
    

#complete a song given the partial song sequence from user
def completeSong():
    pi = piano.piano()
    songCompletion = hf.getSongCompletion(pi.chords)
    print()
    print("The song you played is:")
    print(pi.chords)
    print()
    print("The song completion is:")
    print(songCompletion) #text for the completed song
    pi.playCompleteSong(songCompletion) #audio for the completed song

#MENU for the piano app
menu = {}
menu['1']="Save a song" #user plays a song and we save it
menu['2']="Remember a song" #user plays a song and we see which saved song it most resembles
menu['3']="Complete a song" #user plays part of a song and we complete the song based on which saved song it most resembles
menu['4']="Exit" #exit the app


savedASongBool = False #becomes true if the user has saved at least one song

#run a loop until user exits
while True: 
    options=menu.keys()
    
    print('MENU')
    for entry in options: 
      print(entry, menu[entry])

    choice=input("Enter your choice:") 
    if choice =='1': 
      savedASongBool = True
      saveSongs()
    elif choice == '2': 
      if savedASongBool != True:
        print("You must save a song before you can remember a song")
      else:
        rememberSong()
    elif choice == '3':
      if savedASongBool != True:
        print("You must save a song before you can complete a song")
      else:
        completeSong()
    elif choice == '4': 
      break
    else: 
      print("Invalid choice")

    print()

