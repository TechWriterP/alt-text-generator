<div align="center">

# 🖼️ Alt Text Generator

### Clear, concise alt text for technical documentation

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-6C47FF?style=for-the-badge)](https://developers.openai.com/codex/use-cases)
[![Accessibility](https://img.shields.io/badge/Accessibility-First-0078D4?style=for-the-badge)](#-quality-principles)
[![Inputs](https://img.shields.io/badge/Inputs-Local%20%7C%20URL-00A36C?style=for-the-badge)](#-supported-image-inputs)
[![License](https://img.shields.io/badge/License-Not%20yet%20added-F59E0B?style=for-the-badge)](#)

Generate documentation-ready alt text for UI screenshots, diagrams, charts, product images, and decorative visuals.

[Get started](#-quick-start) · [Install](#-personal-installation) · [Examples](#-example-prompts) · [Privacy](#-privacy-and-security)

</div>

---

## ✨ What this skill does

Alt Text Generator is a reusable Codex skill that examines an image and produces concise alt text focused on the image's purpose in technical documentation.

| Capability | What it provides |
|---|---|
| 🖥️ UI screenshots | Relevant controls, states, values, and results |
| 🔀 Diagrams | Important relationships, sequences, and flows |
| 📊 Charts | Key trends, comparisons, and notable values |
| 📦 Product images | Task-relevant features, orientation, and physical details |
| ✨ Decorative images | Empty alt text when the image adds no information |
| ✏️ Alt-text review | Clearer replacements for vague or redundant descriptions |

Optional page or topic context helps the skill explain why the image matters instead of inventorying every visible detail.

> [!TIP]
> Include the nearby heading, procedure step, or reader goal. Context usually produces more useful alt text.

## 📥 Supported image inputs

Provide one image in any of these forms:

| Input | Example |
|---|---|
| Attached image | Attach an image directly to the Codex request |
| Project-relative path | `docs/images/deployment-status.png` |
| Absolute local path | `C:\docs\images\router-rear.png` |
| Public image URL | `https://example.com/images/chart.png` |

Relative paths resolve from the project root. For an online image, the skill verifies that the URL returns an image. If a temporary download is needed for inspection, it is not added to the project.

## 🚀 Quick start

### 1. Clone the repository

```powershell
git clone https://github.com/TechWriterP/alt-text-generator.git
cd alt-text-generator
```

### 2. Open the project in Codex

Start a new task from the cloned folder. Codex discovers the project-local skill at:

```text
.agents/skills/alt-text-generator/
```

### 3. Generate alt text

```text
Use $alt-text-generator for docs/images/deployment-status.png.

Page context: Verify that the production deployment succeeded.
Maximum length: 150 characters.
```

## 👤 Personal installation

A personal installation makes the skill available across your Codex projects.

Ask Codex:

```text
Install the alt-text-generator skill from:
https://github.com/TechWriterP/alt-text-generator/tree/main/.agents/skills/alt-text-generator
```

Or install it manually with PowerShell:

```powershell
git clone https://github.com/TechWriterP/alt-text-generator.git

$source = ".\alt-text-generator\.agents\skills\alt-text-generator"
$destination = "$env:USERPROFILE\.codex\skills\alt-text-generator"

New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse -Force $source $destination
```

> [!NOTE]
> If a skill with the same name is already installed, remove or rename it before copying the new version. Start a new Codex task after installation.

## 💬 Example prompts

<details open>
<summary><strong>UI screenshot from the project</strong></summary>

```text
Use $alt-text-generator for docs/images/deployment-status.png.

Page context: This image appears in a procedure for verifying that a production deployment succeeded.
Maximum length: 150 characters.
```

</details>

<details>
<summary><strong>Chart from an online URL</strong></summary>

```text
Use $alt-text-generator for:
https://example.com/images/api-performance.png

Topic: API performance after the June optimization.
Focus on the main trend rather than every data point.
```

</details>

<details>
<summary><strong>Product image from an absolute path</strong></summary>

```text
Use $alt-text-generator for C:\docs\images\router-rear.png.

Topic: Show readers where to find the router reset control.
```

</details>

<details>
<summary><strong>Improve existing alt text</strong></summary>

```text
Use $alt-text-generator to improve the alt text for docs/images/sign-in-error.png.

Existing alt text: Screenshot of a dialog box on a computer screen.
Page context: Troubleshoot an invalid password during sign-in.
```

</details>

## ✅ Example output

```yaml
alt_text: "Production deployment for version 2.4.1 has a Success status"
classification: "ui-screenshot"
source: "docs/images/deployment-status.png"
```

For a decorative image:

```yaml
alt_text: ""
classification: "decorative"
note: "The image adds no information to the page."
source: "docs/images/decorative-wave.png"
```

## ♿ Quality principles

The skill aims to produce alt text that is:

- **Purposeful:** Communicates why the image matters on the page
- **Concise:** Usually one sentence and preferably no more than 150 characters
- **Accurate:** Avoids unsupported assumptions
- **Direct:** Leads with the most useful information
- **Nonredundant:** Avoids phrases such as “image of” and “screenshot of”
- **Accessible:** Does not depend on color alone to communicate meaning

## ⚠️ Limitations

- Human review is recommended, especially for published or regulated content.
- Missing context can produce a visually accurate but less useful description.
- Dense charts and complex diagrams may also require a data table, caption, or long description.
- Small, blurry, cropped, or low-resolution text might not be readable.
- Private, authenticated, expired, or access-restricted URLs might not be retrievable.
- Remote inputs support only `http://` and `https://` URLs.
- URLs that return web pages instead of image content are rejected.

## 🔐 Privacy and security

> [!WARNING]
> Review every image before processing it or committing it to a public repository.

- Remove or obscure passwords, tokens, customer data, email addresses, internal URLs, and account identifiers.
- Treat pre-signed or token-bearing image URLs as secrets.
- Confirm that you have permission to download, process, and redistribute online images.
- Do not commit temporary downloads of remote images.
- Remember that files committed to a public GitHub repository are available to anyone.

## 📁 Repository structure

```text
alt-text-generator/
├── README.md
└── .agents/
    └── skills/
        └── alt-text-generator/
            ├── SKILL.md
            ├── agents/
            │   └── openai.yaml
            └── references/
                ├── contract.md
                └── test-cases.md
```

---

<div align="center">

Built for clearer, more accessible technical documentation.

[View the skill](.agents/skills/alt-text-generator/SKILL.md) · [Report an issue](https://github.com/TechWriterP/alt-text-generator/issues)

</div>
