# Example: Resource-Based Skill - Canvas Design

## Overview

This example demonstrates creating a **skill with resources and assets** - a skill that bundles fonts, licenses, and other resources for typography and design tasks.

## User Request

```
Create a skill called canvas-design that provides access to curated typography
resources, font management, and design asset handling for Canva and other
design platforms.
```

## Skill Type

**Complexity**: Simple to Intermediate (SKILL.md + resources)
**Scripts**: No (but has resource files)
**Target Platform**: All (Desktop, Code, API)

## Generated Structure

```
canvas-design/
├── SKILL.md                    # Typography and design guide (350 lines)
├── canvas-fonts/               # 82 font files (resources directory)
│   ├── LICENSE.txt             # Font license
│   ├── font-files/             # Actual font files (.ttf, .otf)
│   └── font-metadata/          # Font information
└── README.md                   # Installation and usage
```

## Key Features

### SKILL.md Contains

1. **YAML Frontmatter**
   ```yaml
   ---
   name: canvas-design
   description: Curated typography and design assets for professional
     visual content creation including font selection, pairing, and usage
   ---
   ```

2. **Typography Fundamentals**
   - Font classification (serif, sans-serif, display, etc.)
   - Font selection criteria
   - Readability guidelines
   - Pairing principles

3. **Design Asset Management**
   - Font organization
   - License compliance
   - Asset storage
   - Version management

4. **Platform-Specific Guidance**
   - Canva integration
   - Figma usage
   - Adobe Creative Cloud
   - Web platforms

5. **Best Practices**
   - Font pairing combinations
   - Hierarchy and scale
   - Contrast and readability
   - Professional standards

### Resource Directory (canvas-fonts/)

**82 Font Files** including:
- Open Sans (various weights)
- Roboto (various weights)
- Lato (various weights)
- Montserrat (various weights)
- Playfair Display (various weights)
- And many more...

**LICENSE.txt**
- Font licensing terms
- Usage rights and restrictions
- Attribution requirements
- Commercial use guidelines

## How This Skill Works

When invoked, Claude will:

1. **Recommend fonts** based on project type
2. **Suggest font pairings** (heading + body)
3. **Provide font guidance** (sizes, weights, spacing)
4. **Check licensing** before use
5. **Access font files** from bundled resources
6. **Apply typography principles** to designs

## Example Usage

```
"Use canvas-design to select fonts for my presentation"
"Recommend a heading and body font pairing for my website"
"Check if Open Sans Bold can be used commercially"
"Suggest fonts for a corporate annual report"
```

## Why This Is a Good Resource-Based Skill

✓ **Practical Resources**: Actual font files bundled
✓ **License Management**: Clear usage rights
✓ **Professional Content**: Industry-standard fonts
✓ **Expert Guidance**: Typography best practices
✓ **Platform Integration**: Works with design tools
✓ **Self-Contained**: All assets in skill directory

## Resource Bundling Patterns

### Directory Structure for Assets

```
skill-name/
├── SKILL.md
├── resources/              # Generic asset directory
│   ├── fonts/             # Type-specific subdirectory
│   ├── images/            # Images subdirectory
│   ├── templates/          # Template files
│   └── licenses/          # License files
└── README.md
```

### Resource Types You Can Bundle

**Fonts** (.ttf, .otf, .woff):
- TrueType fonts
- OpenType fonts
- Web fonts
- Variable fonts

**Images** (.png, .jpg, .svg):
- Logos
- Icons
- Illustrations
- Photos

**Templates** (.pptx, .xlsx, .docx):
- Document templates
- Slide templates
- Spreadsheet templates

**Data Files** (.json, .yaml, .csv):
- Configuration data
- Reference data
- Sample data

**Libraries**:
- Code libraries
- Utility functions
- Helper scripts

## Best Practices Demonstrated

1. **Resource Organization**
   - Separate directory for assets
   - Clear naming conventions
   - Logical grouping by type

2. **License Management**
   - Include LICENSE.txt with resources
   - Specify usage rights
   - Note attribution requirements

3. **File References**
   - Refer to resources in SKILL.md
   - Use relative paths
   - Describe resource contents

4. **Size Considerations**
   - Keep total skill size reasonable
   - Consider common vs. rare resources
   - Balance completeness with size

5. **Quality vs. Quantity**
   - Curated selection over comprehensive
   - Professional-grade resources
   - Well-tested and reliable

## Metadata Quality

| Field | Value | Status |
|-------|-------|--------|
| Name | canvas-design | ✓ 13 chars (well under 64) |
| Description | Curated typography and design assets... | ✓ 151 chars (under 200) |
| Version | Not specified | ⚠ Consider adding v1.0.0 |

## Resource Directory Analysis

**canvas-fonts/** breakdown:
- **83 items** total (82 fonts + 1 LICENSE)
- **File types**: .ttf, .otf, .txt
- **Size**: ~2.6 MB (compressed for distribution)
- **Font families**: 6 major families
- **Weights per family**: 4-6 variants

## Asset Management Guidelines

### When Bundling Resources

1. **Verify Licenses**
   - Check commercial use rights
   - Note attribution requirements
   - Document redistribution terms

2. **Optimize Assets**
   - Compress large files
   - Remove unnecessary variants
   - Use efficient formats

3. **Document Assets**
   - Create manifest/listing
   - Describe each resource
   - Provide usage examples

4. **Organize Logically**
   - Group by type or purpose
   - Use clear naming
   - Maintain directory depth < 3 levels

5. **Test Access**
   - Verify paths work correctly
   - Test on target platforms
   - Check permissions

## Alternative Applications

This pattern works well for:

- **Font Libraries** - Typography resources
- **Icon Sets** - Icon and symbol libraries
- **Template Collections** - Document/presentation templates
- **Code Snippets** - Reusable code fragments
- **Data Sets** - Reference data, lookup tables
- **Style Guides** - Brand assets, logos, colors
- **Media Assets** - Images, audio, video files

## Learning Outcomes

By studying this example, you'll learn:

1. How to bundle resources with skills
2. Managing licenses and usage rights
3. Organizing asset directories
4. Referencing resources in SKILL.md
5. Keeping skill size manageable
6. Balancing completeness with practicality
7. Documentation for bundled assets
8. Platform-specific resource usage

## Real-World Usage

**Before**: Scattered font files, unclear licenses
```
Designer needs: Professional font for presentation
Searches through: Downloads folder, Google Fonts, unclear licenses
Result: Risk of license violation, inconsistent selection
```

**After**: Curated fonts with clear licenses
```
Designer uses: "Use canvas-design to select presentation fonts"
Claude provides: Curated professional fonts, license info, usage guidance
Result: Compliant, professional typography
```

## Content Analysis

### SKILL.md Breakdown (350 lines)
- **Typography Fundamentals**: 80 lines
- **Design Asset Management**: 60 lines
- **Platform-Specific Guidance**: 120 lines
- **Best Practices**: 70 lines
- **Examples**: 20 lines

### Resource Directory
- **82 font files**: Various weights and styles
- **LICENSE.txt**: Font usage terms
- **Subdirectories**: Organized by font family

## Comparison with Other Skill Types

| Aspect | Resource-Based | Simple | Script-Based |
|--------|----------------|--------|-------------|
| **SKILL.md** | Medium (200-400) | Small (100-200) | Medium (200-400) |
| **Directories** | 2-3 | 1 | 3-5 |
| **Scripts** | 0 | 0 | 1-5 |
| **Resources** | Many (10+) | 0 | 0-5 |
| **File Size** | Large (MBs) | Small (KBs) | Small (KBs) |
| **Maintenance** | Medium | Low | High |
| **Distribution** | ZIP essential | Any | Any |

## Resource Best Practices

### DO ✓
- Bundle only what you need
- Include license files
- Compress large assets
- Document each resource
- Test on all platforms
- Keep paths relative

### DON'T ✗
- Include excessive assets
- Forget licenses
- Use absolute paths
- Duplicate resources
- Make directories too deep
- Include proprietary/illegal content

## Platform-Specific Notes

### Claude Desktop
- All resources accessible
- No size limits mentioned
- Manual ZIP upload

### Claude Code
- Filesystem access to resources
- Paths relative to skill root
- Automatic loading

### Claude API
- Resources must be in ZIP
- All files uploaded
- Ensure size reasonable

## File Reference

**Original Skill**: `../../claude_skills_example/example2-canvas-design/SKILL.md`
**Lines**: 350 (main) + 82 font files
**Resource Size**: ~2.6 MB
**Complexity**: Simple to Intermediate (resource-based)

---

**Related Examples**:
- `example_brand_guidelines_skill.md` - Compare with simple skill
- `example_complex_mcp_builder.md` - Compare with script-based complex skill
