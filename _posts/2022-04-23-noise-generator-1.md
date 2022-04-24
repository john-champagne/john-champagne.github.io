---
layout: post
title: Noise Generator 1 – Audio Hardware and Spectrum Analysis
author: Johnny Champagne
math: true
tags:
- signal-processing
date: 2022-04-23 13:56 +0500
---

I like to sleep with white noise on in the background. I usually sleep with a small fan on, which provides sufficient noise and airflow. In the colder months, however, it becomes harder to justify blowing air around the room. Sometimes, I'll turn the fan on and point it away from my bed, just so I can hear the noise. What I really need is a white noise generator.

There are a lot of pre-made solutions to this. I personally like the variety of white noise videos available on youtube. Unfortunately, I don't like streaming 'videos' all night that consist of nothing more than randomly generated audio samples. It wastes bandwidth and is unreliable (what if my internet goes off?).

There's also premade 'white noise machines' available on Amazon like the one shown below.
![Amazon white noise machine](/assets/2022-04-23-noise-generator-1/white_noise_amazon.png)
I don't know... Something about this $23.99 piece of hardware screams 'unreliable' to me. Plus, I have no idea how loud this thing can get.

# Project Goals

The goal of this project is to make my own white noise generator. Something that has
* Mimimum hardware (Keep it Simple, Stupid)
* Minimal power consumption. At least less than a fan
* Not connected to the internet
* Relatively inexpensive

# Audio Hardware

I took a trip to the local goodwill to find some sort of speaker and pretty quickly found... a karaoke machine! This thing is pretty old. It has a CD player and a CRT monitor built in. I figured it was more than enough for my application and grabbed it for $10.99.
![karaoke](/assets/2022-04-23-noise-generator-1/karaoke-1.jpg)

I plugged this guy in and am immediately hit with a high pitch squeal... Ouch.

The spectrum analyzer showed a pretty obvious tone at ~15 kHz.

![karaoke-2](/assets/2022-04-23-noise-generator-1/15k-sound.svg)
 
At this point I turned to my coworker who is a bit of an audiophile. After a little back-and-forth with him, he suggested trying to power off the CRT. Sure enough, the noise vanished.

![karaoke-3](/assets/2022-04-23-noise-generator-1/15k-sound-2.svg)

A little bit of reading indicates that this noise is the result of the flyback transformer within the CRT. Either way, problem solved.

# Volume Test

From this point, I pulled out my laptop and plugged into the speaker via an 3.5mm audio cable. I want to see if this thing can go as loud as I'd like it to. I pulled up my favorite 'brown noise' video on youtube and adjusted the volume until I was satisfied. Perfect results; the speaker is more than loud enough for my application. Plus, it has a volume nob, so I can always reduce the volume later.

I measured the signal coming over the audio cable with an oscilloscope. I will use this signal as a reference for my hardware going forward. See the picture below.
![Scope](/assets/2022-04-23-noise-generator-1/scope.png)

I saved the data from the scope to perform some spectrum analysis.

# Audio Analysis

I loaded up my data into python and started poking around. The first piece of good news is that the total voltage swing within the 6 second window is relatively small:

$$-0.72V < v < 0.76V$$

Most DACs can generate at least 0 – 3.3 V without any sort of amplifier circuit.

In order to recreate this audio sample, our noise generator will have to match the volume and spectrum of our sample. A good way to measure the 'volume' of the noise is just to take the standard deviation. For this we have:

$$\sigma = 0.180 \,\mathrm{volts}$$

The spectrum is a little trickier. We can take the FFT of the sample and plot it using a log scale. See the plot below.

![Spectrum](/assets/2022-04-23-noise-generator-1/spectrum.svg)

Looks like a pretty straight forward 20 dB/decade rolloff. I couldn't identify any cutoff frequency; it's likely that the cutoff is below the audio band. I included the plot up to 40 kHz to demonstrate how well my laptop soundboard can band limit the signal to 20 kHz.

# Going Forward

From here, I will develop a hardware solution to emulate the audio spectrum and drive the speaker. I want to keep my options open, so I won't specify what hardware or peripherals I'll use.