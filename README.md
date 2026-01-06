# Create Skill

A comprehensive Claude Skill for creating, structuring, and packaging new Claude Skills.

## Overview

The create-skill skill provides a complete toolkit for developing Claude Skills, from initial concept to deployment-ready package. It guides you through skill creation with proper metadata, directory structure, and packaging for all Claude platforms.

## Features

- **Interactive Skill Creation**: Guided workflow for creating skills
- **Template Generation**: Pre-built templates for simple, intermediate, and complex skills
- **Python Script Templates**: Ready-to-use script scaffolds with type hints and docstrings
- **Metadata Validation**: Ensures skills meet Claude's requirements
- **ZIP Packaging**: Packages skills for distribution across all Claude platforms
- **Best Practices Guidance**: Follows Claude's recommended patterns

## Installation

### Claude Desktop
1. Package the skill:
   ```bash
   zip -r create-skill.zip create-skill/
   ```
2. Upload via Settings → Capabilities → Skills

### Claude Code
```bash
cp -r create-skill/ ~/.claude/skills/
```

### Claude API
Upload via `/v1/skills` endpoint with create-skill.zip

## Usage

### Option 1: Interactive (Recommended)

Just describe what you want:

```
Create a skill that analyzes financial data from CSV files
```

The skill will guide you through:
1. Skill naming and description
2. Complexity selection
3. Script requirements
4. Platform targeting
5. Customization

### Option 2: Direct Specification

```
Create a skill called csv-analyzer that:
- Reads CSV files
- Calculates statistics
- Generates visualizations
- Complexity: intermediate
- Include Python scripts
```

### Option 3: From Existing Code

```
Create a skill for my code at ./my-project/
Main functionality: Data processing and reporting
```

## Components

### Scripts

The skill includes four Python scripts:

1. **skill_generator.py** - Core generation engine
2. **template_builder.py** - Template-based creation
3. **package_skill.py** - ZIP packaging
4. **validator.py** - Metadata and structure validation

### Reference Materials

- **skill_structure_guide.md** - Complete guide to skill organization
- **template_specs.md** - Template specifications
- **best_practices.md** - Claude skill development standards

### Examples

- **example_simple_skill.md** - Simple brand guidelines skill
- **example_intermediate_skill.md** - Intermediate CSV analyzer skill
- **example_complex_skill.md** - Complex multi-component skill

## Command-Line Usage

You can also use the scripts directly:

```bash
# Generate from specification
python scripts/skill_generator.py --name my-skill --description "My skill"

# Build from template
python scripts/template_builder.py --template intermediate --name my-skill

# Validate existing skill
python scripts/validator.py ../my-skill/

# Package for distribution
python scripts/package_skill.py ../my-skill/ --with-instructions
```

## Skill Templates

### Simple Template
Single-purpose skills without code
- SKILL.md
- README.md

### Intermediate Template
Skills with scripts and configuration
- SKILL.md
- scripts/processor.py
- reference/config.yaml
- README.md

### Complex Template
Multi-component systems
- SKILL.md
- scripts/ (multiple)
- reference/ (documentation)
- examples/ (I/O samples)
- resources/ (assets)
- .claude/docs/ (architecture)

## Metadata Guidelines

### Name (required, max 64 chars)
- Descriptive and human-friendly
- Examples: "Financial Analyzer", "Brand Guidelines"

### Description (required, max 200 chars)
- Explains what skill does and when to use it
- Claude uses this for triggering
- Example: "Analyze CSV files and generate statistical summaries"

### Version (optional)
- Semantic versioning: MAJOR.MINOR.PATCH
- Example: 1.0.0

### Tags (optional)
- Category keywords for discovery
- Example: [data-analysis, csv, statistics]

## Output

When you create a skill, you get:

1. **Skill Directory**: Complete folder structure
2. **SKILL.md**: Properly formatted with YAML frontmatter
3. **Scripts**: Python templates (if needed)
4. **Reference Docs**: Configuration and guides
5. **Examples**: Sample inputs and outputs
6. **README**: Installation and usage instructions
7. **ZIP Package**: Ready to deploy

## Validation

The skill validates:

- ✓ SKILL.md has valid YAML frontmatter
- ✓ Name < 64 characters
- ✓ Description < 200 characters
- ✓ Scripts have shebang lines
- ✓ Scripts are executable
- ✓ No unwanted files (.pyc, __pycache__)
- ✓ Proper ZIP structure

## Best Practices

1. **Start Simple**: Begin with simple template, add complexity as needed
2. **Clear Descriptions**: Write descriptions that answer "when should this be used?"
3. **Specific Focus**: Each skill should do one thing well
4. **Test Incrementally**: Test after each major addition
5. **Version Control**: Use semantic versioning
6. **Document Examples**: Include real examples in SKILL.md

## Troubleshooting

**Skill not triggering?**
- Check description is specific enough (<200 chars)
- Ensure name is clear and descriptive
- Try: "Use the [skill-name] skill"

**Scripts not running?**
- Verify shebang: `#!/usr/bin/env python3`
- Check executable permissions: `chmod +x script.py`
- Test script standalone first

**ZIP not installing?**
- Ensure ZIP root contains skill folder
- Verify SKILL.md is at skill root
- Check YAML frontmatter is valid

## Contributing

This skill is part of the Claude Skills Factory. For improvements or bug reports, please refer to the main project.

## License

MIT License - See LICENSE file for details

## Acknowledgments

This skill was inspired by **Mark Kashef's** excellent YouTube video on Claude Skills:
- [How to Build Custom Skills for Claude](https://youtu.be/7_SL0FaY8MM?si=qDdrVb0vhs_BrF7X)

The video demonstrates the power and potential of Claude Skills, which inspired the creation of this systematic skill generation toolkit.

## Related Resources

- [Claude Skills Documentation](https://platform.claude.com/docs)
- [Mark Kashef on YouTube](https://www.youtube.com/@MarkKashef)
- [Skills Factory](../../)
- [Skill Examples](../../claude_skills_example/)
- [Best Practices](../../claude_skills_documentation/Skill%20authoring%20best%20practices.md)

## Version

Current version: 1.0.0

## Changelog

### v1.0.0 (2025-01-06)
- Initial release
- Four skill generation scripts
- Three template types
- Complete documentation
- Validation and packaging tools
