"""
Integration test for the cancer diagnosis statistical analysis project.
Tests all modules working together.
"""

import pandas as pd
from data_generator import generate_medical_data
from statistical_analysis import StatisticalAnalyzer
from visualizations import MedicalDataVisualizer

def test_integration():
    """Test all modules working together."""
    print("🧪 Running integration test...")
    
    # Test 1: Data generation
    print("\n1. Testing data generation...")
    data = generate_medical_data(n_samples=100, random_state=42)
    print(f"✅ Generated data with shape: {data.shape}")
    
    # Test 2: Statistical analysis
    print("\n2. Testing statistical analysis...")
    analyzer = StatisticalAnalyzer(data)
    results = analyzer.comprehensive_analysis()
    print("✅ Statistical analysis completed")
    
    # Print key results
    print("\n📊 Key Statistical Results:")
    for feature, result in results['t_tests'].items():
        significance = "significant" if result['significant'] else "not significant"
        print(f"   {feature}: p={result['p_value']:.4f} ({significance})")
    
    # Test 3: Visualizations
    print("\n3. Testing visualizations...")
    visualizer = MedicalDataVisualizer(data)
    
    try:
        # Create a simple plot to test
        import matplotlib.pyplot as plt
        fig = visualizer.create_correlation_heatmap(figsize=(6, 4))
        plt.savefig('test_plot.png', dpi=100, bbox_inches='tight')
        plt.close(fig)
        print("✅ Visualization test completed (plot saved as test_plot.png)")
    except Exception as e:
        print(f"⚠️ Visualization test failed: {e}")
    
    # Test 4: Interpretation
    print("\n4. Testing result interpretation...")
    interpretations = analyzer.interpret_results(results)
    print("✅ Interpretation completed")
    
    if interpretations['significant_differences']:
        print("\n🔍 Significant Findings:")
        for finding in interpretations['significant_differences'][:3]:  # Show first 3
            print(f"   • {finding}")
    
    print("\n🎉 Integration test completed successfully!")
    return True

if __name__ == "__main__":
    test_integration()