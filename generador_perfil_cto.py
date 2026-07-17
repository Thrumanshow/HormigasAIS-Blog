import json
import os

# Asegurar que el directorio /posts existe
if not os.path.exists("posts"):
    os.makedirs("posts")

# 1. Cargamos la feromona para obtener la firma (Vínculo de Identidad)
try:
    with open("feromona_posicionamiento.lbh", "r") as f:
        feromona = json.load(f)
    firma = feromona["meta"]["hmac_sha256"]
except FileNotFoundError:
    firma = "PENDIENTE_DE_EMISION_LBH"

# 2. Datos de la Entidad
CTO_DATA = {
    "nombre": "Cristhiam Leonardo Hernández Quiñonez",
    "rol": "CTO & Ingeniero de Protocolos",
    "empresa": "HormigasAIS",
    "especialidades": ["Identidad Soberana", "Criptografía (HMAC-SHA256)", "Arquitectura Descentralizada", "Python", "Protocolo LBH"],
    "linkedin": "https://www.linkedin.com/in/cristhiam-lbh-architect",
    "github": "https://github.com/Thrumanshow"
}

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{CTO_DATA['nombre']} | Perfil Soberano - HormigasAIS</title>
    <link rel="canonical" href="https://blog.hormigasais.com/posts/perfil_cto_cristhiam.html">

    <!-- Schema.org: Vinculación Criptográfica -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "{CTO_DATA['nombre']}",
      "jobTitle": "{CTO_DATA['rol']}",
      "worksFor": {{ "@type": "Organization", "name": "{CTO_DATA['empresa']}" }},
      "sameAs": ["{CTO_DATA['github']}", "{CTO_DATA['linkedin']}"],
      "identifier": {{
        "@type": "PropertyValue",
        "propertyID": "HMAC_SHA256_LBH",
        "value": "{firma}"
      }}
    }}
    </script>
</head>
<body>
    <article>
        <h1>{CTO_DATA['nombre']}</h1>
        <p><strong>{CTO_DATA['rol']} en HormigasAIS</strong></p>
        <p>Arquitecto del Protocolo LBH_BINARY_V1. Identidad validada en nodo: <code>A16-SanMiguel-SV</code></p>
        <p>Firma de validación: <code>{firma[:32]}...</code></p>
    </article>
</body>
</html>"""

# Guardar en la ruta correcta
ruta_archivo = os.path.join("posts", "perfil_cto_cristhiam.html")
with open(ruta_archivo, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Perfil inyectado exitosamente en: {ruta_archivo}")
