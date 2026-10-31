# Customer Intelligence visual identity

The presentation pairs a business analytics tone with the repository's actual
ML experiment. The title is **CUSTOMER INTELLIGENCE**; the subtitle is
**Predicting Customer Churn Through Machine Learning**.

## Palette and typography

| Color | Hex | Purpose |
|---|---|---|
| Midnight navy | `#07111F` | Primary background |
| Deep indigo | `#172554` | Background depth |
| Electric cyan | `#22D3EE` | Connections and primary accent |
| Refined purple | `#8B5CF6` | Decorative risk signals |
| White | `#F8FAFC` | Main title and high-contrast text |

The SVG uses system fonts (`Segoe UI`, Arial, Helvetica, sans-serif), a 1440 ×
480 viewBox, and a 3:1 ratio. The README scales the image to its available width.
The graphic uses a network of customer nodes as an illustration of customer
relationships and risk signals. Node positions, colors, and connections are
decorative; they are not a visualization of dataset records or predictions.

## Asset contract

[The banner](../Images/customer-intelligence-banner.svg) is a self-contained,
static SVG. It has no external fonts, images, scripts, animation, or embedded
HTML. SVG `title` and `desc` elements describe the illustration; the README
provides alternative text for its image embedding.

Keep the banner's role editorial: actual performance numbers belong in the
evaluation section alongside their evidence. At narrow widths, the adjacent
Markdown title and subtitle provide readable text even as the image scales.

For visual review, check the exported SVG at its native size and within a
narrow README layout. Verify that title, subtitle, and network remain separate,
the image retains its aspect ratio, and no text is clipped. Local previews do
not establish that GitHub's sanitizer or renderer was tested.

[Return to the project README](../README.md)
