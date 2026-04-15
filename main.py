# =========================
# 1. Imports/Config:
# =========================

from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style='darkgrid',
              palette='viridis')


# =========================
# 2. Setup:
# =========================

os.makedirs("visuals", exist_ok=True)

# =========================
# 3. Load Data:
# =========================

df = pd.read_csv("data/gaming_mental_health.csv")

# =========================
# 4. Cleaning/Troubleshooting:
# =========================
# null check
## print(df.isna().sum())
## print (df.head())
## print (df.info())

# =========================
# 5. Filters:
# =========================

#Gaming categories
df["gamer_type"]=pd.cut(
    df["daily_gaming_hours"],
    bins=[0,2,5,10],
    labels=["light", "moderate", "heavy"],
    include_lowest=True
)

#Happiness levels
df["happy_group"] = pd.cut(
    df["happiness_score"],
    bins=3,
    labels=["low", "medium", "high"]
)

#socializing levels
df["social_group"] = pd.cut(
    df["social_interaction_score"],
    bins=3,
    labels=["low", "medium", "high"]
)

# =========================
# 6. Research Questions:
# =========================

# Q1: How does gaming intensity relate to different aspects of mental health?

q1_summary = df.groupby("gamer_type")[[
    "sleep_hours",
    "stress_level",
    "anxiety_score",
    "depression_score",
    "happiness_score",
    "addiction_level"
]].mean()

#print(q1_summary)

#What relates to stress?
stress_levels = df.corr(numeric_only=True)["stress_level"].sort_values(ascending=False)
#print(stress_levels)

#It is a weak correlation, but I think its interesting that microtransaction
#spending is the first relation for stress_levels. There is a box plot to look
#at the distribution of microtransaction spending between light, moderate,
#and heavy gaming.

#Q2: How does social interaction influence whether gaming is associated with positive or negative emotional well-being?
q2_summary = df.groupby(["gamer_type", "social_group"])[[
     "happiness_score",
     "loneliness_score",
]].mean()

# =========================
# 7. Linear Regression:
# =========================

#Predict stress levels from gaming + microtransaction spending
X = df[["daily_gaming_hours", "microtransactions_spending"]].dropna()
y = df.loc[X.index, "stress_level"]

model = LinearRegression()
model.fit(X, y)


print("Gaming Hours Coefficient:", model.coef_[0])
print("Microtransaction Spending Coefficient:", model.coef_[1])
print("Intercept:", model.intercept_)
print("R-squared:", model.score(X, y))


# =========================
# 8. Visualizations:
# =========================


#corr matrix
## print(df[[
   # "daily_gaming_hours",
    #"stress_level",
    #"sleep_hours",
    #"addiction_level",
    #"happiness_score",
    #"exercise_hours"
#]].corr())

#Q1:

plt.figure()
q1_summary.plot(kind="bar")
plt.title("Mental Health Metrics by Gaming Intensity")
plt.xlabel("Gamer Type")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("visuals/q1_summary.png")
plt.show()
plt.close()

#Q2:
plt.figure()
sns.barplot(
    x="gamer_type",
    y="happiness_score",
    hue="social_group",
    data=df
)
plt.title("Happiness by Gaming Intensity and Social Interaction")
plt.tight_layout()
plt.savefig("visuals/q2_happiness.png")
plt.show()
plt.close()

plt.figure()
sns.barplot(
    x="gamer_type",
    y="loneliness_score",
    hue="social_group",
    data=df
)
plt.title("Loneliness by Gaming Intensity and Social Interaction")
plt.tight_layout()
plt.savefig("visuals/q2_loneliness.png")
plt.show()
plt.close()

#Microtransactions distribution:
plt.figure()
sns.boxplot(
    x="gamer_type",
    y="microtransactions_spending",
    data=df
)
plt.title("Microtransaction Spending by Gaming Intensity")
plt.xlabel("Gaming Intensity")
plt.ylabel("Spending")
plt.tight_layout()
plt.savefig("visuals/microtransactions_distribution.png")
plt.show()
plt.close()
