# Cancer Diagnosis Statistical Analysis

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29%2B-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

🚀 **[Live Demo](https://cancer-diagnosis-statistical-analysis.streamlit.app/)**

A comprehensive Python project for performing statistical hypothesis testing on cancer diagnosis data, featuring synthetic data generation, advanced statistical analysis, and an interactive Streamlit web application.

## 🎯 Project Overview

This project implements a complete statistical analysis pipeline for cancer diagnosis research, demonstrating professional-grade data science and statistical analysis capabilities. The application combines rigorous statistical methodologies with modern web technologies to create an accessible, interactive platform for medical data analysis.

### Key Features

- **🧬 Synthetic Medical Data Generation**: Creates realistic tumor characteristic data with proper medical distributions and configurable parameters
- **📊 Comprehensive Statistical Testing**: Implements t-tests, ANOVA, chi-square tests with effect size calculations and clinical interpretations
- **📈 Advanced Visualizations**: Interactive Plotly charts, publication-quality matplotlib/seaborn plots, and correlation analysis
- **🖥️ Web-based Interface**: Professional Streamlit application with intuitive design and responsive layout
- **💾 Data Management**: CSV upload/download capabilities, data validation, and reproducible analysis workflows

## 📊 Features

### Data Generation & Management
- Generates synthetic medical data with realistic statistical patterns
- Features include: Tumor Size, Smoothness, Compactness, Patient Age, Diagnosis
- Configurable sample sizes (100-2000) and random seeds for reproducibility
- Proper statistical distributions modeling real-world benign vs malignant cases
- CSV import/export functionality with data validation

### Statistical Analysis Suite
- **Descriptive Statistics**: Comprehensive summaries including mean, median, standard deviation, skewness, kurtosis
- **Independent T-Tests**: Compare means between diagnostic groups with assumption checking
- **One-Way ANOVA**: Analyze variance across multiple groups with post-hoc analysis capability
- **Chi-Square Tests**: Test independence between categorical variables (age groups vs diagnosis)
- **Effect Size Calculations**: Cohen's d, eta-squared (η²), Cramér's V for practical significance
- **Automated Interpretations**: Clinical significance assessments and result explanations

### Visualization Library
- **Distribution Plots**: Histograms with kernel density estimation and diagnostic overlay
- **Comparative Analysis**: Boxplots with quartiles, outliers, and statistical annotations
- **Correlation Analysis**: Heatmaps with hierarchical clustering and significance indicators
- **Interactive Exploration**: Plotly-powered scatter matrices with hover details and zooming
- **Results Summaries**: Statistical test visualizations with p-values and effect sizes
- **Demographic Analysis**: Age distribution breakdowns by diagnosis group

### Web Application Features
- **Dual Input Methods**: Upload CSV files or generate synthetic data in-app
- **Real-time Analysis**: Instant statistical computations with progress indicators
- **Interactive Dashboard**: Organized tabs for different analysis components
- **Responsive Design**: Mobile-friendly layout with optimized viewing
- **Data Export**: Download processed datasets and analysis results
- **Educational Content**: Built-in interpretations and statistical guidance

## 🚀 Quick Start

### Prerequisites

- **Python**: Version 3.7 or higher
- **pip**: Python package manager
- **Git** (optional): For cloning the repository

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nikhilesh9ix/Cancer-Diagnosis-Statistical-Analysis.git
   cd Cancer-Diagnosis-Statistical-Analysis
   ```

   Alternatively, download and extract the ZIP file from GitHub.

2. **Create a virtual environment** (recommended):
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

#### Windows
```bash
# Using batch file
run_app.bat

# Or using PowerShell script
.\run_app.ps1

# Or directly
streamlit run app.py
```

#### macOS/Linux
```bash
streamlit run app.py
```

The application will automatically open in your default browser at `http://localhost:8501`.

### Quick Test Run

```bash
# Test data generation
python data_generator.py

# Test statistical analysis
python statistical_analysis.py

# Test visualizations
python visualizations.py

# Run integration tests
python test_integration.py
```

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
Cancer-Diagnosis-Statistical-Analysis/
│
├── app.py                      # Main Streamlit web application
├── data_generator.py           # Synthetic medical data generation module
├── statistical_analysis.py     # Statistical testing and hypothesis testing
├── visualizations.py           # Plotting and visualization functions
├── test_integration.py         # Integration tests for all modules
│
├── requirements.txt            # Python package dependencies
├── README.md                   # Project documentation (this file)
├── DEPLOYMENT.md              # Streamlit Cloud deployment guide
│
├── run_app.bat                # Windows batch script to run the app
├── run_app.ps1                # PowerShell script to run the app
│
└── cancer_diagnosis_data.csv  # Generated synthetic dataset (created at runtime)
```

### Module Descriptions

- **app.py**: Frontend interface built with Streamlit, handles user interactions, data loading, and result presentation
- **data_generator.py**: Creates realistic synthetic medical data with configurable parameters and statistical distributions
- **statistical_analysis.py**: Implements the `StatisticalAnalyzer` class with all hypothesis testing methods
- **visualizations.py**: Contains the `MedicalDataVisualizer` class for creating static and interactive plots
- **test_integration.py**: Automated tests to verify module functionality and integration

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

## 🔧 Customization & Extension

### Adding New Statistical Tests

Extend the `StatisticalAnalyzer` class in [statistical_analysis.py](statistical_analysis.py):

```python
def mann_whitney_test(self, feature: str) -> Dict[str, Any]:
    """Non-parametric alternative to t-test"""
    benign = self.data[self.data['Diagnosis'] == 'Benign'][feature]
    malignant = self.data[self.data['Diagnosis'] == 'Malignant'][feature]
    statistic, p_value = stats.mannwhitneyu(benign, malignant, alternative='two-sided')
    return {'statistic': statistic, 'p_value': p_value}
```

### Customizing Visualizations

Modify the `MedicalDataVisualizer` class in [visualizations.py](visualizations.py):

```python
def create_violin_plots(self) -> plt.Figure:
    """Add violin plots for distribution visualization"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    for idx, feature in enumerate(self.numeric_features):
        ax = axes[idx // 2, idx % 2]
        sns.violinplot(data=self.data, x='Diagnosis', y=feature, ax=ax)
    return fig
```

### Modifying Data Generation

Edit [data_generator.py](data_generator.py) to adjust distributions:

```python
# Example: Add new feature
texture = np.random.gamma(shape=2.0, scale=1.5, size=n_samples)
data['Texture'] = texture
```

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

## 🧪 Testing

### Automated Testing

Run the integration test suite:

```bash
python test_integration.py
```

This will verify:
- ✅ Data generation functionality
- ✅ Statistical analysis computations
- ✅ Visualization rendering
- ✅ Module integration
- ✅ Error handling

### Manual Testing Checklist

- [ ] Generate synthetic data with different sample sizes (100, 500, 1000, 2000)
- [ ] Upload a valid CSV file with correct format
- [ ] Run complete statistical analysis suite
- [ ] Generate all visualization types
- [ ] Download generated data and verify format
- [ ] Test on different browsers (Chrome, Firefox, Safari, Edge)
- [ ] Verify responsive design on mobile devices
- [ ] Check interpretation accuracy and completeness

### Test Individual Modules

```bash
# Test data generation
python -c "from data_generator import generate_medical_data; print(generate_medical_data(100).head())"

# Test statistical analysis
python -c "from statistical_analysis import StatisticalAnalyzer; import pandas as pd; print('StatisticalAnalyzer imported successfully')"

# Test visualizations
python -c "from visualizations import MedicalDataVisualizer; print('MedicalDataVisualizer imported successfully')"
```

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
- [ ] **Machine Learning Integration**: Implement classification models (Random Forest, SVM, Neural Networks)
- [ ] **Advanced Statistical Tests**: Add multivariate ANOVA, factor analysis, and survival analysis
- [ ] **Export Functionality**: Generate publication-ready figures in PDF/SVG format
- [ ] **Real-time Data Streaming**: Support for live data ingestion and analysis
- [ ] **Multi-language Support**: Internationalization for global accessibility
- [ ] **Database Integration**: PostgreSQL/MongoDB support for large datasets
- [ ] **REST API**: Enable programmatic access to analysis functions
- [ ] **Docker Containerization**: Simplified deployment with Docker
- [ ] **Advanced Reporting**: Automated PDF report generation with LaTeX

### Research Applications
- 🔬 **Medical Research**: Analyze clinical trial data and biomarker discovery
- 🏥 **Diagnostic Validation**: Evaluate diagnostic test accuracy and reliability
- 📊 **Epidemiological Studies**: Public health surveillance and trend analysis
- 🧬 **Genomic Analysis**: Statistical evaluation of genomic markers
- 💊 **Pharmaceutical Research**: Drug efficacy and safety analysis

## 🤝 Contributing

Contributions are welcome! This project is designed for educational and research purposes.

### How to Contribute

1. **Fork the repository** on GitHub
2. **Create a feature branch**: `git checkout -b feature/YourFeature`
3. **Make your changes** with clear, descriptive commits
4. **Add tests** for new functionality
5. **Update documentation** as needed
6. **Submit a pull request** with a detailed description

### Contribution Guidelines

- Follow PEP 8 style guidelines for Python code
- Add docstrings to all functions and classes
- Include type hints where appropriate
- Write clear commit messages
- Ensure all tests pass before submitting PR
- Update README.md if adding new features

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Cancer-Diagnosis-Statistical-Analysis.git
cd Cancer-Diagnosis-Statistical-Analysis

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install pytest black flake8  # Additional dev tools

# Make your changes and test
python test_integration.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Academic Use
If you use this project in academic work, please cite:
```
Cancer Diagnosis Statistical Analysis
Author: Nikhilesh
GitHub: https://github.com/nikhilesh9ix/Cancer-Diagnosis-Statistical-Analysis
Year: 2026
```

## 📞 Contact & Support

### Getting Help

- 📖 **Documentation**: Read through this README and the inline code documentation
- 🐛 **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/nikhilesh9ix/Cancer-Diagnosis-Statistical-Analysis/issues)
- 💬 **Discussions**: Join the conversation in [GitHub Discussions](https://github.com/nikhilesh9ix/Cancer-Diagnosis-Statistical-Analysis/discussions)

### Author

- **GitHub**: [@nikhilesh9ix](https://github.com/nikhilesh9ix)
- **Repository**: [Cancer-Diagnosis-Statistical-Analysis](https://github.com/nikhilesh9ix/Cancer-Diagnosis-Statistical-Analysis)

### Acknowledgments

This project was built using:
- **Streamlit** for the web interface
- **Pandas & NumPy** for data manipulation
- **SciPy** for statistical computations
- **Matplotlib, Seaborn & Plotly** for visualizations
- **Scikit-learn** for data processing utilities

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Built with ❤️ for medical research and statistical education**

[![GitHub stars](https://img.shields.io/github/stars/nikhilesh9ix/Cancer-Diagnosis-Statistical-Analysis?style=social)](https://github.com/nikhilesh9ix/Cancer-Diagnosis-Statistical-Analysis/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/nikhilesh9ix/Cancer-Diagnosis-Statistical-Analysis?style=social)](https://github.com/nikhilesh9ix/Cancer-Diagnosis-Statistical-Analysis/network/members)

</div>