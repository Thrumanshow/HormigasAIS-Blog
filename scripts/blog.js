document.addEventListener("DOMContentLoaded", async () => {
  const feed = document.getElementById('feed');
  if (!feed) return;

  const posts = [
    'uroboro-tecnologico.html',
    'protocolo-lbh-arquitectura.html',
    'arquitectura-soberana-agentes-autonomos.html',
    'perfil_cto_cristhiam.html',
    'lbh-sdk-js-v031.html'
  ];

  for (const file of posts) {
    try {
      const response = await fetch(`posts/${file}`);
      if (!response.ok) continue;

      const text = await response.text();
      const parser = new DOMParser();
      const doc = parser.parseFromString(text, 'text/html');

      let titleEl = doc.querySelector('h1, h2');
      const title = titleEl ? titleEl.textContent.trim() : 'Sin título';

      let excerptEl = doc.querySelector('p');
      let excerpt = excerptEl ? excerptEl.textContent.trim().slice(0, 160) : '';
      if (excerpt) excerpt += '...';

      const card = document.createElement('div');
      card.className = 'post-card';
      card.style.cssText = `
        border: 1px solid #333; 
        padding: 1.8rem; 
        margin-bottom: 2rem; 
        border-radius: 12px; 
        background: #111;
      `;

      card.innerHTML = `
        <div class="post-meta" style="color:#888; font-size:0.75rem; margin-bottom:0.8rem;">
          NODO A16 · ${file.replace('.html','')}
        </div>
        <div class="post-title" style="color:#f5c518; font-size:1.3rem; margin-bottom:1rem; line-height:1.4;">
          ${title}
        </div>
        <div class="post-excerpt" style="color:#aaa; line-height:1.7; margin-bottom:1.2rem;">
          ${excerpt}
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; padding-top:1rem; border-top:1px solid #333;">
          <a href="posts/${file}" style="color:#f5c518; font-weight:700; text-decoration:none;">
            Leer artículo →
          </a>
          <button onclick="compartirArticulo('${title.replace(/'/g, '')}', '${file}')" 
                  style="padding:9px 20px; background:#f5c518; color:#000; border:none; border-radius:8px; cursor:pointer; font-size:0.9rem;">
            🚀 Compartir
          </button>
        </div>
      `;
      feed.appendChild(card);
    } catch (e) {
      console.error("Error cargando post:", file, e);
    }
  }
});

window.compartirArticulo = async (title, file) => {
  const baseUrl = window.location.origin + window.location.pathname.replace('index.html','');
  const url = baseUrl + 'posts/' + file;
  const shareData = { title: title, text: "Artículo de HormigasAIS", url: url };
  try {
    if (navigator.share) await navigator.share(shareData);
    else {
      await navigator.clipboard.writeText(url);
      alert("✅ Enlace copiado");
    }
  } catch (err) {}
};
