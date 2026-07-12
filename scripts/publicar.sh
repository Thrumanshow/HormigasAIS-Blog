#!/bin/bash

FILE=$1
if [ ! -f "$FILE" ]; then echo "❌ Archivo $FILE no encontrado."; exit 1; fi

TITLE=$(grep '^# ' "$FILE" | sed 's/# //')
DATE=$(grep '^\[.*\]' "$FILE" | sed 's/\[//;s/\]//')
CONTENT=$(grep -v '^#' "$FILE" | grep -v '^\[')
FILENAME=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')

# FASE DE PREVISUALIZACIÓN (Terminal)
echo "------------------------------------------"
echo "🔍 PREVISUALIZACIÓN DEL ARTÍCULO:"
echo "TÍTULO: $TITLE"
echo "FECHA: $DATE"
echo "CONTENIDO: ${CONTENT:0:100}..." 
echo "------------------------------------------"
read -p "¿Deseas publicar este artículo? (y/n): " confirm

if [[ $confirm == [yY] ]]; then
    # 1. Crear el archivo en /posts
    cat << HTML > posts/$FILENAME.html
<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><link rel="stylesheet" href="../assets/style.css"><title>$TITLE</title></head>
<body>
  <div class="wrapper">
    <h1>$TITLE</h1>
    <p><em>$DATE</em></p>
    <div>$CONTENT</div>
    <a href="../index.html">← Volver</a>
  </div>
</body>
</html>
HTML

    # 2. Inyectar la card
    NEW_CARD="<article class=\"card\"><div class=\"card-content\"><div style=\"color: #00ff9f; font-size: 0.7rem;\">$DATE</div><h2 class=\"card-title\">$TITLE</h2><a href=\"posts/$FILENAME.html\" class=\"btn-read\">Leer artículo →</a></div></article>"
    sed -i "/<div id=\"feed\">/a $NEW_CARD" index.html

    echo "✅ Post publicado con éxito."
else
    echo "❌ Publicación cancelada."
fi
