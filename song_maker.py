import argparse


class Song:

    def __init__(self, name : str, primary_artists : list, bpm : int, chords : list):
        self.name = name
        self.artists = {'primary_artist' : primary_artists, 'features' : []}
        self.bpm = bpm
        self.chords = chords


    def associated_artists(self, other_artists : str):
        self.artists["features"].append(other_artists)

    def change_beat(self, increase = True, change = 5):
        if increase == True:
            self.bpm += change

        if increase == False:
            self.bpm -= change
            
      
    def modulate(self, steps = 1):
        chromatic_scale = ['C', 'C#' ,'D','D#','E','F','F#','G','G#','A','A#','B']
        modulated_chords = []
        for chord in self.chords:
            if chord in chromatic_scale:
                original_index = chromatic_scale.index(chord)
                new_index = (original_index + int(steps * 2)) % len(chromatic_scale)
                modulated_chords.append(chromatic_scale[new_index])
        self.chords = modulated_chords
               

    def info(self):
        nacb = (f"The name of your artist is: {self.name}, "
                f"your artist featured is: {self.artists}, "
                f"your artists chord is: {self.chords}, "
                f"the songs beats per minute is: {self.bpm}")
        return nacb

    if __name__ == "__main__":
        
        #If name == main statements are statements that basically ask:
        #Is the current script being run natively or as a module?

        #It the script is being run as a module, the block of code under this will not beexecuted.
        #If the script is being run natively, the block of code below this will be executed.

        arguments = parse_args(sys.argv[1:]) #Pass in the list of command line arguments to the parse_args function.
        
        #The returned object is an object with those command line arguments as attributes of an object.
        #We will pass both of these arguments into the main function.
        #Note that you do not need a main function, but you might find it helpfull.
        #You do want to make sure to have minimal code under the 'if __name__ == "__main__":' statement.

        print(info())
