#!/usr/bin/env python3
"""
Skill Validator - Validate Claude Skills for correctness.

This module validates skill structure, metadata, and packaging
to ensure skills meet Claude's requirements.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


class SkillValidator:
    """Validate Claude Skills for compliance."""

    def __init__(self, skill_path: Path):
        """
        Initialize the validator.

        Args:
            skill_path: Path to skill directory
        """
        self.skill_path = Path(skill_path)
        self.issues = []
        self.warnings = []
        self.passed = 0

    def validate(self) -> bool:
        """
        Perform full validation.

        Returns:
            True if all validations pass, False otherwise
        """
        print(f"Validating skill: {self.skill_path.name}\n")

        # Run all validations
        self._validate_structure()
        self._validate_skill_md()
        self._validate_metadata()
        self._validate_scripts()
        self._validate_packaging()

        # Print results
        self._print_results()

        return len(self.issues) == 0

    def _validate_structure(self):
        """Validate directory structure."""
        print("Checking structure...")

        required_files = ['SKILL.md']
        for file_name in required_files:
            file_path = self.skill_path / file_name
            if file_path.exists():
                self.passed += 1
                print(f"  ✓ Found {file_name}")
            else:
                self.issues.append(f"Missing required file: {file_name}")
                print(f"  ✗ Missing {file_name}")

        # Check for common optional files
        optional_files = ['README.md', 'LICENSE']
        for file_name in optional_files:
            file_path = self.skill_path / file_name
            if file_path.exists():
                print(f"  ✓ Found {file_name} (recommended)")

    def _validate_skill_md(self):
        """Validate SKILL.md format."""
        print("\nChecking SKILL.md...")

        skill_md = self.skill_path / 'SKILL.md'
        if not skill_md.exists():
            return

        with open(skill_md, 'r') as f:
            content = f.read()
            lines = content.split('\n')

        # Check for YAML frontmatter
        if not content.startswith('---'):
            self.issues.append("SKILL.md missing YAML frontmatter (must start with ---)")
            print("  ✗ Missing YAML frontmatter")
            return

        print("  ✓ YAML frontmatter present")

        # Extract frontmatter
        frontmatter_end = content.find('---', 4)
        if frontmatter_end == -1:
            self.issues.append("SKILL.md YAML frontmatter not closed (missing closing ---)")
            print("  ✗ Frontmatter not closed")
            return

        frontmatter = content[4:frontmatter_end]

        # Check for required fields
        required_fields = ['name', 'description']
        for field in required_fields:
            if field in frontmatter.lower():
                print(f"  ✓ Has {field} field")
            else:
                self.issues.append(f"SKILL.md missing required field: {field}")
                print(f"  ✗ Missing {field} field")

    def _validate_metadata(self):
        """Validate metadata field values."""
        print("\nChecking metadata...")

        skill_md = self.skill_path / 'SKILL.md'
        if not skill_md.exists():
            return

        with open(skill_md, 'r') as f:
            content = f.read()

        # Extract and validate name
        name_match = re.search(r'name:\s*(.+)', content)
        if name_match:
            name = name_match.group(1).strip()
            if len(name) <= 64:
                print(f"  ✓ Name length OK: {len(name)}/64 chars")
                self.passed += 1
            else:
                self.issues.append(f"Name exceeds 64 characters: {len(name)}")
                print(f"  ✗ Name too long: {len(name)}/64 chars")

            # Check for kebab-case
            if re.match(r'^[a-z0-9-]+$', name):
                print(f"  ✓ Name uses kebab-case")
                self.passed += 1
            else:
                self.warnings.append("Name should use kebab-case (lowercase with hyphens)")
                print(f"  ⚠ Name should use kebab-case")
        else:
            self.issues.append("Name field not found in frontmatter")
            print("  ✗ Name field not found")

        # Extract and validate description
        desc_match = re.search(r'description:\s*(.+)', content)
        if desc_match:
            desc = desc_match.group(1).strip()
            if len(desc) <= 200:
                print(f"  ✓ Description length OK: {len(desc)}/200 chars")
                self.passed += 1
            else:
                self.issues.append(f"Description exceeds 200 characters: {len(desc)}")
                print(f"  ✗ Description too long: {len(desc)}/200 chars")

            # Check description quality
            if len(desc) >= 20:
                print(f"  ✓ Description descriptive enough")
                self.passed += 1
            else:
                self.warnings.append("Description should be more descriptive (>20 chars)")
                print(f"  ⚠ Description too short")
        else:
            self.issues.append("Description field not found in frontmatter")
            print("  ✗ Description field not found")

        # Check for version field
        if re.search(r'version:', content):
            print(f"  ✓ Has version field")
        else:
            self.warnings.append("Version field not found (recommended)")
            print(f"  ⚠ Missing version field (recommended)")

    def _validate_scripts(self):
        """Validate script files."""
        print("\nChecking scripts...")

        scripts_dir = self.skill_path / 'scripts'
        if not scripts_dir.exists():
            print("  (No scripts directory - OK for simple skills)")
            return

        # Check Python scripts
        for script in scripts_dir.glob('*.py'):
            if script.name == '__init__.py':
                continue

            print(f"  Checking {script.name}...")

            # Check for shebang
            with open(script, 'r') as f:
                first_line = f.readline()
                if first_line.startswith('#!'):
                    print(f"    ✓ Has shebang: {first_line.strip()}")
                    self.passed += 1
                else:
                    self.warnings.append(f"{script.name} missing shebang (recommended for executable scripts)")
                    print(f"    ⚠ Missing shebang")

            # Check for executable permission
            if script.stat().st_mode & 0o111:
                print(f"    ✓ Executable permission set")
                self.passed += 1
            else:
                self.warnings.append(f"{script.name} not executable (run: chmod +x {script.name})")
                print(f"    ⚠ Not executable")

    def _validate_packaging(self):
        """Validate packaging readiness."""
        print("\nChecking packaging...")

        # Check for unwanted files
        unwanted_patterns = ['.pyc', '__pycache__', '.DS_Store', '.git']
        for pattern in unwanted_patterns:
            matches = list(self.skill_path.rglob(pattern))
            if matches:
                self.warnings.append(f"Found {pattern} files (should be excluded from ZIP)")
                print(f"  ⚠ Found {pattern} files")
            else:
                print(f"  ✓ No {pattern} files")

        # Check for README
        readme = self.skill_path / 'README.md'
        if readme.exists():
            print(f"  ✓ Has README.md (recommended)")
        else:
            self.warnings.append("Missing README.md (recommended)")
            print(f"  ⚠ Missing README.md")

    def _print_results(self):
        """Print validation results."""
        print(f"\n{'='*60}")
        print(f"Validation Results")
        print(f"{'='*60}")
        print(f"Passed: {self.passed}")
        print(f"Warnings: {len(self.warnings)}")
        print(f"Errors: {len(self.issues)}")

        if self.warnings:
            print(f"\n⚠ Warnings:")
            for warning in self.warnings:
                print(f"  - {warning}")

        if self.issues:
            print(f"\n✗ Errors:")
            for issue in self.issues:
                print(f"  - {issue}")
            print(f"\n❌ Validation FAILED")
            sys.exit(1)
        else:
            print(f"\n✅ Validation PASSED")
            print(f"\nSkill is ready for packaging!")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Validate Claude Skills for compliance'
    )
    parser.add_argument(
        'skill_path',
        help='Path to skill directory'
    )

    args = parser.parse_args()

    # Validate skill
    validator = SkillValidator(args.skill_path)
    validator.validate()


if __name__ == '__main__':
    main()
