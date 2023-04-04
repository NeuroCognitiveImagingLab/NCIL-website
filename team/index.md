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

{% include section.html dark=true%}

## Staff
{:.center}

{% include list.html data="members" component="portrait" filters="role: pi, group: " %}

{% include section.html %}

## Graduate Students
{:.center}

{% include list.html data="members" component="portrait" filters="role: phd, group: " %}

{% include section.html dark=true%}

## Undergraduate Students
{:.center}

{% include list.html data="members" component="portrait" filters="role: undergrad, group: " %}

{% include section.html background="images/20111102_BrainRepair_01.jpg" dark=true %}

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

{% include section.html %}

## Partners
{:.center}

{% capture content %}
[![SURGE](/images/team/S_Color_horizontal_medium_lightBG.png)](https://www.surgeinnovation.ca/)

[![Ensuring Full Literacy](/images/team/Ensuring_Full_Literacy_logo.png)](https://ensuringliteracy.ca/)

[![Brain Repair Centre](/images/team/BRC_logo.png)](https://www.brainrepair.ca/)

[![IWK Health Centre](/images/team/IWKLOGO.png)](https://www.iwk.nshealth.ca/)

[![QEII Health Sciences Centre Foundation](/images/team/QEII_logo.svg)](https://qe2foundation.ca/)

{% endcapture %}

{% include grid.html content=content %}

{% include section.html %}

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

{% include section.html %}

## Funding
{:.center}

Our work is made possible by funding from several organizations.
{:.center}

[![SSHRC](/images/team/sshrc-fip-full-color-eng.jpg)](https://www.sshrc-crsh.gc.ca/home-accueil-eng.aspx)
[![Brain Repair Centre](/images/team/BRC_logo.png)](https://www.brainrepair.ca/)
[![NSERC](/images/team/NSERC_FIP_RGB.png)](https://www.nserc-crsng.gc.ca/index_eng.asp)
[![Mitacs](/images/team/Mitacs.png)](https://www.mitacs.ca/en)
