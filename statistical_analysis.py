"""
Statistical Analysis Module for Cancer Diagnosis
Implements descriptive statistics and hypothesis testing functions.
"""

import pandas as pd
import numpy as np
from scipy import stats
from typing import Dict, List, Tuple, Any
import warnings
warnings.filterwarnings('ignore')

class StatisticalAnalyzer:
    """
    A comprehensive statistical analysis class for cancer diagnosis data.
    """
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the analyzer with the dataset.
        
        Parameters:
        -----------
        data : pd.DataFrame
            The cancer diagnosis dataset
        """
        self.data = data
        self.numeric_features = ['Tumor_Size', 'Smoothness', 'Compactness', 'Patient_Age']
        self.categorical_features = ['Diagnosis']
    
    def descriptive_statistics(self) -> Dict[str, pd.DataFrame]:
        """
        Calculate comprehensive descriptive statistics for all features.
        
        Returns:
        --------
        Dict[str, pd.DataFrame]
            Dictionary containing overall and group-wise statistics
        """
        results = {}
        
        # Overall descriptive statistics
        overall_stats = self.data[self.numeric_features].describe()
        results['overall'] = overall_stats
        
        # Group-wise statistics (by diagnosis)
        benign_data = self.data[self.data['Diagnosis'] == 'Benign'][self.numeric_features]
        malignant_data = self.data[self.data['Diagnosis'] == 'Malignant'][self.numeric_features]
        
        results['benign'] = benign_data.describe()
        results['malignant'] = malignant_data.describe()
        
        # Additional statistics
        results['skewness'] = self.data[self.numeric_features].skew()
        results['kurtosis'] = self.data[self.numeric_features].kurtosis()
        
        return results
    
    def independent_t_tests(self) -> Dict[str, Dict[str, float]]:
        """
        Perform independent t-tests for each numeric feature between benign and malignant groups.
        
        Returns:
        --------
        Dict[str, Dict[str, float]]
            T-test results for each feature
        """
        results = {}
        
        benign_data = self.data[self.data['Diagnosis'] == 'Benign']
        malignant_data = self.data[self.data['Diagnosis'] == 'Malignant']
        
        for feature in self.numeric_features:
            benign_values = benign_data[feature].dropna()
            malignant_values = malignant_data[feature].dropna()
            
            # Perform independent t-test
            t_stat, p_value = stats.ttest_ind(benign_values, malignant_values)
            
            # Calculate effect size (Cohen's d)
            pooled_std = np.sqrt(((len(benign_values) - 1) * benign_values.var() + 
                                 (len(malignant_values) - 1) * malignant_values.var()) / 
                                (len(benign_values) + len(malignant_values) - 2))
            cohens_d = (benign_values.mean() - malignant_values.mean()) / pooled_std
            
            results[feature] = {
                't_statistic': t_stat,
                'p_value': p_value,
                'cohens_d': cohens_d,
                'significant': p_value < 0.05,
                'benign_mean': benign_values.mean(),
                'malignant_mean': malignant_values.mean(),
                'benign_std': benign_values.std(),
                'malignant_std': malignant_values.std()
            }
        
        return results
    
    def one_way_anova(self) -> Dict[str, Dict[str, float]]:
        """
        Perform one-way ANOVA for each numeric feature across diagnosis groups.
        
        Returns:
        --------
        Dict[str, Dict[str, float]]
            ANOVA results for each feature
        """
        results = {}
        
        benign_data = self.data[self.data['Diagnosis'] == 'Benign']
        malignant_data = self.data[self.data['Diagnosis'] == 'Malignant']
        
        for feature in self.numeric_features:
            benign_values = benign_data[feature].dropna()
            malignant_values = malignant_data[feature].dropna()
            
            # Perform one-way ANOVA
            f_stat, p_value = stats.f_oneway(benign_values, malignant_values)
            
            # Calculate eta-squared (effect size)
            ss_between = len(benign_values) * (benign_values.mean() - self.data[feature].mean())**2 + \
                        len(malignant_values) * (malignant_values.mean() - self.data[feature].mean())**2
            ss_total = ((self.data[feature] - self.data[feature].mean())**2).sum()
            eta_squared = ss_between / ss_total
            
            results[feature] = {
                'f_statistic': f_stat,
                'p_value': p_value,
                'eta_squared': eta_squared,
                'significant': p_value < 0.05
            }
        
        return results
    
    def chi_square_tests(self) -> Dict[str, Any]:
        """
        Perform chi-square tests for categorical associations.
        
        Returns:
        --------
        Dict[str, Any]
            Chi-square test results
        """
        results = {}
        
        # Create age groups for chi-square analysis
        age_bins = [0, 40, 55, 70, 100]
        age_labels = ['Young (≤40)', 'Middle-aged (41-55)', 'Older (56-70)', 'Elderly (>70)']
        self.data['Age_Group'] = pd.cut(self.data['Patient_Age'], bins=age_bins, labels=age_labels)
        
        # Chi-square test for Age Group vs Diagnosis
        contingency_table = pd.crosstab(self.data['Age_Group'], self.data['Diagnosis'])
        chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
        
        # Calculate Cramér's V (effect size)
        n = contingency_table.sum().sum()
        cramers_v = np.sqrt(chi2 / (n * (min(contingency_table.shape) - 1)))
        
        results['age_diagnosis'] = {
            'chi2_statistic': chi2,
            'p_value': p_value,
            'degrees_of_freedom': dof,
            'cramers_v': cramers_v,
            'significant': p_value < 0.05,
            'contingency_table': contingency_table,
            'expected_frequencies': expected
        }
        
        return results
    
    def correlation_analysis(self) -> pd.DataFrame:
        """
        Calculate correlation matrix for numeric features.
        
        Returns:
        --------
        pd.DataFrame
            Correlation matrix
        """
        return self.data[self.numeric_features].corr()
    
    def comprehensive_analysis(self) -> Dict[str, Any]:
        """
        Perform a comprehensive statistical analysis.
        
        Returns:
        --------
        Dict[str, Any]
            Complete analysis results
        """
        results = {
            'descriptive_stats': self.descriptive_statistics(),
            't_tests': self.independent_t_tests(),
            'anova': self.one_way_anova(),
            'chi_square': self.chi_square_tests(),
            'correlations': self.correlation_analysis(),
            'sample_sizes': {
                'total': len(self.data),
                'benign': len(self.data[self.data['Diagnosis'] == 'Benign']),
                'malignant': len(self.data[self.data['Diagnosis'] == 'Malignant'])
            }
        }
        
        return results
    
    def interpret_results(self, results: Dict[str, Any]) -> Dict[str, List[str]]:
        """
        Provide interpretation of statistical results.
        
        Parameters:
        -----------
        results : Dict[str, Any]
            Results from comprehensive_analysis
        
        Returns:
        --------
        Dict[str, List[str]]
            Interpretations of the results
        """
        interpretations = {
            'significant_differences': [],
            'effect_sizes': [],
            'recommendations': []
        }
        
        # Interpret t-test results
        for feature, result in results['t_tests'].items():
            if result['significant']:
                direction = "higher" if result['malignant_mean'] > result['benign_mean'] else "lower"
                interpretations['significant_differences'].append(
                    f"{feature}: Malignant tumors have significantly {direction} values "
                    f"(p = {result['p_value']:.4f})"
                )
                
                # Interpret effect size
                abs_d = abs(result['cohens_d'])
                if abs_d < 0.2:
                    size = "small"
                elif abs_d < 0.8:
                    size = "medium"
                else:
                    size = "large"
                
                interpretations['effect_sizes'].append(
                    f"{feature}: {size} effect size (Cohen's d = {result['cohens_d']:.3f})"
                )
        
        # Interpret chi-square results
        if results['chi_square']['age_diagnosis']['significant']:
            interpretations['significant_differences'].append(
                f"Age distribution differs significantly between diagnosis groups "
                f"(p = {results['chi_square']['age_diagnosis']['p_value']:.4f})"
            )
        
        # Add recommendations
        interpretations['recommendations'].extend([
            "Features with significant differences could be important for diagnosis",
            "Large effect sizes indicate clinically meaningful differences",
            "Consider these findings for feature selection in predictive modeling"
        ])
        
        return interpretations

def main():
    """Test the statistical analysis functions."""
    # This would typically load data from the CSV file
    print("Statistical Analysis Module loaded successfully!")
    print("Use StatisticalAnalyzer class to analyze your cancer diagnosis data.")

if __name__ == "__main__":
    main()