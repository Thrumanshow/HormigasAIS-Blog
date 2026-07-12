#!/data/data/com.termux/files/usr/bin/bash
# ============================================================
# 🐜 HormigasAIS — fix_blog.sh
# Corrige y completa la estructura del blog:
#   - assets/style.css     (estilos soberanos)
#   - index.html           (limpio, sin duplicados)
#   - posts/uroboro.html   (errores tipográficos corregidos)
#   - .nojekyll            (GitHub Pages sin Jekyll)
# ============================================================

set -uo pipefail

echo "🐜 Corrigiendo y completando HormigasAIS-Blog..."
echo "------------------------------------------------------------"

# ── 1. assets/style.css ──────────────────────────────────────
python3 << 'PYEOF'
css = """@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@700;800&display=swap');

* { box-sizing: border-box; }

body {
  background: #0a0a0a;
  color: #e8e8e8;
  font-family: 'Space Mono', monospace;
  margin: 0;
  padding: 0;
}

/* NAV */
nav {
  background: #000;
  border-bottom: 1px solid #1a1a1a;
  padding: 1rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 100;
}
.nav-brand {
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: 1.1rem;
  color: #f5c518;
  text-decoration: none;
}
.nav-links { display: flex; gap: 1.5rem; }
.nav-links a {
  font-size: 0.78rem;
  color: #888;
  text-decoration: none;
}
.nav-links a:hover { color: #f5c518; }

/* WRAPPER */
.wrapper { max-width: 800px; margin: 0 auto; padding: 3rem 1.5rem; }

/* HEADER */
.blog-header { margin-bottom: 2.5rem; border-bottom: 1px solid #1a1a1a; padding-bottom: 2rem; }
.blog-title {
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: 1.6rem;
  color: #f5c518;
  margin-bottom: 0.4rem;
}
.blog-subtitle { font-size: 0.8rem; color: #555; }

/* TARJETA DE IDENTIDAD */
.identity-card {
  background: #111;
  border: 1px solid #222;
  border-radius: 12px;
  padding: 1.2rem 1.5rem;
  margin-bottom: 2rem;
  font-size: 0.78rem;
  color: #555;
  display: flex;
  align-items: center;
  gap: 1rem;
}
.identity-card a { color: #f5c518; text-decoration: none; }
.identity-card a:hover { text-decoration: underline; }

/* FEED DE ARTÍCULOS */
#feed { margin-top: 1rem; }

.post-card {
  border: 1px solid #222;
  padding: 1.8rem;
  margin-bottom: 1.5rem;
  border-radius: 12px;
  background: #111;
  transition: border-color 0.2s ease;
}
.post-card:hover { border-color: #f5c518; }

.post-meta {
  font-size: 0.7rem;
  color: #555;
  margin-bottom: 0.6rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.post-category {
  display: inline-block;
  background: rgba(0,255,159,0.06);
  border: 1px solid rgba(0,255,159,0.2);
  color: #00ff9f;
  border-radius: 4px;
  padding: 0.1rem 0.5rem;
  font-size: 0.65rem;
  margin-left: 0.5rem;
}
.post-title {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 1.1rem;
  color: #fff;
  margin-bottom: 0.8rem;
  line-height: 1.4;
}
.post-excerpt { font-size: 0.8rem; color: #888; line-height: 1.7; margin-bottom: 1rem; }
.post-footer {
  font-size: 0.7rem;
  color: #444;
  border-top: 1px solid #1a1a1a;
  padding-top: 0.8rem;
  margin-top: 1rem;
}

/* FOOTER */
.site-footer {
  font-size: 0.7rem;
  color: #555;
  margin-top: 3rem;
  border-top: 1px solid #1a1a1a;
  padding-top: 1rem;
  text-align: right;
}
.site-footer a { color: #555; text-decoration: none; }
.site-footer a:hover { color: #888; }

/* Estilos para contenido de artículos cargados por JS */
#feed h2 { color: #f5c518; font-family: 'Syne', sans-serif; font-size: 1.2rem; margin-top: 0; }
#feed h3 { color: #f5c518; font-size: 1rem; border-left: 3px solid #f5c518; padding-left: 10px; }
#feed p { color: #888; font-size: 0.82rem; line-height: 1.7; }
#feed code { background: #1a1a1a; padding: 2px 5px; border-radius: 4px; font-size: 0.8rem; }
#feed blockquote, #feed p[style*="italic"] {
  background: #1a1a1a;
  border-left: 2px solid #f5c518;
  padding: 1rem;
  border-radius: 6px;
  font-style: italic;
}
"""

with open("assets/style.css", "w", encoding="utf-8") as f:
    f.write(css)
print("✅ assets/style.css creado")
PYEOF

# ── 2. index.html limpio ─────────────────────────────────────
python3 << 'PYEOF'
html = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bitácora de la Colonia — HormigasAIS</title>
  <meta property="og:title" content="Bitácora de la Colonia — HormigasAIS">
  <meta property="og:description" content="Blog soberano del ecosistema HormigasAIS. Inteligencia distribuida, protocolo LBH y edge computing desde El Salvador.">
  <meta property="og:image" content="https://raw.githubusercontent.com/Thrumanshow/Thrumanshow/main/logo_soberano_hd.png">
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>

<nav>
  <a href="https://hormigasais.com" class="nav-brand">🐜 HormigasAIS</a>
  <div class="nav-links">
    <a href="https://hormigasais.com">Inicio</a>
    <a href="https://docs.hormigasais.com/sdk.html">SDK</a>
    <a href="https://docs.hormigasais.com">Docs</a>
  </div>
</nav>

<div class="wrapper">

  <div class="blog-header">
    <div class="blog-title">🐜 Bitácora de la Colonia</div>
    <div class="blog-subtitle">
      Inteligencia soberana en el borde · Protocolo LBH · Edge Computing desde El Salvador
    </div>
  </div>

  <div class="identity-card">
    <img src="https://raw.githubusercontent.com/Thrumanshow/Thrumanshow/main/logo_soberano_hd.png"
         alt="HormigasAIS" style="width:40px;height:40px;border-radius:50%;border:1px solid #f5c518;">
    <div>
      Nodo A16-SanMiguel-SV ·
      <a href="https://docs.hormigasais.com">Ecosistema</a> ·
      <a href="https://docs.hormigasais.com/institucionalidad.html">Institucionalidad</a> ·
      <a href="https://docs.hormigasais.com/sdk.html">SDK</a>
    </div>
  </div>

  <div id="feed">
    <!-- Los artículos se cargan dinámicamente desde posts/ -->
  </div>

  <div class="site-footer">
    CERT::LBH-BLOG-V1-CLHQ | Nodo A16-SanMiguel-SV<br>
    <a href="https://hormigasais.com">hormigasais.com</a> ·
    <a href="https://docs.hormigasais.com/legal.html">⚖️ Legal</a>
  </div>

</div>

<script src="scripts/blog.js"></script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("✅ index.html reconstruido (sin duplicados)")
PYEOF

# ── 3. Corregir errores tipográficos en el artículo ──────────
python3 << 'PYEOF'
ruta = "posts/uroboro-tecnologico.html"
with open(ruta, "r", encoding="utf-8") as f:
    contenido = f.read()

correcciones = {
    "Cerrar el ínculo":       "Cerrar el vínculo",
    "polí4ica":               "política",
    "ingenieria":             "ingeniería",
    "autarquia":              "autarquía",
    "Santo Gral":             "Santo Grial",
    "autentificar":           "autenticar",
    "propietaa cabeza":       "propietarios. La cabeza",
}

cambios = 0
for viejo, nuevo in correcciones.items():
    if viejo in contenido:
        contenido = contenido.replace(viejo, nuevo)
        cambios += 1

with open(ruta, "w", encoding="utf-8") as f:
    f.write(contenido)

print(f"✅ uroboro-tecnologico.html corregido ({cambios} correcciones)")
PYEOF

# ── 4. .nojekyll para GitHub Pages ───────────────────────────
touch .nojekyll
echo "✅ .nojekyll creado (GitHub Pages sin Jekyll)"

# ── 5. Verificación ──────────────────────────────────────────
echo ""
echo "🔍 Estado del repo:"
ls -la
echo ""
echo "🔍 assets/:"
ls assets/
echo ""
echo "🔍 posts/:"
ls posts/

# ── 6. Commit y push ─────────────────────────────────────────
source "$HOME/.hormigas_secrets" 2>/dev/null || true

git remote set-url origin https://Thrumanshow:${HORMIGAS_TOKEN}@github.com/Thrumanshow/HormigasAIS-Blog.git

git add .
git commit -m "🐜 FIX: blog completo — style.css, index.html limpio, errores tipográficos corregidos, .nojekyll"
git push origin main

echo ""
echo "------------------------------------------------------------"
echo "✅ HormigasAIS-Blog corregido y publicado"
echo ""
echo "PRÓXIMO PASO:"
echo "  Activar GitHub Pages en el repo:"
echo "  Settings → Pages → Source: main / (root)"
echo "------------------------------------------------------------"

