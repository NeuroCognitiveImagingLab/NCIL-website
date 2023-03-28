---
---

# NeuroCognitiveImagingLab's Website

The NeuroCognitive Imaging Lab (NCIL) at Dalhousie University in Halifax, Nova Scotia, Canada, conducts basic and applied cognitive neuroscience research. Much of our research is focused on language and neuroplasticity — how the brain changes with experience. The ultimate goal of our work is to help people live healthier, happier, and more productive lives. To this end, our activities follow a cycle including basic research, active participation in clinical settings, clinical research, and knowledge translation and application. 


NCIL is located in Mi’kma’ki, the ancestral and unceded territory of the Mi’kmaq. We are all Treaty people. 

We recognize that African Nova Scotians are a distinct people whose histories, legacies and contributions have enriched that part of Mi'kma'ki known as Nova Scotia for over 400 years.

{% include section.html %}

## Highlights
{% capture text %}

Welcome to NCIL's new website...

{%
  include button.html
  link="research"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="tools"
  text="Browse our projects"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="projects"
  title="Our Projects"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

DELETE THIS TEXT - TESTING ONLY

{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="team"
  title="Our Team"
  text=text
%}
