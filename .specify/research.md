# Research Notes: Blacklines.gr Portfolio Website

Decision: Use pelican-alchemy (sketchy) with CSS-first galleries (no JS lightbox by default)
Rationale: Theme matches desired aesthetic; CSS grid + `loading="lazy"` keeps footprint small and meets Lightweight/Fast principles while remaining compatible with Pelican 4.11+.
Alternatives considered: pelican-plugins (photos, gallery, or lightbox) add dependencies/JS weight; custom JS lightbox rejected to keep JS-free baseline.

Decision: Enable Pelican Atom feeds per section (sitewide + category feeds)
Rationale: Pelican provides feeds out-of-the-box; valuable for DevOps readers and low-cost to generate.
Alternatives considered: No feeds (misses distribution), RSS-only (Atom suffices and is default in Pelican).

Decision: Omit search at launch; rely on clear navigation and taxonomy
Rationale: Static search (lunr.js) adds JS and bundle weight; site scope is small and well-categorized.
Alternatives considered: lunr.js/elasticlunr client search (too heavy for v1); external search (needs third-party scripts).

Decision: Contact info = email, LinkedIn, GitHub, optional Instagram for sketches; surface in bio + contact page
Rationale: Covers professional + creative channels with minimal maintenance overhead.
Alternatives considered: Contact form (requires backend), comments system (adds scripts/trackers) both rejected for static simplicity and privacy.

Decision: Disable comments; provide "Email me" or contact links instead
Rationale: Keeps site static and secure; avoids moderation overhead and third-party embeds.
Alternatives considered: Disqus/Utterances/Staticman (adds JS, tracking, complexity).

Decision: Use blacklines.gr custom domain with HTTPS; fallback to Render subdomain during bring-up
Rationale: Aligns branding; Render supports free HTTPS and redirects to enforce HTTPS.
Alternatives considered: Only Render subdomain (keeps setup simple but loses branding).

Decision: Security headers via Render `static.json` and SRI on any external assets
Rationale: Render static sites honor `static.json` for headers; CSP + HSTS + referrer-policy can be set centrally; SRI ensures integrity when CDNs are unavoidable.
Alternatives considered: Inline meta CSP (less reliable, harder to maintain); Netlify-style `_headers` not Render-standard.

Decision: Testing/QA = Pelican build (dev + publish), html5 validation/link check as dev dependency, manual Lighthouse smoke for each section
Rationale: Keeps checks lightweight while catching broken links/markup; aligns with constitution for speed/security without adding heavy test harness.
Alternatives considered: Full E2E suite (overkill for static brochure site); no automated validation (risks regressions).

Decision: Image handling = pre-optimized WebP/AVIF preferred with JPEG fallback, responsive sizes + `srcset`, lazy loading everywhere
Rationale: Meets performance targets on mobile and keeps within free-tier bandwidth limits.
Alternatives considered: Serving originals (too heavy); JS-based galleries (extra weight).

