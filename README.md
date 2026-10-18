# Stuck on Shuffle

Academic project website for **Stuck on Shuffle: On Attribute–Object Binding in Vision–Language Models**. Built from the [ExplainableML Academic Project Page Template](https://github.com/ExplainableML/academic-project-page-template), with the supplied manuscript's abstract, figures, method, and results.

## Preview

No build step or package installation is required:

```sh
python3 -m http.server 8000
```

Open http://localhost:8000.

## GitHub Pages

In the repository's **Settings → Pages**, choose **Deploy from a branch**, select `main` and `/ (root)`, and save. The site is intended for https://stuck-on-shuffle.github.io/. `.nojekyll` keeps deployment static.

## Content

- `index.html`: page content, metadata, results, and BibTeX.
- `static/css/index.css`: project-specific responsive styling.
- `static/css/template.css` and `bulma.min.css`: template styles.
- `static/js/index.js`: accessible citation copying with a manual fallback.
- `static/images/`: figures extracted from the supplied paper and a custom SVG favicon.

The manuscript is used only as a source for text, tables, and figures. Do not add the paper PDF or a paper download link to this website.

Author names and affiliations were supplied by the authors and are reflected in the header, BibTeX, citation metadata, and structured data. Author links use personal websites where available, otherwise LinkedIn. Netanel’s name is displayed and cited as Netanel Y. Tamir. Rami’s personal website is https://www.benarirami.com/, as supplied by the author. Publication date and public research resource links have not been provided. Update the visible header, BibTeX, citation metadata, and structured data together when publication details become available. The four resource buttons intentionally have no URLs yet; their icons and labels use the top navigation’s gray whenever `href` is absent, and black when a link is present. To enable each button, add its `href` and remove `aria-disabled`, `role`, `tabindex`, `aria-describedby`, and the coming-soon `title`; update the release note to reflect which links are available. No speculative links or dates are included.

Figures reproduce Figures 1, 2, and 3 as high-resolution JPEGs. Click the benchmark figure or use the view controls to switch between multiple-choice examples and nested chains, each with its own caption. Both figures remain visible when JavaScript is unavailable. The SABER results chart and table use Table 2. The instance retrieval carousel contains the three Figure 6 examples, exported as 3136 × 1104 JPEGs; its controls support arrows, direct selection, keyboard navigation, and swiping. All three examples are visible without JavaScript. The instance retrieval bar chart covers both models and all nine settings in Table 6, with exact scores labeled above the bars. The abstract is verbatim apart from paragraph breaks and typographical normalization; explanatory sections summarize the manuscript.

To regenerate the Table 6 plot, install Matplotlib in a Python environment and run `python scripts/plot_instance_retrieval.py`. This writes standalone SVG and high-resolution PNG assets; the website uses the SVG and needs no Python runtime.

## Attribution

The website template is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Its attribution to the [Academic Project Page Template](https://github.com/ExplainableML/academic-project-page-template) and [Nerfies](https://nerfies.github.io/) is retained in the footer. The template license does not assign a license to the paper or its research assets.

The arXiv and GitHub SVG brand icons are from [Simple Icons](https://simpleicons.org/).
