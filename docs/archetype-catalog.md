# Elementor Section Archetype Catalog

Purpose: complete inventory of every reusable section archetype used in Elementor builds. Each archetype defines the **purpose**, **widget tree**, **responsive behavior**, and **industry fit**. Editions (visual variants) are listed as stubs to be filled in Phase 2.

Format: `archetype-name` — one-line purpose → widget tree → responsive notes → edition stubs → industry tags.

---

## 1. header

**Purpose:** Site navigation — logo, nav links, optional CTA, contact info. Usually sticky/fixed.

**Widget tree:**
```
container (flex_direction: row, justify_content: space-between, align_items: center)
├── container (row, gap: 12px)
│   ├── image (logo)
│   └── heading (site name, optional)
├── nav-menu (or icon-list as fallback)
└── container (row, gap: 12px)
    ├── button (primary CTA, e.g. "Call Now")
    └── icon-list (phone + email inline)
```

**Responsive:** Mobile collapses to hamburger. Logo stays left, CTA may shift below nav.

**Edition stubs:**
- `header-minimal` — logo + nav only, no CTA
- `header-standard` — logo + nav + CTA button
- `header-dual-row` — top bar (phone/email) + main nav row
- `header-transparent` — transparent overlay on hero, solid on scroll
- `header-mega` — logo + nav + multi-column dropdown areas (Pro)

**Industries:** all

---

## 2. hero

**Purpose:** Primary above-the-fold section — H1 headline, subtitle, primary + secondary CTA. Sets page tone.

**Widget tree (text-left):**
```
container (flex_direction: column or row, min_height: 500px, padding: 80/40)
├── heading (H1)
├── text-editor (subtitle/description)
├── container (row, gap: 16px, justify_content: flex-start)
│   ├── button (primary CTA)
│   └── button (secondary CTA, outline or ghost)
└── [optional] image/mockup/visual (right side in split layout)
```

**Responsive:** Splits stack to column on mobile. CTA buttons center on mobile.

**Edition stubs:**
- `hero-minimal` — clean white bg, left-aligned text, strong H1
- `hero-overlay` — full-bleed bg image + dark overlay + white text
- `hero-split` — 50/50 text | image split
- `hero-video` — video background (autoplay muted loop)
- `hero-editorial` — magazine-style: large type, narrow column, accent line
- `hero-app-mockup` — SaaS product screenshot/mockup on right
- `hero-centered` — centered text, no image, gradient or solid bg
- `hero-dark` — dark bg, white text, bold accent color CTAs
- `hero-gradient` — gradient bg, floating shapes, modern SaaS feel

**Industries:** all (selection varies by industry)

---

## 3. social-proof-strip

**Purpose:** Trust signal bar — client logos, certifications, "as seen in", partner badges.

**Widget tree:**
```
container (flex_direction: row, justify_content: center, align_items: center, gap: 32px, padding: 32/20)
├── heading (small label: "Trusted by" / "As featured in")
├── container (row, wrap, justify_content: center, gap: 24px)
│   ├── image (logo 1)
│   ├── image (logo 2)
│   ├── image (logo 3)
│   └── image (logo N)
```

**Responsive:** Logos wrap to 2-3 per row on mobile.

**Edition stubs:**
- `proof-logo-strip` — grayscale logos, hover to color
- `proof-badge-row` — certification badges with labels
- `proof-as-seen-in` — media publication logos with label
- `proof-numbers` — big stats: "500+ clients", "10 years", "99% satisfaction"
- `proof-carousel` — logo carousel (Pro image-carousel)

**Industries:** B2B, SaaS, consulting, legal, enterprise

---

## 4. stats-bar

**Purpose:** Numeric metrics — counters showing achievements, scale, or social proof.

**Widget tree:**
```
container (flex_direction: row, justify_content: center, gap: 40px, padding: 48/24, bg: dark or brand)
├── container (column, align_items: center)
│   ├── counter (number)
│   └── heading (label: "Happy Clients", h4)
├── container (column, align_items: center)
│   ├── counter (number)
│   └── heading (label)
├── container (column, align_items: center)
│   ├── counter (number)
│   └── heading (label)
└── container (column, align_items: center)
    ├── counter (number)
    └── heading (label)
```

**Responsive:** 2×2 grid on tablet, full stack on mobile.

**Edition stubs:**
- `stats-dark` — dark bg, white numbers, brand accent
- `stats-light` — light bg, dark numbers, subtle divider
- `stats-icon` — icon above each counter
- `stats-animated` — counter animation on scroll (Pro)
- `stats-inline` — horizontal inline separators instead of grid

**Industries:** SaaS, enterprise, portfolio, legal, financial

---

## 5. feature-grid

**Purpose:** Multi-column feature or service cards — icon/image + title + description + optional link.

**Widget tree:**
```
container (flex_direction: column, padding: 60/24)
├── heading (section title, H2, centered)
├── text-editor (subtitle/intro, centered)
└── container (flex_direction: row, gap: 24px, padding: 20/0)
    ├── container (column, padding: 32, bg: card, border_radius)
    │   ├── icon or image
    │   ├── heading (H3, feature name)
    │   └── text-editor (description)
    ├── container (column, padding: 32, bg: card, border_radius)
    │   ├── icon/image
    │   ├── heading (H3)
    │   └── text-editor
    └── container (column, padding: 32, bg: card, border_radius)
        ├── icon/image
        ├── heading (H3)
        └── text-editor
```

**Responsive:** 3-col desktop → 2-col tablet → 1-col mobile (or 2×2 on mobile for 4 cards).

**Edition stubs:**
- `feature-icon-cards` — FA icons, card bg, subtle shadow
- `feature-numbered` — large numbers (01, 02, 03) as visual anchors
- `feature-screenshot` — screenshot/image above text in each card
- `feature-alternating` — alternating image-left/image-right rows (see split-section)
- `feature-bento` — asymmetric grid: one large card + smaller ones
- `feature-minimal` — no card bg, just icon + text, generous spacing
- `feature-dark-cards` — dark bg section, light cards
- `feature-border` — bordered cards instead of filled bg
- `feature-hover-lift` — cards with hover shadow/scale effect

**Industries:** all

---

## 6. split-section

**Purpose:** Image + text side-by-side. Flexible: image left or right. Used for About, service detail, benefit explanation.

**Widget tree:**
```
container (flex_direction: row, gap: 40px, padding: 60/24, align_items: center)
├── container (column, width: 50%)
│   ├── image (full-width, border_radius)
│   └── [optional] small caption or badge
└── container (column, width: 50%)
    ├── heading (H2, section title)
    ├── text-editor (body copy)
    ├── icon-list (bullet points / benefits)
    └── button (CTA)
```

**Responsive:** Stacks to column on mobile. Image on top.

**Edition stubs:**
- `split-image-left` — image left, text right
- `split-image-right` — text left, image right (reverse)
- `split-video` — video embed instead of image
- `split-overlay` — image with text overlaid (not side-by-side)
- `split-icon-accent` — small accent icon/shape between columns
- `split-stats` — text side includes inline stats/counters
- `split-testimonial` — quote/testimonial as the text content

**Industries:** all

---

## 7. cta-band

**Purpose:** Full-width call-to-action section — headline + CTA button(s). Conversion-focused.

**Widget tree:**
```
container (flex_direction: column, align_items: center, text-align: center, padding: 64/24, bg: brand or dark)
├── heading (H2, action-oriented, white or high-contrast)
├── text-editor (supporting line, urgency, or benefit)
└── container (row, gap: 16px, justify_content: center)
    ├── button (primary CTA)
    └── button (secondary CTA, optional)
```

**Responsive:** CTA buttons stack on mobile, centered.

**Edition stubs:**
- `cta-dark-band` — dark bg, white text, brand CTA
- `cta-brand-band` — primary brand color bg
- `cta-gradient-band` — gradient bg, modern feel
- `cta-card` — CTA inside a floating card on lighter bg
- `cta-split` — CTA left, image/form right
- `cta-urgent` — countdown timer or urgency element included
- `cta-minimal` — just heading + single button, lots of whitespace

**Industries:** all

---

## 8. testimonial

**Purpose:** Customer/client quotes — build trust through social proof.

**Widget tree (single quote):**
```
container (flex_direction: column, align_items: center, padding: 60/24, bg: light)
├── heading (H2, "What Our Clients Say", centered)
└── container (column, align_items: center, max_width: 700px, padding: 32, bg: card, border_radius)
    ├── star-rating (5 stars)
    ├── text-editor (quote, italic or large)
    ├── container (row, align_items: center, gap: 12px)
    │   ├── image (client photo, circular, 48px)
    │   └── container (column)
    │       ├── heading (client name, small, H4)
    │       └── text-editor (role/company, muted)
```

**Widget tree (carousel/grid):**
```
container (column, padding: 60/24)
├── heading (H2, centered)
└── container (row, gap: 24px)
    ├── container (column, card: quote + author) [repeated 3×]
```

**Responsive:** 3-col → 1-col on mobile.

**Edition stubs:**
- `testimonial-single` — one featured quote, large and centered
- `testimonial-grid` — 3-column card grid
- `testimonial-carousel` — Pro testimonial-carousel widget
- `testimonial-video` — video testimonials
- `testimonial-inline` — quotes inline with page copy
- `testimonial-minimal` — no card bg, just quote marks + text
- `testimonial-dark` — dark bg, white quotes, accent stars

**Industries:** all (essential for services, optional for SaaS)

---

## 9. pricing

**Purpose:** Pricing comparison — plan tiers with features, highlighting recommended option.

**Widget tree:**
```
container (flex_direction: column, padding: 60/24)
├── heading (H2, "Plans & Pricing", centered)
├── text-editor (subtitle, centered)
├── [optional] toggle (monthly/annual, Pro form or tabs)
└── container (flex_direction: row, gap: 24px, align_items: flex-start)
    ├── container (column, card, padding: 32, border_radius)
    │   ├── heading (plan name, H3)
    │   ├── heading (price, large, accent)
    │   ├── text-editor (billing period)
    │   ├── divider
    │   ├── icon-list (features, check icons)
    │   └── button (CTA: "Get Started")
    ├── container (column, card, padding: 32, border_radius, border: brand, scale: 1.05)
    │   ├── heading (plan name + "Popular" badge)
    │   ├── heading (price)
    │   ├── text-editor (billing period)
    │   ├── divider
    │   ├── icon-list (features, check icons)
    │   └── button (primary CTA, brand color)
    └── container (column, card, padding: 32, border_radius)
        ├── heading (plan name, H3)
        ├── heading (price)
        ├── text-editor (billing period)
        ├── divider
        ├── icon-list (features, check icons)
        └── button (CTA)
```

**Responsive:** 3-col → stacks on mobile, featured card first.

**Edition stubs:**
- `pricing-3-col` — standard 3-tier, middle featured
- `pricing-2-col` — simple 2-tier comparison
- `pricing-toggle` — monthly/annual toggle with price change
- `pricing-comparison-table` — feature matrix table (Pro)
- `pricing-enterprise` — free tier + "Contact us" for enterprise
- `pricing-dark` — dark bg, light cards
- `pricing-minimal` — no cards, just text + price + CTA

**Industries:** SaaS, subscription services, memberships

---

## 10. faq

**Purpose:** Frequently asked questions — handle objections, reduce support load, improve SEO.

**Widget tree:**
```
container (flex_direction: column, padding: 60/24)
├── heading (H2, "Frequently Asked Questions", centered)
├── text-editor (subtitle/intro, centered)
└── accordion OR toggle (faq_schema: yes for SEO)
    ├── tab 1: question → answer (text-editor with HTML)
    ├── tab 2: question → answer
    └── tab N: question → answer
```

**Responsive:** Full-width on mobile. Accordion is naturally responsive.

**Edition stubs:**
- `faq-accordion` — standard accordion (one open at a time)
- `faq-toggle` — toggle (multiple can be open)
- `faq-two-col` — two accordion columns side by side
- `faq-categorized` — tabs above categories, accordion below
- `faq-with-cta` — FAQ section followed by CTA band

**Industries:** all (especially services, SaaS, legal, financial)

---

## 11. team-grid

**Purpose:** Team member profiles — photo, name, role, brief bio, social links.

**Widget tree:**
```
container (flex_direction: column, padding: 60/24)
├── heading (H2, "Meet Our Team", centered)
├── text-editor (subtitle, centered)
└── container (flex_direction: row, gap: 24px)
    ├── container (column, card, align_items: center, padding: 24)
    │   ├── image (circular or square, border_radius)
    │   ├── heading (name, H4, centered)
    │   ├── text-editor (role/title, muted, centered)
    │   ├── text-editor (short bio, optional)
    │   └── social-icons (centered)
    └── [repeated for each member]
```

**Responsive:** 4-col → 2-col tablet → 1-2-col mobile.

**Edition stubs:**
- `team-cards` — card per member, photo + details
- `team-minimal` — no cards, just photo + name + role inline
- `team-hover` — overlay bio on hover
- `team-large` — fewer members, larger photos, more bio
- `team-leadership` — leadership only, with longer bios

**Industries:** professional services, agencies, consultancies

---

## 12. logo-strip

**Purpose:** Partner/client/vendor logo display — horizontal strip or grid.

**Widget tree:**
```
container (flex_direction: row, justify_content: center, align_items: center, gap: 32px, padding: 32/20)
├── image (logo 1, fixed height)
├── image (logo 2)
├── image (logo 3)
└── [repeated]
```

**Responsive:** Wrap to 2-3 per row. Logos scale down on mobile.

**Edition stubs:**
- `logo-grayscale` — grayscale, color on hover
- `logo-uniform` — all logos normalized to same height
- `logo-marquee` — scrolling/marquee animation (Pro)
- `logo-with-labels` — logos with company name labels below
- `logo-grid` — grid layout instead of single strip

**Industries:** B2B, enterprise, agencies

---

## 13. timeline

**Purpose:** Sequential steps or history — process steps, milestones, "how it works".

**Widget tree (horizontal):**
```
container (flex_direction: column, padding: 60/24)
├── heading (H2, "How It Works", centered)
└── container (flex_direction: row, gap: 24px, position: relative)
    ├── container (column, align_items: center, width: 25%)
    │   ├── heading (step number, large, accent)
    │   ├── heading (step title, H4)
    │   └── text-editor (step description)
    └── [repeated 4×]
```

**Widget tree (vertical):**
```
container (column, padding: 60/24)
├── heading (H2)
└── [repeated N×]
    └── container (row, gap: 20px)
        ├── container (column, align_items: center, width: 48px)
        │   ├── icon or number circle
        │   └── divider (vertical line)
        └── container (column)
            ├── heading (step title)
            └── text-editor (description)
```

**Responsive:** Horizontal → vertical stack on mobile.

**Edition stubs:**
- `timeline-horizontal` — left-to-right steps
- `timeline-vertical` — top-to-bottom steps with connecting line
- `timeline-alt` — alternating left/right zigzag
- `timeline-numbered` — large numbers as visual anchors
- `timeline-icon` — icons instead of numbers
- `timeline-progress` — visual progress bar connecting steps (Pro progress-tracker)

**Industries:** services, legal, financial, onboarding flows

---

## 14. gallery

**Purpose:** Photo/image showcase — portfolio, project photos, team events, product images.

**Widget tree:**
```
container (flex_direction: column, padding: 60/24)
├── heading (H2, centered)
└── container (flex_direction: row, flex_wrap: wrap, gap: 8px)
    ├── image (col-span: 2, border_radius)
    ├── image (col-span: 1)
    ├── image (col-span: 1)
    └── [repeated]
```

**Responsive:** 3-4 col → 2 col → 1 col.

**Edition stubs:**
- `gallery-grid` — uniform grid, equal sizing
- `gallery-masonry` — varied heights, masonry layout
- `gallery-carousel` — horizontal scroll/carousel (Pro)
- `gallery-lightbox` — clickable images with lightbox
- `gallery-filtered` — category filter tabs above grid (Pro)
- `gallery-featured` — one large hero image + smaller thumbnails

**Industries:** portfolio, hospitality, events, real estate, creative

---

## 15. newsletter

**Purpose:** Email capture — newsletter signup, lead magnet, mailing list opt-in.

**Widget tree:**
```
container (flex_direction: column, align_items: center, padding: 48/24, bg: brand or dark)
├── heading (H3, "Stay Updated", white text)
├── text-editor (benefit of subscribing, white text)
└── [Pro] form widget OR [free] container (row)
    ├── text-editor (placeholder "Enter your email")
    └── button ("Subscribe")
```

**Responsive:** Form stacks on mobile, centered.

**Edition stubs:**
- `newsletter-simple` — inline form in a band
- `newsletter-card` — card floating on lighter bg
- `newsletter-lead-magnet` — includes freebie/lead magnet description
- `newsletter-minimal` — just email field + button, no heading
- `newsletter-footer` — integrated into footer section

**Industries:** all

---

## 16. contact

**Purpose:** Contact information + map + optional form.

**Widget tree:**
```
container (flex_direction: row, gap: 40px, padding: 60/24, align_items: flex-start)
├── container (column, width: 50%)
│   ├── heading (H2, "Get in Touch")
│   ├── text-editor (intro copy)
│   ├── icon-list (phone, email, address with icons)
│   ├── social-icons
│   └── button (optional: "Book a Consultation")
└── container (column, width: 50%)
    ├── google_maps (address, height: 350px, border_radius)
    └── [optional] Pro form widget
```

**Responsive:** Stacks on mobile, map on bottom.

**Edition stubs:**
- `contact-map-left` — map left, info right
- `contact-map-right` — info left, map right
- `contact-full-map` — full-width map below info
- `contact-with-form` — includes contact form
- `contact-minimal` — just info, no map
- `contact-card` — info in a card with map below
- `contact-multi-location` — multiple office locations with tabs

**Industries:** all (essential for local services)

---

## 17. blog-grid

**Purpose:** Blog post listing — latest articles, preview cards with featured images.

**Widget tree:**
```
container (flex_direction: column, padding: 60/24)
├── heading (H2, "Latest Insights", centered)
└── container (flex_direction: row, gap: 24px)
    ├── container (column, card, overflow: hidden)
    │   ├── image (featured image, full-width)
    │   ├── container (column, padding: 20)
    │   │   ├── text-editor (category/tag, small, muted)
    │   │   ├── heading (post title, H4)
    │   │   ├── text-editor (excerpt, 2-3 lines)
    │   │   └── button ("Read More", small)
    └── [repeated 3× or 6×]
```

**Responsive:** 3-col → 2-col → 1-col.

**Edition stubs:**
- `blog-cards` — standard card with image on top
- `blog-list` — horizontal cards, image left + text right
- `blog-minimal` — text only, no images, clean typography
- `blog-featured` — one large featured post + smaller below
- `blog-masonry` — varied card heights, masonry grid
- `blog-grid-pro` — Pro posts widget with query control

**Industries:** all (content marketing)

---

## 18. portfolio-grid

**Purpose:** Project/case study showcase — thumbnail + title + category.

**Widget tree:**
```
container (flex_direction: column, padding: 60/24)
├── heading (H2, "Our Work", centered)
└── container (flex_direction: row, flex_wrap: wrap, gap: 16px)
    ├── container (column, position: relative, overflow: hidden, border_radius)
    │   ├── image (project thumbnail)
    │   └── container (overlay, position: absolute, bottom: 0, padding: 16)
    │       ├── heading (project name, white text)
    │       └── text-editor (category, small)
    └── [repeated]
```

**Responsive:** 3-col → 2-col → 1-col.

**Edition stubs:**
- `portfolio-overlay` — title overlay on image on hover
- `portfolio-cards` — title below image, card style
- `portfolio-filtered` — category filter tabs (Pro)
- `portfolio-fullwidth` — large single project per row
- `portfolio-masonry` — varied aspect ratios
- `portfolio-grid-pro` — Pro portfolio widget

**Industries:** creative, agencies, developers, architecture

---

## 19. before-after

**Purpose:** Visual transformation comparison — before/after results.

**Widget tree (free):**
```
container (flex_direction: row, gap: 16px, padding: 40/20)
├── container (column, align_items: center)
│   ├── image (before photo, border_radius)
│   └── heading (label: "Before", small, centered)
└── container (column, align_items: center)
    ├── image (after photo, border_radius)
    └── heading (label: "After", small, centered)
```

**Edition stubs:**
- `before-after-side` — side-by-side images
- `before-after-slider` — draggable slider comparison (Pro or custom)
- `before-after-stack` — stacked vertically on mobile
- `before-after-grid` — multiple before/after pairs in grid

**Industries:** renovation, cosmetic, cleaning, design, photography

---

## 20. comparison-table

**Purpose:** Feature comparison — compare plans, services, or options in table format.

**Widget tree:**
```
container (flex_direction: column, padding: 60/24)
├── heading (H2, "Compare Plans", centered)
└── [Pro] table widget OR [free] container structure mimicking table
    ├── header row: Feature | Plan A | Plan B | Plan C
    ├── row: Feature 1 | check | check | check
    ├── row: Feature 2 | check | check | —
    └── row: Feature N | — | check | check
```

**Responsive:** Horizontal scroll on mobile or stacks to card view.

**Edition stubs:**
- `comparison-standard` — clean table, check/X marks
- `comparison-highlight` — recommended column highlighted
- `comparison-cards` — card-based comparison for mobile
- `comparison-detailed` — detailed descriptions per feature

**Industries:** SaaS, services, membership tiers

---

## 21. video-embed

**Purpose:** Embedded video — product demo, explainer, testimonial, brand story.

**Widget tree:**
```
container (flex_direction: column, align_items: center, padding: 60/24)
├── heading (H2, centered)
├── text-editor (subtitle, centered)
└── container (column, max_width: 800px, width: 100%)
    └── video (video_type: youtube, aspect_ratio: 169, border_radius, box_shadow)
```

**Responsive:** Video scales to 100% width on mobile.

**Edition stubs:**
- `video-hero` — video as hero background
- `video-centered` — centered video with heading above
- `video-split` — video on one side, text on other
- `video-gallery` — multiple videos in grid
- `video-thumbnail` — custom thumbnail + play button overlay
- `video-autoplay` — autoplay muted background video

**Industries:** all (product demos, explainers, brand stories)

---

## 22. countdown

**Purpose:** Urgency timer — launch countdown, event countdown, limited offer.

**Widget tree:**
```
container (flex_direction: column, align_items: center, padding: 48/24, bg: dark or brand)
├── heading (H2, "Launching Soon", white text)
├── text-editor (event/offer description)
└── countdown (Pro widget: days, hours, minutes, seconds)
```

**Responsive:** Timer digits shrink on mobile, stack if needed.

**Edition stubs:**
- `countdown-launch` — product/service launch timer
- `countdown-event` — event countdown with location
- `countdown-offer` — limited-time offer with CTA below
- `countdown-minimal` — just the timer, no heading

**Industries:** events, launches, seasonal offers

---

## 23. footer

**Purpose:** Site footer — navigation, contact info, social links, copyright, legal links.

**Widget tree:**
```
container (flex_direction: column, bg: dark or brand, padding: 60/24/30)
├── container (flex_direction: row, gap: 40px, justify_content: space-between)
│   ├── container (column, width: 25%)
│   │   ├── image (logo)
│   │   ├── heading (site name)
│   │   └── text-editor (tagline/description)
│   ├── container (column, width: 20%)
│   │   ├── heading (H4, "Quick Links")
│   │   └── icon-list (nav links, white text)
│   ├── container (column, width: 20%)
│   │   ├── heading (H4, "Services")
│   │   └── icon-list (service links)
│   └── container (column, width: 25%)
│       ├── heading (H4, "Contact")
│       ├── icon-list (phone, email, address)
│       └── social-icons
├── divider (full-width, subtle)
└── container (row, justify_content: space-between)
    ├── text-editor (copyright, small, muted)
    └── container (row, gap: 16px)
        └── text-editor (privacy, terms links)
```

**Responsive:** 4-col → 2-col → 1-col stack on mobile.

**Edition stubs:**
- `footer-standard` — 4-column with logo, links, services, contact
- `footer-minimal` — single column, just copyright + social
- `footer-dark` — dark bg, white text
- `footer-brand` — brand color bg
- `footer-cta` — includes CTA band above the footer content
- `footer-sitemap` — comprehensive link columns
- `footer-with-newsletter` — newsletter signup above footer content

**Industries:** all

---

## 24. banner

**Purpose:** Promotional announcement bar — top-of-page alert, sale banner, maintenance notice.

**Widget tree:**
```
container (flex_direction: row, justify_content: center, align_items: center, padding: 12/20, bg: accent or warning color)
├── text-editor (announcement text, centered, small)
└── [optional] button ("Learn More", small)
```

**Responsive:** Full-width text on mobile, button may drop below.

**Edition stubs:**
- `banner-sale` — promotional/sale banner
- `banner-announcement` — general announcement
- `banner-urgent` — red/warning color for urgent notices
- `banner-sticky` — fixed/pinned at top of page
- `banner-dismissable` — with close button (custom)

**Industries:** all (seasonal, promotional)

---

## 25. about-summary

**Purpose:** Company overview section — mission, values, brief history, key differentiators.

**Widget tree:**
```
container (flex_direction: column, padding: 60/24)
├── heading (H2, "About Us" or "Who We Are", centered)
├── text-editor (intro paragraph, centered, max-width: 700px)
├── divider (short, centered, accent color)
├── container (flex_direction: row, gap: 32px, padding: 32/0)
│   ├── container (column, align_items: center, width: 33%)
│   │   ├── icon (value/mission icon)
│   │   ├── heading (H4, value name)
│   │   └── text-editor (value description)
│   └── [repeated 3×]
└── button (optional: "Learn More About Us")
```

**Responsive:** 3-col → 1-col on mobile.

**Edition stubs:**
- `about-values` — mission + values grid
- `about-story` — narrative/history timeline style
- `about-numbers` — includes stats bar inline
- `about-leadership` — team/leadership focused
- `about-minimal` — just text, no icons

**Industries:** all (essential for services, agencies, consultancies)

---

## 26. services-list

**Purpose:** Detailed service catalog — each service gets its own block with description, features, and CTA.

**Widget tree:**
```
container (flex_direction: column, padding: 60/24)
├── heading (H2, "Our Services", centered)
├── text-editor (intro, centered)
└── [repeated per service]
    └── container (flex_direction: row, gap: 32px, padding: 32/0, border_bottom or card)
        ├── icon or image (service icon, large)
        ├── container (column)
        │   ├── heading (H3, service name)
        │   ├── text-editor (service description)
        │   └── icon-list (key features/benefits)
        └── button (optional: "Learn More")
```

**Responsive:** Row → column on mobile.

**Edition stubs:**
- `services-horizontal-cards` — each service as a horizontal card
- `services-accordion` — services in accordion (Pro)
- `services-tabs` — tabbed service descriptions (Pro tabs)
- `services-icon-rows` — icon + text rows, no card bg
- `services-cards-grid` — services in card grid (see feature-grid)
- `services-numbered` — numbered service list

**Industries:** professional services, legal, financial, agencies

---

## 27. bento-grid

**Purpose:** Asymmetric, modern grid layout — varied cell sizes for visual interest. Popular in modern SaaS/tech design.

**Widget tree:**
```
container (flex_direction: row, flex_wrap: wrap, gap: 16px, padding: 40/20)
├── container (column, width: 66%, bg: card, padding: 32, border_radius) — large feature
├── container (column, width: 33%, bg: card, padding: 32, border_radius) — small feature
├── container (column, width: 33%, bg: card, padding: 32, border_radius) — small feature
├── container (column, width: 66%, bg: card, padding: 32, border_radius) — large feature
└── container (column, width: 33%, bg: card, padding: 32, border_radius) — small feature
```

**Responsive:** All cells go to 100% width on mobile, stacked.

**Edition stubs:**
- `bento-features` — feature highlights in asymmetric grid
- `bento-stats` — stats and features mixed
- `bento-cards` — varied content cards (text, image, CTA)
- `bento-dark` — dark bg section with light cards
- `bento-minimal` — minimal borders, clean spacing

**Industries:** SaaS, tech, creative, modern brands

---

## 28. off-canvas-menu

**Purpose:** Slide-out mobile menu — hamburger-triggered overlay navigation.

**Widget tree (Pro):**
```
off-canvas widget (trigger: hamburger icon)
├── container (column, padding: 32)
│   ├── image (logo)
│   ├── icon-list (nav links, large)
│   ├── divider
│   ├── icon-list (contact info)
│   └── social-icons
```

**Responsive:** Only visible/triggered on mobile.

**Edition stubs:**
- `offcanvas-standard` — slide from right, full-height
- `offcanvas-fullscreen` — full-screen overlay
- `offcanvas-minimal` — compact, links only
- `offcanvas-with-cta` — includes CTA button in menu

**Industries:** all

---

## 29. breadcrumb

**Purpose:** Navigation breadcrumb trail — shows page hierarchy.

**Widget tree (Pro):**
```
container (padding: 16/24, bg: light)
└── text-editor (breadcrumb: Home > Services > Service Name)
  OR Pro breadcrumb widget if available
```

**Edition stubs:**
- `breadcrumb-standard` — Home / Parent / Current
- `breadcrumb-minimal` — just the current page name
- `breadcrumb-hero` — overlaid on hero background

**Industries:** all (especially sites with deep hierarchies)

---

## 30. page-title-banner

**Purpose:** Branded inner-page title banner — sits above content on service/about/contact pages. Solves Hello Elementor theme title leak with a designed solution.

**Widget tree:**
```
container (flex_direction: column, align_items: center, text-align: center, padding: 60/24, bg: dark-gradient)
├── heading (H1, page title, white text)
├── divider (short, gold/accent, centered)
└── text-editor (subtitle/breadcrumb, muted white)
```

**Responsive:** Reduced padding on mobile.

**Edition stubs:**
- `banner-dark` — dark navy gradient, gold accent line
- `banner-brand` — brand color bg, white text
- `banner-image` — bg image + overlay + centered title
- `banner-minimal` — light bg, dark text, subtle divider
- `banner-with-breadcrumb` — includes breadcrumb trail

**Industries:** all (inner pages)

---

## Phase 2 Build Results (COMPLETED — 83 editions)

Built and saved as templates on willinstructions-new.affinitydns.uk (draft status).

### Hero (8 editions)
- hero-minimal → page 314, template 368 ✅
- hero-overlay → page 316, template 370 ✅
- hero-dark → page 318, template 372 ✅
- hero-centered → page 320, template 374 ✅
- hero-split → page 322, template 376 ✅
- hero-editorial → page 324, template 378 ✅
- hero-gradient → page 326, template 380 ✅
- hero-mockup → page 328, template 382 ✅

### CTA-band (5 editions)
- cta-dark-band → page 330, template 384 ✅
- cta-brand-band → page 332, template 386 ✅
- cta-gradient-band → page 334, template 388 ✅
- cta-card → page 336, template 390 ✅
- cta-minimal → page 338, template 392 ✅

### Feature-grid (9 editions)
- feature-icon-cards → page 340, template 394 ✅
- feature-numbered → page 342, template 396 ✅
- feature-minimal → page 344, template 398 ✅
- feature-dark-cards → page 346, template 400 ✅
- feature-border → page 348, template 402 ✅
- feature-screenshot → page 438, template 556 ✅
- feature-alternating → page 440, template 558 ✅
- feature-bento → page 442, template 560 ✅
- feature-hover-lift → page 444, template 562 ✅

### Footer (6 editions)
- footer-standard → page 350, template 404 ✅
- footer-minimal → page 352, template 406 ✅
- footer-cta → page 354, template 408 ✅
- footer-newsletter → page 356, template 410 ✅
- footer-brand → page 446, template 564 ✅
- footer-sitemap → page 448, template 566 ✅

### Split-section (5 editions)
- split-image-left → page 358, template 412 ✅
- split-image-right → page 360, template 414 ✅
- split-video → page 362, template 416 ✅
- split-testimonial → page 364, template 418 ✅
- split-stats → page 366, template 420 ✅

### Stats-bar (3 editions)
- stats-dark → page 450, template 568 ✅
- stats-light → page 452, template 570 ✅
- stats-icon → page 454, template 572 ✅

### Social-proof-strip (3 editions)
- proof-logo-strip → page 456, template 574 ✅
- proof-numbers → page 458, template 576 ✅
- proof-badge-row → page 460, template 578 ✅

### Testimonial (5 editions)
- testimonial-single → page 462, template 580 ✅
- testimonial-grid → page 464, template 582 ✅
- testimonial-minimal → page 466, template 584 ✅
- testimonial-dark → page 468, template 586 ✅
- testimonial-inline → page 470, template 588 ✅

### Pricing (5 editions)
- pricing-3-col → page 472, template 590 ✅
- pricing-2-col → page 474, template 592 ✅
- pricing-dark → page 476, template 594 ✅
- pricing-minimal → page 478, template 596 ✅
- pricing-enterprise → page 480, template 598 ✅

### FAQ (3 editions)
- faq-accordion → page 482, template 600 ✅
- faq-toggle → page 484, template 602 ✅
- faq-with-cta → page 486, template 604 ✅

### Team-grid (3 editions)
- team-cards → page 488, template 606 ✅
- team-minimal → page 490, template 608 ✅
- team-large → page 492, template 610 ✅

### Logo-strip (3 editions)
- logo-grayscale → page 494, template 612 ✅
- logo-with-labels → page 496, template 614 ✅
- logo-grid → page 498, template 616 ✅

### Timeline (3 editions)
- timeline-horizontal → page 500, template 618 ✅
- timeline-vertical → page 502, template 620 ✅
- timeline-numbered → page 504, template 622 ✅

### Gallery (3 editions)
- gallery-grid → page 506, template 624 ✅
- gallery-masonry → page 508, template 626 ✅
- gallery-featured → page 510, template 628 ✅

### Newsletter (3 editions)
- newsletter-simple → page 512, template 630 ✅
- newsletter-card → page 514, template 632 ✅
- newsletter-lead-magnet → page 516, template 634 ✅

### Contact (3 editions)
- contact-map-right → page 518, template 636 ✅
- contact-minimal → page 520, template 638 ✅
- contact-card → page 522, template 640 ✅

### Blog-grid (2 editions)
- blog-cards → page 524, template 642 ✅
- blog-list → page 526, template 644 ✅

### Video-embed (1 edition)
- video-centered → page 528, template 646 ✅

### Banner (3 editions)
- banner-announcement → page 530, template 648 ✅
- banner-sale → page 532, template 650 ✅
- banner-urgent → page 534, template 652 ✅

### About-summary (1 edition)
- about-values → page 536, template 654 ✅

### Services-list (1 edition)
- services-icon-rows → page 538, template 656 ✅

### Bento-grid (1 edition)
- bento-features → page 540, template 658 ✅

### Header (2 editions)
- header-standard → page 542, template 660 ✅
- header-minimal → page 544, template 662 ✅

### Page-title-banner (2 editions)
- page-title-dark → page 546, template 664 ✅
- page-title-minimal → page 548, template 666 ✅

### Before-after (1 edition)
- before-after-side → page 550, template 668 ✅

### Comparison-table (1 edition)
- comparison-standard → page 552, template 670 ✅

### Countdown (1 edition)
- countdown-launch → page 554, template 672 ✅

**Total: 83 editions built and saved as templates across 24 archetypes.**

Not yet built (off-canvas-menu, breadcrumb require Elementor Pro widgets; remaining editions are lower priority stubs for future expansion).

---

## Phase 3: Verification Results

### 3A: Structure Verification (All 86 pages)
All 86 pages verified via MCP `get-page-structure` — every page has valid Elementor data with containers and widgets present. Zero empty structures, zero errors.

**Result: ✅ 86/86 PASS**

### 3B: Visual Spot-Check (12 representative pages)

Published temporarily, DOM-rendered at desktop viewport (1280px), verified key elements, then reverted to draft.

| Page ID | Edition | Key Elements Verified | Result |
|---------|---------|----------------------|--------|
| 314 | hero-minimal | H1, 2 CTA buttons, header, footer | ✅ PASS |
| 324 | hero-editorial | H1, buttons, image area, header, footer | ✅ PASS |
| 330 | cta-dark-band | Heading, buttons, header, footer | ✅ PASS |
| 342 | feature-numbered | H2 title, 3 numbered steps (01/02/03) | ✅ PASS |
| 350 | footer-standard | 4-col layout (brand/links/services/contact), social, copyright | ✅ PASS |
| 364 | split-testimonial | Heading, testimonial area, buttons | ✅ PASS |
| 462 | testimonial-single | Testimonial widget, heading | ✅ PASS |
| 472 | pricing-3-col | 3 pricing tiers (Starter/Professional/Enterprise), prices, CTAs | ✅ PASS |
| 482 | faq-accordion | H2 title, 5 accordion items with expand/collapse | ✅ PASS |
| 502 | timeline-vertical | H2 title, 4 numbered steps (1-4) | ✅ PASS |
| 522 | contact-card | Headings, icon-boxes, layout | ✅ PASS |
| 552 | comparison-standard | H2 title, 16 text-editor cells | ⚠️ FUNCTIONAL |

**Notes:**
- comparison-standard uses text-editor widgets for table cells rather than a proper table widget — functional but visually basic. Could improve with Elementor Pro table widget or a more structured grid layout in future iteration.
- All pages have responsive flex-wrap, 100% width rules, mobile menu support, and responsive srcset images.
- The site's global header (Elementor theme header) and global footer CTA appear on all library pages — this is expected since they're theme-level templates. When assembling actual client sites, only the library section content is used.

### 3C: Responsive Checks
- Desktop (1280px): All pages render with boxed content widths, proper column layouts
- Flex-wrap present on all pages for responsive column stacking
- Mobile menu (hamburger) available on all pages
- Responsive images (srcset) on all pages
- No JavaScript errors detected during rendering

**Result: ✅ 11/12 PASS, 1 functional but basic**

---

## Phase 4: Industry Playbooks

Complete industry playbooks with assembly recipes for 10 client types, plus style family groupings and color palette defaults.

👉 **See `industry-playbooks.md`** for the full playbook document.

### Playbooks Included:
1. **Legal / Professional Services** — solicitors, will writers, accountants
2. **Trades / Home Services** — plumbers, electricians, builders
3. **Health / Wellness** — clinics, therapists, gyms
4. **Hospitality / Food** — restaurants, hotels, catering
5. **E-commerce / Retail** — online shops, boutiques, product brands
6. **SaaS / Technology** — software, apps, hosting platforms
7. **Creative / Portfolio / Agency** — designers, photographers, agencies
8. **Education / Training** — tutors, course creators, academies
9. **Real Estate / Property** — estate agents, property managers
10. **Non-profit / Charity** — charities, community orgs, clubs

### Style Families:
- 🏛️ **Classic** — Legal, finance, medical (hero-centered + feature-icon-cards + footer-standard)
- 🌑 **Dark** — SaaS, tech, agencies (hero-dark + feature-dark-cards + cta-dark-band)
- ✨ **Minimal** — Creative, portfolio, boutique (hero-minimal + feature-minimal + cta-minimal)
- 🎨 **Brand** — E-commerce, retail, food (hero-split + feature-hover-lift + cta-gradient-band)
- 🏗️ **Functional** — Corporate, B2B, hosting (hero-centered + feature-numbered + footer-sitemap)

### Design Library Index Page
A live, browsable index page is published on the staging site at:
👉 **https://willinstructions-new.affinitydns.uk/design-library/** (page ID 737)

Contains all 86 editions organized by archetype with Preview buttons linking to each live edition page.

---

## Quick Reference Matrix

| Archetype | Core Widgets | Pro Needed? | Primary Use |
|---|---|---|---|
| header | image, heading, nav-menu/icon-list, button | No (Pro for nav-menu) | Site navigation |
| hero | heading, text-editor, button, image | No | Above-the-fold impact |
| social-proof-strip | heading, image | No | Trust signals |
| stats-bar | counter, heading | No (Pro for animation) | Metrics display |
| feature-grid | icon/heading/text-editor in cards | No | Feature/service showcase |
| split-section | image, heading, text-editor, button | No | Content + visual balance |
| cta-band | heading, text-editor, button | No | Conversion section |
| testimonial | star-rating, text-editor, image, heading | No (Pro for carousel) | Social proof |
| pricing | heading, text-editor, icon-list, button | No (Pro for toggle) | Plan comparison |
| faq | accordion/toggle | No | Objection handling |
| team-grid | image, heading, text-editor, social-icons | No | Team showcase |
| logo-strip | image | No | Partner/client display |
| timeline | heading, text-editor, icon, divider | No (Pro for progress) | Process/history |
| gallery | image | No (Pro for lightbox/filter) | Photo showcase |
| newsletter | heading, text-editor, button | Pro for form | Email capture |
| contact | heading, text-editor, icon-list, google_maps | No (Pro for form) | Contact + map |
| blog-grid | image, heading, text-editor, button | No (Pro for posts widget) | Blog listing |
| portfolio-grid | image, heading, text-editor | No (Pro for filter) | Project showcase |
| before-after | image, heading | No (Pro for slider) | Transformation display |
| comparison-table | container structure or Pro table | Pro for table | Feature comparison |
| video-embed | video, heading, text-editor | No | Video content |
| countdown | heading, text-editor | Yes (countdown widget) | Urgency timer |
| footer | image, heading, text-editor, icon-list, social-icons, divider | No | Site footer |
| banner | text-editor, button | No | Promotional bar |
| about-summary | heading, text-editor, icon, divider, button | No | Company overview |
| services-list | icon/heading/text-editor/icon-list/button | No (Pro for tabs/accordion) | Service catalog |
| bento-grid | container, icon, heading, text-editor | No | Modern asymmetric grid |
| off-canvas-menu | off-canvas, icon-list, social-icons | Yes | Mobile menu |
| breadcrumb | text-editor or Pro widget | Pro for widget | Page hierarchy |
| page-title-banner | heading, divider, text-editor | No | Inner page title |

---

## Phase 2: Edition Building Priority

Build editions in this order based on frequency of use across our client sites:

1. **hero** (8 editions) — every site needs one
2. **cta-band** (5 editions) — every site needs one
3. **feature-grid** (7 editions) — services/features on every site
4. **footer** (5 editions) — every site needs one
5. **split-section** (5 editions) — about/service pages
6. **header** (4 editions) — every site needs one
7. **testimonial** (5 editions) — most service sites
8. **faq** (3 editions) — most service sites
9. **contact** (5 editions) — every site needs one
10. **pricing** (5 editions) — SaaS/membership sites
11. **stats-bar** (3 editions) — enterprise/SaaS
12. **social-proof-strip** (3 editions) — B2B/enterprise
13. **team-grid** (3 editions) — professional services
14. **timeline** (4 editions) — process/How It Works pages
15. **newsletter** (3 editions) — content/marketing sites
16. **blog-grid** (4 editions) — content marketing
17. **portfolio-grid** (4 editions) — creative/portfolio
18. **services-list** (4 editions) — service catalog pages
19. **bento-grid** (3 editions) — modern SaaS/tech
20. **before-after** (2 editions) — renovation/cosmetic
21. **comparison-table** (2 editions) — SaaS comparison
22. **video-embed** (4 editions) — product demo sites
23. **countdown** (2 editions) — event/launch pages
24. **banner** (3 editions) — promotional/seasonal
25. **about-summary** (3 editions) — about pages
26. **logo-strip** (3 editions) — B2B/enterprise
27. **gallery** (4 editions) — hospitality/portfolio
28. **off-canvas-menu** (2 editions) — mobile-first sites
29. **breadcrumb** (2 editions) — deep-hierarchy sites
30. **page-title-banner** (3 editions) — inner pages

Total: ~110 editions to build across 30 archetypes.

---

## Phase 5: Design Philosophy Library (40 editions)

8 completely different design philosophies, each with 5 key sections (hero, features, CTA, testimonial, footer). These use inline-styled HTML widgets to bypass Elementor's global kit, ensuring each philosophy looks genuinely unique.

**Philosophy Index:** https://willinstructions-new.affinitydns.uk/design-philosophy-library/ (page 1493)

### Swiss/International 📐
Grid-obsessed, red/black/white, Roboto uppercase, systematic spacing, sharp corners
- swiss-hero → page 1253, template 1257
- swiss-features → page 1259, template 1263
- swiss-cta → page 1265, template 1269
- swiss-testimonial → page 1271, template 1275
- swiss-footer → page 1277, template 1281

### Editorial/Magazine 📰
Warm whites, serif headings (Playfair Display), literary feel, thin rules, generous rhythm
- editorial-hero → page 1283, template 1287
- editorial-features → page 1289, template 1293
- editorial-cta → page 1295, template 1299
- editorial-testimonial → page 1301, template 1305
- editorial-footer → page 1307, template 1311

### Glassmorphism 🔮
Purple-to-cyan gradient, semi-transparent cards, rounded corners (20px), Inter font, techy
- glassmorphism-hero → page 1313, template 1317
- glassmorphism-features → page 1319, template 1323
- glassmorphism-cta → page 1325, template 1329
- glassmorphism-testimonial → page 1331, template 1335
- glassmorphism-footer → page 1337, template 1341

### Brutalist ⚡
Thick borders, Courier New mono, 72px headings, magenta accent, sharp edges, raw energy
- brutalist-hero → page 1343, template 1347
- brutalist-features → page 1349, template 1353
- brutalist-cta → page 1355, template 1359
- brutalist-testimonial → page 1361, template 1365
- brutalist-footer → page 1367, template 1371

### Luxury/Premium ✨
Dark backgrounds, gold accents (#C9A94E), Playfair Display serif, generous whitespace, elegant
- luxury-hero → page 1373, template 1377
- luxury-features → page 1379, template 1383
- luxury-cta → page 1385, template 1389
- luxury-testimonial → page 1391, template 1395
- luxury-footer → page 1397, template 1401

### Playful/Bubble 🎈
Bright saturated colors, Nunito rounded font, pill buttons (30px radius), bouncy energy
- playful-hero → page 1403, template 1407
- playful-features → page 1409, template 1413
- playful-cta → page 1415, template 1419
- playful-testimonial → page 1421, template 1425
- playful-footer → page 1427, template 1431

### Corporate/Enterprise 🏢
Navy/blue palette, Open Sans, structured cards, subtle shadows, Fortune 500 feel
- corporate-hero → page 1433, template 1437
- corporate-features → page 1439, template 1443
- corporate-cta → page 1445, template 1449
- corporate-testimonial → page 1451, template 1455
- corporate-footer → page 1457, template 1461

### Retro/Vintage 📻
Cream/brown tones, Merriweather serif, double borders, warm nostalgic feel
- retro-hero → page 1463, template 1467
- retro-features → page 1469, template 1473
- retro-cta → page 1475, template 1479
- retro-testimonial → page 1481, template 1485
- retro-footer → page 1487, template 1491

**Total: 40 philosophy editions (8 philosophies × 5 sections)**

---

## Phase 5B: Design Philosophy Library Batch 2 (40 more editions)

8 more completely different design philosophies, same inline-styled approach.

### Art Deco 🏛️
Dark + gold geometric, Poiret One display font, champagne cream text, sharp edges, 1920s glamour
- artdeco-hero → page 1497, template 1501
- artdeco-features → page 1503, template 1507
- artdeco-cta → page 1509, template 1513
- artdeco-testimonial → page 1515, template 1519
- artdeco-footer → page 1521, template 1525

### Neo-Minimalist ⬜
Extreme whitespace (120px section padding), Inter 300-weight, near-zero borders, Japanese-inspired restraint
- neominimal-hero → page 1527, template 1531
- neominimal-features → page 1533, template 1537
- neominimal-cta → page 1539, template 1543
- neominimal-testimonial → page 1545, template 1549
- neominimal-footer → page 1551, template 1555

### Organic/Nature 🌿
Earthy greens, DM Serif Display + Lora, cream backgrounds, pill buttons (30px radius), eco-friendly
- organic-hero → page 1557, template 1561
- organic-features → page 1563, template 1567
- organic-cta → page 1569, template 1573
- organic-testimonial → page 1575, template 1579
- organic-footer → page 1581, template 1585

### Cyberpunk/Neon 💚
Near-black bg, green matrix text (#00FF41), hot pink accent (#FF0080), Orbitron font, Share Tech Mono body
- cyberpunk-hero → page 1587, template 1591
- cyberpunk-features → page 1593, template 1597
- cyberpunk-cta → page 1599, template 1603
- cyberpunk-testimonial → page 1605, template 1609
- cyberpunk-footer → page 1611, template 1615

### Material Design 📐
Google-inspired, elevation/shadows, Roboto 500-weight, purple accent (#6200EE), clean card radius
- material-hero → page 1617, template 1621
- material-features → page 1623, template 1627
- material-cta → page 1629, template 1633
- material-testimonial → page 1635, template 1639
- material-footer → page 1641, template 1645

### Grunge/Distressed 🔥
Dark moody, Impact font, 68px headings, red accent (#FF4444), thick 4px borders, raw industrial
- grunge-hero → page 1647, template 1651
- grunge-features → page 1653, template 1657
- grunge-cta → page 1659, template 1663
- grunge-testimonial → page 1665, template 1669
- grunge-footer → page 1671, template 1675

### Mid-Century Modern 🛋️
Warm oranges/teals, Josefin Sans + Lato, cream backgrounds (#FDF6E3), 3px borders, 1950s warmth
- midcentury-hero → page 1677, template 1681
- midcentury-features → page 1683, template 1687
- midcentury-cta → page 1689, template 1693
- midcentury-testimonial → page 1695, template 1699
- midcentury-footer → page 1701, template 1705

### Isometric/3D 🔮
Deep navy bg (#1A1B2E), purple accent (#7C3AED), Space Grotesk font, 16px radius, futuristic
- isometric-hero → page 1707, template 1711
- isometric-features → page 1713, template 1717
- isometric-cta → page 1719, template 1723
- isometric-testimonial → page 1725, template 1729
- isometric-footer → page 1731, template 1735

**Total: 80 philosophy editions (16 philosophies × 5 sections)**

---

## Phase 5C: Real-World Brand Studies (80 editions)

16 real-world brand designs extracted from the popular-web-designs skill (54 design systems). Each uses authentic colors, fonts, spacing, and border-radius from the actual website.

**Complete Library Index:** https://willinstructions-new.affinitydns.uk/complete-design-library/ (page 2221)

### Stripe 💳
White bg, purple accent (#635BFF), Source Sans 3, 52px headings, fintech premium
- stripe-hero → page 1741, template 1745
- stripe-features → page 1747, template 1751
- stripe-cta → page 1753, template 1757
- stripe-testimonial → page 1759, template 1763
- stripe-footer → page 1765, template 1769

### Linear 🌙
Dark bg (#0A0A0B), purple accent (#8B5CF6), Inter 510-weight, -2px tracking, dark mode SaaS
- linear-hero → page 1771, template 1775
- linear-features → page 1777, template 1781
- linear-cta → page 1783, template 1787
- linear-testimonial → page 1789, template 1793
- linear-footer → page 1795, template 1799

### Vercel ▲
Pure black bg, white accent, Geist font, -2.4px tracking, developer minimal
- vercel-hero → page 1801, template 1805
- vercel-features → page 1807, template 1811
- vercel-cta → page 1813, template 1817
- vercel-testimonial → page 1819, template 1823
- vercel-footer → page 1825, template 1829

### Apple 🍎
White bg, blue accent (#0071E3), SF Pro, 56px headings, pill buttons, machined precision
- apple-hero → page 1831, template 1835
- apple-features → page 1837, template 1841
- apple-cta → page 1843, template 1847
- apple-testimonial → page 1849, template 1853
- apple-footer → page 1855, template 1859

### Notion 📝
White bg, blue accent (#2EAADC), Inter, -2.1px tracking, productivity clean
- notion-hero → page 1861, template 1865
- notion-features → page 1867, template 1871
- notion-cta → page 1873, template 1877
- notion-testimonial → page 1879, template 1883
- notion-footer → page 1885, template 1889

### Framer ⚡
Black bg, blue accent (#0099FF), Inter, 80px headings, -3.5px tracking, kinetic
- framer-hero → page 1891, template 1895
- framer-features → page 1897, template 1901
- framer-cta → page 1903, template 1907
- framer-testimonial → page 1909, template 1913
- framer-footer → page 1915, template 1919

### Spotify 🎵
Dark bg (#121212), green accent (#1ED760), DM Sans, 64px headings, content-first darkness
- spotify-hero → page 1921, template 1925
- spotify-features → page 1927, template 1931
- spotify-cta → page 1933, template 1937
- spotify-testimonial → page 1939, template 1943
- spotify-footer → page 1945, template 1949

### Airbnb 🏠
White bg, red accent (#FF385C), DM Sans, 56px headings, photography-forward, warm
- airbnb-hero → page 1951, template 1955
- airbnb-features → page 1957, template 1961
- airbnb-cta → page 1963, template 1967
- airbnb-testimonial → page 1969, template 1973
- airbnb-footer → page 1975, template 1979

### SpaceX 🚀
Pure black bg, white accent, Inter, 60px headings, +1px tracking, cinematic full-bleed
- spacex-hero → page 1981, template 1985
- spacex-features → page 1987, template 1991
- spacex-cta → page 1993, template 1997
- spacex-testimonial → page 1999, template 2003
- spacex-footer → page 2005, template 2009

### NVIDIA 💚
Black bg, green accent (#76B900), Inter, 48px headings, GPU-powered engineering
- nvidia-hero → page 2011, template 2015
- nvidia-features → page 2017, template 2021
- nvidia-cta → page 2023, template 2027
- nvidia-testimonial → page 2029, template 2033
- nvidia-footer → page 2035, template 2039

### Coinbase 🪙
White bg, blue accent (#0052FF), DM Sans, 56px headings, trustworthy crypto
- coinbase-hero → page 2041, template 2045
- coinbase-features → page 2047, template 2051
- coinbase-cta → page 2053, template 2057
- coinbase-testimonial → page 2059, template 2063
- coinbase-footer → page 2065, template 2069

### BMW 🏁
White bg, blue accent (#1C69D4), DM Sans, 300-weight uppercase, +3px tracking, automotive luxury
- bmw-hero → page 2071, template 2075
- bmw-features → page 2077, template 2081
- bmw-cta → page 2083, template 2087
- bmw-testimonial → page 2089, template 2093
- bmw-footer → page 2095, template 2099

### Figma 🎨
White bg, blue accent (#0D99FF), Inter, 64px headings, -0.96px tracking, design tool precision
- figma-hero → page 2101, template 2105
- figma-features → page 2107, template 2111
- figma-cta → page 2113, template 2117
- figma-testimonial → page 2119, template 2123
- figma-footer → page 2125, template 2129

### Uber 🚗
White bg, black accent, DM Sans, pill buttons (999px radius), monochrome ride-share
- uber-hero → page 2131, template 2135
- uber-features → page 2137, template 2141
- uber-cta → page 2143, template 2147
- uber-testimonial → page 2149, template 2153
- uber-footer → page 2155, template 2159

### IBM 🔵
White bg, blue accent (#0F62FE), IBM Plex Sans, 300-weight headings, Carbon Design System
- ibm-hero → page 2161, template 2165
- ibm-features → page 2167, template 2171
- ibm-cta → page 2173, template 2177
- ibm-testimonial → page 2179, template 2183
- ibm-footer → page 2185, template 2189

### Zapier ⚡
White bg, orange accent (#FF4F00), Inter, 72px headings, -2px tracking, automation energy
- zapier-hero → page 2191, template 2195
- zapier-features → page 2197, template 2201
- zapier-cta → page 2203, template 2207
- zapier-testimonial → page 2209, template 2213
- zapier-footer → page 2215, template 2219

**Total: 80 brand editions (16 brands × 5 sections)**

---

## Library Summary

| Category | Editions | Page IDs |
|---|---|---|
| Original archetypes (24 types) | 86 | 314-554 |
| Design philosophies (16 styles) | 80 | 1253-1735 |
| Real-world brand studies (16 brands) | 80 | 1741-2215 |
| **Grand Total** | **246** | **246 pages + 246 templates** |

### Browse the library:
- **Archetype Library (86):** /design-library/ (page 737)
- **Philosophy Library (80):** /design-philosophy-library/ (page 1737)
- **Complete Library Index (246):** /complete-design-library/ (page 2221)
