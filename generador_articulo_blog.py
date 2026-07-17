import json
import os
from datetime import datetime

os.makedirs("posts", exist_ok=True)

def generar_articulo(titulo, contenido_html, nombre_archivo):
    try:
        with open("feromona_posicionamiento.lbh", "r", encoding="utf-8") as f:
            feromona = json.load(f)
        firma = feromona.get("meta", {}).get("hmac_sha256", "PENDIENTE")
    except:
        firma = "PENDIENTE"
    
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo} | HormigasAIS</title>
    <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
    <article>
        <h1>{titulo}</h1>
        {contenido_html}
        
        <div class="firma-validacion">
            <strong>🔐 Firma de validación LBH:</strong><br>
            <code>{firma[:32]}...</code>
        </div>
        
        <p style="margin-top: 40px; color: #777; font-size: 0.95rem;">
            <em>Emitido desde Nodo A16-SanMiguel-SV</em>
        </p>
    </article>
</body>
</html>'''
    
    ruta = os.path.join("posts", nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Nuevo artículo creado → posts/{nombre_archivo}")

# Ejemplo:
# generar_articulo("Mi Nuevo Artículo", "<p>Contenido aquí...</p>", "mi-nuevo-articulo.html")
