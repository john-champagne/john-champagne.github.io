---
layout: post
title: Noise Generator 2 – Hardware Updates and Software Plans
author: Johnny Champagne
math: true
tags:
- signal-processing
date: 2022-12-23 22:00 +0500
---

It's been a minute since my last post on this project. This doesn't surprise me, as I often find myself very busy with everything *else* going on. In this time, I've rethought a couple of things on this project which I believe will make it both more portable and easier to maintain.

# The big change: no speaker/amplifier

"But Johnny!", I hear you say, "How can you make a noise generator without a speaker!?".

I have one word for you: **television**.

The purpose of the noise generator is, after all, to help me get to sleep. It occurred to me that every room that I sleep in has some kind of television set with, you guessed it, a speaker!

By losing the speaker, I can also make the project much more portable. No more lugging around a speaker and amplifier. The project can be as simple as a microcontroller and an HDMI cable. And who knows, maybe I can add some visuals on the screen?

# Microcontroller: Raspberry Pi B3+

With the TV setup in mind, my goal is to use my old Raspberry Pi B3+ SoC as the audio generator. I've tested a couple of noise generation codes on Python with good success. Hopefully this will translate well onto the Pi.

# Notes on the audio spectrum

My testing with the brown noise generation has led me to some interesting observations. The sample I provided in the first post demonstrated a 20dB/decade rolloff, which sounds quite nice. In preliminary testing, I notice that sharper rolloffs correspond to 'deeper' sounding brown noise, which can be more soothing.

Our ears don't hear low frequencies as well; and speakers don't tend to produce them very well. Thus the 'deeper' the brown noise, the louder the speaker has to be to produce the same volume in our ears. I forsee this being a problem with playing 'deep' brown noise. I hope to add some configuration on the software side to tune to whatever speaker setup I run into.

# Going Forward

The next steps for me are:
* Write a reliable Python script for generating and playing brown noise.
* Configure the Raspberry Pi B3+ OS to boot into this script.
* Debug where I can.
