# DSA-210
DSA 210 Term Project
# FC25 Player Rating Analysis in the Big 5 Leagues

## Project Motivation
The aim of this project is to analyze whether the overall ratings of players in FC25 are directly related to their in-game stats. Our hypothesis suggests that player overall ratings are significantly influenced by individual stat values and that we can determine which stat has the most impact on these ratings. Additionally, we will examine whether FIFA ratings align with real-life player performances in the previous season.

## Hypothesis
1. Player overall ratings in FC25 are directly correlated with individual stats such as pace, shooting, passing, dribbling, defending, and physicality.
2. We can identify the most influential stat that determines a player’s overall rating.
3. There is a potential discrepancy between FC25 ratings and real-life player performances from the last season.

## Data Sources
- **Kaggle**: FC25 player ratings and stats datasets
- **FBref**: Real-life player performance data for the 2023-2024 season

## Data Collection and Processing
- The dataset containing FC25 player ratings and stats will be obtained from **Kaggle**.
- The real-life performance statistics of players from the **Big 5 leagues** (Premier League, La Liga, Bundesliga, Serie A, Ligue 1) will be collected from **FBref**.
- Data will be cleaned and preprocessed in **Python** using libraries such as `pandas`, `numpy`, and `scikit-learn`.

## Data Analysis & Techniques
- **Exploratory Data Analysis (EDA)**: Understanding data distributions and relationships
- **Correlation Analysis**: Checking the statistical relationship between FC25 ratings and in-game stats
- **Feature Importance Analysis**: Using regression models (Linear Regression, Random Forest) to determine which stats influence player ratings the most
- **Comparative Analysis**: Examining differences between FC25 ratings and real-life player performances using statistical tests

## Expected Findings
- The key in-game stat(s) that contribute the most to a player’s overall rating.
- Insights into how well FC25 ratings align with real-life player performances.
- Any potential biases in the FC25 rating system compared to real-world data.

## Limitations and Future Work
- Possible inaccuracies due to missing or outdated data.
- Future work may involve expanding the dataset to include multiple FIFA versions for a historical comparison.
- Advanced machine learning models could be used to predict FC25 ratings based on real-life performance metrics.

## Project Timeline
- **March 10**: Submit project proposal (this README file)
- **April 18**: Collect and preprocess data; perform exploratory data analysis
- **May 23**: Apply machine learning methods to analyze stat importance
- **May 30**: Final report submission and presentation

## Technical Requirements
- **Programming Language**: Python
- **Libraries**: pandas, numpy, scikit-learn, matplotlib, seaborn

## Sources
- [Kaggle](https://www.kaggle.com) for FC25 player ratings and stats
- [FBref](https://fbref.com) for real-life player performance data

## Contribution & Documentation
- AI tools (LLMs) have been used for analysis and documentation and are explicitly mentioned where applicable.
- The project will be regularly updated and shared on **GitHub**.

