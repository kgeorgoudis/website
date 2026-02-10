# Data Model: Blacklines.gr Portfolio Website

## Entities

### Article/Post
- Fields: `title` (string, required), `date` (ISO date, required), `author` (string, required), `category` (enum: devops|sketchnotes|diy, required), `tags` (list<string>), `slug` (string, derived or provided, unique within category), `summary`/`excerpt` (string, optional), `content` (markdown body, required), `status` (draft|published, default published), `featured_image` (path, optional), `language` (default en).
- Relationships: belongs to one Category; many Tags; many Images (references by path/alt text); authored by Author.
- Validation: required frontmatter keys (`title`, `date`, `category`, `author`); slug must be filesystem-safe; category must map to folder path; ensure code blocks render with syntax highlighting (pygments).

### Page
- Fields: `title`, `slug`, `template` (e.g., page), `content` (markdown), `order` (optional for nav), `language`.
- Relationships: standalone; linked in navigation (Home/Bio, Contact).
- Validation: slug unique across pages; contact info present on contact page.

### Category
- Fields: `name` (DevOps, Sketchnotes, DIY), `slug`, `description` (optional), `cover_image` (optional).
- Relationships: has many Posts; appears in nav.
- Validation: only defined categories allowed; slug matches folder name.

### Tag
- Fields: `name`, `slug`.
- Relationships: many-to-many with Posts.
- Validation: slug lowercase/kebab-case; limit tag list per post to keep nav usable.

### Image
- Fields: `filename`, `path`, `alt` (required), `caption` (optional), `dimensions` (optional), `sizes/srcset` variants (optional WebP + JPEG fallback), `lazy` (boolean, default true).
- Relationships: attached to Post or Page.
- Validation: alt text required; ensure responsive sizes; avoid >1MB originals without optimization.

### Author
- Fields: `name`, `bio`, `email`, `social` (LinkedIn, GitHub, Instagram optional), `photo` (path, alt).
- Relationships: authors posts/pages; bio appears on homepage.
- Validation: contact methods present; photo optimized/responsive.

## State & Workflow
- Content lives under `src/content/{devops,sketchnotes,diy,pages}` with matching category names; draft posts use `status: draft` until ready.
- Build steps enforce: missing frontmatter causes build failure; missing images produce warnings; 404 page included.
- Deployment flow: markdown → Pelican → static HTML/CSS/assets → Render static hosting with CSP/SRI headers.

