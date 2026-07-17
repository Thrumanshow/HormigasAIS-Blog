
document.addEventListener("DOMContentLoaded", async () => {
    const feed = document.getElementById('feed');
    const posts = [
        'uroboro-tecnologico.html',
        'protocolo-lbh-arquitectura.html',
        'arquitectura-soberana-agentes-autonomos.html'
    ];

    for (const file of posts) {
        try {
            const response = await fetch(`posts/${file}`);
            if (!response.ok) continue;
            const text = await response.text();

            const parser = new DOMParser();
            const doc = parser.parseFromString(text, 'text/html');

            const title = doc.querySelector('h1, h2')?.textContent?.trim() || 'Sin título';
            const firmaMatch = text.match(/[a-f0-9]{32,64}/);
            const firma = firmaMatch ? firmaMatch[0].slice(0,32) + '...' : 'Sin firma LBH';

            const card = document.createElement('div');
            card.className = 'post-card';
            card.innerHTML = `
                <div class="post-meta">NODO A16 · ${file.replace('.html','')}</div>
                <div class="post-title">${title}</div>
                <div class="post-firma"><code>${firma}</code></div>
                <a href="posts/${file}" style="color:#f5c518;font-size:0.78rem;text-decoration:none;">
                Leer artículo →
                </a>
            `;
            feed.appendChild(card);
        } catch (e) {
            console.error("Error cargando post:", e);
        }
    }
});
