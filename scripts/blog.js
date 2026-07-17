document.addEventListener("DOMContentLoaded", async () => {
    const feed = document.getElementById('feed');
    if (!feed) return;

    const posts = [
        'uroboro-tecnologico.html',
        'protocolo-lbh-arquitectura.html',
        // 'perfil_cto_cristhiam.html'  // Descomenta cuando exista
    ];

    for (const file of posts) {
        try {
            const response = await fetch(`posts/${file}`);
            if (!response.ok) continue;

            const text = await response.text();
            const parser = new DOMParser();
            const doc = parser.parseFromString(text, 'text/html');

            // Título más robusto
            const title = doc.querySelector('h1, h2')?.textContent?.trim() 
                       || doc.title 
                       || 'Sin título';

            // Excerpt (resumen)
            const excerpt = doc.querySelector('article p, p')?.textContent?.trim().slice(0, 160) + '...' 
                         || 'Sin descripción disponible.';

            // Firma HMAC (más flexible)
            const firmaMatch = text.match(/[a-f0-9]{32,64}/i);
            const firma = firmaMatch 
                ? firmaMatch[0].slice(0, 24) + '...' 
                : 'Sin firma LBH';

            const card = document.createElement('div');
            card.className = 'post-card';

            card.innerHTML = `
                <div class="card-header">
                    <span class="node-badge">NODO A16</span>
                    <span class="file-name">${file.replace('.html', '')}</span>
                </div>
                <h2 class="post-title">${title}</h2>
                <p class="post-excerpt">${excerpt}</p>
                <div class="firma">🔐 <span>${firma}</span></div>
                <a href="posts/${file}" class="btn-acceder">Leer artículo →</a>
            `;

            feed.appendChild(card);

        } catch (e) {
            console.error(`Error cargando post ${file}:`, e);
        }
    }
});