#!/usr/bin/env python3
"""
Setup Script for Blue Salt Analysis Project
==========================================
This script creates the complete project structure for your GitHub repository.
Run this first to set up all directories and files.
"""

import os
import shutil

def create_project_structure():
    """Create the complete project directory structure."""
    
    # Define directory structure
    directories = [
        'data',
        'data/raw',
        'data/raw/transcripts',
        'data/processed',
        'outputs',
        'outputs/visualizations',
        'outputs/reports',
        'notebooks',
        'scripts',
        'config',
        'tests',
        'docs'
    ]
    
    # Create directories
    print("Creating project directory structure...")
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"  ✓ Created {directory}/")
    
    # Create placeholder files
    print("\nCreating placeholder files...")
    
    # Data directory READMEs
    with open('data/README.md', 'w') as f:
        f.write("# Data Directory\n\n")
        f.write("This directory contains all data files for the Blue Salt analysis.\n\n")
        f.write("## Structure\n")
        f.write("- `raw/` - Original interview data and transcripts\n")
        f.write("- `processed/` - Cleaned and processed data files\n\n")
        f.write("## Privacy Note\n")
        f.write("All participant data is anonymized. Raw transcripts are not tracked in git.\n")
    
    with open('data/raw/.gitkeep', 'w') as f:
        f.write("# This file ensures the directory is tracked by git\n")
    
    # Output directory README
    with open('outputs/README.md', 'w') as f:
        f.write("# Output Directory\n\n")
        f.write("This directory contains all analysis outputs.\n\n")
        f.write("## Structure\n")
        f.write("- `visualizations/` - Charts and graphs\n")
        f.write("- `reports/` - Analysis reports and summaries\n")
    
    # Notebooks README
    with open('notebooks/README.md', 'w') as f:
        f.write("# Notebooks Directory\n\n")
        f.write("This directory contains Jupyter notebooks for exploratory analysis.\n\n")
        f.write("## Notebooks\n")
        f.write("- `exploratory_analysis.ipynb` - Main analysis notebook\n")
        f.write("- `visualization_gallery.ipynb` - All visualizations\n")
    
    # Create sample config file
    with open('config/analysis_config.yaml', 'w') as f:
        f.write("# Blue Salt Analysis Configuration\n\n")
        f.write("project:\n")
        f.write("  name: Blue Salt Customer Analysis\n")
        f.write("  version: 1.0.0\n")
        f.write("  author: Your Name\n\n")
        f.write("data:\n")
        f.write("  sample_size: 7\n")
        f.write("  date_range:\n")
        f.write("    start: 2025-01-15\n")
        f.write("    end: 2025-01-20\n\n")
        f.write("analysis:\n")
        f.write("  confidence_level: 0.95\n")
        f.write("  min_segment_size: 3\n")
    
    # Create test file
    with open('tests/test_analysis.py', 'w') as f:
        f.write("import pytest\n")
        f.write("import pandas as pd\n")
        f.write("from blue_salt_customer_analysis import BlueSaltAnalysis\n\n")
        f.write("def test_data_loading():\n")
        f.write("    \"\"\"Test that data loads correctly.\"\"\"\n")
        f.write("    analyzer = BlueSaltAnalysis()\n")
        f.write("    data = analyzer.collect_interview_data()\n")
        f.write("    assert len(data) == 7\n")
        f.write("    assert 'participant_id' in data.columns\n")
    
    print("  ✓ Created README files")
    print("  ✓ Created configuration files")
    print("  ✓ Created test templates")
    
    # Create run script
    with open('run_analysis.sh', 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("# Run the complete Blue Salt analysis pipeline\n\n")
        f.write("echo 'Starting Blue Salt Customer Analysis...'\n")
        f.write("echo '======================================'\n\n")
        f.write("# Check Python version\n")
        f.write("python --version\n\n")
        f.write("# Install requirements if needed\n")
        f.write("if [ ! -d 'venv' ]; then\n")
        f.write("    echo 'Creating virtual environment...'\n")
        f.write("    python -m venv venv\n")
        f.write("    source venv/bin/activate\n")
        f.write("    pip install -r requirements.txt\n")
        f.write("fi\n\n")
        f.write("# Run main analysis\n")
        f.write("python blue_salt_customer_analysis.py\n\n")
        f.write("# Generate sample outputs\n")
        f.write("python generate_sample_outputs.py\n\n")
        f.write("echo 'Analysis complete! Check outputs/ directory for results.'\n")
    
    # Make run script executable
    os.chmod('run_analysis.sh', 0o755)
    
    print("  ✓ Created run script")
    
    print("\n" + "="*50)
    print("Project structure created successfully!")
    print("="*50)
    print("\nNext steps:")
    print("1. Copy all Python files to the project root")
    print("2. Run: pip install -r requirements.txt")
    print("3. Run: python blue_salt_customer_analysis.py")
    print("4. Commit to GitHub")

def main():
    """Main execution function."""
    print("Blue Salt Analysis Project Setup")
    print("================================\n")
    
    # Check if we're in the right directory
    if os.path.exists('blue_salt_customer_analysis.py'):
        response = input("Project files already exist. Continue anyway? (y/n): ")
        if response.lower() != 'y':
            print("Setup cancelled.")
            return
    
    # Create project structure
    create_project_structure()
    
    print("\n✅ Setup complete!")


if __name__ == "__main__":
    main()
