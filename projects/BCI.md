---
title: Brain-Computer Interfaces
---
# Brain-Computer Interfaces for Visual Selection

## Project Rationale

A brain-computer interface (BCI) is an electronic system that converts users’ brain activity into control commands to operate external software or devices (e.g., typing programs, electronic wheelchairs). BCIs offer promising assistive technology solutions for people suffering with severe motor dysfunction. Beyond clinical use, applications are being developed for gaming systems, smart home control, and other uses. 

One class of BCIs use visual stimuli to elicit the necessary input signal(s). A number of pictures (or letters, numbers, etc.) are presented on a screen, and the user attends to the one they want to select. The system then identifies the user’s target based on the brain activity elicited by the target stimulus. An important part of this process is modifying the visual stimuli so that we can determine which one the user is paying attention to. Our project is focused on testing different kinds of visual stimuli, and ways of presenting them, to determine which ones are most effective at eliciting the necessary brain activity.

One of the biggest challenges with BCIs is that no two brains, or brain responses are identical. So, the best method of stimulation may vary from person to person, and even within the same person at different times. Brain signals are affected by things like tiredness, boredom, and hunger. Consequently, there is no BCI that works extremely well for all users, nor for a single user all the time. Our goal is to optimize the performance of BCIs by maximizing the distinction between the brain activity elicited by the target and non-target stimuli.

## Project Description

We are testing different ways of presenting stimuli, and analyzing the brain responses, to determine which approaches work best, or how they can be combined to improve performance. One way of presenting the stimuli is to use the *oddball* paradigm, where each stimulus (picture) is highlighted in some way, one at a time, in a random order. The highlighting can involve making that stimulus bigger, brighter, a different colour, a different object (such as a face) etc.. When the highlight occurs on the attended stimulus, the brain response is different (or at least stronger) than when the highlight occurs on a non-attended stimulus. Another approach is for the different stimuli to flicker at different rates. Flickering stimuli elicit *steady-state visual evoked potentials* (SSVEPs), which are brain responses that oscillate (get stronger and weaker) at the same rate as the flicker frequency. The SSVEP response to the attended stimulus is stronger than to the non-attended stimuli. We are testing different ways of combining these two approaches to see if we can get a stronger response than either one alone. For fun (and because we're in Halifax, a coastal city), we are using pirate-themed stimuli!

{%
  include figure.html
  image="images/bci_pirates.png"
  caption="An example BCI stimulus, using green pirate faces as highlights"
  width="400px"
%}

## Mission

Optimize BCI performance by maximizing the distinction between target and non-target responses—for any user, at any time.

## Overview

Phase 1: We have created custom stimuli and are testing specific manipulations to determine which combination of stimulus features elicits the most distinct target response. 

Phase 2: We will then combine two stimulus presentation methods to elicit a hybrid target response composed of multiple signals and signal types.

Phase 3: Once the performance metrics have been maximized, we aim to integrate this stimulus presentation approach into an *online* BCI system designed to identify users' target objects and execute their corresponding commands in real time. 

## Current State of Project and Lab Volunteer Contribution Opportunities
We have finalized the stimulus protocol for Phase 2, and will be piloting the study over summer 2024. We will conduct several statistical and machine learning analyses on this data during the Fall 2024 semester. In parallel we are beginning Phase 3 with the gamification and online implementation of a pirate-based BCI paradigm.

Overall, this is a complex study that intersects neuroscience, computer science, and data science. Involvement opportunities exist at all levels (independent study, honours, graduate students) during any phase. Note that while domain knowledge is considered an asset, especially [NESC/PSYO 3505 *Neural Data Science*](https://dalpsychneuro.github.io/NESC_3505/), it may not be required for some roles/tasks. 

## Funding Sources
Funded by the Natural Sciences and Engineering Research Council of Canada (NSERC).

{%
  include figure.html
  image="images/logos/nserc_logo.png"
  link="https://www.nserc-crsng.gc.ca/"
  tooltip="NSERC"
  height='100px'
%}
