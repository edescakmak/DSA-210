
# FIFA 25 Player Rating Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load player data
players_df = pd.read_csv('players_data.csv')

# 1. Calculate 'Overall' score for each player by averaging key in-game stats
players_df['Overall'] = players_df[['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physicality']].mean(axis=1)

# 2. Calculate average overall rating per team
team_avg = players_df.groupby('Team')['Overall'].mean().reset_index()
team_avg.columns = ['Squad', 'Avg_Overall']

# 3. Load team performance data and merge with average player ratings
team_data = pd.read_excel('team_stats.xlsx')
team_data['Squad'] = team_data['Squad'].str.strip().str.lower()
team_avg['Squad'] = team_avg['Squad'].str.strip().str.lower()
merged = pd.merge(team_data, team_avg, on='Squad')
merged['Pts'] = pd.to_numeric(merged['Pts'], errors='coerce')

# 4. Graph 1: Team performance vs average player rating
plt.figure(figsize=(10, 6))
sns.regplot(data=merged, x='Pts', y='Avg_Overall')
plt.title('Team Performance vs. Avg. Player Overall')
plt.xlabel('Total Points (2023/24 Season)')
plt.ylabel('Average Overall Rating')
plt.grid(True)
plt.tight_layout()
plt.savefig('team_vs_rating_plot.png')
plt.close()

# 5. Feature importance analysis: Identify which stats affect 'Overall' the most
features = ['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physicality']
X = players_df[features]
y = players_df['Overall']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# 6. Graph 2: Visualize importance of each stat in predicting 'Overall'
importances = model.feature_importances_
plt.figure(figsize=(8, 5))
sns.barplot(x=importances, y=features)
plt.title('Feature Importance for Overall Rating')
plt.tight_layout()
plt.savefig('feature_importance_plot.png')
plt.close()
