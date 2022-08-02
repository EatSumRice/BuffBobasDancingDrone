note taking:

day 1:
using pyAudioAnalysis to recognize audio file (.wav or .mp3) first, then try basic feature extraction (bpm)

so scratch that, seems like Librosa is the way to go
ran very simple script, was able to determine BPM of a random music track with very high accuracy
is NOT a fan of .mp3, use .wav

things to note about tempo tracker: is not great at determining time signature, so tempo of fast songs tend to be recorded in half time 
(i.e. 140 bpm --> 69.84 bpm)
actually makes our lives easier since the drone has speed limitations already


day 2:
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






important links:
https://hackernoon.com/audio-handling-basics-how-to-process-audio-files-using-python-cli-jo283u3y       - manipulating audio files
https://towardsdatascience.com/top-3-python-packages-to-learn-audio-data-science-project-cbd11c100fe7   - audio analysis packages