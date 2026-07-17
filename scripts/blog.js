document.addEventListener("DOMContentLoaded", async () => {
  const feed = document.getElementById('feed');
  if (!feed) return;

  const posts = [
    'uroboro-tecnologico.html',
    'protocolo-lbh-arquitectura.html'
    // Agrega aquí nuevos artículos
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

      // Extraer primer párrafo para excerpt
      const excerptEl = doc.querySelector('p');
      let excerpt = excerptEl ? excerptEl.textContent.trim().slice(0, 160) : '';
      if (excerpt) excerpt += '...';

      const firmaMatch = text.match(/[a-f0-9]{32,64}/i);
      const firma = firmaMatch ? firmaMatch[0].slice(0, 24) + '...' : 'Sin firma';

      const card = document.createElement('div');
      card.className = 'post-card';
      card.innerHTML = `
        <div class="post-meta">NODO A16 · ${file.replace('.html', '')}</div>
        <div class="post-title">${title}</div>
        <div class="post-excerpt">${excerpt}</div>
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #333;">
          <a href="posts/${file}" style="color:#f5c518; font-weight:700;">Leer artículo →</a>
        </div>
      `;
      feed.appendChild(card);
    } catch (e) {
      console.error("Error cargando post:", file, e);
    }
  }
});
