#!/usr/bin/env python3
"""
Generate Sample Outputs for Blue Salt Analysis
===========================================
This script creates sample visualizations to demonstrate
what the analysis outputs would look like.
"""

import matplotlib.pyplot as plt
import numpy as np

def create_sample_visualizations():
    """Create sample output visualizations for the project."""
    
    # Set style
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # 1. JTBD Distribution Sample
    fig, ax = plt.subplots(figsize=(8, 6))
    jobs = ['Social\nBonding', 'Healthy\nMeal', 'Gratification']
    percentages = [43, 29, 29]
    colors = ['#667eea', '#764ba2', '#f093fb']
    
    bars = ax.bar(jobs, percentages, color=colors, alpha=0.8)
    
    # Add percentage labels
    for bar, pct in zip(bars, percentages):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{pct}%', ha='center', va='bottom', fontweight='bold', fontsize=12)
    
    ax.set_ylim(0, 50)
    ax.set_ylabel('Percentage of Customers (%)', fontsize=12)
    ax.set_xlabel('Primary Job to be Done', fontsize=12)
    ax.set_title('Jobs to be Done Distribution - Blue Salt', fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('outputs/visualizations/jtbd_distribution_sample.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    # 2. Customer Journey Satisfaction Sample
    fig, ax = plt.subplots(figsize=(10, 6))
    
    stages = ['Awareness', 'Consideration', 'Purchase', 'Usage', 'Loyalty']
    satisfaction = [75, 65, 70, 45, 60]
    
    # Create line plot with area fill
    x = np.arange(len(stages))
    ax.plot(x, satisfaction, 'o-', color='#667eea', linewidth=3, markersize=10)
    ax.fill_between(x, satisfaction, alpha=0.3, color='#667eea')
    
    # Add value labels
    for i, (stage, score) in enumerate(zip(stages, satisfaction)):
        ax.annotate(f'{score}%', xy=(i, score), xytext=(0, 10),
                   textcoords='offset points', ha='center', fontweight='bold')
    
    # Highlight pain point
    ax.annotate('Visual disappointment\nimpacts usage satisfaction',
                xy=(3, 45), xytext=(2.5, 25),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.7),
                fontsize=10, color='darkred')
    
    ax.set_ylim(0, 100)
    ax.set_xlim(-0.5, len(stages)-0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(stages)
    ax.set_ylabel('Customer Satisfaction Score (%)', fontsize=12)
    ax.set_xlabel('Customer Journey Stage', fontsize=12)
    ax.set_title('Customer Satisfaction Across Journey Stages', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('outputs/visualizations/journey_satisfaction_sample.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("✓ Sample visualizations created successfully!")
    print("  - outputs/visualizations/jtbd_distribution_sample.png")
    print("  - outputs/visualizations/journey_satisfaction_sample.png")


if __name__ == "__main__":
    # Create output directories
    import os
    os.makedirs('outputs/visualizations', exist_ok=True)
    
    # Generate samples
    create_sample_visualizations()
