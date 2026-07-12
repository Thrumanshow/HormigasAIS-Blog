// Motor del Blog HormigasAIS
document.addEventListener('DOMContentLoaded', () => {
  const feed = document.getElementById('feed');
  
  // Registro de artículos publicados (lectura de directorio estática)
  const posts = [
    'uroboro-tecnologico.html' // Aquí agregarás futuros artículos
  ];

  // Cargar cada artículo de forma asíncrona
  posts.forEach(file => {
    fetch(`posts/${file}`)
      .then(res => {
        if (!res.ok) throw new Error(`Error al cargar ${file}`);
        return res.text();
      })
      .then(html => {
        const article = document.createElement('article');
        article.className = 'post-card';
        // Estilo base alineado a tu tarjeta principal (Soberano)
        article.style.cssText = 'border: 1px solid #333; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px; background: #111; transition: border-color 0.3s;';
        article.onmouseover = () => article.style.borderColor = '#f5c518';
        article.onmouseout = () => article.style.borderColor = '#333';
        article.innerHTML = html;
        feed.appendChild(article);
      })
      .catch(err => console.error(err));
  });
});
