# Elementor Design Library

A comprehensive collection of **436 reusable Elementor templates** organized across three axes:

- **86 Archetype Templates** — section-purpose patterns (hero, CTA, features, pricing, etc.)
- **80 Philosophy Editions** — visual style interpretations (Swiss, Brutalist, Luxury, etc.)
- **160 Real-World Brand Editions** — design tokens from 54 top tech brands (Stripe, Linear, Vercel, etc.)
- **3 Index Pages** — browsable library indexes

## Structure

```
templates/
├── archetypes/     # 86 base section templates
├── philosophy/     # 80 design philosophy editions  
├── brands/         # 270 brand-study editions (54 brands × 5 sections)
└── index-pages/    # Library index/browsing pages
scripts/            # Import/export/build scripts
docs/               # Catalog, playbooks, state docs
```

## Usage

Each template is a standalone JSON file containing:
- `page_id` — source page ID
- `category` — archetype/philosophy/brand classification
- `elementor_data` — full Elementor structure (importable via MCP `import-template`)
- `exported_at` — timestamp

### Import into WordPress

```bash
# Via Elementor MCP
mcp_call('elementor-mcp-import-template', {
    "post_id": TARGET_PAGE_ID,
    "template_json": template_data['elementor_data']
})
```

## Source

Built on staging at `willinstructions-new.affinitydns.uk` using the Elementor MCP plugin.

