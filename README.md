# Technical Documentation

This repository contains comprehensive technical documentation for various in-depth projects, built using [MkDocs](https://www.mkdocs.org/) with the [Material theme](https://squidfunk.github.io/mkdocs-material/).

## Projects

- **Jeep LJ Cummins R2.8 Build** - Complete electrical system documentation for engine swap with dual battery system
- **Nissan NV 3500 Van Build** - 12V accessory electrical system: dual AGM batteries, four switch panels, and Starlink on a DC-fed Advanced Power Supply

## Setup

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
# Install MkDocs and Material theme
pip3 install mkdocs mkdocs-material
```

### Local Development

```bash
# Serve the documentation locally with live reload
mkdocs serve

# Or use the full path if mkdocs is not in PATH
/Users/seobrien/Library/Python/3.9/bin/mkdocs serve
```

The documentation will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Building

```bash
# Build static site to site/ directory
mkdocs build

# Or use the full path
/Users/seobrien/Library/Python/3.9/bin/mkdocs build
```

## Project Structure

```
.
├── mkdocs.yml              # MkDocs configuration
├── docs/                   # Documentation source files
│   ├── index.md           # Home page
│   └── jeep_lj/           # Jeep LJ project documentation
│       ├── index.md       # Project overview
│       ├── 01-power-generation.md
│       ├── 02-front-battery-distribution.md
│       ├── 03-rear-battery-distribution.md
│       ├── 04-engine-systems.md
│       ├── 05-auxiliary-systems.md
│       ├── 06-cabin-body-control.md
│       ├── 07-cabin-lighting-accessories.md
│       ├── 08-communication-audio.md
│       ├── 09-cargo-exterior.md
│       ├── 10-wire-routing.md
│       └── 11-project-management.md
└── site/                   # Generated static site (not in git)
```

## Adding New Projects

1. Create a new directory under `docs/` (e.g., `docs/new_project/`)
2. Add an `index.md` overview page
3. Create section files as needed
4. Update `mkdocs.yml` navigation to include the new project
5. Run `mkdocs serve` to preview

## Features

- **Material Design** - Clean, responsive design
- **Dark/Light Mode** - Automatic theme switching
- **Search** - Full-text search across all documentation
- **Navigation** - Hierarchical navigation with sections and tabs
- **Code Highlighting** - Syntax highlighting for code blocks
- **Tables** - Full markdown table support
- **Admonitions** - Info, warning, and note callout boxes

## Documentation Best Practices

- Use clear, descriptive headings (H1-H4)
- Include tables of contents for long pages
- Use admonitions for important notes:
  ```markdown
  !!! info "Title"
      Content here

  !!! warning "Title"
      Warning content
  ```
- Cross-reference between pages using relative links:
  ```markdown
  [Link text](../other-section/page.md)
  ```

## Contributing

When adding or updating documentation:

1. Edit the markdown files in `docs/`
2. Test locally with `mkdocs serve`
3. Verify all links work
4. Check formatting and readability
5. Commit changes to git

## License

Documentation for personal projects.
