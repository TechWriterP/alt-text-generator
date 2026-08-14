---
name: alt-text-generator
description: Generate concise, documentation-ready alt text from a project-local image path, an absolute local image path, an attached image, or an HTTP/HTTPS image URL, with optional page or topic context. Use for accessibility text for technical documentation images, including UI screenshots, diagrams, charts, product images, and decorative images; also use to review or improve existing alt text.
---

# Alt Text Generator

## Workflow

1. Resolve the image input using the rules in [references/contract.md](references/contract.md).
2. Inspect the actual image. Do not rely only on its file name, URL, or surrounding text.
3. Read any supplied page or topic context and identify the image's purpose in that context.
4. Classify the image as a UI screenshot, diagram, chart, product image, or decorative image.
5. Identify the minimum information a reader needs to receive the same value as a sighted reader.
6. Write one concise alt-text string using the rules in [references/contract.md](references/contract.md).
7. Check the result against the quality checklist before returning it.

For a local path, resolve a relative path from the project root and inspect the file with the available image-viewing capability. For an HTTP or HTTPS URL, fetch or open the image with the available web capability; if necessary, download it to a temporary working location before inspection. Do not add downloaded images to the project. Do not access non-HTTP URL schemes.

If the path does not exist, the URL is inaccessible, the response is not an image, or the image is unreadable, report the specific problem and request a usable input instead of guessing. If context is absent, describe only what is unambiguous in the image. If context materially changes the likely purpose, state the assumption in `note`.

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
