
# FIFA 25 Player Rating Analysis (Extended Version)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load data
players_df = pd.read_csv('players_data.csv')
team_data = pd.read_excel('team_stats.xlsx')

# Clean team names for merging
team_data['Squad'] = team_data['Squad'].str.strip().str.lower()
players_df['Team'] = players_df['Team'].str.strip().str.lower()

# 1. Calculate Overall rating from 6 core attributes
features = ['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physicality']
players_df['Overall'] = players_df[features].mean(axis=1)

# Merge with team performance data
team_avg = players_df.groupby('Team')['Overall'].mean().reset_index()
team_avg.columns = ['Squad', 'Avg_Overall']
merged = pd.merge(team_data, team_avg, on='Squad')
merged['Pts'] = pd.to_numeric(merged['Pts'], errors='coerce')

# ===================== GRAPH 1 =====================
# Team Performance vs. Average Player Overall
plt.figure(figsize=(10, 6))
sns.regplot(data=merged, x='Pts', y='Avg_Overall')
plt.title('Team Performance vs. Avg. Player Overall')
plt.xlabel('Total Points (2023/24)')
plt.ylabel('Average Overall Rating')
plt.grid(True)
plt.tight_layout()
plt.savefig('team_vs_rating_plot.png')
plt.close()

# ===================== GRAPH 2 =====================
# Feature Importance (Random Forest)
X = players_df[features]
y = players_df['Overall']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

importances = model.feature_importances_
plt.figure(figsize=(8, 5))
sns.barplot(x=importances, y=features)
plt.title('Feature Importance for Overall Rating')
plt.tight_layout()
plt.savefig('feature_importance_plot.png')
plt.close()

# ===================== GRAPH 3 =====================
# Distribution of Overall Ratings (Histogram)
plt.figure(figsize=(8, 5))
sns.histplot(players_df['Overall'], bins=15, kde=True)
plt.title('Distribution of Player Overall Ratings')
plt.xlabel('Overall Rating')
plt.ylabel('Number of Players')
plt.tight_layout()
plt.savefig('overall_distribution.png')
plt.close()

# ===================== GRAPH 4 =====================
# Correlation Heatmap between Stats
plt.figure(figsize=(8, 6))
corr = players_df[features + ['Overall']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Between Stats and Overall')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.close()
