import json
import os
from datetime import datetime

# Asegurar directorio
os.makedirs("posts", exist_ok=True)

# Cargar feromona
try:
    with open("feromona_posicionamiento.lbh", "r", encoding="utf-8") as f:
        feromona = json.load(f)
    firma = feromona["meta"]["hmac_sha256"]
    ts = feromona["meta"]["timestamp"]
except:
    firma = "PENDIENTE"
    ts = datetime.now().isoformat()

# ==================== PLANTILLA BASE ====================
def generar_articulo(titulo, contenido_html, nombre_archivo):
    articulo_html = f'''<!DOCTYPE html>
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
        
        <p><em>Publicado desde Nodo A16-SanMiguel-SV • {ts[:10]}</em></p>
    </article>
</body>
</html>'''
    
    ruta = os.path.join("posts", nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(articulo_html)
    print(f"✅ Artículo generado: posts/{nombre_archivo}")

# Ejemplo de uso futuro:
# generar_articulo("Nuevo Título", "<p>Contenido aquí...</p>", "nuevo-articulo.html")
