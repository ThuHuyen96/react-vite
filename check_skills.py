import os
import re
import json

skills_dir = '.agent/skills'
skills = [d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d)) and d != '_template']

report = ""

for skill in sorted(skills):
    skill_path = os.path.join(skills_dir, skill)
    skill_md = os.path.join(skill_path, 'SKILL.md')
    metadata_json = os.path.join(skill_path, 'metadata.json')
    
    if not os.path.exists(skill_md):
        continue
        
    with open(skill_md, 'r') as f:
        content = f.read()
        
    lines = content.split('\n')
    words = len(re.findall(r'\w+', content))
    
    issues = []
    
    # Check frontmatter
    if content.startswith('---'):
        end_idx = content.find('---', 3)
        if end_idx != -1:
            frontmatter = content[3:end_idx]
            if 'name:' not in frontmatter:
                issues.append("Missing `name` in frontmatter")
            if 'description:' not in frontmatter:
                issues.append("Missing `description` in frontmatter")
            if '\ndependencies:' in frontmatter:
                issues.append("Uses `dependencies` instead of `depends_on` in frontmatter")
        else:
            issues.append("Malformed frontmatter")
    else:
        issues.append("Missing frontmatter")
        
    # Check references
    if '@skill:' in content:
        issues.append("Contains cross-skill reference `@skill:`")
    if re.search(r'(?i)#+\s+See Also', content):
        issues.append("Contains `See Also` section")
    if re.search(r'(?i)#+\s+Related Skills', content):
        issues.append("Contains `Related Skills` section")
        
    # Check metadata.json
    if not os.path.exists(metadata_json):
        issues.append("Missing `metadata.json`")
    else:
        try:
            with open(metadata_json, 'r') as mf:
                data = json.load(mf)
                if 'version' not in data:
                    issues.append("`metadata.json` missing `version`")
                if 'references' not in data:
                    issues.append("`metadata.json` missing `references`")
        except Exception as e:
            issues.append(f"Invalid `metadata.json`: {e}")
            
    # Check framing
    if re.search(r'(?i)#+\s+NEVER', content) or re.search(r'\nNEVER:', content):
        issues.append("Contains `NEVER` section instead of Anti-Patterns table")
        
    # Check examples
    if '|' not in content and '```' not in content:
        issues.append("Lacks ✅/❌ tables or code snippets")
        
    # Check size
    if words > 2000:
        issues.append(f"Too long: {words} words (limit ~2000)")
        
    status = "✅ PASS" if not issues else "⚠️ NEEDS WORK" if len(issues) <= 2 else "❌ FAIL"
    
    report += f"### {skill}\n"
    report += f"- **Size**: {len(lines)} lines / {len(content)} chars ({words} words)\n"
    report += f"- **Verdict**: {status}\n"
    if issues:
        report += f"- **Issues**: {', '.join(issues)}\n"
        report += "- **Action**: Update SKILL.md to fix listed issues.\n"
    else:
        report += "- **Issues**: None found automatically.\n"
        report += "- **Action**: Looks good.\n"
    report += "\n"

print(report)
