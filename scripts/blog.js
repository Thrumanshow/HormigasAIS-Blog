
document.addEventListener("DOMContentLoaded", async () => {
    const feed = document.getElementById('feed');
    // ACTUALIZA ESTA LISTA CADA VEZ QUE SUBAS UN NUEVO POST
    const posts = [
        'uroboro-tecnologico.html', 
        'protocolo-lbh-arquitectura.html', 
        'perfil_cto_cristhiam.html'
    ];
    
    for (const file of posts) {
        try {
            const response = await fetch(`posts/${file}`);
            if (!response.ok) continue;
            const text = await response.text();
            
            const parser = new DOMParser();
            const doc = parser.parseFromString(text, 'text/html');
            const title = doc.querySelector('h1')?.innerText || 'Sin título';
            const firmaMatch = text.match(/<code>([a-f0-9]{32})/);
            const firma = firmaMatch ? firmaMatch[1] + '...' : 'Sin firma';

            const card = document.createElement('div');
            card.className = 'post-card';
            card.innerHTML = `
                <div class="post-meta">NODO A16 | ${file}</div>
                <div class="post-title">${title}</div>
                <div class="post-excerpt">Firma soberana: <code>${firma}</code></div>
                <a href="posts/${file}" style="color:#f5c518; font-size:0.7rem;">[ACCEDER AL NODO]</a>
            `;
            feed.appendChild(card);
        } catch (e) {
            console.error("Error cargando post:", e);
        }
    }
});
