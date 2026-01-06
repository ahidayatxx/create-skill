#!/usr/bin/env python3
"""
Package Skill - Package Claude Skills for distribution.

This module creates properly formatted ZIP files for skill distribution
across all Claude platforms (Desktop, Code, API).
"""

import argparse
import shutil
import zipfile
from pathlib import Path
from typing import Optional


class SkillPackager:
    """Package Claude Skills for distribution."""

    def __init__(self, skill_path: Path):
        """
        Initialize the packager.

        Args:
            skill_path: Path to skill directory
        """
        self.skill_path = Path(skill_path)
        self.skill_name = self.skill_path.name

    def validate(self) -> bool:
        """
        Validate skill structure before packaging.

        Returns:
            True if valid, False otherwise
        """
        # Check if skill path exists
        if not self.skill_path.exists():
            print(f"❌ Error: Skill path does not exist: {self.skill_path}")
            return False

        # Check for SKILL.md
        skill_md = self.skill_path / 'SKILL.md'
        if not skill_md.exists():
            print(f"❌ Error: SKILL.md not found in {self.skill_path}")
            return False

        # Validate SKILL.md has frontmatter
        with open(skill_md, 'r') as f:
            first_line = f.readline()
            if not first_line.strip().startswith('---'):
                print(f"❌ Error: SKILL.md missing YAML frontmatter")
                return False

        print("✓ Skill structure validated")
        return True

    def package(self, output_dir: Optional[Path] = None) -> Path:
        """
        Package skill as ZIP file.

        Args:
            output_dir: Output directory for ZIP file

        Returns:
            Path to created ZIP file
        """
        if not self.validate():
            raise ValueError("Skill validation failed")

        # Determine output path
        if output_dir is None:
            output_dir = self.skill_path.parent
        else:
            output_dir = Path(output_dir)

        zip_path = output_dir / f"{self.skill_name}.zip"

        # Create ZIP file
        print(f"Packaging {self.skill_name}...")

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in self.skill_path.rglob('*'):
                if file_path.is_file() and not file_path.name.startswith('.'):
                    # Calculate archive path (relative to skill directory)
                    arcname = f"{self.skill_name}/{file_path.relative_to(self.skill_path)}"
                    zipf.write(file_path, arcname)
                    print(f"  + {arcname}")

        print(f"\n✓ Created: {zip_path}")
        print(f"  Size: {zip_path.stat().st_size:,} bytes")

        return zip_path

    def package_with_install_instructions(self, output_dir: Optional[Path] = None) -> Path:
        """
        Package skill and create install instructions.

        Args:
            output_dir: Output directory for ZIP file

        Returns:
            Path to created ZIP file
        """
        zip_path = self.package(output_dir)

        # Create install instructions
        install_md = output_dir / f"{self.skill_name}-INSTALL.md"
        with open(install_md, 'w') as f:
            f.write(f"""# {self.skill_name} - Installation Instructions

## Package Contents

- `{self.skill_name}/` - Skill directory
  - `SKILL.md` - Skill metadata and instructions
  - Additional files based on skill complexity

## Installation Methods

### Claude Desktop (Recommended for most users)

1. Open Claude Desktop
2. Go to **Settings** → **Capabilities** → **Skills**
3. Click **Add Skill**
4. Select `{self.skill_name}.zip`
5. Confirm installation

The skill will be available immediately.

### Claude Code (For developers)

1. Extract the ZIP file:
   ```bash
   unzip {self.skill_name}.zip
   ```

2. Copy to skills directory:
   ```bash
   cp -r {self.skill_name}/ ~/.claude/skills/
   ```

3. Restart Claude Code

### Claude API (For programmatic access)

1. Use the `/v1/skills` endpoint:
   ```bash
   curl -X POST \\
     https://api.anthropic.com/v1/skills \\
     -H "x-api-key: YOUR_API_KEY" \\
     -F "skill=@{self.skill_name}.zip"
   ```

## Verification

After installation, verify the skill is available:

**In Claude Desktop/Code:**
- Start a new conversation
- Say: "Use {self.skill_name}"
- Claude should acknowledge the skill

## Usage

Invoke the skill by describing your needs:

```
Use {self.skill_name} to help me with...
```

## Troubleshooting

**Skill not appearing:**
- Verify SKILL.md has valid YAML frontmatter
- Check ZIP file contains skill folder at root
- Try reinstalling

**Scripts not running:**
- Verify shebang lines: `#!/usr/bin/env python3`
- Check file permissions
- Test scripts standalone

## Uninstallation

### Claude Desktop
1. Go to **Settings** → **Capabilities** → **Skills**
2. Find {self.skill_name}
3. Click **Remove**

### Claude Code
```bash
rm -rf ~/.claude/skills/{self.skill_name}
```

## Support

For issues or questions, refer to the skill documentation or
contact the skill maintainer.
""")

        print(f"\n✓ Created: {install_md}")
        return zip_path


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Package Claude Skills for distribution'
    )
    parser.add_argument(
        'skill_path',
        help='Path to skill directory'
    )
    parser.add_argument(
        '--output-dir',
        help='Output directory for ZIP file (default: same as skill)'
    )
    parser.add_argument(
        '--with-instructions',
        action='store_true',
        help='Create installation instructions file'
    )

    args = parser.parse_args()

    # Package skill
    packager = SkillPackager(args.skill_path)

    if args.with_instructions:
        packager.package_with_install_instructions(args.output_dir)
    else:
        packager.package(args.output_dir)


if __name__ == '__main__':
    main()
