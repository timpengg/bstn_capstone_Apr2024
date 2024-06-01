# BrainStation Capstone - Markers for Detecting Elderly Falls
=======================================================================================

### Executive Summary

#### The Problem Area: 
Falls are a significant problem amongst senior citizens, negatively impacting their quality of life, causing significant health complications, and even leading to death. Society seems to accept this as the norm, but this project aims to highlight certain markers to prevent falls from ever happening and what seniors and their loved ones can do today to prevent falls. 

#### Proposed Data Science Solution:
With predictive modelling, there is an opportunity to identify common variables that are indicators to predict the likelihood of a fall. The proposed solution:
1) Data Preprocessing (Tools: Pandas, Numpy, Matplotlib, Plotly) - We will pull from existing datasets to first clean and manipulate the data
2) Model Selection and Training (Tools: Scikit-learn, logistic regression, decision trees, random forests) - To check for statistical significance and train our model to predict likelihood of falls occuring
3) Model Deployment (Tools: AWS, Google Cloud) - For cloud-based deployment and scaling

#### Key Takeaway:
The key takeaways from this project would be to identify which variables (physical activity, diet, or social connection), have a high correlation with an accident like a fall occurring. 

### Demo

#### Data Visualization

![Scatter_grip_vs_age](https://github.com/timpengg/bstn_capstone_Apr2024/assets/124457182/44388a22-75dc-4a2b-8fe8-10ec7665f948)

We can see a negative correlation with age and grip strength. Grip strength will be explored as a potential marker and predictor for if a fall will occur. 

![Walking_diff](https://github.com/timpengg/bstn_capstone_Apr2024/assets/124457182/eb42445e-e5c1-47c9-9c7e-dae6fd42a6f0)

![grip_vs_fall](https://github.com/timpengg/bstn_capstone_Apr2024/assets/124457182/e677acf4-2632-4625-993f-fd765c5c8a37)


### Methodology

![Screenshot 2024-06-01 at 9 29 08 AM](https://github.com/timpengg/bstn_capstone_Apr2024/assets/124457182/c2fc3fa9-7ee7-4d5d-a6bd-88fad1a0d3b2)

### Organization

#### Repository 

* `data`
  
https://drive.google.com/drive/folders/1egZ4YCGwGGWB89Tk81Mo11M5_WP3i3di?usp=drive_link

* `model`
 --TBD--
    - `joblib` dump of final model(s)

* `notebooks`
    - contains all final notebooks involved in the project

* `docs` --TBD--
    - contains final report, presentations which summarize the project

* `references` --TBD--
    - contains papers / tutorials used in the project

* `src` --TBD--
    - Contains the project source code (refactored from the notebooks)

* `.gitignore` --TBD--
    - Part of Git, includes files and folders to be ignored by Git version control

* `conda.yml` 
          conda version : 24.1.2 
    conda-build version : 24.1.2 
         python version : 3.11.7.final.0

* `README.md`
    - Project landing page (this page)

* `LICENSE`
    - Project license

#### Datasets

https://drive.google.com/drive/folders/1egZ4YCGwGGWB89Tk81Mo11M5_WP3i3di?usp=drive_link

### Credits & References


