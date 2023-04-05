---
title: Team
nav:
  order: 2
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team
{:.center}
Great people doing amazing work is what makes NCIL. Here’s who we are:
{:.center}

## Staff
{:.center}

{% include list.html data="members" component="portrait" filters="role: pi, group: " %}

## Graduate Students
{:.center}

{% include list.html data="members" component="portrait" filters="role: phd, group: " %}

## Undergraduate Students
{:.center}

{% include list.html data="members" component="portrait" filters="role: undergrad, group: " %}

{% include section.html background="images/team/join.png" dark=true %}

{%
  include button.html
  icon="fa-solid fa-handshake-angle"
  text="Join the Team"
  link="join"
  style="button"
%}
{:.center}

{% include section.html %}

## Collaborators
{:.center}

{% include list.html data="members" component="portrait" filters="role: collab, group: " %}

## Partners
{:.center}

{% capture content %}
{% include figure.html image="images/team/S_Color_horizontal_medium_lightBG.png" link="https://www.surgeinnovation.ca/" %}
{% include figure.html image="images/team/Ensuring_Full_Literacy_logo.png" link="https://ensuringliteracy.ca/" %}
{% include figure.html image="images/team/BRC_logo.png" link="https://www.brainrepair.ca/" %}
{% include figure.html image="images/team/IWK-Logo-Colour-1080.png" link="https://www.iwk.nshealth.ca/" %}
{% include figure.html image="images/team/ML-Logo-Header.svg" link="https://mangolanguages.com/" width="600px"%}
{% include figure.html image="images/team/QEII_logo.svg" link="https://qe2foundation.ca/" width="800px"%}

{% endcapture %}

{% include grid.html content=content %}

## Alumni
{:.center}
Gone but never forgotten.
These are past lab members who have moved on to other school programs, new jobs, or elsewhere.
{:.center}

{% include list.html data="members" component="portrait" filters="role: pi, group: alum" style="small" %}
{% include list.html data="members" component="portrait" filters="role: postdoc, group: alum" style="small" %}
{% include list.html data="members" component="portrait" filters="role: phd, group: alum" style="small" %}
{% include list.html data="members" component="portrait" filters="role: undergrad, group: alum" style="small" %}
{% include list.html data="members" component="portrait" filters="role: programmer, group: alum" style="small" %}
{% include list.html data="members" component="portrait" filters="role: mascot, group: alum" style="small" %}
{% include list.html data="members" component="portrait" filters="role: collab, group: alum" style="small" %}

## Funding
{:.center}

Our work is made possible by funding from several organizations.
{:.center}

{% include figure.html image="images/team/sshrc-fip-full-color-eng.png" link="https://www.sshrc-crsh.gc.ca/home-accueil-eng.aspx" %}
{% include figure.html image="images/team/NSERC_FIP_RGB.png" link="https://www.nserc-crsng.gc.ca/index_eng.asp" height="400px"%}
{% include figure.html image="images/team/BRC_logo.png" link="https://www.brainrepair.ca/" height="200px"%}
{% include figure.html image="images/team/Mitacs.png" link="https://www.mitacs.ca/en" %}