#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import librosa
import librosa.display

# In[16]:


filename = './trial_audio.mp3'
y, sr = librosa.core.load(filename, sr=22050)

# In[17]:


# Root Mean Square Energy
y_rmse = librosa.feature.rms(y=y)[0]

# In[18]:


# Loudness
y_loud = librosa.core.amplitude_to_db(y)

# In[19]:


# Pitches,magnitudes
# pitch tells us the frequency of of the pitch
# magnitude tells us the the amplitude of the frequency-domain signal at that pitch
pitches, magnitudes = librosa.core.piptrack(y=y)

# In[20]:


# Fourier Tempogram
y_ftemp = librosa.feature.fourier_tempogram(y=y, sr=22050)

# In[23]:


# ACF-Tempogram
y_temp = librosa.feature.tempogram(y=y, sr=22050, center=True, window='hann')

# In[27]:


# Average tempo
# Strength
# Spectral centroid for clarity
# Onset frequency
y_tempo = librosa.beat.tempo(y=y, sr=22050, max_tempo=320.0)
y_strength = librosa.onset.onset_strength(y=y, sr=22050, max_size=1)
y_speccent = librosa.feature.spectral_centroid(y=y, sr=22050, n_fft=2048, window='hann', center=True)
y_onset_det = librosa.onset.onset_detect(y=y, sr=22050, onset_envelope=None, backtrack=False)

# In[28]:


# 120 MFCC Coefficients
y_mfcc = librosa.feature.mfcc(y=y, sr=22050, n_mfcc=120, norm='ortho')

# In[29]:


# Different Spectral Characteristics
y_spec_band = librosa.feature.spectral_bandwidth(y=y, sr=22050, S=None, n_fft=2048, window='hann', center=True,
                                                 pad_mode='reflect', p=2)
y_spec_contrast = librosa.feature.spectral_contrast(y=y, sr=22050, window='hann', center=True, pad_mode='reflect',
                                                    fmin=200.0, n_bands=6, quantile=0.02, linear=False)
y_spec_flatness = librosa.feature.spectral_flatness(y=y, S=None, n_fft=2048, pad_mode='reflect', amin=1e-10, power=2.0)

# In[31]:


# Exact chroma features are not there..The derivatives of those features are present
y_chr_sftf = librosa.feature.chroma_stft(y=y, sr=22050, window='hann', pad_mode='reflect', n_chroma=12)
y_chroma_cqt = librosa.feature.chroma_cqt(y=y, sr=22050, n_chroma=12, n_octaves=7, cqt_mode='full')

# In[ ]:
