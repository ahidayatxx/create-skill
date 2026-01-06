# Example: Creating an Intermediate Skill

## User Request

Create an intermediate skill called "csv-analyzer" that reads CSV files and generates statistical summaries with Python scripts for data processing.

## Generated Skill Structure

```
csv-analyzer/
├── SKILL.md
├── scripts/
│   ├── __init__.py
│   ├── processor.py
│   └── helpers.py
├── reference/
│   └── config.yaml
└── README.md
```

## Generated SKILL.md (excerpt)

```yaml
---
name: CSV Analyzer
description: Analyze CSV files and generate statistical summaries with visualizations
version: 1.0.0
tags: [data-analysis, csv, statistics, visualization]
---
```

## Generated processor.py

```python
#!/usr/bin/env python3
"""CSV analysis processor."""

import argparse
import pandas as pd
from typing import Dict, Any

def analyze_csv(file_path: str) -> Dict[str, Any]:
    """Analyze CSV file and return statistics."""
    df = pd.read_csv(file_path)

    result = {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),
        "summary": df.describe().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict()
    }

    return result

def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Analyze CSV files")
    parser.add_argument('--file', required=True, help='CSV file to analyze')
    args = parser.parse_args()

    result = analyze_csv(args.file)
    print(result)

if __name__ == '__main__':
    main()
```

## How to Use

```
"Use csv-analyzer to analyze sales_data.csv"
"Get statistics from my CSV file using csv-analyzer"
```

## What Gets Created

1. **SKILL.md** with:
   - YAML frontmatter
   - Capabilities list
   - Usage instructions
   - Example prompts

2. **scripts/processor.py** with:
   - Shebang for execution
   - Type hints
   - Docstrings
   - CLI argument parsing
   - Error handling

3. **scripts/helpers.py** with:
   - Utility functions
   - Data validation
   - Formatters

4. **reference/config.yaml** with:
   - Default analysis settings
   - Output format options
   - Visualization preferences

5. **README.md** with:
   - Installation instructions
   - Dependency requirements (pandas, numpy)
   - Usage examples
   - Troubleshooting

## Customization Steps

1. Add your specific analysis logic to `processor.py`
2. Configure default settings in `config.yaml`
3. Add visualization helpers if needed
4. Update SKILL.md with your specific capabilities
5. Test with sample CSV files
6. Package for distribution

## Dependencies to Install

```bash
pip install pandas numpy matplotlib
```

## Result

A fully functional data analysis skill that can:
- Read CSV files
- Calculate statistics
- Generate summaries
- Create visualizations
- Handle edge cases
