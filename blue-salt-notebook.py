"""
Jupyter Notebook Template for Blue Salt Analysis
================================================
This file shows the structure of a Jupyter notebook for exploratory analysis.
Convert to .ipynb format or copy cells into Jupyter.
"""

# %% [markdown]
# # Blue Salt Customer Analysis - Exploratory Data Analysis
# 
# **Author**: [Your Name]  
# **Date**: January 2025  
# **Course**: Cornell Executive MBA - Marketing Strategy
# 
# ## Notebook Overview
# This notebook provides interactive exploration of Blue Salt customer interview data.

# %% [markdown]
# ## 1. Setup and Import Libraries

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

print("Libraries imported successfully!")
print(f"Analysis date: {datetime.now().strftime('%Y-%m-%d')}")

# %% [markdown]
# ## 2. Load and Explore Data

# %%
# Load the cleaned data
df = pd.read_csv('blue_salt_clean_data.csv')

print(f"Dataset shape: {df.shape}")
print(f"\nColumns: {list(df.columns)}")
print(f"\nData types:\n{df.dtypes}")

# %% [markdown]
# ### 2.1 First Look at the Data

# %%
# Display first few rows
df.head()

# %%
# Basic statistics
df.describe()

# %%
# Check for missing values
missing_data = df.isnull().sum()
print("Missing values per column:")
print(missing_data[missing_data > 0])

# %% [markdown]
# ## 3. Demographic Analysis

# %%
# Age distribution
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Histogram
ax1.hist(df['age'], bins=10, edgecolor='black', alpha=0.7)
ax1.set_xlabel('Age')
ax1.set_ylabel('Count')
ax1.set_title('Age Distribution of Participants')
ax1.axvline(df['age'].mean(), color='red', linestyle='--', label=f'Mean: {df["age"].mean():.1f}')
ax1.legend()

# Box plot by gender
df.boxplot(column='age', by='gender', ax=ax2)
ax2.set_title('Age by Gender')
ax2.set_xlabel('Gender')
ax2.set_ylabel('Age')

plt.tight_layout()
plt.show()

# %%
# Income analysis
print(f"Average income: ${df['income'].mean():,.0f}")
print(f"Median income: ${df['income'].median():,.0f}")
print(f"\nIncome by gender:")
print(df.groupby('gender')['income'].agg(['mean', 'median', 'count']))

# %% [markdown]
# ## 4. Jobs to be Done Analysis

# %%
# JTBD distribution
jtbd_counts = df['primary_jtbd'].value_counts()
jtbd_pct = (jtbd_counts / len(df) * 100).round(1)

# Create pie chart
plt.figure(figsize=(10, 8))
colors = ['#667eea', '#764ba2', '#f093fb']
plt.pie(jtbd_pct, labels=jtbd_pct.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Jobs to be Done Distribution', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.show()

# %%
# JTBD by demographics
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# By income bracket
jtbd_income = pd.crosstab(df['income_bracket'], df['primary_jtbd'])
jtbd_income.plot(kind='bar', ax=ax1, rot=0)
ax1.set_title('JTBD by Income Bracket')
ax1.set_xlabel('Income Bracket')
ax1.set_ylabel('Count')
ax1.legend(title='Job')

# Average income by JTBD
income_by_jtbd = df.groupby('primary_jtbd')['income'].mean().sort_values(ascending=False)
income_by_jtbd.plot(kind='bar', ax=ax2, color='#667eea')
ax2.set_title('Average Income by JTBD')
ax2.set_xlabel('Primary Job')
ax2.set_ylabel('Average Income ($)')
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

plt.tight_layout()
plt.show()

# %% [markdown]
# ## 5. Pain Points Analysis

# %%
# Calculate pain point percentages
pain_points = {
    'Price Concerns': (df['has_price_concern'].sum() / len(df) * 100),
    'Visual Disappointment': (df['disappointed_visual'].sum() / len(df) * 100),
    'Taste Uncertainty': ((~df['positive_taste']).sum() / len(df) * 100)
}

# Create horizontal bar chart
plt.figure(figsize=(10, 6))
pain_df = pd.DataFrame(list(pain_points.items()), columns=['Pain Point', 'Percentage'])
bars = plt.barh(pain_df['Pain Point'], pain_df['Percentage'], color=['#e74c3c', '#e67e22', '#f39c12'])

# Add percentage labels
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2, 
             f'{width:.0f}%', ha='left', va='center', fontweight='bold')

plt.xlabel('Percentage of Customers (%)')
plt.title('Customer Pain Points Analysis', fontsize=14, fontweight='bold')
plt.xlim(0, 80)
plt.tight_layout()
plt.show()

# %% [markdown]
# ## 6. Usage Patterns

# %%
# Usage frequency analysis
usage_dist = df['usage_category'].value_counts()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Usage distribution
usage_dist.plot(kind='bar', ax=ax1, color=['#2ecc71', '#3498db', '#9b59b6'])
ax1.set_title('Usage Frequency Distribution')
ax1.set_xlabel('Usage Category')
ax1.set_ylabel('Number of Customers')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)

# Income by usage pattern
usage_income = df.groupby('usage_category')['income'].mean()
usage_income.plot(kind='bar', ax=ax2, color=['#2ecc71', '#3498db', '#9b59b6'])
ax2.set_title('Average Income by Usage Pattern')
ax2.set_xlabel('Usage Category')
ax2.set_ylabel('Average Income ($)')
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)

plt.tight_layout()
plt.show()

# %% [markdown]
# ## 7. Customer Segmentation

# %%
# Create customer segments based on usage and income
df['segment'] = 'Unknown'

# High-value occasional users
mask1 = (df['usage_category'] == 'occasional') & (df['income'] > 200000)
df.loc[mask1, 'segment'] = 'Premium Gift Buyers'

# Regular health-conscious users
mask2 = (df['usage_category'].isin(['daily', 'weekly'])) & (df['primary_jtbd'] == 'healthy_meal')
df.loc[mask2, 'segment'] = 'Health Enthusiasts'

# Social users
mask3 = df['primary_jtbd'] == 'social_bonding'
df.loc[mask3, 'segment'] = 'Social Entertainers'

# Others
mask4 = df['segment'] == 'Unknown'
df.loc[mask4, 'segment'] = 'General Users'

# Visualize segments
segment_counts = df['segment'].value_counts()

plt.figure(figsize=(10, 6))
segment_counts.plot(kind='bar', color=['#e74c3c', '#3498db', '#2ecc71', '#f39c12'])
plt.title('Customer Segments', fontsize=14, fontweight='bold')
plt.xlabel('Segment')
plt.ylabel('Count')
plt.xticks(rotation=45)

# Add count labels
for i, v in enumerate(segment_counts):
    plt.text(i, v + 0.1, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# %% [markdown]
# ## 8. Key Insights Summary

# %%
# Create insights summary
insights = {
    'Total Participants': len(df),
    'Average Age': f"{df['age'].mean():.1f} years",
    'Average Income': f"${df['income'].mean():,.0f}",
    'Would Recommend': f"{(df['would_recommend_binary'].sum()/len(df)*100):.0f}%",
    'Price Concerns': f"{(df['has_price_concern'].sum()/len(df)*100):.0f}%",
    'Visual Disappointment': f"{(df['disappointed_visual'].sum()/len(df)*100):.0f}%",
    'Dominant JTBD': df['primary_jtbd'].value_counts().index[0],
    'JTBD Concentration': f"{(df['primary_jtbd'].value_counts().iloc[0]/len(df)*100):.0f}%"
}

# Display as formatted table
insights_df = pd.DataFrame(list(insights.items()), columns=['Metric', 'Value'])
print("KEY INSIGHTS SUMMARY")
print("="*40)
for _, row in insights_df.iterrows():
    print(f"{row['Metric']:<25} {row['Value']}")

# %% [markdown]
# ## 9. Strategic Recommendations

# %%
# Visual representation of strategic pivot
fig, ax = plt.subplots(figsize=(12, 8))

# Create visual framework
categories = ['Positioning', 'Target', 'Price', 'Value Prop']
current = ['Premium Salt', 'Health Conscious', '$14.99-$19.99', 'Healthier Salt']
recommended = ['Social Currency', 'Status Conscious', '$8.99', 'Conversation Starter']

x = np.arange(len(categories))
width = 0.35

bars1 = ax.bar(x - width/2, [1]*4, width, label='Current', color='#e74c3c', alpha=0.7)
bars2 = ax.bar(x + width/2, [1]*4, width, label='Recommended', color='#2ecc71', alpha=0.7)

# Add text
for i, (cat, curr, rec) in enumerate(zip(categories, current, recommended)):
    ax.text(i - width/2, 0.5, curr, ha='center', va='center', rotation=90, fontweight='bold')
    ax.text(i + width/2, 0.5, rec, ha='center', va='center', rotation=90, fontweight='bold')

ax.set_ylabel('Strategic Direction')
ax.set_title('Strategic Pivot: FROM Current TO Recommended', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.set_ylim(0, 1.5)
ax.set_yticks([])

plt.tight_layout()
plt.show()

# %% [markdown]
# ## 10. Next Steps
# 
# Based on this analysis:
# 
# 1. **Immediate Actions**:
#    - Enhance blue color intensity
#    - Adjust pricing to $8.99
#    - Develop social occasion marketing
# 
# 2. **Further Research**:
#    - Expand sample size for validation
#    - Test new positioning with target segment
#    - Measure price elasticity
# 
# 3. **Success Metrics**:
#    - Trial-to-repeat conversion >40%
#    - Social media mentions +200%
#    - Gift purchase rate >30%

# %%
# Save enhanced dataset
df.to_csv('blue_salt_enhanced_analysis.csv', index=False)
print("Enhanced dataset saved successfully!")
