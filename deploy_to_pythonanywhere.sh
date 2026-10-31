#!/usr/bin/env bash
#
# Upload project files to PythonAnywhere and reload the web app, using the
# PythonAnywhere API (no SSH needed — works on the free tier).
#
# Setup (one-time):
#   1. On PythonAnywhere, go to Account -> API Token -> create a token.
#   2. In your local terminal (NOT in this script, keep it out of source control):
#        export PA_USERNAME="JoeBloggs123"
#        export PA_API_TOKEN="paste-your-token-here"
#   3. Run this script from the project root: ./deploy_to_pythonanywhere.sh
#
# What it does:
#   - Uploads app.py, templates/index.html, static/style.css, requirements.txt
#     to /home/$PA_USERNAME/proj/... on PythonAnywhere.
#   - Reloads the JoeBloggs123.pythonanywhere.com web app so changes go live.

set -euo pipefail

if [[ -z "${PA_USERNAME:-}" || -z "${PA_API_TOKEN:-}" ]]; then
    echo "Error: set PA_USERNAME and PA_API_TOKEN environment variables first." >&2
    echo "  export PA_USERNAME=\"your-username\"" >&2
    echo "  export PA_API_TOKEN=\"your-api-token\"" >&2
    exit 1
fi

REMOTE_BASE="/home/${PA_USERNAME}/proj"
API_BASE="https://www.pythonanywhere.com/api/v0/user/${PA_USERNAME}"

upload_file() {
    local local_path="$1"
    local remote_path="$2"
    echo "Uploading ${local_path} -> ${remote_path}"
    curl -sf -X POST \
        -H "Authorization: Token ${PA_API_TOKEN}" \
        "${API_BASE}/files/path${remote_path}/" \
        -F "content=@${local_path}" > /dev/null
}

upload_file "app.py"                 "${REMOTE_BASE}/app.py"
upload_file "requirements.txt"       "${REMOTE_BASE}/requirements.txt"
upload_file "templates/index.html"   "${REMOTE_BASE}/templates/index.html"
upload_file "static/style.css"       "${REMOTE_BASE}/static/style.css"

echo "Reloading web app..."
curl -sf -X POST \
    -H "Authorization: Token ${PA_API_TOKEN}" \
    "${API_BASE}/webapps/${PA_USERNAME}.pythonanywhere.com/reload/" > /dev/null

echo "Done. Visit https://${PA_USERNAME}.pythonanywhere.com/"
