---
title: Development of Punctuation Sensitivity in Early Readers
description: NCIL poster presented at the Society for the Neurobiology of Language Annual Meeting, 2026.
---

<!--
  This page is the target of the QR code printed on the poster
  (https://ncil.science/posters/snl2026/). Do NOT move or rename this directory,
  and do NOT add a permalink to the front matter.

  The PDF download button and the poster preview below appear automatically once
  these two files are committed to this directory — no edits to this page needed:
    - Newman_2026_SNLposter.pdf   (the exported poster)
    - thumbnail.png               (page 1 of the PDF, 1200px wide)
  Until then the page shows a short "available after the session" note instead.
-->

{% assign poster_pdf = "posters/snl2026/Newman_2026_SNLposter.pdf" | file_exists %}
{% assign poster_thumb = "posters/snl2026/thumbnail.png" | file_exists %}

# Development of Punctuation Sensitivity in Early Readers
{:.center}

### An ERP Investigation of the Closure Positive Shift in Grades 3–5
{:.center}

**Aaron J. Newman, Emily Wei, Arjun Litt, Saisha Rankaduwa, Emma Abray, Jadelyn Kershaw, and Cindy Hamon-Hill**
{:.center}

NeuroCognitive Imaging Lab, Department of Psychology and Neuroscience, Dalhousie University, Halifax, NS, Canada
{:.center}

Poster presented at the [Society for the Neurobiology of Language](https://www.neurolang.org) Annual Meeting, 2026.
{:.center}

{% if poster_pdf %}
{%
  include button.html
  link="posters/snl2026/Newman_2026_SNLposter.pdf"
  text="Download the poster (PDF)"
  icon="fas fa-file-pdf"
%}
{:.center}
{% else %}
The full-resolution poster PDF will be posted here during the meeting. In the
meantime, the abstract is below — or email us using the link at the foot of this page.
{:.center}
{% endif %}

{% include section.html %}

{% if poster_thumb %}
{%
  include figure.html
  image="posters/snl2026/thumbnail.png"
  link="posters/snl2026/Newman_2026_SNLposter.pdf"
  caption="Click the poster to open the full-resolution PDF."
  width="800px"
%}

{% include section.html %}
{% endif %}

## Abstract

A key challenge for developing readers is learning to use punctuation cues to guide their reading. Awareness of the role of punctuation, and its correct use, is predictive of future gains in reading comprehension [1]. Reading comprehension gains are mediated by prosodic awareness, suggesting that children use punctuation as cues to prosodic structure that in turn inform syntactic structure to facilitate comprehension [2].

Little work to date has investigated real-time measures of punctuation processing in developing readers. In adults, an event-related potential (ERP) component known as the closure positive shift (CPS) is elicited by both prosodic phrase boundaries in spoken language, and commas in written text. In spoken language, the CPS is elicited by intonational phrase boundaries [2]. In written language, a CPS is likewise elicited by commas marking phrase boundaries, and the size of the CPS was larger in participants who showed stricter adherence to linguistic rules when given a task to insert commas in text [3]. This suggests that the CPS is sensitive to individual differences in how commas are used to guide parsing.

Given this evidence, we predicted that the CPS may emerge in developing readers as they develop sensitivity to proper punctuation, and that the size of the CPS may reflect sensitivity to punctuation in building syntactic representations of text. However, while the CPS has been shown to emerge by age 6 during spoken language comprehension [5], no published work to date has investigated the CPS during reading in children.

We recruited children from grades 3–5 to investigate whether, and at what age, the CPS in response to commas emerged. This age range represents a transitional period between beginning and fluent reading, over which children show increasing use of syntactic awareness to support reading comprehension [1], as well as increasing awareness of the role of punctuation in reading [2].

Children were given standardized tests of reading ability and tests of punctuation sensitivity, followed by an ERP paradigm in which they silently read short, age-appropriate stories presented word by word. Across sentences, the stories contained commas at both syntactically appropriate and inappropriate positions, as well as missing commas at positions where they were required.

Preliminary data (n=18) show a significantly larger positivity for incorrect than correct commas over posterior midline channels between approximately 300–500 ms, as well as evidence of a larger positivity for correct than missing commas over anterior midline channels in the same time window. Additional data collection is underway; with a full sample, we will additionally investigate relationships between the magnitude of these effects and grade, punctuation sensitivity, and reading comprehension.

{% include section.html %}

## References

1. MacKay, E. J. (2023). [hdl.handle.net/10222/82818](https://hdl.handle.net/10222/82818)
2. Ryken, A. M., Wade-Woolley, L., & Deacon, S. H. (2025). [doi.org/10.1007/s11145-024-10517-8](https://doi.org/10.1007/s11145-024-10517-8)
3. Steinhauer, K., Alter, K., & Friederici, A. D. (1999). [doi.org/10.1038/5757](https://dx.doi.org/10.1038/5757)
4. Steinhauer, K., & Friederici, A. D. (2001). [doi.org/10.1023/a:1010443001646](https://dx.doi.org/10.1023/a:1010443001646)
5. Männel, C., & Friederici, A. D. (2011). [doi.org/10.1111/j.1467-7687.2010.01025.x](https://dx.doi.org/10.1111/j.1467-7687.2010.01025.x)

{% include section.html %}

## Related

This poster comes out of our research on reading development in children.

{%
  include button.html
  link="projects/What-Makes-a-Skilled-Reader"
  text="More about our reading development research"
  icon="fas fa-arrow-right"
  flip=true
%}
{:.center}

{% include section.html %}

## Contact

Questions about this work? Email [Aaron.Newman@dal.ca](mailto:Aaron.Newman@dal.ca) or
[ncil@dal.ca](mailto:ncil@dal.ca).

This research was supported by the Social Sciences and Humanities Research Council of Canada (SSHRC).
