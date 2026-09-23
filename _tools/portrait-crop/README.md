# portrait-crop

Crops team photos to a consistent square head-and-shoulders framing, so the
portraits on `/team` read as one set rather than as fifty phone photos.

Underscore-prefixed, so Jekyll ignores it; nothing here ships with the site.

## The framing contract

Two numbers decide everything:

- **`FACE_FRAC` (0.44)** — the detected face box is 44% of the square's height.
- **`EYE_FRAC` (0.40)** — the eye line sits 40% of the way down from the top.

Everything else is clamping to stay inside the source image. When a face sits
near an edge the crop slides back in rather than padding, so framing degrades
gracefully instead of producing a letterboxed portrait.

**It never upscales.** A 42px face blown up to 600px looks worse than a small
sharp one, so the output is `min(600, available)` and anything that lands under
350px is reported as `LOW-RES` — that person needs a better source photo, and no
amount of cropping will fix it.

## Running it

Needs macOS (Vision framework) and Pillow. No other dependencies.

```bash
swiftc -O -o facedetect facedetect.swift

export W=/path/to/workdir          # expects $W/originals/ to hold the sources
cd "$W/originals" && ls | xargs "$W/facedetect" > "$W/faces.json"
W="$W" python3 crop.py "$W/out"
```

Output filenames match the inputs exactly, extension included, because the
member front matter in `_members/` points straight at them.

Exclude the lab/group photos (`LLL_team`, `Eskes-Lab`, `LangDevLab`, `MOM-LINC`,
`PVSRG`, `join.jpg`) — they are not portraits and face-centring ruins them.

## Where the source photos come from

New members upload one to the REDCap intake form. It arrives via the **Website
profile** report and lands in
`NCIL Admin/03_People-HR/Onboarding-Intake/<year>/Intake Forms/<Name>/<record_id>_photo.<ext>`.
Use that full-resolution original as the crop source, never the copy already in
`images/team/` — cropping an already-cropped image throws away pixels twice.
