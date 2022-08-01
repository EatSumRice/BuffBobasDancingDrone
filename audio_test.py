from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
from pyAudioAnalysis import MidTermFeatures
# import matplotlib.pyplot as plt
import numpy as np
# import warnings

file_name = "LOVE_DIVE.mp3"

# Extract the Sampling Rate (Fs) and the Raw Signal Data (signal)
[Fs, signal] = audioBasicIO.read_audio_file(file_name)

# Uncomment if signal has two channels
# signal = signal[:,0]

# Function to Normalize the Signal
def normalize_signal(signal):
  signal = np.double(signal)
  return (signal - signal.mean()) / ((np.abs(signal)).max() + 0.0000000001)

# Short Term Features
# For each short-term window a set of features is extracted. This would result in a sequence of feature
# vectors stored in a np matrix (in this case Features_midTerm)

signal = normalize_signal(signal)

# Fs - frequency sampling Rate
print("The Sampling Freq: ",Fs)

# Total Signal Len
signal_len = len(signal)
print("Total Signal Length: ",signal_len)

# Total Time Len of Song in Seconds
len_of_song = signal_len / Fs
print("Total Song Time (s): ",len_of_song)

# Window Size in mseconds
windowSize_in_ms = 50
windowSize_in_s = windowSize_in_ms/1000
# Window Size in Samples
windowSize_in_samples = Fs * (windowSize_in_ms / 1000) #divide by 1000 to turn to seconds
print("Window Size (samples): ",windowSize_in_samples)

# Window Step in mseconds
wStep_in_ms = 25
# Window Step in Samples
wStep_in_samples = Fs * (wStep_in_ms / 1000) #divide by 1000 to turn to seconds
print("Window Step in Samples: ", wStep_in_samples)

# Oversampling Percentage
oversampling_Percentage = (wStep_in_ms / windowSize_in_ms) * 100
print("Oversampling Percentage (overlap of windows): ",oversampling_Percentage)

# Total Number of Windows in Signal
total_number_windows = signal_len / windowSize_in_samples
print("Total Number of Windows in Signal: ",total_number_windows)

# Total number of feature samples produced (windows/size * total windows)
feature_samples_points_total_cal = int(total_number_windows * (windowSize_in_ms/wStep_in_ms))
print("Calculated Total of Points Produced per Short Term Feature: ",feature_samples_points_total_cal)

# Extract features and their names. Each index has its own vector of features. The total number should be the same
# as the calculated total of points produced per feature.
Features_shortTerm, feature_names = ShortTermFeatures.feature_extraction(signal, Fs, windowSize_in_samples, wStep_in_samples)

# Exact Number of points in the Features
feature_samples_points_total_exact = len(Features_shortTerm[0])
print("Exact Total of Points Produced per Short Term Feature: ",feature_samples_points_total_exact)

# Mid-window (in seconds)
mid_window_seconds = int(1 * Fs)

# Mid-step (in seconds)
mid_step_seconds = int(1 * Fs)

# MID FEATURE Extraction
Features_midTerm, short_Features_ignore, mid_feature_names = MidTermFeatures.mid_feature_extraction(signal,Fs,mid_window_seconds,mid_step_seconds,windowSize_in_samples,wStep_in_samples)

# Exact Mid-Term Feature Total Number of Points
midTerm_features_total_points = len(Features_midTerm)
print("Exact Mid-Term Total Number of Feature Points: ",midTerm_features_total_points)

# Beats per min
# The Tempo of music determins the speed at which it is played (measured in BPM)
bpm,confidence_ratio = MidTermFeatures.beat_extraction(Features_shortTerm,1)
print("Beats per Minute (bpm): ",bpm)
print("Confidence ratio for BPM: ", confidence_ratio)

# Figure out why the BPM does not match the actual reading
# of 115 BPM. It is showing 30 BPM which is for sure wrong.