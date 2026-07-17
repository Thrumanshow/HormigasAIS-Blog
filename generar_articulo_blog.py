import json
import os

# Asegurar que el directorio /posts existe
if not os.path.exists("posts"):
    os.makedirs("posts")

# 1. Cargamos la feromona actual
with open("feromona_posicionamiento.lbh", "r") as f:
    feromona = json.load(f)

firma = feromona["meta"]["hmac_sha256"]
ts = feromona["meta"]["timestamp"]

# 2. Definimos la ruta de salida en /posts/
ruta_salida = os.path.join("posts", "protocolo-lbh-arquitectura.html")

articulo_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Protocolo LBH: Arquitectura de identidad soberana | HormigasAIS</title>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "TechArticle",
      "headline": "Implementación del Protocolo LBH_BINARY_V1",
      "author": {{ 
        "@type": "Person", 
        "name": "Cristhiam Leonardo Hernández Quiñonez",
        "url": "https://blog.hormigasais.com/posts/perfil_cto_cristhiam.html"
      }},
      "programmingLanguage": "Python",
      "description": "Feromona de posicionamiento soberano HormigasAIS mediante criptografía HMAC-SHA256",
      "datePublished": "{ts}",
      "identifier": {{
        "@type": "PropertyValue",
        "propertyID": "HMAC_SHA256",
        "value": "{firma}"
      }}
    }}
    </script>
</head>
<body>
    <article>
        <h1>Cómo construimos una red de señales (Feromonas) con Git y Python</h1>
        <p>En HormigasAIS desarrollamos LBH_BINARY_V1, un protocolo que garantiza la integridad de nuestra identidad soberana en el nodo A16-SanMiguel-SV.</p>
        <p><strong>Firma de validación actual:</strong> <code>{firma[:32]}...</code></p>
        <hr>
        <p><em>Artículo desarrollado por el <a href="perfil_cto_cristhiam.html">CTO & Ingeniero de Protocolos</a>.</em></p>
    </article>
</body>
</html>"""

with open(ruta_salida, "w", encoding="utf-8") as f:
    f.write(articulo_html)

print(f"✅ Artículo generado en: {ruta_salida}")
