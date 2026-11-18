import os, re, sys, html
repo, body_path = sys.argv[1], sys.argv[2]
SLUG = "baldor-de-la-habana-a-latinoamerica.html"
TITLE = "Baldor, de La Habana a las aulas de Latinoamérica: lo que dice la portada y lo que no"
DESC = "Qué dicen las fuentes sobre Aurelio Baldor, la portada con Al-Juarismi y el camino del Álgebra de Cuba a México y la región, con lo verificado, lo dudoso y lo pendiente."
ISO = "2026-11-18"
HUMAN = "18 de noviembre de 2026"
URL = "https://blog.hormigasais.com/posts/" + SLUG

out_html = os.path.join(repo, "posts", SLUG)
blog_js = os.path.join(repo, "scripts", "blog.js")
if not os.path.isdir(os.path.join(repo, "posts")) or not os.path.isfile(blog_js):
    sys.exit("FALLO: no parece el repo del blog")
if os.path.exists(out_html):
    sys.exit("FALLO: ya existe posts/" + SLUG)
body = open(body_path, encoding="utf-8").read()
if "{{" in body or "@@" in body:
    sys.exit("FALLO: el cuerpo tiene marcadores sin resolver")

SVG = """<svg viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ruta editorial: La Habana, Ciudad de México, aulas de la región">
  <rect width="800" height="200" fill="#111"/>
  <line x1="150" y1="100" x2="400" y2="100" stroke="#f5c518" stroke-width="2" stroke-dasharray="6 6"/>
  <line x1="400" y1="100" x2="650" y2="100" stroke="#00ff9f" stroke-width="2" stroke-dasharray="6 6"/>
  <circle cx="150" cy="100" r="16" fill="#f5c518"/><circle cx="400" cy="100" r="16" fill="#f5c518"/><circle cx="650" cy="100" r="16" fill="#00ff9f"/>
  <g font-family="Space Mono, monospace" font-size="14" fill="#ddd" text-anchor="middle">
    <text x="150" y="145">La Habana</text><text x="150" y="165" fill="#888">1941</text>
    <text x="400" y="145">Ciudad de México</text><text x="400" y="165" fill="#888">1948 (derechos)</text>
    <text x="650" y="145">Aulas de la región</text><text x="650" y="165" fill="#888">por documentar</text>
  </g>
  <text x="400" y="45" font-family="Syne, sans-serif" font-weight="800" font-size="22" fill="#f5c518" text-anchor="middle">Álgebra: ruta editorial</text>
</svg>"""

PAGE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>@@TITLE_E@@ | HormigasAIS</title>
<meta name="description" content="@@DESC_E@@">
<meta property="og:type" content="article">
<meta property="og:title" content="@@TITLE_E@@">
<meta property="og:description" content="@@DESC_E@@">
<meta property="og:url" content="@@URL@@">
<link rel="canonical" href="@@URL@@">
<link rel="stylesheet" href="../assets/style.css">
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">
<style>
  .post-content { max-width: 800px; margin: 0 auto; padding: 2.5rem 1.5rem; }
  .post-content h1 { font-family: 'Syne', sans-serif; font-weight: 800; color: #f5c518; font-size: 1.5rem; margin-bottom: 0.5rem; }
  .post-content h2 { font-family: 'Syne', sans-serif; color: #f5c518; font-size: 1.1rem; border-left: 3px solid #f5c518; padding-left: 10px; margin-top: 2rem; }
  .post-content p, .post-content ul, .post-content li { color: #aaa; font-size: 0.88rem; line-height: 1.8; }
  .post-content a { color: #f5c518; }
  .post-content figure { margin: 1.5rem 0; }
  .post-content svg { width: 100%; height: auto; border-radius: 8px; border: 1px solid #222; }
  .post-content table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.8rem; }
  .post-content th, .post-content td { border: 1px solid #222; padding: 0.55rem 0.7rem; color: #aaa; text-align: left; vertical-align: top; }
  .post-content th { color: #f5c518; background: #111; }
  .note-box { background: #111; border: 1px solid #00ff9f33; border-left: 4px solid #00ff9f; padding: 1rem; border-radius: 6px; margin: 1.5rem 0; font-size: 0.85rem; color: #aaa; line-height: 1.8; }
  .meta-tag { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.08em; color: #00ff9f; }
  .post-date { font-size: 0.75rem; color: #555; }
  .tags-box { margin-top: 2rem; font-size: 0.72rem; color: #555; }
</style>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Article","headline":"@@TITLE_J@@","description":"@@DESC_J@@","inLanguage":"es","datePublished":"@@ISO@@","mainEntityOfPage":"@@URL@@","author":{"@type":"Person","name":"Cristhiam Leonardo Hernández Quiñonez","url":"https://blog.hormigasais.com/posts/perfil_cto_cristhiam.html"},"publisher":{"@type":"Organization","name":"HormigasAIS","url":"https://hormigasais.com"}}
</script>
</head>
<body>

<nav>
  <a href="https://blog.hormigasais.com" style="font-family:'Syne',sans-serif;font-weight:800;color:#f5c518;text-decoration:none;">HormigasAIS</a>
  <div style="display:flex;gap:1.5rem;">
    <a href="https://hormigasais.com" style="font-size:0.78rem;color:#888;text-decoration:none;">Inicio</a>
    <a href="https://docs.hormigasais.com" style="font-size:0.78rem;color:#888;text-decoration:none;">Docs</a>
  </div>
</nav>

<article class="post-content">
  <header style="text-align: center;">
    <span class="meta-tag">INVESTIGACIÓN · HISTORIA EDITORIAL</span>
    <h1>@@TITLE_E@@</h1>
    <p class="post-date">@@HUMAN@@ | Nodo A16-SanMiguel-SV</p>
  </header>

  <figure>
@@SVG@@
  </figure>

@@BODY@@

  <p style="margin-top: 30px; color: #777; font-size: 0.85rem;">
    <em>Investigación y redacción: CLHQ | HormigasAIS</em>
  </p>

  <a href="../index.html" style="display:inline-block;margin-top:1rem;font-size:0.78rem;color:#555;text-decoration:none;">Volver al blog</a>
</article>
</body>
</html>
"""
jq = lambda s: s.replace("\\", "\\\\").replace('"', '\\"')
rep = {"@@TITLE_E@@": html.escape(TITLE), "@@DESC_E@@": html.escape(DESC, quote=True),
       "@@TITLE_J@@": jq(TITLE), "@@DESC_J@@": jq(DESC), "@@URL@@": URL,
       "@@ISO@@": ISO, "@@HUMAN@@": HUMAN, "@@SVG@@": SVG, "@@BODY@@": body.rstrip("\n")}
page = PAGE
for k, v in rep.items():
    page = page.replace(k, v)
if "@@" in page:
    sys.exit("FALLO: quedaron marcadores sin sustituir")

js = open(blog_js, encoding="utf-8").read()
ms = list(re.finditer(r"const posts = \[(.*?)\n  \];", js, re.S))
if len(ms) != 1:
    sys.exit("FALLO: no encontre la lista de posts en blog.js exactamente una vez")
if SLUG in js:
    sys.exit("FALLO: blog.js ya menciona " + SLUG)
m = ms[0]
ent = m.group(1).rstrip()
new_ent = ent + ("" if ent.endswith(",") else ",") + "\n    '" + SLUG + "'"
js2 = js[:m.start(1)] + new_ent + js[m.end(1):]

open(out_html, "w", encoding="utf-8").write(page)
open(blog_js, "w", encoding="utf-8").write(js2)
print("OK posts/" + SLUG + "  (" + str(len(page)) + " bytes)")
print("OK scripts/blog.js: post anadido al final de la lista")
