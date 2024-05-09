# Configuration file for the Sphinx documentation builder.
# -- Project information
project = "sphinx-revealjs on RTD"
copyright = "2021, Kazuya Takei"
author = "Kazuya Takei"
release = "2024.5.10"

# -- General configuration
extensions = [
    "sphinx.ext.todo",
    "sphinx_revealjs",
]
templates_path = ["_templates"]
exclude_patterns = []

# -- For extension
# - sphinx_revealjs
revealjs_html_theme = "revealjs-simple"
revealjs_static_path = ["_static"]
revealjs_script_conf = {
    "controls": True,
    "progress": True,
    "hash": True,
    "center": True,
    "transition": "slide",
}
revealjs_script_plugins = [
    {
        "name": "RevealCustomControls",
        "src": "https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/customcontrols/plugin.js",
    },
]
revealjs_js_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/js/all.min.js",
    "https://assets.readthedocs.org/static/javascript/readthedocs-doc-embed.js",
    "rtd-badge.js",
]
revealjs_css_files = [
    "revealjs/plugin/highlight/zenburn.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css",
    "https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/customcontrols/style.css",
    "https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css",
    "rtd-badge.css",
]


def override_builder(app, config):
    app.registry.builders["html"] = app.registry.builders["revealjs"]
    # NOTE: This is not working cachings
    # override_target = os.environ.get("TO_REVEALJS", None)
    # if not override_target:
    #     return
    # elif override_target not in app.registry.builders:
    #     warnings.warn("Invalid target")
    #     return
    # elif "revealjs" not in app.registry.builders:
    #     warnings.warn("sphinx-revealjs is not loaded")
    #     return
    # app.registry.builders[override_target] = app.registry.builders["revealjs"]


def _inject_rtd_version(app, pagename, templatename, context, doctree):
    if not doctree:
        return
    context["READTHEDOCS"] = True
    if "READTHEDOCS" in context:
        output = app.builder.templates.render("_rtd-versions.html", context)
        context["revealjs_page_confs"].append(
            {"customcontrols": {"controls": [{"icon": output}]}}
        )


def setup(app):
    app.connect("config-inited", override_builder)
    app.connect("html-page-context", _inject_rtd_version)
