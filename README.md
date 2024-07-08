# BrainStation Capstone - Markers for Detecting Elderly Falls
=======================================================================================

## Executive Summary

### The Problem Area: 
Falls are a significant problem amongst senior citizens, negatively impacting their quality of life, causing significant health complications, and even leading to death. Society seems to accept this as the norm, but this project aims to highlight certain markers to prevent falls from ever happening and what seniors and their loved ones can do today to prevent falls. 

### Data Science Solution:
With predictive modelling, there is an opportunity to identify common variables that are indicators to predict the likelihood of a fall. The proposed solution:
1) Data Preprocessing (Tools: Pandas, Numpy, Matplotlib, Plotly) - We will pull from existing datasets to first clean and manipulate the data
2) Model Selection and Training (Tools: Scikit-learn, logistic regression, decision trees, random forests) - To check for statistical significance and train our model to predict likelihood of falls occuring
3) Model Deployment (Tools: AWS, Google Cloud) - For cloud-based deployment and scaling

### Key Takeaway:
The key takeaways from this project would be to identify which variables (physical activity, diet, or social connection), have a high correlation with an accident like a fall occurring. 

# Data Dictionary

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
reaching_overhead_difficulty | Participant's own assesment of their reaching overhead difficulty on 1-5 scale
walking_difficulty | Participant's own assesment of their walking difficulty on 1-5 scale
difficult_short_walking | 1 = Yes; 0 = No
difficult_light_housework | 1 = Yes; 0 = No
difficult_bathing | 1 = Yes; 0 = No
has_fallen | 1 = Yes; 0 = No
has_near_fallen | 1 = Yes; 0 = No
near_fall_count | Count of near fall
trial_1_eyes_closed_feet_apart_velocity_0_1 | acceleration measurment on wii balance board
trial_1_eyes_closed_feet_apart_velocity_0_2 | acceleration measurment on wii balance board
trial_1_eyes_closed_feet_apart_velocity_0_3 | acceleration measurment on wii balance board
trial_2_eyes_open_feet_together_velocity_0_1 | acceleration measurment on wii balance board
trial_2_eyes_open_feet_together_velocity_0_2 | acceleration measurment on wii balance board
trial_2_eyes_open_feet_together_velocity_0_3 | acceleration measurment on wii balance board
avg_grip_strength | Average of left and right hand grip measurements
grip_difference | Absolute difference between left and right hand grip measurements

## Data Visualization

![Scatter_grip_vs_age](https://github.com/timpengg/bstn_capstone_Apr2024/assets/124457182/44388a22-75dc-4a2b-8fe8-10ec7665f948)

We can see a negative correlation with age and grip strength. Grip strength will be explored as a potential marker and predictor for if a fall will occur. 

![Probability_falling_avggrip](https://github.com/timpengg/bstn_capstone_Apr2024/assets/124457182/3c994545-0653-4835-b0a1-f98d684c1cd8)

With every unit increase in average grip strength, it can be observed that the probability of falling decreases by 0.05 or 5%

## Notebooks
1) **Exploratory Data Analysis** - basic EDA was performed on the dataset to clean and preprocess the data as well as a first "deep dive" in order to pull some hypothesis and insights
2) **Feature Engineering** - new features were created from the existing dataset
3) **Baseline Models** - Logistic regression and Random Forest classifier model were implimented as baseline models with decent results
4) **Advanced Models** - Our models were built more rigorously using cross validation and hyper parameter optimization
5) **Insights** - This notebook was used to calculate the log odds ratio of certain variables such as age and average grip strength

## Datasets

https://drive.google.com/drive/folders/1egZ4YCGwGGWB89Tk81Mo11M5_WP3i3di?usp=drive_link

## References

Sean M. Mullan, Nicholas J. Evans, Daniel K. Sewell, Shelby L. Francis, Linnea A. Polgreen, Alberto M. Segre, and Philip M. Polgreen. (2022). Wii balance board movement of the elderly [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/3907218 

