# Slide 179 — orbit video

Model: Seedance 2.5 (`seedance_2_5`), explicitly requested by user.
Job: `b6d6d266-df4f-46ec-b295-bbe64015a355`
Requested: 10 seconds, 1:1, 1080p, generated audio.
Source: approved storyboard `../ORBIT-STORYBOARD.md`.
Start frame: `../orbit-frames/01-sit.png`.
End frame: `../orbit-frames/04-coffee.png`.
Intermediate visual references: `02-snap.png`, `03-orbit.png`.
Exact submitted prompt: `prompt.txt`.
Submission response: `submission.json`; result metadata: `result.json`.

The heading is HTML over the video, not embedded/generated lettering. Service data and original table remain in `../combined.html`.

## Delivered / QA
Completed job output: 1440×1440, 24 fps, 10.05s, HEVC + AAC. Original preserved as `vlad-orbit-seedance25-original.mp4`; web copy encoded H.264 + AAC with faststart, same dimensions/duration.
Sampled all ten seconds: sitting, snap, real panel orbit, coffee action present; no strobe. Minor generated continuity issue: a second mug remains on the side table while Vlad holds a mug near the ending. No claim of perfect object continuity.
Browser playback: readyState 4, no media error. Seven service data objects exactly match services.json.
