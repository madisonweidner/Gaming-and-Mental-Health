# Gaming & Mental Health Analysis: 
### Madison Weidner 

## Introduction: 
This project explores the relationship between gaming behavior and mental health outcomes. The goal is to better
understand how gaming intensity and social interactions impact our emotional well-being. 

I selected this dataset because I grew up playing video games and was curious whether screen time truly had negative effects, or if my mother may have been slightly exaggerating. Before analyzing this data, I expected to see relationships such as high gaming hours/stress and low sleep. 

### Research Questions:
1. How does gaming intensity relate to different aspects of mental health?
2. How does social interaction influence whether gaming is associated with positive or negative emotional well-being?

## Selection of Data:
Dataset: 
- [Gaming and Mental Health](https://www.kaggle.com/datasets/sharmajicoder/gaming-and-mental-health?resource=download)

It is important to note that this dataset is simulated. The dataset includes features such as daily gaming hours, stress levels, anxiety, depression, happiness scores, social interaction, and microtransaction spending.

Feature engineering was applied to categorize:

gaming intensity (light, moderate, heavy)
happiness levels (low, medium, high)
social interaction levels (low, medium, high)
## Methods:
The following tools and libraries were used:
- Python 
- NumPy 
- Pandas
- Matplotlib & seaborn
- Scikit-learn

Methods:
- Data grouping and aggregation using groupby
- Correlation analysis to identify relationships
- Data visualization using bar plots and box plots
- Linear regression to model stress levels based on gaming habits and microtransaction spending. 


## Results:
1. How does gaming intensity relate to different aspects of mental health?

Mental health differences across gaming intensity levels are relatively small for most metrics, including sleep, depression, anxiety. This suggests that overall time spent gaming alone does not have a strong impact.

However, addiction levels increase significantly from light to heavy gamers, suggesting a stronger relationship between gaming intensity and addictive behavior than with general emotional well-being.

2. How does social interaction influence whether gaming is associated with positive or negative emotional well-being?

Happiness and loneliness scores remain consistent across different levels of gaming intensity and social interaction. This suggests that social interaction within gaming does not have a strong measurable effect on these outcomes in this dataset.

Additionally,  a linear regression model to predict stress based on daily gaming hours and microtransaction spending. The model produced an extremely low R² value, indicating that these variables explain virtually none of the variation in stress.

Both coefficients were very close to zero, suggesting that neither gaming intensity nor spending has a meaningful impact on stress levels.
## Discussion: 

These findings suggest that gaming itself is not inherently harmful or beneficial. Instead, its impact appears to rely on external factors that are outside the scope of this dataset. 
## Summary: 
Gaming intensity alone does not appear to be a strong predictor of specific mental health outcomes. Although increased gaming is associated with higher levels of addiction, most other mental health measures remain relatively consistent across different levels of intensity. 

My regression model further supported this, producing an extremely low R² value and indicating that gaming hours and microtransaction spending are not meaningful predictors of stress. 
 