# Plan: on-device receipt reading

Written: 2025-04-15, by Priya Raman, at the start of the project and before the first experiment.

## What we don't know
Whether a model under 30 MB can read receipt fields (amount, date, merchant) at 95% accuracy or better on
crumpled, faded thermal paper, on the phone itself.

## What is known, and why it isn't enough
- The smallest published OCR model we found is 18 MB. Published models that read faded prints well are over
  100 MB, about 4 times our 30 MB budget.
- The work we checked on enhancing degraded documents is about scanned pages, not phone photos of thermal
  receipts, and reports no results under 30 MB.

## How we will test it
- First a fair test set: 1,200 receipts from 6 phone models, labelled twice, about 40% faded thermal paper.
- H1: the 18 MB published model reaches 95% on our set (the baseline).
- H2, if it doesn't: a student distilled from a large teacher keeps 95% at about 25 MB.
- H3: training on faded examples closes the gap on faded prints.
- Done when field accuracy is 95% or better overall AND on faded thermal, under 30 MB, on the device.
- Each run gets a note in docs/experiments/ with the plan before it starts and the result the same day.
