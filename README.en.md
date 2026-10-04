# Long-form to Chinese Carousel Copy

![Long-form to carousel promo](assets/promo-1600x900.png)

Turn an original or licensed Chinese long-form article into a reader-friendly carousel brief: a cover hook, one focused point per page, and actionable image requirements. It helps local shop owners, fiction writers, and social-media creators reuse substantial content without inventing facts.

This is a Markdown-only skill. It has no API, browser, or image-rendering dependency.

## Input and output

Provide the full authorized article and a target audience. Optionally add platform, page count, voice, and conversion goal. The output is a 6–10-page copy brief with a cover hook, page copy, visual direction, a facts-vs-suggestions split, and a pre-publish check.

If the article, authorization, or audience is missing, the skill asks for it instead of fabricating content.

## Self-test

Run from this directory:

```bash
python3 scripts/self_test.py
```

It validates package structure and fixture expectations only; it does not claim to validate real writing behavior.

## Source and license

The scope was informed by the [carousel-writer entry in social-media-skills/skills](https://github.com/social-media-skills/skills/blob/main/skills/carousel-writer/SKILL.md). This repository's documentation, workflow, and examples are original. Licensed under [MIT](LICENSE).
