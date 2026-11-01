"""
AI influencer content planner (template-based, no API key required).

Generates a batch of social media post ideas for an AI character:
  - an image prompt (paste into your image-gen tool, e.g. Higgsfield/Midjourney/
    Stable Diffusion, to generate the actual visual)
  - a caption
  - hashtags

This does NOT post anything automatically — output is meant for manual review
and manual upload to Instagram.

Usage:
    python content_generator.py --days 7
    python content_generator.py --days 7 --out content_plan.json
"""

import argparse
import json
import random
from datetime import date, timedelta
from pathlib import Path

ACTIVITIES = [
    "napping in a sunbeam",
    "knocking a pen off a desk",
    "staring judgmentally out a window",
    "curled up in a cardboard box",
    "chasing a laser dot",
    "perched on a windowsill at sunset",
    "wearing a tiny knitted sweater",
    "investigating an open suitcase",
    "sitting inside a kitchen cabinet",
    "watching rain from behind glass",
]

MOODS = ["cozy", "mischievous", "dramatic", "sleepy", "curious", "majestic"]

LOCATIONS = [
    "a sunlit living room",
    "a cluttered writer's desk",
    "a cafe windowsill",
    "a cozy blanket fort",
    "a minimalist Scandinavian apartment",
    "a rainy city window",
]

CAPTION_TEMPLATES = [
    "{name} {activity} today. {mood} energy only. {hashtags}",
    "Just {name}, {activity}. No further questions. {hashtags}",
    "{mood} o'clock. {name} is {activity}. {hashtags}",
    "POV: {name} caught {activity} again. {hashtags}",
    "{name}'s daily report: {activity}. Rating: 10/10 {mood}. {hashtags}",
]


def load_persona(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_image_prompt(persona: dict) -> str:
    activity = random.choice(ACTIVITIES)
    location = random.choice(LOCATIONS)
    mood = random.choice(MOODS)
    return (
        f"A photorealistic cat named {persona['name']}, {activity}, in {location}, "
        f"{mood} mood, soft natural lighting, high detail, consistent character design"
    )


def generate_caption(persona: dict) -> str:
    activity = random.choice(ACTIVITIES)
    mood = random.choice(MOODS)
    hashtags = " ".join(persona["base_hashtags"])
    template = random.choice(CAPTION_TEMPLATES)
    return template.format(name=persona["name"], activity=activity, mood=mood, hashtags=hashtags)


def generate_content_plan(persona: dict, days: int) -> list[dict]:
    plan = []
    start = date.today()
    for i in range(days):
        plan.append(
            {
                "date": str(start + timedelta(days=i)),
                "image_prompt": generate_image_prompt(persona),
                "caption": generate_caption(persona),
            }
        )
    return plan


def main():
    parser = argparse.ArgumentParser(description="Generate an AI influencer content plan.")
    parser.add_argument("--days", type=int, default=7, help="Number of posts to generate")
    parser.add_argument("--persona", default="persona.json", help="Path to persona config")
    parser.add_argument("--out", default="content_plan.json", help="Output file path")
    args = parser.parse_args()

    base_dir = Path(__file__).parent
    persona = load_persona(base_dir / args.persona)
    plan = generate_content_plan(persona, args.days)

    out_path = base_dir / args.out
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2)

    print(f"Generated {len(plan)} post ideas -> {out_path}")
    for post in plan:
        print(f"\n{post['date']}")
        print(f"  Image prompt: {post['image_prompt']}")
        print(f"  Caption: {post['caption']}")


if __name__ == "__main__":
    main()
