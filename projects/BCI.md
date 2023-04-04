---
title: BCI
---
# A Novel Flickering Oddball Stimulation Paradigm for Hybrid Brain-Computer Interfaces

## Project Rationale
A brain-computer interface (BCI) is an electronic system that converts users’ brain activity into control commands to operate external software or devices (e.g., typing programs, electronic wheelchairs). BCIs receive input directly from task-related brain signals rather than from traditional input methods that require muscular control to operate (e.g., mouse/keyboard, joystick). Most BCIs use visual stimuli to elicit the necessary input signal(s). An array of objects is presented and the user attends to the one that he/she wants to select—the *target*. The objects are highlighted systematically, using stimulation techniques known to elicit predictable signals of interest when the target is highlighted, but not (as strongly) when non-targets are highlighted. Neuroimaging equipment records the user’s brain activity, and machine learning algorithms are trained to classify target and non-target responses based on the presence or absence of the predicted signals. The user’s target is determined to be the object that elicited signal-present responses. The system selects the target object and executes its corresponding control command. In this way, BCIs offer promising assistive technology solutions for people suffering with severe motor dysfunction. Beyond clinical use, applications are being developed for gaming systems, smart home control, and other uses. 

In theory, target stimuli will consistently elicit distinct response signals from all users, all the time. In practice, however, this has yet to be the case. No two brains are identical, and no one’s brain activity remains constant under varying circumstances (e.g., fatigue, hunger, mood). As such, signal features (e.g., strength, timing) in response to a given stimulus will vary widely—both between users and within an individual user at different points in time. This variability compromises classification accuracy and, in turn, overall system performance. Consequently, there is no BCI that works extremely well for all users, nor for a single user all the time. 

## Mission

Optimize BCI performance by maximizing the distinction between target and non-target responses—for any user, at any time.

## Overview

Phase 1: We have created custom stimuli and are testing specific manipulations to determine which combination of stimulus features elicits the most distinct target response. 

Phase 2: We will then combine two stimulus presentation methods to elicit a hybrid target response composed of multiple signals and signal types.

Phase 3: Once the performance metrics have been maximized, we aim to integrate this stimulus presentation approach into an *online* BCI system designed to identify users' target objects and execute their corresponding commands in real time. 

## Current State of Project and Lab Volunteer Contribution Opportunities
We are finalizing the stimulus protocol for Phase 1, and will be collecting data during the Fall 2022 semester. We will conduct several statistical and machine learning analyses on this data during the Winter 2023 semester. In parallel, across both semesters, we will integrate our second stimulation method and begin Phase 2 data collection. Phase 2 analyses and Phase 3 preparation will be conducted thereafter. 


Overall, this is a complex study that intersects neuroscience, computer science, and data science. Involvement opportunities exist at all levels (volunteer, independent study, honours, graduate students) during any phase. Note that while domain knowledge is considered an asset, especially [NESC/PSYO 3505 *Neural Data Science*](https://dalpsychneuro.github.io/NESC_3505/), it may not be required for some roles/tasks. 

## Funding Sources
Funded by the Nova Scotia Graduate Scholarship (NSGS) and the Dalhousie Medical Research Foundation (DMRF).

{%
  include gallery.html

  image1="images/DMRF_Logo.svg"
  link1="https://dmrf.ca/"
  tooltip1="DMRF"

%}
