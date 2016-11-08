"""Allow {{  cookiecutter.project_slug  }} to be executable through `python -m {{  cookiecutter.project_slug  }}`."""
from __future__ import absolute_import

{%- if 'no' not in cookiecutter.command_line_interface|lower %}
from .cli import main


if __name__ == "__main__":  # pragma: no cover
        main(prog_name="{{  cookiecutter.project_slug  }}")
{%- endif %}
{%- if 'no' in cookiecutter.command_line_interface|lower %}
if __name__ == "__main__":  # pragma: no cover
    pass # TODO: call entry point
{%- endif %}
