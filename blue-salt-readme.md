# Blue Salt Customer Journey Analysis 🧂

## Project Overview
This repository contains a comprehensive data analysis of customer interviews for Eupherbia Blue Salt, conducted as part of Cornell Executive MBA's Marketing Strategy course (NBAB620/MBQC932).

### 🎯 Objective
Analyze customer interview data to:
- Identify Jobs to be Done (JTBD) for Blue Salt
- Map the complete customer journey
- Uncover pain points and opportunities
- Provide data-driven strategic recommendations

## 📊 Key Findings

Based on analysis of 7 in-depth customer interviews:

1. **No Dominant Job**: Customers split across 3 different jobs (Social Bonding 43%, Health 29%, Gratification 29%)
2. **Major Pain Points**: 57% visual disappointment, 57% price concerns
3. **Usage Paradox**: Higher income ($267K) correlates with less frequent use
4. **Strategic Pivot Needed**: From "Premium Health Salt" to "Social Currency Tool"

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
pip install -r requirements.txt
```

### Running the Analysis
```bash
python blue_salt_customer_analysis.py
```

### Output Files
The analysis generates:
- `blue_salt_analysis_dashboard.png` - Visual summary dashboard
- `customer_journey_satisfaction.png` - Journey stage analysis
- `blue_salt_analysis_report.txt` - Executive summary report
- `blue_salt_clean_data.csv` - Cleaned dataset for further analysis

## 📁 Project Structure
```
blue-salt-analysis/
│
├── blue_salt_customer_analysis.py   # Main analysis script
├── data_collection_guide.md         # Interview methodology
├── requirements.txt                 # Python dependencies
├── README.md                       # This file
│
├── data/                           # Data directory
│   ├── raw/                        # Raw interview transcripts
│   └── processed/                  # Cleaned data files
│
├── outputs/                        # Analysis outputs
│   ├── visualizations/            # Generated charts
│   └── reports/                   # Analysis reports
│
└── notebooks/                      # Jupyter notebooks (optional)
    └── exploratory_analysis.ipynb
```

## 🔍 Methodology

### Data Collection
- **Sample Size**: 7 customers across North America
- **Method**: Semi-structured interviews following customer journey stages
- **Demographics**: Ages 35-70, income $50k-$300k+, diverse locations
- **Ethics**: Full informed consent, data anonymization, secure storage

### Analysis Pipeline
1. **Data Collection**: Structured interview data from 7 participants
2. **Data Cleaning**: Standardization, missing value handling, feature engineering
3. **Demographic Analysis**: Sample characteristics and segmentation
4. **JTBD Analysis**: Job distribution and correlation with demographics
5. **Pain Point Analysis**: Key friction points in customer experience
6. **Usage Pattern Analysis**: Frequency and behavioral patterns
7. **Strategic Recommendations**: Data-driven positioning strategy

## 📈 Key Visualizations

### Jobs to be Done Distribution
![JTBD Distribution](outputs/visualizations/jtbd_distribution_sample.png)

### Customer Journey Satisfaction
![Journey Satisfaction](outputs/visualizations/journey_satisfaction_sample.png)

## 💡 Strategic Recommendations

Based on the analysis, we recommend:

**FROM**: Premium Salt Brand → **TO**: Social Currency Tool
- **Price Point**: $8.99 (accessible luxury)
- **Target**: Status-conscious entertainers
- **Key Value**: Conversation starter for social occasions

## 🛠️ Technical Details

### Dependencies
- pandas: Data manipulation and analysis
- numpy: Numerical computations
- matplotlib: Visualization framework
- seaborn: Statistical data visualization

### Data Privacy
- All participant data anonymized
- Secure storage protocols followed
- Data destruction scheduled for August 31, 2025

## 👥 Team

**Team 1 - Cornell Executive MBA 2026**
- Data Analysis Lead: [Your Name]
- Project Contributors: Jade Leone, Mark Lee, Paul Skerry, Paroz Mehta, Leilani Rebolledo, Stone Wu, Matthew Street

## 📝 License

This project is part of academic coursework at Cornell University. All rights reserved.

## 🤝 Acknowledgments

Special thanks to:
- Interview participants for their valuable insights
- Dr. Monica LaBarge for course guidance
- Cornell SC Johnson College of Business

---

*For questions or additional information, please contact the project team.*