# Contributing to Blacklines.gr

This is a personal portfolio website, but suggestions and improvements are welcome!

## How to Contribute

### Reporting Issues

If you notice:
- Broken links
- Typos or errors
- Accessibility issues
- Performance problems
- Security concerns

Please [open an issue](https://github.com/yourusername/website/issues) or [contact me](/contact/).

### Suggesting Improvements

Ideas for:
- Better performance optimizations
- Accessibility enhancements
- SEO improvements
- Build process improvements

Are always welcome! Open an issue to discuss.

## Development Setup

See [QUICKSTART.md](QUICKSTART.md) for quick setup instructions.

## Code Standards

This project follows these principles (see [CONSTITUTION.md](CONSTITUTION.md)):

- **Lightweight**: Minimal dependencies, no unnecessary JavaScript
- **Fast**: Optimize for performance (Lighthouse ≥95)
- **Secure**: HTTPS, CSP headers, static site architecture
- **Easy to Maintain**: Clear structure, good documentation
- **Free Tier Compatible**: Must work on Render.com free tier

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Test locally:
   ```bash
   cd src
   uv run pelican content -s pelicanconf.py
   uv run pelican --listen --port 8100
   ```
5. Ensure build completes without errors
6. Commit with clear messages
7. Push and create a pull request

## Content Guidelines

### Writing Articles

- Clear, concise writing
- Code examples with proper syntax highlighting
- Alt text on all images
- Links to external resources where appropriate
- Personal voice and experience

### Images

- Optimize before adding (< 500KB preferred)
- Use WebP when possible with JPEG fallback
- Include descriptive alt text
- Add captions where helpful

### Code Examples

- Use proper markdown code fences with language
- Include comments for clarity
- Keep examples concise and focused
- Test that code works before publishing

## Testing

Before submitting:

```bash
# Clean build
cd src
make clean
make html

# Check for errors
uv run pelican content -s pelicanconf.py -D

# Production build test
make publish
```

## Questions?

Feel free to [contact me](/contact/) with any questions about contributing!

---

Thank you for helping make this site better! 🙏

