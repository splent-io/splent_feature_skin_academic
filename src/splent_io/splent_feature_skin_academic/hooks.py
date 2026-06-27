"""skin_academic injects its aesthetic stylesheet into the public shell's
``layout.head`` slot, layered on top of the theme's base public.css.
"""

from flask import url_for

from splent_framework.hooks.template_hooks import register_template_hook


def academic_styles():
    return (
        '<link rel="stylesheet" href="'
        + url_for("skin_academic.assets", subfolder="css", filename="skin_academic.css")
        + '">'
    )


register_template_hook("layout.head", academic_styles)
