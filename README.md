# Cancer Diagnosis Statistical Analysis

A comprehensive Python project for performing statistical hypothesis testing on cancer diagnosis data, featuring synthetic data generation, advanced statistical analysis, and an interactive Streamlit web application.

## 🎯 Project Overview

This project implements a complete statistical analysis pipeline for cancer diagnosis research, including:

- **Synthetic Medical Data Generation**: Creates realistic tumor characteristic data with proper medical distributions
- **Comprehensive Statistical Testing**: Performs t-tests, ANOVA, and chi-square tests
- **Advanced Visualizations**: Interactive plots, correlation analysis, and statistical summaries
- **Web-based Interface**: User-friendly Streamlit application for data upload and analysis

## 📊 Features

### Data Generation
- Generates synthetic medical data with realistic patterns
- Features: Tumor Size, Smoothness, Compactness, Patient Age, Diagnosis
- Configurable sample sizes and random seeds
- Proper statistical distributions for benign vs malignant cases

### Statistical Analysis
- **Descriptive Statistics**: Mean, median, standard deviation, skewness, kurtosis
- **Independent T-Tests**: Compare means between benign and malignant groups
- **One-Way ANOVA**: Analyze variance across diagnostic groups
- **Chi-Square Tests**: Test associations between categorical variables
- **Effect Size Calculations**: Cohen's d, eta-squared, Cramér's V

### Visualizations
- **Histograms**: Distribution plots with diagnostic overlay
- **Boxplots**: Group comparisons with outlier detection
- **Correlation Heatmaps**: Feature relationship analysis
- **Interactive Scatter Matrices**: Plotly-powered exploration
- **Statistical Summary Plots**: P-values and effect sizes
- **Age Distribution Analysis**: Demographic breakdowns

### Web Application
- **File Upload**: Support for CSV data import
- **Data Generation**: In-app synthetic data creation
- **Interactive Dashboard**: Real-time statistical analysis
- **Downloadable Results**: Export processed data
- **Responsive Design**: Works on desktop and mobile

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone or download the project:**
   ```bash
   # If using git
   git clone https://github.com/nikhilesh9ix/Cancer-Diagnosis-Statistical-Analysis.git
   cd Cancer-Diagnosis-Statistical-Analysis
   
   # Or download and extract the ZIP file
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser:**
   - The app will automatically open at `http://localhost:8501`
   - If not, navigate to the URL shown in your terminal

## 📖 Usage Guide

### Option 1: Generate Synthetic Data

1. **Select "Generate Synthetic Data"** in the sidebar
2. **Configure parameters:**
   - Number of samples (100-2000)
   - Random seed for reproducibility
3. **Click "Generate Data"** to create the dataset
4. **Review the data** in the overview section

### Option 2: Upload Your Own Data

1. **Select "Upload CSV File"** in the sidebar
2. **Choose your CSV file** with the required format:
   ```
   Patient_ID,Tumor_Size,Smoothness,Compactness,Patient_Age,Diagnosis
   P0001,12.5,0.095,0.089,45,Benign
   P0002,18.7,0.074,0.135,38,Malignant
   ```
3. **Review the uploaded data** in the overview section

### Performing Analysis

1. **Click "Run Statistical Analysis"** to perform all tests
2. **Explore the results** in the tabbed interface:
   - **Descriptive Stats**: Summary statistics by group
   - **T-Tests**: Mean comparisons with p-values and effect sizes
   - **ANOVA**: Variance analysis across groups
   - **Chi-Square**: Categorical associations

3. **Generate visualizations** by selecting from the dropdown:
   - Histograms for distribution analysis
   - Boxplots for group comparisons
   - Correlation heatmaps for feature relationships
   - Statistical summaries for test results
   - Age analysis for demographic insights

4. **View interpretations** to understand the clinical significance

## 📁 Project Structure

```
cancer_diagnosis_stats/
├── app.py                    # Main Streamlit application
├── data_generator.py         # Synthetic data generation
├── statistical_analysis.py   # Statistical testing functions
├── visualizations.py         # Plotting and visualization functions
├── requirements.txt          # Python dependencies
├── README.md                # This documentation file
└── cancer_diagnosis_data.csv # Generated dataset (created when running)
```

## 🔬 Statistical Methods

### Descriptive Statistics
- **Central Tendency**: Mean, median, mode
- **Variability**: Standard deviation, variance, range
- **Distribution Shape**: Skewness, kurtosis
- **Group Comparisons**: Stratified by diagnosis

### Hypothesis Testing

#### Independent T-Tests
- **Purpose**: Compare means between benign and malignant groups
- **Assumptions**: Normal distribution, equal variances
- **Output**: t-statistic, p-value, Cohen's d effect size
- **Interpretation**: Statistical and clinical significance

#### One-Way ANOVA
- **Purpose**: Analyze variance across diagnostic groups
- **Output**: F-statistic, p-value, eta-squared effect size
- **Use Case**: Alternative to multiple t-tests

#### Chi-Square Tests
- **Purpose**: Test independence between categorical variables
- **Application**: Age groups vs diagnosis association
- **Output**: Chi-square statistic, p-value, Cramér's V
- **Interpretation**: Strength of association

### Effect Sizes
- **Cohen's d**: Standardized mean difference (small: 0.2, medium: 0.5, large: 0.8)
- **Eta-squared**: Proportion of variance explained
- **Cramér's V**: Association strength for categorical variables

## 🎨 Visualization Features

### Static Plots (Matplotlib/Seaborn)
- **Histograms**: Overlaid distributions by diagnosis
- **Boxplots**: Group comparisons with quartiles and outliers
- **Heatmaps**: Correlation matrices with color coding
- **Bar Charts**: Statistical test results and effect sizes

### Interactive Plots (Plotly)
- **Scatter Matrices**: Multi-dimensional data exploration
- **Hover Information**: Detailed data point inspection
- **Zoom and Pan**: Dynamic plot interaction
- **Responsive Design**: Adapts to screen size

## 🔧 Customization

### Modifying Data Generation
Edit `data_generator.py` to:
- Add new features or modify existing ones
- Change statistical distributions
- Adjust sample size ranges
- Modify realistic value constraints

### Adding New Tests
Extend `statistical_analysis.py` to include:
- Non-parametric tests (Mann-Whitney U, Kruskal-Wallis)
- Multiple comparison corrections (Bonferroni, FDR)
- Advanced effect size measures
- Custom interpretation functions

### Enhancing Visualizations
Customize `visualizations.py` to:
- Add new plot types (violin plots, density plots)
- Modify color schemes and styling
- Include additional interactive features
- Export plots in different formats

## 🐛 Troubleshooting

### Common Issues

1. **Module Import Errors**
   ```bash
   # Ensure all dependencies are installed
   pip install -r requirements.txt
   ```

2. **Port Already in Use**
   ```bash
   # Run on a different port
   streamlit run app.py --server.port 8502
   ```

3. **Data Upload Errors**
   - Check CSV format matches expected columns
   - Ensure no missing values in critical columns
   - Verify numeric columns contain valid numbers

4. **Memory Issues with Large Datasets**
   - Reduce sample size for synthetic data
   - Consider data sampling for uploaded files
   - Close other memory-intensive applications

### Performance Tips

1. **Large Datasets**: Use data sampling for initial exploration
2. **Slow Visualizations**: Generate plots selectively rather than all at once
3. **Memory Management**: Clear session state when switching datasets

## 🧪 Testing the Application

### Automated Testing
Run the individual modules to verify functionality:

```bash
# Test data generation
python data_generator.py

# Test statistical analysis
python statistical_analysis.py

# Test visualizations
python visualizations.py
```

### Manual Testing Checklist

- [ ] Generate synthetic data with different parameters
- [ ] Upload a valid CSV file
- [ ] Run statistical analysis and verify results
- [ ] Generate each type of visualization
- [ ] Download generated data
- [ ] Test responsive design on different screen sizes

## 📈 Example Analysis Results

### Typical Findings
With the default synthetic data, you should expect:

1. **Tumor Size**: Malignant tumors significantly larger (p < 0.001)
2. **Smoothness**: Benign tumors more smooth/regular (p < 0.001)
3. **Compactness**: Malignant tumors more compact (p < 0.001)
4. **Patient Age**: Slight age difference between groups (p < 0.05)

### Effect Sizes
- Large effect sizes (Cohen's d > 0.8) for tumor characteristics
- Medium effect sizes (0.2 < d < 0.8) for demographic factors
- Strong correlations between physical tumor properties

## 🔮 Future Enhancements

### Planned Features
- [ ] Machine learning model integration
- [ ] Advanced statistical tests (multivariate ANOVA, factor analysis)
- [ ] Export functionality for publication-ready figures
- [ ] Real-time data streaming capabilities
- [ ] Multi-language support

### Research Applications
- Medical research data analysis
- Clinical trial statistical evaluation
- Biomarker discovery studies
- Diagnostic test validation
- Public health surveillance

## 🤝 Contributing

This project is designed for educational and research purposes. Contributions welcome:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request with detailed description

## 📄 License

This project is intended for educational use. Please cite appropriately if used in academic work.

## 📞 Support

For questions or issues:
1. Check the troubleshooting section
2. Review the code comments for implementation details
3. Test with the provided synthetic data first
4. Ensure all dependencies are correctly installed

## 🎓 Educational Objectives

This project demonstrates:
- Statistical hypothesis testing in medical contexts
- Data visualization best practices
- Web application development with Streamlit
- Code organization and documentation
- Reproducible research principles

---

**Built with ❤️ for medical research and statistical education**