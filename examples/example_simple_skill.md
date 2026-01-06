# Example: Creating a Simple Skill

## User Request

Create a simple skill called "brand-style-guide" that applies my company's brand guidelines to documents.

## Generated Skill Structure

```
brand-style-guide/
├── SKILL.md
└── README.md
```

## Generated SKILL.md (excerpt)

```yaml
---
name: Brand Style Guide
description: Apply company brand guidelines including colors, fonts, and logo usage to documents
version: 1.0.0
tags: [branding, marketing, documents]
---
```

## How to Use

```
"Use brand-style-guide to help me format this presentation"
"Apply brand-style-guide to my document"
```

## What Gets Created

1. **SKILL.md** with:
   - Proper YAML frontmatter
   - Company brand colors section
   - Typography guidelines
   - Logo usage rules
   - Example usage prompts

2. **README.md** with:
   - Installation instructions
   - Usage examples
   - Customization guide

## Customization Steps

1. Edit SKILL.md to add your specific brand:
   - Add your company's hex colors
   - Specify font names and sizes
   - Include logo spacing rules

2. Add examples of branded documents

3. Package for distribution:
   ```bash
   zip -r brand-style-guide.zip brand-style-guide/
   ```

## Result

A ready-to-use skill that ensures all documents follow your brand guidelines.
