### note taking:

# day 1:

using pyAudioAnalysis to recognize audio file (.wav or .mp3) first, then try basic feature extraction (bpm)

so scratch that, seems like Librosa is the way to go
ran very simple script, was able to determine BPM of a random music track with very high accuracy
is NOT a fan of .mp3, use .wav

things to note about tempo tracker: is not great at determining time signature, so tempo of fast songs tend to be recorded in half time 

(i.e. 140 bpm --> 69.84 bpm)

actually makes our lives easier since the drone has speed limitations already


# day 2:

there is a way to extract all the times another beat starts, which could prove very helpful for timing dance moves

will look into it more to see if the half-time tempo quirk described above has any effect on these values

the returned beat frames do NOT align with note start times OR the estimated tempo. there are minor fluctuations in the duration
between recorded beats, which is kind of strange, but it means that it is actively listening for beats. something to keep in mind

problem: how to handle audio files that contain "extraneous sounds" (like the start of the Baby Shark video)

based on the returned beat frames, the algorithm recognizes empty space after the music stops playing, which is good

Baby Shark has a tempo of 115 bpm, the algorithm estimated 117.45 bpm

after some experimentation, the algorithm doesn't return anything different, for better or for worse. this means that extraneous
audio shouldn't pose a problem (especially if we are taking song requests on the spot)

however, this also means there's no explanation for the tempo inaccuracy besides noise and, as it stands, there seems to be no real
workaround. taking into account the movement of the drone, however, it's highly unlikely that such a small inaccuracy would create a
noticeable error.

proposed solution: use the estimated BPM to initialize speed of the drone's movements, use the beat frames to make sure the drone
does not fall out of time (move off beat)

now: see if I can use the beat frames to make events happen on time (will just do print statements for now or something)
events can align very accurately with the beat of the music, seemingly adjusting to subtle tempo changes as well. will try seeing
how it fares against music with more noticeable tempo changes (rubato?)

tested on Chopin's Waltz in A Minor: algorithm REALLY does not like drastic tempo changes. gets confused as tempo doesn't usually
change on a whim like that, so sometimes counts extra beats or misses beats. fortunately, it always gets right back on track, so this isn't
really an issue. 

the only thing to note from this: if we have plans on making moves based on time signature (4 different moves for a 4/4 measure, for example),
we can implement a method to check if any beats fluctuate significantly from the average beat length. if it does, then the recorded beats
will not reliably or accurately reflect the actual beats or number of beats per measure. ALSO, we have no means of determining time signature with
this method. however, if Jaden figures out the chord/note recognition, we can use changes in the bass chord as a metric for when measure changes are
happening (C --> A chord, for example) 

a bit of an issue to note with syncing: the program knows to ignore empty noise before and after a song. if we try to sync music playback with the beat
detection, however, the beat detection may start before the actual music starts, causing the program to terminate before the music does. 

brief outline of how music playback and tempo detection works right now:

1. download a .wav
2. pass its path through to the program (maybe implement `input()` to allow for user-inputted music, but would still have to exist on the hard drive)
3. .wav is preprocessed (can take a short while, depending on how long the song is)
4. tempo/sample rate are returned, two arrays are generated (beat times and beat durations)
5. brief countdown begins to allow user time to start music playback, then events begin happening (will be drone movements, but are print statements for now)

flaws with current method: 

.wav files are uncompressed and take up significant hard drive space; we need to be careful with how many songs we decide to go with

music download can also be a lengthy process, taking at least a minute just to get a song (which will pose a problem if we take song reqeusts)

importing the libraries takes a while (nothing we can do here, but just keep that in mind)

currently no way to initiate music playback through the program, so the synchronization between the dance moves and the music falls on the user


tentative proposed solution:

    from pygame import mixer

    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()

use pygame audio player to start music concurrently with the dance sequence

issue: possible to remove silence from start and end of audio file, but no way to save it and play it back. only solution now is to strip it
manually beforehand, which will make it effectively impossible to take live song requests. if we want, we can ask instructors and other people
what songs they would like to hear in advance.


another issue: note recognition is really really difficult, so we may have to rely entirely on the beat to control the dance moves. no feasible
way to implement time signature detection at the moment, so we could ask the user to input the time signature instead if they know.


synchronization is still difficult. we will have to cut the audio files really precisely beforehand in order to get them to sync up properly.
fortunately, most of these examples tend to fall into beat eventually if the audio files aren't perfectly trimmed.




# day 3:

potential issues that may arise with integrating beat with dance moves:

1. **input lag**: the drone may have noticeable lag responding to commands

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;experiment with hardcoded buffers in music playback in order to improve synchronicity 

2. **too fast**: BPM of most songs might be too fast for the drone to dance on every beat

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;determine upper BPM limits of drone movement, half the BPM if songs exceed that tempo

assuming the drone can do 1 move per second:

**0 - 60 BPM**:     1 move per beat

**61 - 120 BPM**:   1 move per 2 beats

**121+ BPM**:

    if (beats_per_measure % 3 == 0):      # if the beats per measure is evenly divisible by 3
        do_move every 3 beats

    elif (beats_per_measure < 6):         # if the beats per measure is not 3 and less than 6
        do_move at start of measure

    elif (beats_per_measure > 6):         # if the beats per measure is not evenly divisible by 3 and more than 6
        x = beats_per_measure // 3
        do_move x times per measure
    
things to note: so far, the algorithm hasn't really recognized any songs outside of the 61-120 bpm threshold; songs outside of this range are either so slow
or so fast that they are classified in double time or half-time, respectively. though I'll keep these conditionals just in case, the more important thing to
consider here is the time signature, *not* the tempo.

here's why:

in most cases, music will fall under the 61-120 bpm category, which means a dance move should occur every 2 beats (every odd beat). however, you would also
have to consider the time signature; if there is an odd number of beats per measure, then the program would inevitably send two commands in a row. for example:

    BEATS
    1    2    3    4    5 || 1    2    3    4    5
    ^         ^         ^    ^         ^         ^

in a time signature of 3/4, 5/4, 7/4, etc... a dance move occurs at the start *and* end of a measure, so a check needs to be put in place to make sure
no dance move occurs on the last beat. so, adding onto the info above:

**61 - 120 BPM**:   1 move per 2 beats

    if beat % 2 == 1:       # if the beat is an odd number
        if beat != beats_per_measure:       # if not the last beat
            do_move

also, we need to make special cases for when the time signature is equal to 0 and 1. since there are so few beats, the dance move exceptions cannot be measure
based, but instead based on the absolute beat of the song (e.g. beat 43 of the song vs. beat 3 of measure 11)

these numbers are subject to change, but until we try testing the drone at these speeds, it's unclear if this pacing is too quick. will revisit later.

## FOR INTEGRATION:

1. provide a snippet of the song
2. based on this snippet, the user can decide how many beats they want per measure (and add a pickup note)
3. ask user to draw dance moves
4. calculate when the dance moves will happen in each measure
5. drone takeoff
6. begin music playback and start dance sequence
7. iterate through dance move sequence (generated by user), using times calculated in music preprocessing node

steps already done:

- all user input (drawings, music info)
- beat calculation (when dance moves are going to happen)
- music playback and sequence initialization

steps to accomplish:

- how to choose a snippet
- determine delay and fine-tune a buffer value in order to synchronize music and dance moves perfectly
- determine how long dance moves take and revise timing values in `bpm_test.py`
- storing dance moves in an ordered and iterable sequence

# day 4:

bringing everything together in ROS, trying to figure out how to handle publisher and subscribers. ideally, all music data would be published in one message, and the driver node would subscribe to this message and save all this preprocessing information. 

# day 5:

the drone is not the most capable piece of hardware, so the dance moves just register and happen too slowly to be doing 2 beats/measure at 120 bpm. 

two possible solutions:

1. opt for 1 dance move per measure (the only way to make the dance moves occur in a rhythmically "satisfying" manner)

pros include:
- more universal and compatible with various songs
- simpler implementation, would remove the need to do extra calculations on different time signatures

cons include:
- not as interesting of a dance

2. choose slower audio so the drone has more time in between each dance move

pros include:
- would allow for more complex dance

cons include:
- baby shark :(&nbsp;&nbsp;&nbsp;&nbsp;(unless we slow down baby shark?)

all that's left to do now is the presentations! we made it :)

&nbsp;

&nbsp;

&nbsp;

&nbsp;
### important links:
https://hackernoon.com/audio-handling-basics-how-to-process-audio-files-using-python-cli-jo283u3y       - manipulating audio files

https://towardsdatascience.com/top-3-python-packages-to-learn-audio-data-science-project-cbd11c100fe7   - audio analysis packages