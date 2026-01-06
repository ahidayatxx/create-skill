# Example: Simple Skill - Brand Guidelines

## Overview

This example demonstrates creating a **simple skill** (SKILL.md only, no scripts) for applying corporate brand guidelines.

## User Request

```
Create a skill called applying-brand-guidelines that applies consistent
corporate branding and styling to all generated documents including colors,
fonts, layouts, and messaging.
```

## Skill Type

**Complexity**: Simple (SKILL.md only)
**Scripts**: No
**Target Platform**: All (Desktop, Code, API)

## Generated Structure

```
applying-brand-guidelines/
├── SKILL.md          # Complete brand guidelines (172 lines)
└── README.md         # Installation instructions
```

## Key Features

### SKILL.md Contains

1. **YAML Frontmatter** (Required)
   ```yaml
   ---
   name: applying-brand-guidelines
   description: This skill applies consistent corporate branding and styling
     to all generated documents including colors, fonts, layouts, and messaging
   ---
   ```

2. **Brand Identity Section**
   - Company name and tagline
   - Industry context
   - Visual standards

3. **Color Palette**
   - Primary colors with hex/RGB values
   - Secondary colors (success, warning, error)
   - Usage guidelines

4. **Typography**
   - Font families
   - Font hierarchy (H1-H3, body, caption)
   - Size guidelines

5. **Document Standards**
   - PowerPoint templates
   - Excel formatting
   - PDF layout

6. **Content Guidelines**
   - Tone of voice
   - Standard phrases
   - Data presentation

7. **Quality Standards**
   - Before finalizing checklist
   - Prohibited elements

## How This Skill Works

When invoked, Claude will:

1. **Apply brand colors** to any generated content
2. **Use specified fonts** at correct sizes
3. **Follow layout rules** for margins and spacing
4. **Maintain professional tone** in all text
5. **Use brand terminology** in openings/closings
6. **Format data** according to guidelines

## Example Usage

```
"Use applying-brand-guidelines to create a sales presentation"
"Format this Excel report according to brand guidelines"
"Apply brand standards to this PDF document"
```

## Why This Is a Good Simple Skill

✓ **Single Purpose**: Focuses on one specific task (branding)
✓ **No Code Needed**: Pure instructions, no scripts required
✓ **Clear Scope**: Well-defined what it does and doesn't do
✓ **Reusable**: Works across document types (slides, sheets, docs)
✓ **Self-Contained**: All information in SKILL.md
✓ **Maintainable**: Easy to update colors/fonts centrally

## Best Practices Demonstrated

1. **Descriptive Name** (24 chars): "applying-brand-guidelines"
2. **Clear Description** (138 chars): Explains exactly what it does
3. **Structured Content**: Organized into logical sections
4. **Specific Guidelines**: Concrete hex codes, sizes, rules
5. **Examples**: Real formatting standards for different apps
6. **Quality Checks**: What to verify before finalizing

## Customization Guide

To adapt this skill for your organization:

1. **Replace company information**
   - Change "Acme Corporation" to your company name
   - Update tagline and industry

2. **Update color palette**
   - Replace hex codes with your brand colors
   - Keep the same structure (primary/secondary)

3. **Modify typography**
   - Change font families to your brand fonts
   - Adjust sizes to match your standards

4. **Add document types**
   - Include your common formats (Reports, Invoices, etc.)
   - Specify templates for each

5. **Update terminology**
   - Replace standard phrases with your preferred language
   - Add industry-specific terms

## Metadata Quality

| Field | Value | Status |
|-------|-------|--------|
| Name | applying-brand-guidelines | ✓ 24 chars (well under 64) |
| Description | Applies consistent corporate branding... | ✓ 138 chars (well under 200) |
| Version | Not specified | ⚠ Consider adding v1.0.0 |

## Alternative Applications

This pattern works well for:

- **Style Guides** - Writing style, AP style, Chicago style
- **Design Systems** - Component libraries, UI kits
- **Templates** - Report templates, proposal formats
- **Guidelines** - Coding standards, documentation standards
- **Checklists** - QA checklists, review criteria

## Learning Outcomes

By studying this example, you'll learn:

1. How to structure a simple, single-purpose skill
2. Writing clear descriptions that Claude uses for triggering
3. Organizing content into logical sections
4. Providing specific, actionable guidelines
5. Creating reusable instructions that work across contexts
6. When scripts are NOT needed (most simple skills)

## Real-World Usage

**Before**: Inconsistent formatting across documents
```
Sales Presentation: Uses default PowerPoint template
Excel Report: Basic formatting, no company colors
PDF Document: Inconsistent fonts and layouts
```

**After**: Consistent brand application
```
Sales Presentation: Uses Acme Blue title slides, proper logo placement
Excel Report: Headers in brand colors, alternating row colors
PDF Document: Segoe UI fonts, 1-inch margins, proper headers/footers
```

## File Reference

**Original Skill**: `../../claude_skills_example/applying-brand-guidelines/SKILL.md`
**Lines**: 172
**Complexity**: Simple

---

**Next Steps**: See `example_complex_mcp_builder.md` for a multi-component skill example.
