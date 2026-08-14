---
name: alt-text-generator
description: Generate concise, documentation-ready alt text from an image and optional page or topic context. Use for accessibility text for technical documentation images, including UI screenshots, diagrams, charts, product images, and decorative images; also use to review or improve existing alt text.
---

# Alt Text Generator

## Workflow

1. Inspect the image itself. Do not rely only on its file name or surrounding text.
2. Read any supplied page or topic context and identify the image's purpose in that context.
3. Classify the image as a UI screenshot, diagram, chart, product image, or decorative image.
4. Identify the minimum information a reader needs to receive the same value as a sighted reader.
5. Write one concise alt-text string using the rules in [references/contract.md](references/contract.md).
6. Check the result against the quality checklist before returning it.

If the image is missing or unreadable, request a usable image instead of guessing. If context is absent, describe only what is unambiguous in the image. If context materially changes the likely purpose, state the assumption in `note`.

## Image-specific guidance

- **UI screenshot:** Name the product or page only when identifiable and useful. Describe the relevant control, state, value, or result. Ignore incidental chrome.
- **Diagram:** Describe the main relationship, direction, sequence, or hierarchy. Do not inventory every shape.
- **Chart:** State the chart type only when helpful, then give the main trend, comparison, or notable value. Do not reproduce every data point.
- **Product image:** Identify the product and the feature, orientation, connector, or physical detail relevant to the topic. Avoid marketing language.
- **Decorative image:** Return empty alt text when the image adds no information and the publishing format supports an empty alt attribute.

## Output

Return the YAML shape defined in [references/contract.md](references/contract.md). Return only those fields unless the user asks for an explanation or alternatives.

## Quality check

Before responding, verify that the alt text:

- communicates purpose, not every visible detail;
- is accurate and does not infer unsupported meaning;
- is concise, usually one sentence and preferably no more than 150 characters;
- begins with the most useful information;
- uses plain, direct, sentence-style language;
- avoids "image of," "picture of," "screenshot of," file names, and redundant surrounding text;
- expands or avoids unfamiliar abbreviations when practical;
- uses punctuation only where it improves comprehension;
- contains no markdown, HTML, quotation marks, or trailing period unless requested by the target system.

Read [references/test-cases.md](references/test-cases.md) when evaluating, teaching, or extending this skill.
