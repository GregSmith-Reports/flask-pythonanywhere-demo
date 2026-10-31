
# Flask Web Page (PythonAnywhere)

## When to Use
- The user asks you to create/build a web page or small web app, e.g. "create a web page for...", "build me a site that...".
- The user mentions PythonAnywhere or wants to deploy a Python web app to PythonAnywhere.
- The user runs `/flask-webpage`.

## Procedure
1. Scaffold a minimal Flask app in the workspace (create only if it doesn't already exist):
   - `app.py` — Flask app with at least one route (`/`) rendering the requested page content.
   - `templates/index.html` — Jinja2 template for the page, using the content/topic the user described.
   - `static/style.css` — basic styling for the page.
   - `requirements.txt` — containing at least `Flask`.
2. Keep the page content focused on what the user actually asked for — don't add unrelated features, sign-up forms, databases, etc. unless requested.
3. After scaffolding, show the user how to run it locally:
   ```
   pip install -r requirements.txt
   python app.py
   ```
4. Provide PythonAnywhere deployment steps:
   - Sign in to PythonAnywhere and open a **Bash console** (or use the Files tab) to upload the project files.
   - Create a new **Web app** from the PythonAnywhere dashboard, choosing **Flask** and the matching Python version.
   - Point the generated WSGI config file (`/var/www/<username>_pythonanywhere_com_wsgi.py`) to import your Flask `app` object, e.g.:
     ```python
     import sys
     path = '/home/<username>/<project-folder>'
     if path not in sys.path:
         sys.path.insert(0, path)
     from app import app as application
     ```
   - Install dependencies from `requirements.txt` in a PythonAnywhere Bash console: `pip install --user -r requirements.txt`.
   - Set the working directory and static files mapping (e.g. URL `/static/` → path `/home/<username>/<project-folder>/static`) in the Web tab.
   - Reload the web app from the PythonAnywhere Web tab to apply changes.
5. Remind the user that PythonAnywhere free tier has one web app per account and specific domain naming (`<username>.pythonanywhere.com`).

## Example
Input: "Create a web page for my photography portfolio and help me get it on PythonAnywhere."
Output: Scaffolds `app.py`, `templates/index.html`, `static/style.css`, `requirements.txt` for a simple portfolio page, then walks through local run + PythonAnywhere upload/WSGI/static-files setup.
