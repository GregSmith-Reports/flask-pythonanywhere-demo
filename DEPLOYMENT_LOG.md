# PythonAnywhere Deployment Log — skills-practice Flask App

## Local Project (on this laptop)
Location: `C:\Users\grega\Desktop\skills-practice\`

- `app.py` — Flask app with a `/` route rendering `index.html`
- `templates/index.html` — page template
- `static/style.css` — page styling
- `requirements.txt` — contains `Flask`
- `.venv/` — local virtual environment with Flask installed (minimal footprint, installed with `--no-cache-dir`)

### Run locally
```bash
# from bash, venv not activated:
./.venv/Scripts/python.exe app.py

# or if venv is activated (shows (.venv) in prompt), in cmd:
python app.py
```
Visit `http://127.0.0.1:5000/`.

## PythonAnywhere Account
- Username: `JoeBloggs123`
- Dashboard: `https://www.pythonanywhere.com/user/JoeBloggs123/`
- Free tier: 512 MB quota, one web app per account, domain `joebloggs123.pythonanywhere.com`

### Remote project folder
Created via Bash console at `/home/JoeBloggs123/proj/` (NOT `mysite` — that was the PythonAnywhere Quickstart default, which was cancelled in favor of manual setup).

Structure confirmed present:
```
~/proj/
├── app.py              (201 bytes)
├── requirements.txt    (7 bytes)
├── static/
│   └── style.css       (222 bytes)
└── templates/
    └── index.html      (353 bytes)
```

### Steps completed so far
1. Opened Bash console on PythonAnywhere.
2. `mkdir proj && cd proj`
3. `mkdir templates static`
4. Used `nano app.py`, `nano templates/index.html`, `nano static/style.css`, `nano requirements.txt` to paste in file contents matching the local versions.
5. Verified files with `ls -la` / `ls -ls`.
6. On the **Web** tab, clicked **Add a new web app** → kept default domain
   `JoeBloggs123.pythonanywhere.com` → chose **Manual configuration** → selected
   **Python 3.10** (matches local venv's `Python 3.10.2`). Web app created successfully
   ("All done! Your web app is now set up.").
7. In the **Static files** section, set:
   - URL: `/static/`
   - Directory: `/home/JoeBloggs123/proj/static`
8. Created a dedicated virtualenv for the web app (instead of relying on
   `pip install --user`) via Bash console:
   ```bash
   cd ~/proj
   mkvirtualenv --python=/usr/bin/python3.10 proj-venv
   pip install -r requirements.txt
   ```
   This creates the venv at `/home/JoeBloggs123/.virtualenvs/proj-venv` and installs
   Flask + dependencies into it.

### Remaining steps to finish deployment
1. Confirm the `pip install -r requirements.txt` inside `proj-venv` finished without errors.
2. On the **Web** tab, in the **Virtualenv** section, enter the path:
   ```
   /home/JoeBloggs123/.virtualenvs/proj-venv
   ```
3. Edit the WSGI config file (linked from the Web tab, path like
   `/var/www/joebloggs123_pythonanywhere_com_wsgi.py`):
   ```python
   import sys
   path = '/home/JoeBloggs123/proj'
   if path not in sys.path:
       sys.path.insert(0, path)

   from app import app as application
   ```
4. Click the green **Reload JoeBloggs123.pythonanywhere.com** button on the Web tab.
5. Visit `https://joebloggs123.pythonanywhere.com/` to confirm it works.

## Related Skill
A reusable skill for this workflow was created at
[.github/skills/flask-webpage/SKILL.md](.github/skills/flask-webpage/SKILL.md) — covers scaffolding
a minimal Flask app plus PythonAnywhere deployment steps for future projects.

## Notes / Gotchas
- `./path` syntax only works in Bash/Git Bash terminals, not `cmd` — in `cmd`, use
  `python app.py` (if venv activated) or `.venv\Scripts\python.exe app.py`.
- PythonAnywhere's "Quickstart new Flask project" wizard auto-generates its own
  `flask_app.py` and WSGI config — skip it if you already have your own project
  structure, and choose **Manual configuration** instead.
- The WSGI configuration file is accessed via the **Web** tab (not the Files tab) —
  it has a direct link to `/var/www/<username>_pythonanywhere_com_wsgi.py`.
