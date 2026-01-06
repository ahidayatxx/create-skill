# Skill Structure Guide

## Claude Skill Directory Structures

Claude Skills can be organized at three complexity levels. Choose the structure that matches your skill's requirements.

## Simple Skills

**Best for**: Single-purpose skills without code execution

```
skill-name/
├── SKILL.md          # Required: Metadata and instructions
└── README.md         # Recommended: Setup and usage
```

**Characteristics**:
- 50-150 lines in SKILL.md
- No external scripts
- Minimal configuration
- Fast to create and maintain

**Examples**:
- Brand guidelines application
- Text template expansion
- Style checking
- Checklist validation

---

## Intermediate Skills

**Best for**: Skills with data processing or calculations

```
skill-name/
├── SKILL.md
├── scripts/
│   ├── __init__.py
│   ├── processor.py        # Main processing logic
│   └── helpers.py           # Utility functions (optional)
├── reference/
│   └── config.yaml          # Configuration (optional)
└── README.md
```

**Characteristics**:
- 150-300 lines in SKILL.md
- Python/JavaScript scripts
- Configuration files
- Data transformation capabilities

**Examples**:
- CSV analysis
- File conversion
- Data validation
- API integration

---

## Complex Skills

**Best for**: Multi-component systems with extensive resources

```
skill-name/
├── SKILL.md
├── scripts/
│   ├── __init__.py
│   ├── processor.py
│   ├── helpers.py
│   └── validators.py
├── reference/
│   ├── config.yaml
│   ├── documentation.md
│   └── schemas/            # Data schemas
├── examples/
│   ├── example_input.md
│   └── example_output.md
├── resources/              # Assets (fonts, templates, etc.)
│   └── assets/
├── .claude/
│   └── docs/
│       └── architecture.md
└── README.md
```

**Characteristics**:
- 300-500 lines in SKILL.md
- Multiple scripts and utilities
- Comprehensive documentation
- External service integration
- Resource assets

**Examples**:
- MCP server builders
- Multi-step workflows
- Complex data pipelines
- Service integrations

---

## File Specifications

### SKILL.md (Required)

**Must have YAML frontmatter**:
```yaml
---
name: Skill Name
description: One-sentence description
version: 1.0.0
tags: [category, purpose]
---
```

**Field requirements**:
- `name`: Max 64 characters, descriptive
- `description`: Max 200 characters, explains when to use
- `version`: Optional, recommended format: MAJOR.MINOR.PATCH
- `tags`: Optional, list of category keywords

### Scripts (Optional)

**Python scripts** should:
- Start with shebang: `#!/usr/bin/env python3`
- Have type hints on functions
- Include docstrings
- Be executable (`chmod +x`)

**Example structure**:
```python
#!/usr/bin/env python3
"""Script description."""

import argparse
from typing import Dict

def process(input_data: str) -> Dict:
    """Process input and return result."""
    # Implementation
    pass

def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser()
    # Add arguments
    args = parser.parse_args()
    # Process

if __name__ == '__main__':
    main()
```

### Reference Files

**YAML configuration**:
```yaml
settings:
  debug: false
  verbose: true

parameters:
  timeout: 30
  retries: 3
```

**Documentation**:
- Use Markdown format
- Include examples
- Explain configuration options
- Document API integrations

### Examples

**Example inputs/outputs**:
- Show realistic use cases
- Include expected formats
- Demonstrate edge cases
- Provide copy-paste examples

---

## Naming Conventions

### Directories
- Use **kebab-case** (lowercase with hyphens)
- Examples: `my-skill/`, `data-processor/`, `api-integrator/`

### Files
- **SKILL.md**: Always uppercase, exactly as shown
- **scripts/**: Lowercase with underscores: `processor.py`, `data_helper.py`
- **reference/**: Descriptive names: `config.yaml`, `documentation.md`

### Skill Names
- Keep under 64 characters
- Use descriptive, human-friendly names
- Examples:
  - ✅ "Financial Analyzer"
  - ✅ "Brand Style Guide"
  - ✅ "CSV to JSON Converter"
  - ❌ "skill1"
  - ❌ "My Script"

---

## Progressive Disclosure

Organize your SKILL.md to load information progressively:

**Level 1 (Metadata)**: Always loaded (~100 tokens)
- Name, description, tags

**Level 2 (Core)**: Loaded when triggered (~5k tokens)
- Main instructions
- How to use
- Examples

**Level 3 (Reference)**: Loaded as needed (unlimited)
- Detailed documentation
- Configuration guides
- Advanced usage

---

## Common Patterns

### Error Handling
```markdown
## Troubleshooting

**Common Issues:**
- **Problem**: Description
  - **Solution**: How to fix
```

### Best Practices Section
```markdown
## Best Practices

1. **Practice 1**: Description
2. **Practice 2**: Description
3. **Practice 3**: Description
```

### Limitations
```markdown
## Limitations

- **Limitation 1**: Description and workaround
- **Limitation 2**: Description and alternative approach
```

---

## Packaging

For distribution, package as ZIP:

```bash
zip -r skill-name.zip skill-name/
```

**Important**: ZIP root must contain skill folder, not loose files.

**Correct structure**:
```
skill-name.zip
└── skill-name/
    ├── SKILL.md
    └── ...
```

**Incorrect structure**:
```
skill-name.zip
├── SKILL.md
└── ...
```

---

## Platform-Specific Notes

### Claude Desktop
- Upload ZIP via Settings → Capabilities → Skills
- All script dependencies must be pre-installed
- Scripts run in sandboxed environment

### Claude Code
- Copy to `~/.claude/skills/skill-name/`
- Can install dependencies at load time
- Has access to local filesystem

### Claude API
- Upload via `/v1/skills` endpoint
- All dependencies must be pre-installed
- Cannot install packages at runtime

---

## Validation Checklist

Before packaging, verify:

- [ ] SKILL.md has valid YAML frontmatter
- [ ] Name is < 64 characters
- [ ] Description is < 200 characters
- [ ] Description explains when to use the skill
- [ ] Scripts have shebang lines
- [ ] Scripts are executable
- [ ] Examples demonstrate real usage
- [ ] README.md explains installation
- [ ] No unwanted files (.pyc, __pycache__, .DS_Store)
- [ ] ZIP has correct structure

---

## Resources

- [Claude Skills Documentation](https://platform.claude.com/docs)
- [Skill Authoring Best Practices](https://platform.claude.com/docs/agents-and-tools/agent-skills/best-practices)
- [Skills Factory Examples](../../claude_skills_example/)
