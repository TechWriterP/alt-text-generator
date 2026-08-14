# Input and output contract

## Input

Required:

- `image`: Exactly one of the following:
  - an image attached to the request;
  - a relative path to an image in the current project;
  - an absolute local image path;
  - a direct or publicly accessible `http://` or `https://` image URL.

Optional:

- `page_context`: The nearby heading, paragraph, procedure step, or reason the image appears.
- `topic`: A short description of the documentation topic or user task.
- `existing_alt_text`: Alt text to review or revise.
- `max_characters`: A publishing limit. Default target: 150 characters.
- `output_format`: `yaml` by default; use `plain` only when requested.

Treat context as guidance, not as evidence of details that are not visible in the image.

## Image input resolution

1. Prefer an explicitly supplied image over any image inferred from context.
2. Resolve a relative local path from the project root, not from the skill folder.
3. Verify that a local file exists and is a supported image before inspecting it.
4. For an HTTP or HTTPS URL, follow ordinary redirects and verify that the retrieved content is an image.
5. If URL inspection requires a local copy, store it only in a temporary working location and do not commit it.
6. Reject unsupported schemes such as `file:`, `ftp:`, or `data:` unless the image is already attached through the client.
7. Never guess from a file name, URL slug, page title, or unavailable preview.

## Output

Default YAML:

```yaml
alt_text: "Concise alt text"
classification: "ui-screenshot | diagram | chart | product-image | decorative"
note: "Optional assumption, uncertainty, or empty-alt rationale"
source: "Optional normalized local path or URL"
```

Omit `note` when it adds no value. Include `source` when the user supplied a path or URL; omit it for an attachment. For a decorative image, return `alt_text: ""` and explain the decision briefly in `note`.

If `output_format` is `plain`, return only the alt-text string. Do not wrap it in quotation marks.

## Quality rubric

Accept an answer only when all applicable checks pass:

1. **Equivalent:** It conveys the image's useful information or function.
2. **Contextual:** It focuses on why the image is present on this page.
3. **Accurate:** Every stated detail is visible or clearly supported by context.
4. **Concise:** It removes decorative, incidental, and repeated details.
5. **Clear:** It uses familiar words, active phrasing, and sentence-style capitalization.
6. **Nonredundant:** It does not announce the medium or repeat the caption verbatim.
7. **Accessible:** It does not depend on color alone; pair color with a label, position, shape, or value when color matters.

If the full meaning cannot fit within the character limit, use alt text for the image's purpose and recommend a nearby caption, data table, or long description in `note`.
