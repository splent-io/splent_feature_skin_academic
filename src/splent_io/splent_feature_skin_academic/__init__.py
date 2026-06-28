from splent_framework.blueprints.base_blueprint import create_blueprint

skin_academic_bp = create_blueprint(__name__)

# Design tokens (the real DIVERSO LAB academic/university palette/fonts).
ACADEMIC_TOKENS = {
    "primary": "#DD3333",
    "primary_contrast": "#ffffff",
    "accent": "#B02A2A",
    "bg": "#ffffff",
    "surface": "#F7F7F8",
    "text": "#2b2b2b",
    "heading": "#222222",
    "muted": "#6b7280",
    "border": "#e5e7eb",
    "radius": "6px",
    "container": "1170px",
    "font_body": "'Roboto', system-ui, sans-serif",
    "font_heading": "'Roboto Slab', Georgia, serif",
    "font_display": "'Oswald', system-ui, sans-serif",
    "font_url": "https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;500;700&family=Roboto:wght@400;500;700&family=Oswald:wght@400;500;600&display=swap",
}


def init_feature(app):
    # A skin sets the theme tokens and registers its stylesheet (order 200, so it
    # cascades last) on top of the theme's brand-agnostic base public.css.
    from splent_framework.assets.asset_registry import register_asset

    app.config["THEME_TOKENS"] = ACADEMIC_TOKENS
    register_asset(
        "css",
        "skin_academic.assets",
        order=200,
        subfolder="css",
        filename="skin_academic.css",
    )


def inject_context_vars(app):
    return {}
