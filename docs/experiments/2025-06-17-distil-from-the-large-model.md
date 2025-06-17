# Distil from the large model

Date: 2025-06-17
Who: Priya Raman, Ahmed Siddiqui
Uncertainty: U1 Small model on faded thermal paper

## Plan (written before the run)

Hypothesis: A 25 MB student distilled from a 120 MB teacher keeps 95%.
What changes: Student trained on teacher outputs over 40,000 receipts.
Setup: Phone test set, on-device.

## Result (written the same day)

Result: 92% overall, 84% on faded thermal; 26 MB.
Learned: Big gain, but faded prints still trail by 11 points.
Outcome: Partly worked
