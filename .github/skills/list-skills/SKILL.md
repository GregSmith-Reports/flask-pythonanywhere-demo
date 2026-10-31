
# List Skills

## When to Use
- The user asks what skills are available, e.g. "what skills do I have", "list my skills", "show available skills".
- The user runs `/list-skills`.

## Procedure
1. Look at the full list of skills provided in your system/instructions context (each skill has a `name`, `description`, and `file` path) — this is the authoritative source, not just what's on disk.
2. Present them as a concise list: skill name, then a one-line summary of what it does (based on its description).
3. If the user asks for more detail on a specific skill, read that skill's file and summarize its "When to Use" and "Procedure" sections.
4. Do not fabricate skills that aren't present in the available list.

## Example
Input: "What skills do I have?"
Output:
- **pirate-speak** — Rewrite replies in a light pirate accent.
- **russian-speak** — Rewrite replies with a Russian accent/style.
- **list-skills** — List all available skills.
