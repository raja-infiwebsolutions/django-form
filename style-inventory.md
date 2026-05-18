# Style Inventory

Scanned HTML/Django template files in the repository.

Found templates:

- userform/templates/form.html
  - No inline `style` attributes detected.
  - No `<style>` blocks detected.
  - Uses default form rendering `{{ form.as_p }}` and a plain `<button>` element.

- userform/templates/success.html
  - No inline `style` attributes detected.
  - No `<style>` blocks detected.
  - Contains a heading and a simple anchor link.

Notes:
- There was no `base.html` in the project. I created a project base template at `userform/templates/base.html` and updated the existing templates to extend it.
- No JavaScript files were found in the repository.

Next steps implemented in this change set:
- Added a small CSS architecture under `static/css/` (normalize.css, _variables.css, main.css).
- Updated templates to use semantic classes and link the stylesheet via Django static files.
- Created a short changelog at `styles/CHANGELOG.md` describing the template changes.
