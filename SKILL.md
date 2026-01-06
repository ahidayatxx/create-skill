---
name: create-skill
description: Create new Claude Skills with proper structure, metadata, and packaging for deployment to Claude Desktop, Claude Code, or Claude API
version: 1.0.0
tags: [skill-development, claude-skills, automation, template-generation]
---

# Create Skill

A comprehensive skill development toolkit that guides you through creating, structuring, and packaging Claude Skills. This skill automates the creation of skill templates with proper metadata, directory structure, and packaging for immediate deployment.

## Capabilities

- **Interactive Skill Creation**: Guided workflow to create new Claude Skills step-by-step
- **Template Generation**: Automatically generates SKILL.md with proper YAML frontmatter
- **Directory Structure**: Creates correct folder organization (simple, intermediate, or complex)
- **Script Templates**: Provides Python/JavaScript script templates when needed
- **ZIP Packaging**: Packages skills for distribution across all Claude platforms
- **Best Practices Guidance**: Ensures skills follow Claude's recommended patterns
- **Metadata Validation**: Validates skill names, descriptions, and tags

## How to Use

### Option 1: Interactive Creation (Recommended)

1. **Describe your skill**: Tell me what you want your skill to do
2. **Answer prompts**: I'll ask about complexity, scripting needs, and target platform
3. **Review generated skill**: Examine the generated SKILL.md and structure
4. **Customize**: Add your specific instructions and logic
5. **Package**: Export as ready-to-deploy ZIP

### Option 2: Direct Specification

Provide these details in one message:
```
Create a skill called [skill-name] that [does what].
Complexity: simple | intermediate | complex
Scripts needed: yes | no
Target platform: desktop | code | api | all
```

### Option 3: From Existing Code

Already have code? Tell me:
```
Create a skill for my code at /path/to/code
Main functionality: [description]
```

## Input Format

This skill accepts various input formats:

- **Natural language description**: "I need a skill that analyzes financial data"
- **Structured specification**: JSON with skill details
- **Existing code reference**: Path to existing scripts or functions
- **Use case description**: "When users ask about X, do Y"

## Output Format

Generated skill includes:

- **SKILL.md**: Complete skill file with YAML metadata and instructions
- **Directory structure**: Organized folders based on complexity level
- **Scripts/**: Python/JavaScript templates (if needed)
- **reference/**: Configuration and documentation files (if needed)
- **examples/**: Example inputs and outputs (if needed)
- **README.md**: Setup and usage instructions
- **skill-name.zip**: Ready-to-deploy package

## Example Usage

**Example 1: Simple skill**
```
Create a skill called brand-style-guide that applies my company's
brand colors and fonts to documents.
```

**Example 2: Intermediate skill with scripts**
```
Create a skill called csv-analyzer that reads CSV files and generates
summary statistics. Include Python scripts for data processing.
```

**Example 3: Complex multi-component skill**
```
Create a skill for managing Docker containers. It should:
- Generate docker-compose.yml files
- Validate Docker configurations
- Provide container health check scripts
- Include reference documentation
```

## Skill Templates

### Simple Skill Template
Best for: Single-purpose skills without code
```
skill-name/
├── SKILL.md          # Metadata + instructions
└── README.md
```

### Intermediate Skill Template
Best for: Skills with scripts and configuration
```
skill-name/
├── SKILL.md
├── scripts/
│   └── processor.py  # Your code
├── reference/
│   └── config.yaml   # Configuration
└── README.md
```

### Complex Skill Template
Best for: Multi-component systems with resources
```
skill-name/
├── SKILL.md
├── scripts/          # Multiple scripts
├── reference/        # Documentation & config
├── examples/         # Sample I/O
├── resources/        # Assets (fonts, templates)
├── .claude/docs/     # Architecture docs
└── README.md
```

## Scripts

- `skill_generator.py`: Core skill generation engine
- `template_builder.py`: Creates skill templates from specifications
- `package_skill.py`: Packages skill as deployable ZIP
- `validator.py`: Validates skill metadata and structure

## Best Practices

1. **Start Simple**: Begin with a simple skill, add complexity as needed
2. **Clear Descriptions**: Write descriptions that answer "when should this skill be used?"
3. **Specific Focus**: Each skill should do one thing well
4. **Test Incrementally**: Test after each major addition
5. **Version Control**: Use semantic versioning (MAJOR.MINOR.PATCH)
6. **Document Examples**: Include real examples in SKILL.md
7. **Validate Metadata**: Ensure name is <64 chars, description <200 chars

## Metadata Guidelines

### Name Field (required, max 64 chars)
- Use descriptive, human-friendly names
- Examples: "Financial Analyzer", "Brand Guidelines", "CSV to JSON"

### Description Field (required, max 200 chars)
- Explain what the skill does and when to use it
- Claude uses this to decide when to invoke your skill
- Examples:
  - "Apply Acme Corp brand guidelines to documents including colors, fonts, and logos"
  - "Analyze CSV files and generate statistical summaries with visualizations"

### Version Field (optional)
- Use semantic versioning: 1.0.0, 1.1.0, 2.0.0
- Increment: MAJOR for breaking changes, MINOR for features, PATCH for fixes

### Tags Field (optional)
- Help with discovery and organization
- Examples: [data-analysis, finance, reporting], [branding, marketing]

## Limitations

- **Claude API Skills**: All dependencies must be pre-installed (no runtime package installation)
- **Skill Size**: Keep individual skills focused under 500 lines of SKILL.md
- **File References**: Use relative paths for portability
- **Script Execution**: Scripts run in sandboxed environment
- **No Cross-Skill References**: Skills cannot explicitly import other skills (but Claude can compose them)

## Creating Skills Programmatically

If you want to generate skills programmatically, use the provided Python scripts:

```bash
# Generate skill from specification
python scripts/skill_generator.py --spec skill-spec.json

# Create from template
python scripts/template_builder.py --template intermediate --name my-skill

# Package existing skill
python scripts/package_skill.py --skill-path ./my-skill

# Validate skill
python scripts/validator.py --skill-path ./my-skill
```

## Skill Complexity Levels

**Simple** (~50-150 lines SKILL.md):
- Single-purpose functionality
- No external scripts
- Minimal configuration
- Example: Brand guidelines, text templates

**Intermediate** (~150-300 lines SKILL.md + scripts):
- Custom Python/JavaScript logic
- Configuration files
- Data processing
- Example: CSV analyzer, file converter

**Complex** (~300-500 lines SKILL.md + multi-component):
- Multiple scripts and resources
- External service integration
- Comprehensive documentation
- Example: MCP server builder, Docker manager

## Troubleshooting

**Skill not triggering?**
- Check description is specific enough (<200 chars)
- Ensure name is clear and descriptive
- Test with explicit: "Use the [skill-name] skill"

**Scripts not running?**
- Verify shebang line: `#!/usr/bin/env python3`
- Check executable permissions
- Test script standalone first

**ZIP not installing?**
- Ensure ZIP root contains skill folder (not loose files)
- Verify SKILL.md is at skill root
- Check YAML frontmatter is valid

## Related Resources

- [Claude Skills Documentation](https://platform.claude.com/docs)
- Claude Skills Factory: `/path/to/claude-skills-factory/`
- Skill examples: `claude_skills_example/`
- Best practices: `claude_skills_documentation/Skill authoring best practices.md`

## Quick Start Template

```yaml
# Copy this template to get started
---
name: Your Skill Name
description: One sentence description of what this skill does
version: 1.0.0
tags: [category, purpose]
---

# Your Skill Name

[2-3 sentence overview]

## Capabilities

- [Capability 1]
- [Capability 2]

## How to Use

1. [Step 1]
2. [Step 2]
3. [Step 3]

## Example Usage

"[Example prompt]"
```

---

**Need Help?** Just describe what you want to create and I'll guide you through building your skill step-by-step.
