---
title: Team
nav:
  order: 2
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team
Great people doing amazing work is what makes NCIL. Here’s who we are:
{:.center}

{% include section.html %}

## Staff
{% include list.html data="members" component="portrait" filters="role: pi, group: " %}

{% include section.html %}

## Graduate Students
{% include list.html data="members" component="portrait" filters="role: phd, group: " %}

{% include section.html %}

## Undergraduate Students
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
{% include list.html data="members" component="portrait" filters="role: collab, group: " %}

{% include section.html %}

## Partners

{% capture content %}
[![SURGE](/images/team/S_Color_horizontal_medium_lightBG.png)](https://www.surgeinnovation.ca/)

[![Ensuring Full Literacy](/images/team/Ensuring_Full_Literacy_logo.png)](https://ensuringliteracy.ca/)

[![Brain Repair Centre](/images/team/BRC_logo.png)](https://www.brainrepair.ca/)

[![IWK Health Centre](/images/team/IWKLOGO.png)](https://www.iwk.nshealth.ca/)

[![QEII Health Sciences Centre Foundation](/images/team/QEII_logo.svg)](https://qe2foundation.ca/)

{% endcapture %}

{% include grid.html content=content %}

{% include section.html %}

