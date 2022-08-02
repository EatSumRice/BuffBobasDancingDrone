## note taking:

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






### important links:
https://hackernoon.com/audio-handling-basics-how-to-process-audio-files-using-python-cli-jo283u3y       - manipulating audio files
https://towardsdatascience.com/top-3-python-packages-to-learn-audio-data-science-project-cbd11c100fe7   - audio analysis packages