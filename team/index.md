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

{% include section.html background="images/20111102_BrainRepair_01.jpg" dark=true%}

{%
  include button.html
  icon="fa-solid fa-handshake-angle"
  text="Join the Team"
  link="join"
  style="button"
%}
{:.center}

{% include section.html %}
