I have entered my ORCID ID in orcid.yaml and pushed the change to trigger citation generation. I get errors for roughly 1/3 of my ORCID entries (https://orcid.org/0000-0001-5290-8342) - all those that have an "EID" associated with them (regardless of whether there is also a DOI for that entry). This error prevents the website from building, so it's pretty consequential.

I found https://github.com/manubot/manubot/issues/365 which suggests that the Greenelab team are aware of the issue. However, it is not in the docs which I think it should be, since I have spent a lot of time first figureing out that it was a known bug, and second trying (unnsuccessfully) to find a solution.

I tried adding an entry to sources.yaml for one of the offending papers, like this:
```
- id: eid:2-s2.0-0036138435
  doi: 10.1038/nn775
```

But that doesn't work - that entry still throws an error. I can get the site to build by putting a single entry in source.yaml like `- doi: 10.1080/02699052.2018.1429022` - however the publications page has lots of entries (looks about the right number) but all of them show "no info" for all fields. Deleting my Scopus ID from ORCID didn't help because that doesn't remove entries previously pulled from Web of Science that have an EID.

At any rate, it would be great if this issue were noted in the docs along with whatever the recommended solution is.


