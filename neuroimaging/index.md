---
title: Neuroimaging
nav:
  order: 4
  tooltip: About neuroimaging 
---

# {% include icon.html icon="fa-solid fa-brain" %}Neuroimaging and Data Science
{:.center}

{%
  include button.html
  link="neuroimaging/#neuroimaging-tools"
  text="Neuroimaging Tools"
  icon="fas fa-gear"
  flip=true
%}

{%
  include button.html
  link="neuroimaging/#data-science"
  text="Data Science"
  icon="fas fa-table"
  flip=true
%}

# Neuroimaging tools
A number of remarkable tools exist to measure and localize the activity of the brain non-invasively. These tools form the primary basis of the field of cognitive neuroscience, which is dedicated to understanding the relationships between cognition and brain activity. NCIL lab director Aaron Newman has published a book that provides and overview of these techniques, [*Research Methods for Cognitive Neuroscience*](https://us.sagepub.com/en-us/nam/research-methods-for-cognitive-neuroscience/book242924), as well as the Dalhousie University course NESC/PSYO 3137. On this page we provide a bit more information on the two techniques we use most in NCIL, and which lab members are most likely to gain experience with.

## Electroencephalography (EEG)
EEG is a technique used for recording ‘brain waves’, or more technically the electrical activity produced by the brain. EEG achieves this by using electrodes that are placed on the scalp, and recording the summed electrical signals the brain produces to operate. NCIL has two state-of-the-art 64 channel EEG systems available for research use. Most of our research projects use EEG, and this is what most trainees start with. Our lab manager, Dr. Cindy Hamon-Hill, runs EEG training sessions at the start of every term to help onboard new lab members. 

{% capture text %}
While EEG is very good at answering questions about *when* in time a cognitive process occurs, and how that process is affected by different experimental manipulations, it is not good at localizing *where* in the brain activity occurs. This is because electrical signals conduct through the head in every direction. So, when different brain areas are active at the same time, their signals all combine when they reach the electrodes on the scalp. 
{% endcapture %}
{%
  include feature.html
  image="images/cindy_eeg_2.JPG"
  link="neuroimaging/#electroencephalography-eeg"
  title=""
  text=text
%}

{% capture text %}
In cognitive neuroscience research, most people use EEG in two ways: **event-related potentials (ERPs)**, and **frequency-domain analyses**. **ERPs** focus on EEG activity that is time-locked to particular events, such as the presentation of a word or picture.Different peaks and troughs in the ERP (called *components*) are associated with different neurocognitive activity, such as sensory perception, or accessing the meaning of a word. **Frequency-domain analyses** involve applying a mathematical transformation to the EEG signal, to computer the power (size) of the signal in different frequency bands. *Frequency* refers to how many peaks/troughs occur in a signal in a given period of time (e.g., alpha activity is 8-12 peaks/second). Human EEG tends to be organized into different frequency bands (delta, theta, alpha, beta, and gamma), which can be associated with different cognitive processes.
{% endcapture %}
{%
  include feature.html
  image="images/DSC_3734.jpg"
  link="neuroimaging/#electroencephalography-eeg"
  title=""
  text=text
  flip=true
%}

## Magnetic Resonance Imaging (MRI)
MRI is used to get images of various parts of the body, including the brain, using a combination of magnetic fields and radio waves. MRI is one of the best ways to look at the brain, because it is very safe (it doesn't use radiation or X-rays), and it can provide both high-resolution anatomical images, and functional images showing which areas "light up" during different cognitive tasks. MRI scanners are very expensive to install and maintain. We do not have an MRI scanner in NCIL, but we have access to MRIs for research purposes at the nearby IWK and QEII health centres. MRI studies are very expensive to run and typically we can only conduct an MRI research study if we have a significant research grant to cover these costs.

{% capture text %}
Functional MRI (fMRI) works by measuring the amount of oxygen delivered to different parts of the brain. When neurons (brain cells) are active, more oxygen is delivered to those parts of the brain. This means that fMRI has excellent spatial resolution: we can localize *where* activity occurs down to the level of a few millimetres. On the other hand, fMRI does not have the same sensitivity as EEG to *when* activity occurs. This is because the changes in blood oxygenation that we measure happen a few seconds after change sin electrical brain activity. For this reason, EEG and fMRI allows us to view brain activity in two complementary ways. We can also use MRI to view the structure of the brain, including diffusion tensor imaging (DTI), which allow us to map the white matter tracts that connect different brain areas. 
{% endcapture %}
{%
  include feature.html
  image="images/child_in_MRI_scanner.jpg"
  link="neuroimaging/#magnetic-resonance-imaging-mri"
  title=""
  text=text
%}

## Functional Near Infrared Spectroscopy (fNIRS)
Functional Near-Infrared Spectroscopy, or fNIRS, is a cool way scientists look inside our brains to understand how they work. It's like peeking through a tiny window into the brain's activities. Unlike big, noisy machines like MRIs, fNIRS is small and quiet, making it easier to use, even on kids!
Here's how it works: our brains need oxygen to do their job, just like muscles need fuel to move. When we think or do stuff, our brain cells use up oxygen. fNIRS measures this oxygen use by shining near-infrared light through our skulls. The light that doesn’t get absorbed by the hemoglobin proteins that carry oxygen, bounces back to detectors, telling scientists which brain areas are busy.

{% capture text %}
Why is this important? Well, scientists use fNIRS to learn about many things, like how we learn, feel, or solve problems. For example, they can see which parts of the brain light up when we read or do math. They can even use it to help kids with learning differences! Also, fNIRS is super handy for kids, since it is non-invasive and allow for more mobility and movement compared to other neuroimaging devices like fMRI. fNIRS helps researchers understand how kids think and learn, and how these processes develop over time. 
In short, fNIRS acts as a non-invasive tool for research, assisting in understanding the complexities of how our brains work. 
{% endcapture %}
{%
  include feature.html
  image="Blonde_fNIRS_lady.jpeg"
  link="neuroimaging/#Functional-Near-Infrared-Spectroscopy-fNIRS"
  title=""
  text=text
%}


# Data Science
{% capture text %}
**Coding** (computer programming) is a vital skill in cognitive neuroscience. Our research relies on large, complicated data sets, and often combining different types of data (such as EEG and behavioural data measured during the same task). Managing and analyzing these data sets requires skills in **data science**, including coding, data management, statistics, and machine learning. Developing and running experiments also requires coding. Our lab primarily uses the Python and R programming languages.
{% endcapture %}
{%
  include feature.html
  image="images/binary-numbers-data-matrix.jpg"
  link="neuroimaging/#data-science"
  title=""
  text=text
  flip=true
%}

You don't need to know how to code to get started volunteering or working on a research project in NCIL. However, to succeed in the lab you will definitely need to learn these skills. Coding and data science skills are also extremely valuable on the job market, and when applying to many graduate programs. Not only do coding skills look great on your CV, but they are good for you as well — coding teaches you to tackle problems in a systematic and logical way, breaking them down into small parts and addressing them in a sequential manner. 

{% capture text %}
Dr. Newman has written a free online textbook, [*Data Science for Psychology and Neuroscience in Python*](https://neuraldatascience.io), an associated [YouTube channel](https://youtube.com/playlist?list=PLtfEWMIgWS22MMZjPIzBRE2cHhMcvEKwp), and teaches a course based on this book, NESC/PSYO 3505 *Neural Data Science*. Everyone working in NCIL should take this course. Beofre you take the course, or for extra learning, all NCIL lab members get free access to [DataCamp](https://datacamp.com), an online learning platform for data science. As well, The [SURGE] sandbox also offers regular [*Discover Coding*](https://www.surgeinnovation.ca/discover) workshops on both Python (developed by Dr. Newman) and R (developed by NCIL alumnus Simon Leger).
{% endcapture %}
{%
  include feature.html
  image="images/discover_coding.jpg"
  link="neuroimaging/#data-science"
  title=""
  text=text
%}