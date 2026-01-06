#!/usr/bin/env python3
"""
Template Builder - Create skill templates from predefined templates.

This module provides pre-built skill templates that can be customized
for specific use cases.
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Dict, List


# Predefined skill templates
SKILL_TEMPLATES = {
    'simple': {
        'description': 'Single-purpose skill with SKILL.md only',
        'structure': ['SKILL.md', 'README.md'],
        'example_use_cases': [
            'Brand guidelines application',
            'Text templates',
            'Style guides',
            'Checklists'
        ]
    },
    'intermediate': {
        'description': 'Skill with scripts and configuration',
        'structure': [
            'SKILL.md',
            'scripts/',
            'scripts/__init__.py',
            'scripts/processor.py',
            'reference/',
            'reference/config.yaml',
            'README.md'
        ],
        'example_use_cases': [
            'Data processing',
            'File conversion',
            'API integration',
            'Calculations'
        ]
    },
    'complex': {
        'description': 'Multi-component skill with full structure',
        'structure': [
            'SKILL.md',
            'scripts/',
            'scripts/__init__.py',
            'scripts/processor.py',
            'scripts/helpers.py',
            'reference/',
            'reference/config.yaml',
            'reference/documentation.md',
            'examples/',
            'examples/example_input.md',
            'examples/example_output.md',
            'resources/',
            '.claude/docs/',
            '.claude/docs/architecture.md',
            'README.md'
        ],
        'example_use_cases': [
            'MCP server builders',
            'Multi-step workflows',
            'External service integration',
            'Complex data pipelines'
        ]
    }
}


class TemplateBuilder:
    """Build skills from predefined templates."""

    def __init__(self, template_type: str, skill_name: str):
        """
        Initialize the template builder.

        Args:
            template_type: Type of template (simple, intermediate, complex)
            skill_name: Name for the new skill
        """
        self.template_type = template_type
        self.skill_name = skill_name
        self.base_path = Path.cwd() / self._to_kebab_case(skill_name)

    def _to_kebab_case(self, text: str) -> str:
        """Convert text to kebab-case."""
        import re
        text = text.lower().replace(' ', '-').replace('_', '-')
        text = re.sub(r'[^a-z0-9-]', '', text)
        text = re.sub(r'-+', '-', text)
        return text.strip('-')

    def build(self) -> Path:
        """
        Build skill from template.

        Returns:
            Path to created skill
        """
        template = SKILL_TEMPLATES[self.template_type]

        print(f"Building {self.template_type} skill: {self.skill_name}")
        print(f"Description: {template['description']}")

        # Create directory structure
        self._create_structure(template['structure'])

        # Generate files
        self._generate_files()

        print(f"\n✓ Template built successfully at: {self.base_path}")
        return self.base_path

    def _create_structure(self, structure: List[str]):
        """Create directory structure from template."""
        for item in structure:
            path = self.base_path / item

            if item.endswith('/'):
                # It's a directory
                path.mkdir(parents=True, exist_ok=True)
                print(f"✓ Created directory: {path}")
            else:
                # It's a file
                path.parent.mkdir(parents=True, exist_ok=True)

    def _generate_files(self):
        """Generate skill files from templates."""
        # Generate SKILL.md
        self._generate_skill_md()

        # Generate README.md
        self._generate_readme()

        # Generate scripts if intermediate or complex
        if self.template_type in ['intermediate', 'complex']:
            self._generate_processor_script()

        # Generate additional files for complex
        if self.template_type == 'complex':
            self._generate_helper_script()
            self._generate_config()
            self._generate_examples()
            self._generate_architecture_docs()

    def _generate_skill_md(self):
        """Generate SKILL.md from template."""
        skill_md = f"""---
name: {self.skill_name}
description: A {self.template_type} Claude Skill for specific tasks
version: 1.0.0
tags: [automation, productivity]
---

# {self.skill_name}

A {self.template_type} Claude Skill that helps accomplish specific tasks efficiently.

## Capabilities

- Task automation
- Data processing
- Result generation

## How to Use

1. **Describe your task**: Tell Claude what you need
2. **Provide context**: Share relevant information
3. **Review results**: Check the generated output
4. **Iterate**: Refine as needed

## Example Usage

"Use {self.skill_name} to help me with my task"

## Best Practices

1. Be specific about your requirements
2. Provide clear context
3. Review generated results
4. Iterate for improvements

## Limitations

- Requires clear input descriptions
- May need iteration for complex tasks
"""

        skill_md_path = self.base_path / 'SKILL.md'
        with open(skill_md_path, 'w') as f:
            f.write(skill_md)
        print(f"✓ Created {skill_md_path}")

    def _generate_readme(self):
        """Generate README.md."""
        readme = f"""# {self.skill_name}

A {self.template_type} Claude Skill.

## Installation

### Claude Desktop
```bash
zip -r {self.skill_name}.zip {self.skill_name}/
# Upload via Settings → Capabilities → Skills
```

### Claude Code
```bash
cp -r {self.skill_name}/ ~/.claude/skills/
```

## Usage

Invoke by name: "Use {self.skill_name} to..."

## Development

- Template: {self.template_type}
- Created: with create-skill
- Version: 1.0.0

## License

MIT
"""

        readme_path = self.base_path / 'README.md'
        with open(readme_path, 'w') as f:
            f.write(readme)
        print(f"✓ Created {readme_path}")

    def _generate_processor_script(self):
        """Generate processor script."""
        processor = '''#!/usr/bin/env python3
"""
Processor script for skill.
"""

import argparse
import json
from typing import Any, Dict


def process(input_data: str) -> Dict[str, Any]:
    """
    Process input data.

    Args:
        input_data: Input to process

    Returns:
        Processed result
    """
    # Add your processing logic here
    return {
        "status": "success",
        "result": input_data
    }


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Skill processor")
    parser.add_argument('--input', required=True, help='Input data')
    args = parser.parse_args()

    result = process(args.input)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
'''

        processor_path = self.base_path / 'scripts' / 'processor.py'
        with open(processor_path, 'w') as f:
            f.write(processor)
        processor_path.chmod(0o755)

        # Create __init__.py
        init_path = self.base_path / 'scripts' / '__init__.py'
        init_path.touch()

        print(f"✓ Created {processor_path}")

    def _generate_helper_script(self):
        """Generate helper script for complex skills."""
        helper = '''#!/usr/bin/env python3
"""
Helper utilities for skill.
"""

from typing import Any, List


def format_output(data: Any) -> str:
    """Format output data."""
    return str(data)


def validate_input(input_data: str) -> bool:
    """Validate input data."""
    return bool(input_data)
'''

        helper_path = self.base_path / 'scripts' / 'helpers.py'
        with open(helper_path, 'w') as f:
            f.write(helper)
        print(f"✓ Created {helper_path}")

    def _generate_config(self):
        """Generate configuration file."""
        config = f"""# {self.skill_name} Configuration

settings:
  debug: false
  verbose: true

parameters:
  timeout: 30
  retries: 3

output:
  format: json
  indent: 2
"""

        config_path = self.base_path / 'reference' / 'config.yaml'
        with open(config_path, 'w') as f:
            f.write(config)
        print(f"✓ Created {config_path}")

    def _generate_examples(self):
        """Generate example files."""
        # Example input
        example_input = f"""# Example Input for {self.skill_name}

## Input:

Your example input here.

## Expected Output:

Describe expected output.
"""

        input_path = self.base_path / 'examples' / 'example_input.md'
        with open(input_path, 'w') as f:
            f.write(example_input)

        # Example output
        example_output = f"""# Example Output for {self.skill_name}

## Input:

(From example_input.md)

## Output:

```json
{{
  "status": "success",
  "result": "processed data"
}}
```
"""

        output_path = self.base_path / 'examples' / 'example_output.md'
        with open(output_path, 'w') as f:
            f.write(example_output)

        print(f"✓ Created examples")

    def _generate_architecture_docs(self):
        """Generate architecture documentation."""
        arch = f"""# {self.skill_name} Architecture

## Overview

{self.skill_name} is a {self.template_type} skill with the following components.

## Components

### Scripts
- `processor.py`: Main processing logic
- `helpers.py`: Utility functions

### Reference
- `config.yaml`: Configuration settings

## Data Flow

1. Input received
2. Validation performed
3. Processing executed
4. Output generated

## Extension Points

- Add new processing functions in `processor.py`
- Add utilities in `helpers.py`
- Update configuration in `config.yaml`
"""

        arch_path = self.base_path / '.claude' / 'docs' / 'architecture.md'
        arch_path.parent.mkdir(parents=True, exist_ok=True)
        with open(arch_path, 'w') as f:
            f.write(arch)
        print(f"✓ Created {arch_path}")


def list_templates():
    """List available templates."""
    print("Available Skill Templates:\n")
    for name, template in SKILL_TEMPLATES.items():
        print(f"{name.upper()}")
        print(f"  Description: {template['description']}")
        print(f"  Use cases: {', '.join(template['example_use_cases'][:3])}")
        print()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Build skills from predefined templates'
    )
    parser.add_argument(
        '--template',
        choices=['simple', 'intermediate', 'complex'],
        default='simple',
        help='Template type to use'
    )
    parser.add_argument(
        '--name',
        required=True,
        help='Name for the new skill'
    )
    parser.add_argument(
        '--list',
        action='store_true',
        help='List available templates'
    )

    args = parser.parse_args()

    if args.list:
        list_templates()
        return

    # Build skill from template
    builder = TemplateBuilder(args.template, args.name)
    builder.build()


if __name__ == '__main__':
    main()
