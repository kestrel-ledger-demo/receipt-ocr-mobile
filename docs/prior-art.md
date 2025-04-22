# Prior-art search: receipt reading under 30 MB on faded thermal paper

Written: 2025-04-22, by Priya Raman, before the first experiment.

## What we searched
- arXiv and Papers with Code: "knowledge distillation OCR mobile", "receipt OCR on-device", "thermal paper fading OCR",
  "degraded document enhancement".
- Model cards of the published receipt and document OCR models we could run on a phone.

## What we found
- Small published receipt models from 18 to 30 MB, with accuracy reported on clean receipts only.
- Models that read faded prints well are over 100 MB.
- Degraded-document enhancement work targets scanned pages, not phone photos of thermal receipts.

## What we did not find
- Any result for a model under 30 MB reading faded thermal receipts at 95% field accuracy.
