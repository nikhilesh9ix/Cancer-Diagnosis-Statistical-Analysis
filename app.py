"""
Streamlit Frontend for Cancer Diagnosis Statistical Analysis
Interactive web application for data upload, visualization, and statistical testing.
"""

import streamlit as st
import pandas as pd
import numpy as np
import io
import base64
from pathlib import Path

# Import our custom modules
from data_generator import generate_medical_data, save_dataset
from statistical_analysis import StatisticalAnalyzer
from visualizations import MedicalDataVisualizer

# Page configuration
st.set_page_config(
    page_title="Cancer Diagnosis Statistical Analysis",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        color: #F24236;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 0.25rem;
        padding: 0.75rem;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #e3f2fd;
        border: 2px solid #2196f3;
        border-radius: 0.5rem;
        padding: 1.5rem;
        margin: 2rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .warning-box h3 {
        color: #1976d2;
        margin-top: 0;
        font-weight: bold;
    }
    .warning-box p {
        color: #333;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    .warning-box ol {
        color: #444;
        font-size: 1.05rem;
        line-height: 1.7;
    }
    .warning-box li {
        margin-bottom: 0.5rem;
    }
    .warning-box strong {
        color: #1976d2;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def load_data():
    """Load or generate data for analysis."""
    if 'data' not in st.session_state:
        st.session_state.data = None
    return st.session_state.data

def save_data(data):
    """Save data to session state."""
    st.session_state.data = data

def create_download_link(df, filename="cancer_data.csv"):
    """Create a download link for the dataframe."""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download CSV file</a>'
    return href

def display_statistical_results(results):
    """Display statistical analysis results in a formatted way."""
    st.markdown('<div class="section-header">📊 Statistical Analysis Results</div>', unsafe_allow_html=True)
    
    # Create tabs for different analyses
    tab1, tab2, tab3, tab4 = st.tabs(["Descriptive Stats", "T-Tests", "ANOVA", "Chi-Square"])
    
    with tab1:
        st.subheader("Descriptive Statistics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Benign Group Statistics**")
            st.dataframe(results['descriptive_stats']['benign'].round(4))
        
        with col2:
            st.write("**Malignant Group Statistics**")
            st.dataframe(results['descriptive_stats']['malignant'].round(4))
        
        st.write("**Overall Statistics**")
        st.dataframe(results['descriptive_stats']['overall'].round(4))
    
    with tab2:
        st.subheader("Independent T-Tests Results")
        
        t_test_df = pd.DataFrame(results['t_tests']).T
        t_test_df = t_test_df.round(4)
        
        # Highlight significant results
        def highlight_significant(row):
            return ['background-color: #ffcccc' if row['significant'] else '' for _ in row]
        
        styled_df = t_test_df.style.apply(highlight_significant, axis=1)
        st.dataframe(styled_df)
        
        st.markdown("**Interpretation:**")
        for feature, result in results['t_tests'].items():
            if result['significant']:
                direction = "higher" if result['malignant_mean'] > result['benign_mean'] else "lower"
                st.write(f"- **{feature}**: Malignant tumors have significantly {direction} values (p = {result['p_value']:.4f})")
    
    with tab3:
        st.subheader("One-Way ANOVA Results")
        
        anova_df = pd.DataFrame(results['anova']).T
        anova_df = anova_df.round(4)
        
        styled_anova = anova_df.style.apply(lambda row: ['background-color: #ffcccc' if row['significant'] else '' for _ in row], axis=1)
        st.dataframe(styled_anova)
    
    with tab4:
        st.subheader("Chi-Square Test Results")
        
        chi_result = results['chi_square']['age_diagnosis']
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Chi-Square Statistic", f"{chi_result['chi2_statistic']:.4f}")
            st.metric("P-Value", f"{chi_result['p_value']:.4f}")
            st.metric("Degrees of Freedom", chi_result['degrees_of_freedom'])
            
        with col2:
            st.metric("Cramér's V", f"{chi_result['cramers_v']:.4f}")
            significant = "Yes" if chi_result['significant'] else "No"
            st.metric("Significant (α=0.05)", significant)
        
        st.write("**Contingency Table: Age Group vs Diagnosis**")
        st.dataframe(chi_result['contingency_table'])

def main():
    """Main Streamlit application."""
    
    # Header
    st.markdown('<div class="main-header">🏥 Cancer Diagnosis Statistical Analysis</div>', unsafe_allow_html=True)
    st.markdown("**An interactive platform for hypothesis testing in medical data**")
    
    # Sidebar for navigation and data management
    with st.sidebar:
        st.header("📋 Data Management")
        
        data_option = st.radio(
            "Choose data source:",
            ["Generate Synthetic Data", "Upload CSV File"]
        )
        
        data = load_data()
        
        if data_option == "Generate Synthetic Data":
            st.subheader("Generate New Dataset")
            
            n_samples = st.slider("Number of samples", 100, 2000, 1000, 50)
            random_seed = st.number_input("Random seed", 1, 1000, 42)
            
            if st.button("Generate Data", type="primary"):
                with st.spinner("Generating synthetic medical data..."):
                    data = generate_medical_data(n_samples=n_samples, random_state=random_seed)
                    save_data(data)
                    st.success(f"Generated {len(data)} samples successfully!")
        
        elif data_option == "Upload CSV File":
            st.subheader("Upload Your Data")
            
            uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
            
            if uploaded_file is not None:
                try:
                    data = pd.read_csv(uploaded_file)
                    save_data(data)
                    st.success("File uploaded successfully!")
                except Exception as e:
                    st.error(f"Error reading file: {str(e)}")
        
        # Data download section
        if data is not None:
            st.subheader("📥 Download Data")
            st.markdown(create_download_link(data), unsafe_allow_html=True)
    
    # Main content area
    if data is not None:
        # Data overview
        st.markdown('<div class="section-header">📋 Dataset Overview</div>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Samples", len(data))
        with col2:
            benign_count = len(data[data['Diagnosis'] == 'Benign'])
            st.metric("Benign Cases", benign_count)
        with col3:
            malignant_count = len(data[data['Diagnosis'] == 'Malignant'])
            st.metric("Malignant Cases", malignant_count)
        with col4:
            malignant_rate = (malignant_count / len(data)) * 100
            st.metric("Malignant Rate", f"{malignant_rate:.1f}%")
        
        # Data preview
        with st.expander("View Raw Data", expanded=False):
            st.dataframe(data)
        
        # Statistical Analysis
        if st.button("Run Statistical Analysis", type="primary"):
            with st.spinner("Performing statistical analysis..."):
                analyzer = StatisticalAnalyzer(data)
                results = analyzer.comprehensive_analysis()
                st.session_state.results = results
            st.success("Statistical analysis completed!")
        
        # Display results if available
        if 'results' in st.session_state:
            display_statistical_results(st.session_state.results)
            
            # Visualizations
            st.markdown('<div class="section-header">📈 Data Visualizations</div>', unsafe_allow_html=True)
            
            viz_option = st.selectbox(
                "Choose visualization:",
                ["Histograms", "Boxplots", "Correlation Heatmap", "Statistical Summary", "Age Analysis"]
            )
            
            if st.button("Generate Visualization"):
                with st.spinner("Creating visualization..."):
                    visualizer = MedicalDataVisualizer(data)
                    
                    if viz_option == "Histograms":
                        fig = visualizer.create_histograms()
                        st.pyplot(fig)
                    elif viz_option == "Boxplots":
                        fig = visualizer.create_boxplots()
                        st.pyplot(fig)
                    elif viz_option == "Correlation Heatmap":
                        fig = visualizer.create_correlation_heatmap()
                        st.pyplot(fig)
                    elif viz_option == "Statistical Summary":
                        fig = visualizer.create_statistical_summary_plot(st.session_state.results)
                        st.pyplot(fig)
                    elif viz_option == "Age Analysis":
                        fig = visualizer.create_age_distribution_plot()
                        st.pyplot(fig)
            
            # Interactive plots
            st.subheader("Interactive Visualizations")
            
            if st.button("Create Interactive Scatter Matrix"):
                with st.spinner("Creating interactive plot..."):
                    visualizer = MedicalDataVisualizer(data)
                    fig = visualizer.create_interactive_scatter_matrix()
                    st.plotly_chart(fig, use_container_width=True)
            
            # Results interpretation
            st.markdown('<div class="section-header">🔍 Results Interpretation</div>', unsafe_allow_html=True)
            
            if st.button("Generate Interpretation"):
                analyzer = StatisticalAnalyzer(data)
                interpretations = analyzer.interpret_results(st.session_state.results)
                
                st.subheader("Key Findings")
                
                if interpretations['significant_differences']:
                    st.write("**Significant Differences Found:**")
                    for finding in interpretations['significant_differences']:
                        st.write(f"• {finding}")
                
                if interpretations['effect_sizes']:
                    st.write("**Effect Sizes:**")
                    for effect in interpretations['effect_sizes']:
                        st.write(f"• {effect}")
                
                if interpretations['recommendations']:
                    st.write("**Recommendations:**")
                    for rec in interpretations['recommendations']:
                        st.write(f"• {rec}")
    
    else:
        # Welcome message when no data is loaded
        st.markdown("""
        <div class="warning-box">
            <h3>🏥 Welcome to Cancer Diagnosis Statistical Analysis!</h3>
            <p><strong>An interactive platform for medical data hypothesis testing and visualization.</strong></p>
            <p>To get started, follow these steps:</p>
            <ol>
                <li><strong>Load Your Data:</strong> Use the sidebar to either generate synthetic data or upload your CSV file</li>
                <li><strong>Explore Data:</strong> Review the dataset overview and examine the raw data</li>
                <li><strong>Run Analysis:</strong> Perform statistical hypothesis tests (t-tests, ANOVA, chi-square)</li>
                <li><strong>Visualize Results:</strong> Create interactive plots and statistical summaries</li>
                <li><strong>Interpret Findings:</strong> Review the clinical significance of your results</li>
            </ol>
            <p><strong>📋 Expected CSV format:</strong> Patient_ID, Tumor_Size, Smoothness, Compactness, Patient_Age, Diagnosis</p>
            <p><em>💡 Tip: Start with "Generate Synthetic Data" to see the application in action!</em></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Sample data format
        st.markdown("---")
        st.markdown('<div class="section-header">📊 Expected Data Format</div>', unsafe_allow_html=True)
        st.info("Your CSV file should contain the following columns with this exact structure:")
        sample_data = pd.DataFrame({
            'Patient_ID': ['P0001', 'P0002', 'P0003'],
            'Tumor_Size': [12.5, 8.3, 18.7],
            'Smoothness': [0.095, 0.112, 0.074],
            'Compactness': [0.089, 0.065, 0.135],
            'Patient_Age': [45, 62, 38],
            'Diagnosis': ['Benign', 'Benign', 'Malignant']
        })
        st.dataframe(sample_data, use_container_width=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>Cancer Diagnosis Statistical Analysis Tool | Built with Streamlit</p>
        <p>Features: Hypothesis Testing • Data Visualization • Interactive Analysis</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()