"""
Visualization Module for Cancer Diagnosis Statistical Analysis
Creates comprehensive plots for data exploration and results presentation.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import Dict, List, Any, Optional
import warnings
warnings.filterwarnings('ignore')

# Set style for matplotlib/seaborn
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class MedicalDataVisualizer:
    """
    A comprehensive visualization class for cancer diagnosis data analysis.
    """
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the visualizer with the dataset.
        
        Parameters:
        -----------
        data : pd.DataFrame
            The cancer diagnosis dataset
        """
        self.data = data
        self.numeric_features = ['Tumor_Size', 'Smoothness', 'Compactness', 'Patient_Age']
        self.colors = {'Benign': '#2E86AB', 'Malignant': '#F24236'}
    
    def create_histograms(self, figsize: tuple = (15, 10)) -> plt.Figure:
        """
        Create histograms for all numeric features with diagnosis overlay.
        
        Parameters:
        -----------
        figsize : tuple
            Figure size (width, height)
        
        Returns:
        --------
        plt.Figure
            Matplotlib figure object
        """
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        axes = axes.ravel()
        
        for i, feature in enumerate(self.numeric_features):
            # Create histogram for each diagnosis group
            benign_data = self.data[self.data['Diagnosis'] == 'Benign'][feature]
            malignant_data = self.data[self.data['Diagnosis'] == 'Malignant'][feature]
            
            axes[i].hist(benign_data, alpha=0.7, label='Benign', color=self.colors['Benign'], bins=20)
            axes[i].hist(malignant_data, alpha=0.7, label='Malignant', color=self.colors['Malignant'], bins=20)
            
            axes[i].set_xlabel(feature.replace('_', ' '))
            axes[i].set_ylabel('Frequency')
            axes[i].set_title(f'Distribution of {feature.replace("_", " ")}')
            axes[i].legend()
            axes[i].grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig
    
    def create_boxplots(self, figsize: tuple = (15, 10)) -> plt.Figure:
        """
        Create boxplots for all numeric features by diagnosis.
        
        Parameters:
        -----------
        figsize : tuple
            Figure size (width, height)
        
        Returns:
        --------
        plt.Figure
            Matplotlib figure object
        """
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        axes = axes.ravel()
        
        for i, feature in enumerate(self.numeric_features):
            sns.boxplot(data=self.data, x='Diagnosis', y=feature, ax=axes[i], 
                       palette=[self.colors['Benign'], self.colors['Malignant']])
            axes[i].set_title(f'{feature.replace("_", " ")} by Diagnosis')
            axes[i].set_xlabel('Diagnosis')
            axes[i].set_ylabel(feature.replace('_', ' '))
            axes[i].grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig
    
    def create_correlation_heatmap(self, figsize: tuple = (10, 8)) -> plt.Figure:
        """
        Create correlation heatmap for numeric features.
        
        Parameters:
        -----------
        figsize : tuple
            Figure size (width, height)
        
        Returns:
        --------
        plt.Figure
            Matplotlib figure object
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        # Calculate correlation matrix
        corr_matrix = self.data[self.numeric_features].corr()
        
        # Create heatmap
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                   square=True, ax=ax, cbar_kws={'label': 'Correlation Coefficient'})
        
        ax.set_title('Correlation Matrix of Tumor Characteristics', fontsize=14, fontweight='bold')
        plt.tight_layout()
        return fig
    
    def create_pairplot(self, figsize: tuple = (12, 10)) -> plt.Figure:
        """
        Create pairplot for numeric features colored by diagnosis.
        
        Parameters:
        -----------
        figsize : tuple
            Figure size (width, height)
        
        Returns:
        --------
        plt.Figure
            Matplotlib figure object
        """
        # Create pairplot
        g = sns.pairplot(data=self.data[self.numeric_features + ['Diagnosis']], 
                        hue='Diagnosis', palette=self.colors,
                        diag_kind='hist', plot_kws={'alpha': 0.6})
        
        g.fig.suptitle('Pairwise Relationships of Tumor Characteristics', 
                      fontsize=14, fontweight='bold', y=1.02)
        
        return g.fig
    
    def create_statistical_summary_plot(self, stats_results: Dict[str, Any], 
                                      figsize: tuple = (15, 10)) -> plt.Figure:
        """
        Create visualization of statistical test results.
        
        Parameters:
        -----------
        stats_results : Dict[str, Any]
            Results from statistical analysis
        figsize : tuple
            Figure size (width, height)
        
        Returns:
        --------
        plt.Figure
            Matplotlib figure object
        """
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        
        # Extract t-test results
        features = list(stats_results['t_tests'].keys())
        p_values = [stats_results['t_tests'][f]['p_value'] for f in features]
        effect_sizes = [abs(stats_results['t_tests'][f]['cohens_d']) for f in features]
        
        # Plot 1: P-values
        bars1 = axes[0, 0].bar(features, p_values, color=['red' if p < 0.05 else 'gray' for p in p_values])
        axes[0, 0].axhline(y=0.05, color='red', linestyle='--', alpha=0.7, label='α = 0.05')
        axes[0, 0].set_ylabel('P-value')
        axes[0, 0].set_title('Statistical Significance (T-tests)')
        axes[0, 0].tick_params(axis='x', rotation=45)
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        
        # Plot 2: Effect sizes
        bars2 = axes[0, 1].bar(features, effect_sizes, color=['darkgreen' if es > 0.8 else 'orange' if es > 0.2 else 'lightblue' for es in effect_sizes])
        axes[0, 1].axhline(y=0.2, color='orange', linestyle='--', alpha=0.7, label='Small effect')
        axes[0, 1].axhline(y=0.8, color='red', linestyle='--', alpha=0.7, label='Large effect')
        axes[0, 1].set_ylabel("Cohen's d (absolute)")
        axes[0, 1].set_title('Effect Sizes')
        axes[0, 1].tick_params(axis='x', rotation=45)
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        
        # Plot 3: Mean differences
        benign_means = [stats_results['t_tests'][f]['benign_mean'] for f in features]
        malignant_means = [stats_results['t_tests'][f]['malignant_mean'] for f in features]
        
        x = np.arange(len(features))
        width = 0.35
        
        axes[1, 0].bar(x - width/2, benign_means, width, label='Benign', color=self.colors['Benign'])
        axes[1, 0].bar(x + width/2, malignant_means, width, label='Malignant', color=self.colors['Malignant'])
        axes[1, 0].set_ylabel('Mean Value')
        axes[1, 0].set_title('Mean Values by Diagnosis')
        axes[1, 0].set_xticks(x)
        axes[1, 0].set_xticklabels(features, rotation=45)
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        
        # Plot 4: Sample sizes and diagnosis distribution
        sample_sizes = stats_results['sample_sizes']
        labels = ['Benign', 'Malignant']
        sizes = [sample_sizes['benign'], sample_sizes['malignant']]
        
        axes[1, 1].pie(sizes, labels=labels, autopct='%1.1f%%', 
                      colors=[self.colors['Benign'], self.colors['Malignant']])
        axes[1, 1].set_title('Diagnosis Distribution')
        
        plt.tight_layout()
        return fig
    
    def create_interactive_scatter_matrix(self) -> go.Figure:
        """
        Create interactive scatter plot matrix using Plotly.
        
        Returns:
        --------
        plotly.graph_objects.Figure
            Interactive Plotly figure
        """
        fig = px.scatter_matrix(
            self.data,
            dimensions=self.numeric_features,
            color='Diagnosis',
            color_discrete_map=self.colors,
            title='Interactive Scatter Plot Matrix of Tumor Characteristics'
        )
        
        fig.update_layout(
            height=600,
            font=dict(size=10)
        )
        
        return fig
    
    def create_age_distribution_plot(self, figsize: tuple = (12, 8)) -> plt.Figure:
        """
        Create age distribution analysis plot.
        
        Parameters:
        -----------
        figsize : tuple
            Figure size (width, height)
        
        Returns:
        --------
        plt.Figure
            Matplotlib figure object
        """
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        
        # Age distribution by diagnosis
        axes[0, 0].hist(self.data[self.data['Diagnosis'] == 'Benign']['Patient_Age'], 
                       alpha=0.7, label='Benign', color=self.colors['Benign'], bins=15)
        axes[0, 0].hist(self.data[self.data['Diagnosis'] == 'Malignant']['Patient_Age'], 
                       alpha=0.7, label='Malignant', color=self.colors['Malignant'], bins=15)
        axes[0, 0].set_xlabel('Age')
        axes[0, 0].set_ylabel('Frequency')
        axes[0, 0].set_title('Age Distribution by Diagnosis')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        
        # Age boxplot
        sns.boxplot(data=self.data, x='Diagnosis', y='Patient_Age', ax=axes[0, 1],
                   palette=[self.colors['Benign'], self.colors['Malignant']])
        axes[0, 1].set_title('Age Distribution by Diagnosis (Boxplot)')
        axes[0, 1].grid(True, alpha=0.3)
        
        # Age groups
        age_bins = [0, 40, 55, 70, 100]
        age_labels = ['≤40', '41-55', '56-70', '>70']
        self.data['Age_Group'] = pd.cut(self.data['Patient_Age'], bins=age_bins, labels=age_labels)
        
        age_diagnosis_ct = pd.crosstab(self.data['Age_Group'], self.data['Diagnosis'])
        age_diagnosis_ct.plot(kind='bar', ax=axes[1, 0], color=[self.colors['Benign'], self.colors['Malignant']])
        axes[1, 0].set_xlabel('Age Group')
        axes[1, 0].set_ylabel('Count')
        axes[1, 0].set_title('Diagnosis Count by Age Group')
        axes[1, 0].tick_params(axis='x', rotation=45)
        axes[1, 0].grid(True, alpha=0.3)
        
        # Proportion plot
        age_diagnosis_prop = age_diagnosis_ct.div(age_diagnosis_ct.sum(axis=1), axis=0)
        age_diagnosis_prop.plot(kind='bar', stacked=True, ax=axes[1, 1], 
                               color=[self.colors['Benign'], self.colors['Malignant']])
        axes[1, 1].set_xlabel('Age Group')
        axes[1, 1].set_ylabel('Proportion')
        axes[1, 1].set_title('Diagnosis Proportion by Age Group')
        axes[1, 1].tick_params(axis='x', rotation=45)
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig
    
    def create_comprehensive_dashboard(self, stats_results: Dict[str, Any]) -> Dict[str, plt.Figure]:
        """
        Create a comprehensive set of visualizations for the analysis.
        
        Parameters:
        -----------
        stats_results : Dict[str, Any]
            Results from statistical analysis
        
        Returns:
        --------
        Dict[str, plt.Figure]
            Dictionary of all created figures
        """
        figures = {}
        
        print("Creating visualizations...")
        
        figures['histograms'] = self.create_histograms()
        figures['boxplots'] = self.create_boxplots()
        figures['correlation_heatmap'] = self.create_correlation_heatmap()
        figures['pairplot'] = self.create_pairplot()
        figures['statistical_summary'] = self.create_statistical_summary_plot(stats_results)
        figures['age_analysis'] = self.create_age_distribution_plot()
        
        print(f"Created {len(figures)} visualization figures")
        return figures

def main():
    """Test the visualization functions."""
    print("Visualization Module loaded successfully!")
    print("Use MedicalDataVisualizer class to create comprehensive plots for your cancer diagnosis data.")

if __name__ == "__main__":
    main()