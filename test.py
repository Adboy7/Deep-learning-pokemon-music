from music21 import *
import glob







if __name__ == "__main__":
    i=0
    # for midi in glob.glob("test/*.mid"):
    for midi in glob.glob("midi/*.mid"):
        i=i+1
        notes_to_parse = None
        print(midi)
        mu = converter.parse(midi)
        # for element in mu.recurse():
        #     print(element)
        s2=instrument.partitionByInstrument(mu)
        notes_to_parse = s2.parts[0].recurse() 
        # for element in notes_to_parse:
        #     print(element)
    print(i)