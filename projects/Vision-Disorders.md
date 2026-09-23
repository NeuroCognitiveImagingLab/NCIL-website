---
title: Objective Diagnosis of Vision Disorders
---

# Objective Diagnosis of Vision Disorders

## Project Rationale

The goal of this study (known in the lab as *eyeAI*) is to gain a better understanding of how machine learning can aid our clinical team at the [IWK Health Centre](https://www.iwk.nshealth.ca) in Halifax in diagnosing and managing disorders affecting how visual information is communicated to the brain. Machine learning is a field of study within computer science, which uses complex mathematical models to find patterns in data and then use those patterns to make predictions, such as whether someone has a medical condition or not.

Electrical recordings from the eye and the brain are already a routine part of clinical eye care, but the interpretation step is the weak link. Reading them relies on the subjective judgement of a trained clinician: which features of the waveform matter, and how far from typical they need to be before they are clinically meaningful. That expertise takes years to build, is unevenly distributed, and — like any human judgement made under uncertainty — carries a risk of bias: a patient's diagnosis can depend on who happens to read their recording. Because a machine learning algorithm's decision rule is fixed, it gives the same answer regardless of who is reading, and so can support the clinician's judgement rather than be depended upon in its place.

## Project Description

We are interested in how patterns of retinal (inner eye) and brain electrical activity might help us better diagnose eye conditions. We measure this activity using electrodes placed on the skin. We currently use these recordings in clinic to help determine where a patient's visual issues may be originating. This has proven very helpful when we can't see physical signs of change during an eye examination. Many factors (like not wearing the right glasses) can affect these recordings and create challenges when trying to interpret the findings accurately.

For this study we are interested in looking at the data obtained from the visual testing commonly ordered by Ophthalmologists/Neurologists. The tests people are commonly booked for include Visually Evoked Potentials (VEPs) and Electroretinograms (ERGs). VEPs measure the electrical response to a visual target from the brain, using a sticker (electrode) placed on the scalp (head). ERGs measure the electrical response to a visual target from the retina (tissue in the back of the eye), using a thread placed on the lower eyelid. This is a very similar concept to having an electrocardiogram (heart function test) done in a clinic, where stickers are placed on the chest and we see the electrical activity of the heart beating on a monitor.

{%
  include figure.html
  image="images/projects/eyeAI-VEP.jpg"
  caption="A visual electrodiagnostic session in the IWK Eye Clinic: electrodes are placed on the scalp (lower panels) and the brain's response is recorded while the participant views a reversing checkerboard pattern (upper panel)"
  width="500px"
%}

The scale of the dataset is what makes this approach possible: machine learning methods need many examples of each condition before they can separate a genuine diagnostic signal from the considerable variability between individuals.

## Objectives

With sufficient participants we hypothesize that the machine learning algorithm will be able to:

1. Distinguish visual electrophysiology waveforms as normal or abnormal given age and other clinical data
2. Quantify the severity of an abnormality
3. Identify the cause of pathology in the waveform, given additional information from the individual's ocular exam.

## Current State of Project

**Data collection is currently going on.** Recruitment for this study is ongoing and open to any interested volunteers, with or without eye conditions. Participation involves coming into the IWK Eye Clinic Visual Electrodiagnostic Lab for one (1) session and completing an eye examination, visual electrodiagnostic testing, and ocular photography.

1. The eye exam consists of testing similar to what people may have experienced at an optometrist, including visual acuity, contrast sensitivity and colour vision testing.
2. The visual electrodiagnostic testing involves looking at various patterns or lights while electrodes placed on the skin or lower eyelid record activity from the visual system.
3. Ocular photography involves taking photos of the back of the eye using specialized cameras.

All of these tests are commonly done in our clinic, and in this study we perform them in the same way we would with patients. A session takes approximately 60–90 minutes. This study has been reviewed and approved by the IWK Research Ethics Board.

If you are interested in participating or would like more information, please email [Jeff Locke](mailto:jeff.locke@dal.ca), or read [more about taking part](https://ncil.science/participate/Vision-Disorders-recruitment).

## For Students

There are no current opportunities to work on this project. However, if you are interested in learning more, you can volunteer to participate, and see how the study is done. Participating is also an opportunity to meet the researchers involved and ask questions about the study.

## Funding Sources

Jeff Locke's work on this project is supported by the Dr. R. Evatt and Rita Mathers Trainee Scholarship in Ophthalmology & Visual Sciences.
