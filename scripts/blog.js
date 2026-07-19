document.addEventListener("DOMContentLoaded", async () => {
  const feed = document.getElementById('feed');
  if (!feed) return;

  const posts = [
    'uroboro-tecnologico.html',
    'arquitectura-soberana-agentes-autonomos.html',
    'lbh-sdk-js-v031.html'
  ];

  for (const file of posts) {
    try {
      const response = await fetch(`posts/${file}`);
      if (!response.ok) continue;

      const text = await response.text();
      const parser = new DOMParser();
      const doc = parser.parseFromString(text, 'text/html');

      const titleEl = doc.querySelector('h1, h2');
      const title = titleEl ? titleEl.textContent.trim() : 'Sin título';

      const excerptEl = doc.querySelector('p');
      let excerpt = excerptEl ? excerptEl.textContent.trim().slice(0, 160) : '';
      if (excerpt) excerpt += '...';

      const card = document.createElement('div');
      card.className = 'post-card';
      card.innerHTML = `
        <div class="post-meta">NODO A16 · ${file.replace('.html','')}</div>
        <div class="post-title">${title}</div>
        <div class="post-excerpt">${excerpt}</div>
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #333; display:flex; justify-content:space-between;">
          <a href="posts/${file}" style="color:#f5c518; font-weight:700;">Leer artículo →</a>
          <button onclick="compartirArticulo('${title}', '${file}')" style="padding:8px 16px; background:#f5c518; color:#000; border:none; border-radius:6px; cursor:pointer;">🚀 Compartir</button>
        </div>
      `;
      feed.appendChild(card);
    } catch (e) {
      console.error("Error cargando post:", file, e);
    }
  }
});

window.compartirArticulo = async (title, file) => {
  const url = window.location.origin + window.location.pathname.replace('index.html','') + 'posts/' + file;
  const shareData = { title: title, text: "Artículo de HormigasAIS", url: url };
  try {
    if (navigator.share) await navigator.share(shareData);
    else {
      await navigator.clipboard.writeText(url);
      alert("✅ Enlace copiado");
    }
  } catch (err) {}
};
