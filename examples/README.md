# Create Skill Examples

This directory contains example workflows showing how to use the **create-skill** skill to build different types of Claude Skills.

## Available Examples

### Quick Reference

| Example | Complexity | Scripts? | Resources? | Best For |
|---------|------------|----------|------------|----------|
| **simple_brand_guidelines** | Simple | ✗ | ✗ | First-time skill creators |
| **intermediate_csv_analyzer** | Intermediate | ✓ | ✗ | Skills with data processing |
| **brand_guidelines_skill** | Simple | ✗ | ✗ | Single-purpose skills |
| **complex_mcp_builder** | Complex | Reference docs | ✗ | Comprehensive development guides |
| **resource_canvas_design** | Resource-Based | ✗ | ✓ (fonts) | Bundling assets and resources |

---

## Examples by Skill Type

### Simple Skills (SKILL.md Only)

**1. Simple Brand Guidelines** ([example_simple_skill.md](example_simple_skill.md))
- **What**: Create a basic brand guidelines skill
- **Use Case**: Single-purpose skill without code
- **Structure**: SKILL.md + README.md only
- **Lines**: ~150 lines
- **Learn**: Basic skill structure, YAML frontmatter

**2. Brand Guidelines Skill** ([example_brand_guidelines_skill.md](example_brand_guidelines_skill.md))
- **What**: Real-world brand guidelines skill
- **Source**: `applying-brand-guidelines` from Skills Factory
- **Use Case**: Corporate branding, style guides
- **Structure**: SKILL.md (172 lines)
- **Learn**: Professional skill organization, clear sections

### Intermediate Skills (With Scripts)

**3. Intermediate CSV Analyzer** ([example_intermediate_skill.md](example_intermediate_skill.md))
- **What**: Create a CSV analysis skill with Python scripts
- **Use Case**: Data processing, file analysis
- **Structure**: SKILL.md + scripts/ + reference/
- **Lines**: ~200 lines + Python code
- **Learn**: Script generation, CLI patterns, type hints

### Complex Skills (Multi-Component)

**4. Complex MCP Builder** ([example_complex_mcp_builder.md](example_complex_mcp_builder.md))
- **What**: Comprehensive MCP server development guide
- **Source**: `example1-mcp-builder` from Skills Factory
- **Use Case**: Framework development, developer tools
- **Structure**: SKILL.md (500+ lines) + reference/ docs
- **Lines**: ~1,239 total (main + references)
- **Learn**: Progressive disclosure, reference docs, workflows

### Resource-Based Skills

**5. Resource Canvas Design** ([example_resource_canvas_design.md](example_resource_canvas_design.md))
- **What**: Typography skill with bundled font files
- **Source**: `example2-canvas-design` from Skills Factory
- **Use Case**: Asset bundling, font libraries, templates
- **Structure**: SKILL.md + resources/ (82 fonts)
- **Size**: ~2.6 MB resources
- **Learn**: Resource bundling, license management, asset organization

---

## Choose Your Example

### I'm Creating My First Skill

Start with: **Simple Brand Guidelines** ([example_simple_skill.md](example_simple_skill.md))

**Why**: Teaches basics without complexity
- Simple structure (just SKILL.md)
- Easy to customize
- No programming required

---

### I Need Data Processing Capabilities

Use: **Intermediate CSV Analyzer** ([example_intermediate_skill.md](example_intermediate_skill.md))

**Why**: Shows script integration
- Python script templates
- CLI argument parsing
- Type hints and documentation
- Data validation patterns

---

### I'm Building a Developer Tool

Study: **Complex MCP Builder** ([example_complex_mcp_builder.md](example_complex_mcp_builder.md))

**Why**: Comprehensive development guide
- Workflow-based organization
- Reference documentation
- Multi-language guidance
- Best practices and testing

---

### I Need to Bundle Assets

Learn from: **Resource Canvas Design** ([example_resource_canvas_design.md](example_resource_canvas_design.md))

**Why**: Shows resource bundling
- Font file organization
- License management
- Asset documentation
- ZIP packaging for large files

---

## Example Deep Dives

### Example 1: Brand Guidelines Skill

**Original**: `applying-brand-guidelines` from Skills Factory

**What It Demonstrates**:
- Clear YAML frontmatter
- Well-organized sections
- Specific guidelines (hex codes, sizes)
- Application instructions
- Quality checklists

**Key Sections**:
1. Brand Identity
2. Visual Standards (colors, fonts)
3. Document Standards (PowerPoint, Excel, PDF)
4. Content Guidelines (tone, phrases)
5. Quality Standards (checklists)

**Takeaways**:
- Simple doesn't mean basic
- Structure information logically
- Be specific and actionable
- Include quality checks

---

### Example 2: MCP Builder

**Original**: `example1-mcp-builder` from Skills Factory

**What It Demonstrates**:
- Comprehensive workflow (4 phases)
- Progressive disclosure (main → references)
- Reference documentation organization
- External resource linking
- Multi-language support

**Key Sections**:
1. Overview
2. Process (Phase 1-4)
3. Reference Docs (3 files, 750+ lines)

**Takeaways**:
- Split complex topics into phases
- Use reference docs for details
- Link to external resources
- Cover multiple languages/stacks
- Include testing strategies

---

### Example 3: Canvas Design

**Original**: `example2-canvas-design` from Skills Factory

**What It Demonstrates**:
- Resource bundling (fonts)
- License management
- Asset organization
- Platform-specific guidance
- Typography best practices

**Key Sections**:
1. Typography Fundamentals
2. Design Asset Management
3. Platform-Specific Guidance
4. Best Practices

**Resources**:
- 82 font files
- LICENSE.txt
- Font metadata

**Takeaways**:
- Bundle only what's needed
- Document licenses clearly
- Organize resources by type
- Keep skill size manageable
- Test resource access

---

## Comparison Matrix

| Aspect | Simple | Intermediate | Complex | Resource-Based |
|--------|--------|--------------|---------|----------------|
| **Purpose** | Single task | Data processing | Development | Asset library |
| **SKILL.md** | 100-200 lines | 200-300 lines | 400-600 lines | 200-400 lines |
| **Scripts** | 0 | 1-3 | 3-10 | 0 |
| **Reference** | 0 | 1 file | 3+ files | 0-1 |
| **Resources** | 0 | 0 | 0-5 | 10+ |
| **Size** | KBs | KBs | KBs | MBs |
| **Maintenance** | Low | Medium | High | Medium |
| **Audience** | End users | Analysts | Developers | Designers |
| **Creator Skill** | Beginner | Intermediate | Advanced | Intermediate |

---

## Learning Path

### Beginner
1. Read `example_simple_skill.md`
2. Create your first simple skill
3. Practice YAML frontmatter
4. Organize content sections

### Intermediate
1. Study `example_intermediate_skill.md`
2. Learn Python script basics
3. Understand CLI patterns
4. Create skill with scripts

### Advanced
1. Analyze `example_complex_mcp_builder.md`
2. Learn progressive disclosure
3. Create reference docs
4. Build comprehensive workflows

### Asset Management
1. Review `example_resource_canvas_design.md`
2. Understand resource bundling
3. Manage licenses
4. Package with assets

---

## Quick Start Examples

### Create a Simple Skill

```
User: "Create a skill called style-guide for writing documentation"
Claude: [Uses create-skill with simple template]
Output: style-guide/ with SKILL.md + README.md
```

### Create an Intermediate Skill

```
User: "Create a CSV analyzer skill with Python scripts"
Claude: [Uses create-skill with intermediate template]
Output: csv-analyzer/ with SKILL.md + scripts/ + reference/
```

### Create a Complex Skill

```
User: "Create a comprehensive API integration guide"
Claude: [Uses create-skill with complex template]
Output: api-integration/ with SKILL.md + scripts/ + reference/ + examples/
```

### Create a Resource-Based Skill

```
User: "Create a font library skill with my favorite fonts"
Claude: [Uses create-skill, adds resources directory]
Output: font-library/ with SKILL.md + fonts/ (80+ files)
```

---

## Best Practices Across Examples

### Common Patterns

**1. Clear Metadata**
- Name < 64 characters
- Description < 200 characters
- Descriptive, not clever

**2. Structured Content**
- Use consistent headings
- Logical section order
- Clear hierarchy

**3. Actionable Instructions**
- Step-by-step guidance
- Specific examples
- Concrete values

**4. Quality Validation**
- Checklist where relevant
- Common mistakes to avoid
- Troubleshooting tips

**5. Professional Presentation**
- Proper grammar and spelling
- Consistent formatting
- Clear examples

---

## Example Files Summary

| File | Lines | Purpose |
|------|-------|---------|
| `example_simple_skill.md` | ~80 | Basic skill creation |
| `example_brand_guidelines_skill.md` | ~150 | Real-world simple skill |
| `example_intermediate_skill.md` | ~100 | Script-based skill |
| `example_complex_mcp_builder.md` | ~200 | Complex multi-component |
| `example_resource_canvas_design.md` | ~250 | Resource bundling |

---

## How to Use These Examples

1. **Choose** an example matching your needs
2. **Read** the example file completely
3. **Understand** the patterns and structure
4. **Adapt** for your specific use case
5. **Create** your skill using create-skill
6. **Validate** using the patterns shown

---

## Contributing

To add new examples:

1. Choose a skill from the Skills Factory examples
2. Analyze its structure and key features
3. Create an example file following this format
4. Include: overview, usage, best practices, takeaways
5. Add to this README index

---

## Related Resources

- [Create Skill SKILL.md](../SKILL.md) - Main skill documentation
- [Skill Structure Guide](../reference/skill_structure_guide.md) - Structure reference
- [Skills Factory Examples](../../claude_skills_example/) - Original examples
- [Best Practices](../../claude_skills_documentation/Skill%20authoring%20best%20practices.md)

---

**Need Help?** Start with the simple examples and work your way up as you become more comfortable with skill creation.
