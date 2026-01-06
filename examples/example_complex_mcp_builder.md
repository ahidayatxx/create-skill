# Example: Complex Skill - MCP Builder

## Overview

This example demonstrates creating a **complex skill** with scripts, reference documentation, and comprehensive guides for building MCP (Model Context Protocol) servers.

## User Request

```
Create a skill called mcp-builder that guides developers through creating
high-quality MCP servers that enable LLMs to interact with external services
through well-designed tools. Should include reference documentation and
examples for both Python and TypeScript.
```

## Skill Type

**Complexity**: Complex (multi-component system)
**Scripts**: Reference documentation only (no executable scripts)
**Target Platform**: All (Desktop, Code, API)

## Generated Structure

```
mcp-builder/
├── SKILL.md                    # Comprehensive MCP development guide
├── reference/                  # MCP documentation and guides
│   ├── mcp_best_practices.md
│   ├── node_mcp_server.md
│   └── python_mcp_server.md
└── README.md                   # Installation and usage
```

## Key Features

### SKILL.md Contains (500+ lines)

1. **YAML Frontmatter**
   ```yaml
   ---
   name: mcp-builder
   description: Guide for creating high-quality MCP servers that enable LLMs
     to interact with external services through well-designed tools
   ---
   ```

2. **Four-Phase Process**
   - Phase 1: Deep Research and Planning
   - Phase 2: Implementation
   - Phase 3: Testing and Validation
   - Phase 4: Documentation and Publishing

3. **Comprehensive Workflow**
   - High-level workflow overview
   - Detailed step-by-step guidance
   - Best practices for each phase
   - Common pitfalls and solutions

4. **Language-Specific Guidance**
   - TypeScript (recommended) with SDK links
   - Python alternatives with SDK links
   - Code examples and patterns

5. **Tool Design Patterns**
   - API coverage vs workflow tools
   - Tool naming conventions
   - Context management
   - Error messaging

### Reference Documentation

**mcp_best_practices.md** (~200 lines)
- Core MCP development principles
- Tool design patterns
- Error handling strategies
- Testing methodologies

**node_mcp_server.md** (~300 lines)
- Project structure for TypeScript
- Package.json setup
- Tool implementation examples
- Zod validation patterns
- Error handling code samples

**python_mcp_server.md** (~250 lines)
- Module organization
- Pydantic validation
- FastMCP patterns
- Decorator usage
- Type hints requirements

## How This Skill Works

When invoked, Claude will:

1. **Guide research phase**
   - Navigate MCP specification
   - Study framework documentation
   - Plan implementation strategy

2. **Provide implementation guidance**
   - Set up project structure
   - Implement core infrastructure
   - Create tools with proper schemas
   - Add error handling

3. **Show testing approaches**
   - Unit testing strategies
   - Integration testing
   - Error simulation
   - Load testing

4. **Documentation standards**
   - README requirements
   - API documentation
   - Example usage
   - Publishing guidelines

## Example Usage

```
"Use mcp-builder to create a GitHub API integration server"
"Help me build an MCP server for my weather API using TypeScript"
"Guide me through MCP server development best practices"
"I need to create an MCP server for Slack integration"
```

## Why This Is a Good Complex Skill

✓ **Comprehensive Coverage**: Complete development lifecycle
✓ **Reference Materials**: Detailed docs in subdirectory
✓ **Multi-Language**: TypeScript and Python guidance
✓ **Best Practices**: Industry-standard approaches
✓ **Practical Examples**: Real code patterns and samples
✓ **Progressive Disclosure**: Main guide + detailed references

## Architectural Patterns Demonstrated

### 1. Progressive Disclosure
```
SKILL.md (main guide)
    ├── Links to reference docs
    ├── └── reference/node_mcp_server.md (TypeScript details)
    ├── └── reference/python_mcp_server.md (Python details)
    └── └── reference/mcp_best_practices.md (core principles)
```

### 2. Reference Documentation Organization
```
reference/
├── Best Practices (domain knowledge)
├── Language Guide 1 (TypeScript)
└── Language Guide 2 (Python)
```

### 3. Workflow-Based Structure
```
Phase 1 → Phase 2 → Phase 3 → Phase 4
  ↓         ↓         ↓         ↓
Planning  Implementation  Testing  Documentation
```

## Content Sections

### SKILL.md Sections

1. **Overview** (lines 6-11)
2. **Process** (lines 14-500)
   - High-Level Workflow
   - Phase 1: Deep Research and Planning
   - Phase 2: Implementation
   - Phase 3: Testing and Validation
   - Phase 4: Documentation and Publishing

### Reference Docs Sections

**mcp_best_practices.md**
- Design Philosophy
- Tool Design
- Error Handling
- Testing
- Documentation

**node_mcp_server.md**
- Project Setup
- Tool Implementation
- Validation
- Error Handling
- Testing

**python_mcp_server.md**
- Module Structure
- Tool Creation
- Validation
- Resource Management
- Testing

## Best Practices Demonstrated

1. **Comprehensive Description** (191 chars): Detailed but under 200 limit
2. **Structured Workflow**: Clear phases with numbered steps
3. **External References**: Links to official documentation
4. **Code Examples**: TypeScript and Python samples
5. **Reference Linking**: Main file links to detailed docs
6. **Multiple Languages**: Covers TypeScript and Python
7. **Testing Coverage**: Includes testing strategies
8. **Error Handling**: Comprehensive error guidance

## Customization Guide

To adapt for your development framework:

1. **Update process phases** for your workflow
2. **Add language guides** for other languages
3. **Include framework-specific** patterns
4. **Add API examples** for your domain
5. **Update best practices** for your context

## Metadata Quality

| Field | Value | Status |
|-------|-------|--------|
| Name | mcp-builder | ✓ 10 chars (well under 64) |
| Description | Guide for creating high-quality MCP servers... | ✓ 191 chars (under 200) |
| Version | Not specified | ⚠ Consider adding v1.0.0 |

## Complexity Indicators

**Structure**:
- SKILL.md: 500+ lines
- Reference docs: 750+ lines total
- Three reference files

**Organization**:
- 4 major phases
- 10+ sub-sections per phase
- Multiple code examples
- External documentation links

**Content Types**:
- Procedural instructions
- Code samples
- Best practices
- Troubleshooting guides
- External references

## Alternative Applications

This pattern works well for:

- **Framework Development** - Any development framework guide
- **API Integration** - REST API, GraphQL API integration
- **SDK Creation** - SDK development guides
- **Developer Tools** - CLI tools, dev utilities
- **Protocol Implementation** - Network protocols, file formats

## Learning Outcomes

By studying this example, you'll learn:

1. How to structure a comprehensive complex skill
2. Organizing reference documentation in subdirectories
3. Progressive disclosure patterns (main → detailed)
4. Linking to external resources effectively
5. Creating workflow-based skill organization
6. Providing multi-language guidance
7. Including testing and validation strategies
8. Balancing breadth and depth in documentation

## Real-World Usage

**Before**: Scattered MCP documentation, inconsistent approaches
```
Developer searches: "How to build MCP server?"
Finds: Fragmented docs, outdated examples, no best practices
Result: Inconsistent server quality, common mistakes
```

**After**: Guided development with best practices
```
Developer uses: "Use mcp-builder to create a server"
Claude provides: Structured workflow, language-specific guides,
               best practices, testing strategies
Result: High-quality servers following standards
```

## Content Analysis

### SKILL.md Breakdown
- **Overview**: 11 lines
- **Process**: 489 lines
  - Phase 1: ~120 lines
  - Phase 2: ~150 lines
  - Phase 3: ~100 lines
  - Phase 4: ~80 lines
  - Additional sections: ~39 lines

### Reference Docs Breakdown
- **mcp_best_practices.md**: ~200 lines
- **node_mcp_server.md**: ~300 lines
- **python_mcp_server.md**: ~250 lines

**Total Documentation**: ~1,239 lines

## Comparison with Simple Skills

| Aspect | Simple Skill | Complex Skill |
|--------|--------------|---------------|
| **Lines** | 150-200 | 500+ (main) + 750+ (refs) |
| **Files** | 1-2 | 5-10 |
| **Scripts** | 0 | Optional (reference docs) |
| **Reference** | None | Multiple .md files |
| **Focus** | Single task | Complete workflow |
| **Audience** | End users | Developers |
| **Maintenance** | Low | Medium-High |

## File Reference

**Original Skill**: `../../claude_skills_example/example1-mcp-builder/SKILL.md`
**Lines**: 500+ (main) + 750+ (references)
**Complexity**: Complex

---

**Related Examples**:
- `example_simple_skill.md` - Compare with simple skill approach
- `example_complex_skill.md` - See resource-based complex skill
