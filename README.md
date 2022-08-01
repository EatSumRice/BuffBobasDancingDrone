note taking:

day 1:
using pyAudioAnalysis to recognize audio file (.wav or .mp3) first, then try basic feature extraction (bpm)

so scratch that, seems like Librosa is the way to go
ran very simple script, was able to determine BPM of a random music track with very high accuracy
is NOT a fan of .mp3, use .wav

things to note about tempo tracker: is not great at determining time signature, so tempo of fast songs tend to be recorded in half time 
(i.e. 140 bpm --> 69.84 bpm)
actually makes our lives easier since the drone has speed limitations already





important links:
https://hackernoon.com/audio-handling-basics-how-to-process-audio-files-using-python-cli-jo283u3y       - manipulating audio files
https://towardsdatascience.com/top-3-python-packages-to-learn-audio-data-science-project-cbd11c100fe7   - audio analysis packages