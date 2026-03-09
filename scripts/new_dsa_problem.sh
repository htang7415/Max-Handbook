#!/bin/sh
# Scaffold a DSA problem module from templates/dsa-problem
# Usage: ./scripts/new_dsa_problem.sh <topic> <slug> "<title>"
# Example: ./scripts/new_dsa_problem.sh array 704-binary-search "704.Binary Search"

set -e

if [ $# -ne 3 ]; then
  echo "Usage: $0 <topic> <slug> \"<title>\""
  echo "Example: $0 array 704-binary-search \"704.Binary Search\""
  exit 1
fi

TOPIC="$1"
SLUG="$2"
TITLE="$3"
TRACK="dsa"
PY_NAME=$(echo "$SLUG" | tr '-' '_')

DEST="modules/$TRACK/$TOPIC/$SLUG"
TEMPLATE_DIR="templates/dsa-problem"

if [ -d "$DEST" ]; then
  echo "Error: $DEST already exists"
  exit 1
fi

mkdir -p "$DEST/python"

sed \
  -e "s/{{TITLE}}/$TITLE/g" \
  -e "s/{{TOPIC}}/$TOPIC/g" \
  -e "s/{{SLUG}}/$SLUG/g" \
  "$TEMPLATE_DIR/README.md" > "$DEST/README.md"

sed "s/{{PY_NAME}}/$PY_NAME/g" \
  "$TEMPLATE_DIR/python/module.py" > "$DEST/python/${PY_NAME}.py"

sed "s/{{PY_NAME}}/$PY_NAME/g" \
  "$TEMPLATE_DIR/python/test_module.py" > "$DEST/python/test_${PY_NAME}.py"

echo "Created DSA problem template at $DEST"
echo "  pytest $DEST/python -q"
