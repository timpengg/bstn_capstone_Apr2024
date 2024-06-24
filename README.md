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

### Data Dictionary

Column | Description
----------|------------
label | Gait-stabilizing device users; 0 = Not gait-stabilizing device users
age | Participant's age
sex | 1 = Male; 0 = Female
grip_r1 | Right hand grip measured with handgrip dynamometer
grip_l1 | Left hand grip measured with handgrip dynamometer
health_rating | Participant's own assesment of their health on 1-5 scale
crouching_difficulty | Participant's own assesment of their crouching ability on 1-5 scale
lifting_difficulty | Participant's own assesment of their lifting difficulty on 1-5 scale
walking_difficulty | Participant's own assesment of their walking difficulty on 1-5 scale
has_fallen | 1 = Yes; 0 = No
has_near_fallen | 1 = Yes; 0 = No
trial_1_eyes_closed_feet_apart_velocity_0_1 | balance test on wii balance board
trial_1_eyes_closed_feet_apart_velocity_0_2 | balance test on wii balance board
trial_1_eyes_closed_feet_apart_velocity_0_3 | balance test on wii balance board
trial_2_eyes_open_feet_together_velocity_0_1 | balance test on wii balance board
trial_2_eyes_open_feet_together_velocity_0_2 | balance test on wii balance board
trial_2_eyes_open_feet_together_velocity_0_3 | balance test on wii balance board

#### Data Visualization

![Scatter_grip_vs_age](https://github.com/timpengg/bstn_capstone_Apr2024/assets/124457182/44388a22-75dc-4a2b-8fe8-10ec7665f948)

We can see a negative correlation with age and grip strength. Grip strength will be explored as a potential marker and predictor for if a fall will occur. 

![Walking_diff](https://github.com/timpengg/bstn_capstone_Apr2024/assets/124457182/eb42445e-e5c1-47c9-9c7e-dae6fd42a6f0)

![grip_vs_fall](https://github.com/timpengg/bstn_capstone_Apr2024/assets/124457182/e677acf4-2632-4625-993f-fd765c5c8a37)


### Baseline Models

Fitting a baseline logistic regression model yielded an accuracy of 78% and an F1 score of 69%. The model was trained on independant variables of `grip_l1`, `has_near_fall`, `health_rating`, and `walking_difficulty` columns. Our target variable was `has_fallen`. 

Fitting a random forest classifier yielded an accuracy of 78% (using 20 n estimators) and an F1 score of 67%.

#### Datasets

https://drive.google.com/drive/folders/1egZ4YCGwGGWB89Tk81Mo11M5_WP3i3di?usp=drive_link

### Credits & References


