# Project 2: Planet Hunters TESS

This folder contains the materials for Project 2 of **Modern Astronomy**, Spring 2026, Peking University.

Project 2 is based on the citizen science platform **Planet Hunters TESS** (link: https://www.zooniverse.org/projects/nora-dot-eisner/planet-hunters-tess). The project explores how exoplanet detection can benefit from the complementary strengths of human visual inspection and algorithmic analysis. In addition to discussing the role of citizen scientists in identifying possible transit signals, this project introduces an automated detection pipeline as a comparison point.

The central question is:

> How can human pattern recognition and algorithmic transit detection work together in citizen science?

## Presentation Video

Video link:  
https://drive.google.com/file/d/1pL-4tP7isgGpf60RGg9NxX_nYbDSSq0I/view?usp=share_link

A small fun note: there is a bird call accidentally recorded at the very beginning of the video. It was not planned, but it ended up giving the opening a bit of unexpected “nature ambience.”

## Folder Structure

```text id="cdtaqw"
project2/
├── README.md
├── modernastro_project2_spr2026.pdf
├── analysis/
│   ├── general_data_processing.ipynb
│   └── tic_*_processing.ipynb
├── data/
│   └── mastDownload/
├── images/
│   ├── pia10106.jpg
│   ├── pia15258.jpg
│   ├── screenshot_01.png
│   ├── screenshot_02.png
│   ├── screenshot_03.png
│   └── screenshot_04.png
├── outputs/
│   ├── planet_hunters_tess_report.pdf
│   ├── planet_hunters_tess_script.docx
│   ├── planet_hunters_tess_presentation.key
│   └── planet_hunters_tess_presentation.pptx
└── report_source/
    ├── report_source.ipynb
    └── report_source.md
```

## Contents

- `analysis/`: Jupyter notebooks used for data processing and algorithmic transit detection.
- `data/mastDownload/`: Original TESS data downloaded from MAST.
- `images/`: Visual materials used in the report and presentation. Files named `piaxxxxx.jpg` are NASA/JPL source images, while `screenshot_xx.png` files are supporting screenshots.
- `outputs/`: Final project deliverables, including the written report, presentation slides, and presentation script.
- `report_source/`: Source files used to generate or draft the written report.
- `modernastro_project2_spr2026.pdf`: Original project assignment handout.

## Project Summary

Planet Hunters TESS is a citizen science project in which participants visually inspect TESS light curves to help identify potential exoplanet transits. This project uses that setting to discuss a broader question in modern astronomy: how should humans and algorithms collaborate when both have different strengths?

The automated pipeline helps clean light curves, search for periodic signals, and identify candidate transit events. Human observers contribute visual judgment, skepticism, and contextual interpretation. Some signals are easier for algorithms to flag, while others require human attention to patterns, artifacts, and physical plausibility.

Rather than treating human and algorithmic approaches as competitors, this project presents them as complementary parts of a more reliable scientific workflow.

