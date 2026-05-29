# Elementor Design Library — State & Resumption Guide

**Last updated:** 2026-05-29  
**Staging site:** https://willinstructions-new.affinitydns.uk  
**MCP endpoint:** `/wp-json/mcp/elementor-mcp-server`  
**MCP session ID:** stored at `/tmp/mcp_sid.txt` (regenerate if expired)

---

## Library Overview

| Collection | Editions | Page IDs | Status |
|---|---|---|---|
| Original Archetypes | 86 | 314–554 | ✅ Complete |
| Design Philosophy Series 1 | 40 | 1253–1491 | ✅ Complete |
| Design Philosophy Series 2 | 40 | 1497–1735 | ✅ Complete |
| Real-World Brands Batch 1 | 80 | 1741–2215 | ✅ Complete |
| Real-World Brands Batch 2 | 80 | 2225–2699 | ✅ Complete |
| Real-World Brands Batch 3 | 110 | 2705–3359 | ✅ Complete |
| **Grand Total** | **436** | | **ALL 54/54 BRANDS BUILT** |

### Index Pages
- **Archetype Library (86):** `/design-library/` (page 737)
- **Philosophy Library (80):** `/design-philosophy-library/` (page 1737)
- **Complete Library Index:** `/complete-design-library/` (page 2221) — **needs rebuild** to include batches 2–3 (currently only covers batch 1)

---

## What's Been Built

### 1. Original Archetypes (86 editions)
24 section types × multiple editions each. Pages 314–554, Templates 368–672.
See `archetype-catalog.md` for full breakdown.

### 2. Design Philosophy Series (80 editions)
**Series 1 (8 philosophies):** Swiss, Editorial, Glassmorphism, Brutalist, Luxury, Playful, Corporate, Retro  
**Series 2 (8 philosophies):** Art Deco, Neo-Minimal, Organic, Cyberpunk, Material, Grunge, Mid-Century, Isometric

Each philosophy: hero + features + CTA + testimonial + footer = 5 sections.

### 3. Real-World Brand Studies (270 editions, all 54/54 brands)

**Batch 1 (16 brands, DONE):**
Stripe, Linear, Vercel, Apple, Notion, Framer, Spotify, Airbnb, SpaceX, NVIDIA, Coinbase, BMW, Figma, Uber, IBM, Zapier

**Batch 2 (16 brands, DONE):**
Claude, Cursor, ElevenLabs, Supabase, Revolut, Wise, Airtable, MongoDB, PostHog, Miro, Sentry, Intercom, Pinterest, Webflow, RunwayML, Clay

**Batch 3 (22 brands, DONE):**
OpenCode, Cohere, Minimax, Mistral AI, Ollama, Replicate, Together AI, VoltAgent, xAI, Composio, Expo, Lovable, Mintlify, Raycast, Resend, Warp, HashiCorp, Sanity, Kraken, Cal.com, Superhuman, ClickHouse

---

## Batch 3 Visual Spot-Checks

| Brand | PID | Key Checks | Result |
|---|---|---|---|
| ClickHouse | 3335 | Black bg, neon yellow #FAFF69 button | ✅ |
| Ollama | 2855 | White bg, black text, black button, 0px radius | ✅ |

---

## How to Continue Expanding

### No more brand templates remain
All 54 templates from `popular-web-designs` skill have been built. Future expansion options:

1. **Rebuild the Complete Library Index page** (PID 2221) to include all 436 editions across all 6 collections
2. **Add more archetype sections** — countdown, banner, gallery, off-canvas-menu, breadcrumb, page-title-banner (catalogued but only some editions built)
3. **Assemble full-page compositions** — combine hero + features + CTA + testimonial + footer from one philosophy into a single-page demo
4. **Industry-specific full sites** — use `industry-playbooks.md` to assemble 5-page sites for legal, restaurant, SaaS, etc.
5. **Responsive variants** — add mobile/tablet-specific layouts
6. **Animation variants** — add entrance animations, scroll effects via Elementor motion settings
7. **Color palette variants** — same structure, 3-4 colorways per philosophy
8. **Dark/light mode variants** — each philosophy in both light and dark versions
9. **Extract from additional sources** — other design systems, Dribbble trends, awwwards winners

### Step-by-step resumption process

1. **Check MCP session is alive:**
   ```bash
   SID=$(cat /tmp/mcp_sid.txt)
   curl -s -X POST 'https://willinstructions-new.affinitydns.uk/wp-json/mcp/elementor-mcp-server' \
     -H 'Content-Type: application/json' -H "Mcp-Session-Id: $SID" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
   ```
   If expired, reinitialize with `elementor-mcp-init`.

2. **For index page rebuild:** Use `build-page` with all 436 edition entries (proven to handle 116KB+ payloads)

3. **For new brand studies from other sources:**
   - Create profile JSON at `/tmp/real_design_profiles_batchN.json`
   - Copy builder script pattern from `/tmp/build_real_batch3.py`
   - Run with `python3 -u script.py` as background process
   - Verify with `browser_navigate` + `browser_console`

### Builder script pattern (proven across 3 batches)

The builder scripts follow this structure:
- Profile JSON: `{brand_key: {label, emoji, bg, bg_alt, text, text_light, accent, dark_bg, dark_text, heading_font, body_font, heading_size_h1, heading_size_h2, heading_weight, heading_transform, letter_spacing, border_style, border_color, border_radius, border_width_top, section_padding, card_padding, btn_padding, btn_radius}}`
- Generator functions: `make_hero(p)`, `make_features(p)`, `make_cta(p)`, `make_testimonial(p)`, `make_footer(p)`
- Each returns an Elementor `structure` array with inline-styled HTML widgets
- HTML widgets use `<p style='...'>` and `<a style='...'>` to bypass Elementor's global kit
- Results saved to `/tmp/real_design_batchN_results.json`

### Technical constraints
- **No custom CSS** — inline styles only (Elementor global kit overrides widget-level settings)
- **HTML widgets** — use `widget_type: "html"` for all styled text
- **Container structure** — `type: "container"` with `flex_direction`, `padding`, `background_color`
- **MCP build-page** creates a NEW page each call (doesn't update existing)
- **Template save** — `elementor-mcp-save-as-template` takes `post_id` + `title`
- **WP REST API basic auth does NOT work** — MCP is the only authenticated channel
- **Vision tool broken** (error 1211) — use `browser_console` + DOM inspection instead
- **MCP 50-call limit per execute_code script** — for large batches, run as background Python process instead

---

## File Locations

| File | Purpose |
|---|---|
| `skills/wordpress-elementor-automation/elementor-mcp-sop/references/archetype-catalog.md` | Master catalog of all editions |
| `skills/wordpress-elementor-automation/elementor-mcp-sop/references/industry-playbooks.md` | 10 industry assembly recipes |
| `/tmp/mcp_sid.txt` | Current MCP session ID |
| `/tmp/real_design_profiles.json` | Batch 1 brand profiles (16 brands) |
| `/tmp/real_design_profiles_batch2.json` | Batch 2 brand profiles (16 brands) |
| `/tmp/real_design_profiles_batch3.json` | Batch 3 brand profiles (22 brands) |
| `/tmp/build_real_designs.py` | Builder script (batch 1 pattern) |
| `/tmp/build_real_batch2.py` | Builder script (batch 2 pattern) |
| `/tmp/build_real_batch3.py` | Builder script (batch 3 pattern) |
| `/tmp/real_design_results.json` | Batch 1 results (80 entries) |
| `/tmp/real_design_batch2_results.json` | Batch 2 results (80 entries) |
| `/tmp/real_design_batch3_results.json` | Batch 3 results (110 entries) |
| `/tmp/phil_v2_results.json` | Philosophy series 1 results |
| `/tmp/phil_v3_results.json` | Philosophy series 2 results |

---

## Quick Reference: MCP Tools Used

| Tool | Purpose | Key Params |
|---|---|---|
| `elementor-mcp-init` | Start session | Returns session ID |
| `elementor-mcp-build-page` | Create page with structure | `title`, `structure` (array) |
| `elementor-mcp-update-page-settings` | Change post status | `post_id`, `settings: {post_status}` |
| `elementor-mcp-save-as-template` | Save as reusable template | `post_id`, `title` |
| `elementor-mcp-get-page-structure` | Verify page structure | `post_id` |
