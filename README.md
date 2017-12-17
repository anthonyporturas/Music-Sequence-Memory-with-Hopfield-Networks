# Music-Sequence-Memory-with-Hopfield-Networks
Remembering saved musical sequences from incorrect or incomplete sequences by implementing a Hopfield Network.

## Brief Explanation
The implementation here is specifically adjusted for our needs. Inverse saved states that are typical in Hopfield Networks are not saved into the system. The weight change in the Hebbian Learning process is important to note. The scaling of the factor varies by a function on the number of measures. At 4 measures, a weight gain of 4 is best. At 8 measures, a weight gain of 6 is best. This is found on Line 53.

## Instructions
Run "mainproj.py". Do not play more notes than the number of measures multiplied by the number of beats. You can modify that in the same file. QWERTYUI correlates to pressing CDEFGABHigh_C, respectively.
