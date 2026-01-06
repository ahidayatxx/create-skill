#!/usr/bin/env python3
"""
Skill Generator - Generate Claude Skills from specifications.

This module creates complete Claude Skills with proper structure,
metadata, and packaging for deployment.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class SkillGenerator:
    """Generate Claude Skills from specifications."""

    def __init__(self, spec: Dict):
        """
        Initialize the skill generator.

        Args:
            spec: Skill specification dictionary
        """
        self.spec = spec
        self.skill_name = self._to_kebab_case(spec.get('name', 'new-skill'))
        self.base_path = Path.cwd() / self.skill_name

    def _to_kebab_case(self, text: str) -> str:
        """
        Convert text to kebab-case.

        Args:
            text: Text to convert

        Returns:
            Kebab-case string
        """
        # Convert to lowercase, replace spaces and underscores with hyphens
        # Remove special characters
        import re
        text = text.lower().replace(' ', '-').replace('_', '-')
        text = re.sub(r'[^a-z0-9-]', '', text)
        # Remove consecutive hyphens
        text = re.sub(r'-+', '-', text)
        return text.strip('-')

    def generate(self) -> Path:
        """
        Generate the complete skill structure.

        Returns:
            Path to generated skill directory
        """
        complexity = self.spec.get('complexity', 'simple')
        has_scripts = self.spec.get('has_scripts', False)

        # Create base directory
        self.base_path.mkdir(parents=True, exist_ok=True)

        # Generate SKILL.md
        self._generate_skill_md()

        # Generate based on complexity
        if complexity in ['intermediate', 'complex']:
            self._create_subdirectories()

        if has_scripts or complexity in ['intermediate', 'complex']:
            self._generate_scripts()

        if complexity == 'complex':
            self._generate_reference()
            self._generate_examples()

        # Generate README
        self._generate_readme()

        return self.base_path

    def _generate_skill_md(self):
        """Generate the SKILL.md file."""
        name = self.spec.get('name', 'New Skill')
        description = self.spec.get('description', 'A new Claude Skill')
        version = self.spec.get('version', '1.0.0')
        tags = self.spec.get('tags', [])

        # Build YAML frontmatter
        frontmatter = f"""---
name: {name}
description: {description}
version: {version}
"""

        if tags:
            frontmatter += f"tags: {json.dumps(tags)}\n"

        frontmatter += "---\n"

        # Build skill body
        body = f"""
# {name}

{self.spec.get('overview', f'{name} helps you accomplish specific tasks with Claude.')}

## Capabilities

"""
        capabilities = self.spec.get('capabilities', [])
        if capabilities:
            for cap in capabilities:
                body += f"- {cap}\n"
        else:
            body += f"- {description}\n"

        body += """
## How to Use

1. **Invoke the skill**: Describe what you need help with
2. **Provide context**: Share relevant details about your task
3. **Review output**: Check the generated results
4. **Iterate**: Refine based on your needs

## Example Usage

"""
        examples = self.spec.get('examples', [])
        if examples:
            for example in examples:
                body += f'"{example}"\n\n'
        else:
            body += f'"{description}"\n\n'

        # Write SKILL.md
        skill_md_path = self.base_path / 'SKILL.md'
        with open(skill_md_path, 'w') as f:
            f.write(frontmatter + body)

        print(f"✓ Created {skill_md_path}")

    def _create_subdirectories(self):
        """Create subdirectories based on complexity."""
        subdirs = ['scripts', 'reference']
        for subdir in subdirs:
            dir_path = self.base_path / subdir
            dir_path.mkdir(exist_ok=True)
            # Create __init__.py if scripts directory
            if subdir == 'scripts':
                init_file = dir_path / '__init__.py'
                init_file.touch(exist_ok=True)
            print(f"✓ Created {dir_path}/")

    def _generate_scripts(self):
        """Generate Python script templates."""
        # Example processor script
        processor_template = '''#!/usr/bin/env python3
"""
{skill_name} - Skill processor script.

This script handles core processing logic for the skill.
"""

import argparse
import json
import sys
from typing import Any, Dict


def process_input(input_data: str) -> Dict[str, Any]:
    """
    Process input data according to skill requirements.

    Args:
        input_data: Input string or data

    Returns:
        Processed result as dictionary
    """
    # Implement your processing logic here
    result = {{
        "status": "success",
        "data": input_data,
        "processed": True
    }}
    return result


def main():
    """Main entry point for CLI usage."""
    parser = argparse.ArgumentParser(
        description="{skill_name} processor"
    )
    parser.add_argument(
        '--input',
        required=True,
        help='Input data to process'
    )
    parser.add_argument(
        '--output',
        help='Output file path (optional)'
    )

    args = parser.parse_args()

    # Process input
    result = process_input(args.input)

    # Output result
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"Results written to {{args.output}}")
    else:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
'''

        processor_path = self.base_path / 'scripts' / 'processor.py'
        with open(processor_path, 'w') as f:
            f.write(processor_template.format(skill_name=self.skill_name))

        # Make executable
        processor_path.chmod(0o755)
        print(f"✓ Created {processor_path}")

    def _generate_reference(self):
        """Generate reference documentation."""
        # Configuration template
        config_template = f"""# {self.skill_name} Configuration

# Skill settings
settings:
  debug: false
  verbose: true

# Processing parameters
parameters:
  timeout: 30
  max_retries: 3

# Output format
output:
  format: json
  indent: 2
"""

        config_path = self.base_path / 'reference' / 'config.yaml'
        with open(config_path, 'w') as f:
            f.write(config_template)
        print(f"✓ Created {config_path}")

    def _generate_examples(self):
        """Generate example inputs and outputs."""
        examples_dir = self.base_path / 'examples'
        examples_dir.mkdir(exist_ok=True)

        # Example input
        example_input = f"""# Example Input for {self.skill_name}

This is an example of how to use the {self.skill_name} skill.

## Input Example:

Provide your input data or description here.

## Expected Output:

The skill will process and return results in the specified format.
"""

        input_path = examples_dir / 'example_input.md'
        with open(input_path, 'w') as f:
            f.write(example_input)
        print(f"✓ Created {input_path}")

    def _generate_readme(self):
        """Generate README.md for the skill."""
        readme_content = f"""# {self.skill_name}

A Claude Skill for {self.spec.get('description', 'accomplishing specific tasks')}.

## Installation

### Claude Desktop
1. Package the skill: `zip -r {self.skill_name}.zip {self.skill_name}/`
2. Upload via Settings → Capabilities → Skills

### Claude Code
1. Copy to: `~/.claude/skills/{self.skill_name}/`
2. Restart Claude Code

### Claude API
1. Upload via `/v1/skills` endpoint

## Usage

Invoke the skill by describing what you need:

```
{self.spec.get('description', 'Help me with a task')}
```

## Development

Generated on: {datetime.now().strftime('%Y-%m-%d')}
Version: {self.spec.get('version', '1.0.0')}

## License

MIT License - See LICENSE file for details
"""

        readme_path = self.base_path / 'README.md'
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        print(f"✓ Created {readme_path}")


def load_spec(spec_path: str) -> Dict:
    """
    Load skill specification from JSON file.

    Args:
        spec_path: Path to specification file

    Returns:
        Specification dictionary
    """
    with open(spec_path, 'r') as f:
        return json.load(f)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate Claude Skills from specifications'
    )
    parser.add_argument(
        '--spec',
        help='Path to skill specification JSON file'
    )
    parser.add_argument(
        '--name',
        help='Skill name'
    )
    parser.add_argument(
        '--description',
        help='Skill description'
    )
    parser.add_argument(
        '--complexity',
        choices=['simple', 'intermediate', 'complex'],
        default='simple',
        help='Skill complexity level'
    )
    parser.add_argument(
        '--scripts',
        action='store_true',
        help='Include script templates'
    )

    args = parser.parse_args()

    # Build specification
    spec = {}

    if args.spec:
        spec = load_spec(args.spec)
    else:
        if not args.name:
            print("Error: --name is required when not using --spec")
            sys.exit(1)

        spec = {
            'name': args.name,
            'description': args.description or f'A skill for {args.name}',
            'complexity': args.complexity,
            'has_scripts': args.scripts,
            'version': '1.0.0',
            'tags': []
        }

    # Generate skill
    generator = SkillGenerator(spec)
    skill_path = generator.generate()

    print(f"\n✓ Skill generated successfully at: {skill_path}")
    print(f"\nNext steps:")
    print(f"1. Review and customize: {skill_path}/SKILL.md")
    print(f"2. Add your logic to: {skill_path}/scripts/ (if applicable)")
    print(f"3. Package for distribution: zip -r {skill_path.name}.zip {skill_path.name}/")


if __name__ == '__main__':
    main()
