# Alt Text Generator

Alt Text Generator is a reusable Codex skill that creates concise, documentation-ready alt text for technical images. It is optimized for UI screenshots, diagrams, charts, product images, and decorative images, with an emphasis on clarity, accessibility, and useful context.

The skill can use optional page or topic context to describe why an image matters instead of listing every visible detail. It can also review and improve existing alt text.

## Supported image inputs

Provide one image in any of these forms:

- An image attached to the Codex request
- A path relative to the current project, such as `Images/Salesforce/example.webp`
- An absolute local path, such as `C:\docs\images\deployment-status.png`
- A publicly accessible `http://` or `https://` image URL

Relative paths are resolved from the project root. For an online image, the skill verifies that the URL returns an image and uses a temporary local copy only when needed for inspection. Temporary downloads are not added to the project.

## Clone and use the project-local skill

Clone the repository:

```powershell
git clone https://github.com/TechWriterP/alt-text-generator.git
cd alt-text-generator
```

Open the cloned folder as a project in Codex and start a new task. Codex discovers the skill from:

```text
.agents/skills/alt-text-generator/
```

Invoke it by name:

```text
Use $alt-text-generator for Images/Salesforce/aad36fccc6ccf3d23917a5ef33dc771f_kix.pyrvpa5gomzb.webp.
```

## Install the skill personally

A personal installation makes the skill available across your Codex projects.

Ask Codex:

```text
Install the alt-text-generator skill from:
https://github.com/TechWriterP/alt-text-generator/tree/main/.agents/skills/alt-text-generator
```

Alternatively, clone the repository and copy the skill folder in PowerShell:

```powershell
git clone https://github.com/TechWriterP/alt-text-generator.git

$source = ".\alt-text-generator\.agents\skills\alt-text-generator"
$destination = "$env:USERPROFILE\.codex\skills\alt-text-generator"

New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse -Force $source $destination
```

If a skill with the same name is already installed, remove or rename the existing installation before copying the new version. Start a new Codex task after installation so the skill is available.

## Example prompts

### UI screenshot from the project

```text
Use $alt-text-generator for Images/deployment-status.png.

Page context: This image appears in a procedure for verifying that a production deployment succeeded.
Maximum length: 150 characters.
```

### Chart from an online URL

```text
Use $alt-text-generator for:
https://example.com/images/api-performance.png

Topic: API performance after the June optimization.
Focus on the main trend rather than every data point.
```

### Product image from an absolute path

```text
Use $alt-text-generator for C:\docs\images\router-rear.png.

Topic: Show readers where to find the router reset control.
```

### Improve existing alt text

```text
Use $alt-text-generator to improve the alt text for Images/sign-in-error.png.

Existing alt text: Screenshot of a dialog box on a computer screen.
Page context: Troubleshoot an invalid password during sign-in.
```

## Example output

By default, the skill returns YAML:

```yaml
alt_text: "Production deployment for version 2.4.1 has a Success status"
classification: "ui-screenshot"
source: "Images/deployment-status.png"
```

For a decorative image, it returns empty alt text and explains why:

```yaml
alt_text: ""
classification: "decorative"
note: "The image adds no information to the page."
source: "Images/decorative-wave.png"
```

## Limitations

- Generated alt text should be reviewed by a person familiar with the page and its audience.
- Missing context can produce a visually accurate description that does not communicate the image's purpose.
- The skill does not infer details that are not visible or supported by supplied context.
- Dense charts and complex diagrams may need a nearby data table, caption, or long description in addition to alt text.
- Text in small, blurry, cropped, or low-resolution images might not be readable.
- Private, authenticated, expired, or access-restricted URLs might not be retrievable.
- A URL that returns a web page instead of an image is rejected.
- Only `http://` and `https://` URLs are supported for remote images.

## Privacy considerations

- Review images before sharing them with Codex or committing them to a public repository.
- Remove or obscure passwords, access tokens, customer information, email addresses, internal URLs, account identifiers, and other sensitive data.
- Treat pre-signed and token-bearing image URLs as secrets. Do not place them in prompts, documentation, logs, or commits unless disclosure is explicitly authorized.
- Confirm that you have permission to download, process, and redistribute online images.
- Do not commit temporary copies of remote images.
- Remember that a public GitHub repository makes committed example images available to anyone.

## Repository structure

```text
alt-text-generator/
|-- README.md
|-- Images/
`-- .agents/
    `-- skills/
        `-- alt-text-generator/
            |-- SKILL.md
            |-- agents/
            |   `-- openai.yaml
            `-- references/
                |-- contract.md
                `-- test-cases.md
```

## Learn more

OpenAI describes skills as reusable workflows that Codex can keep available for repeated work. See the [Codex use cases](https://developers.openai.com/codex/use-cases).
