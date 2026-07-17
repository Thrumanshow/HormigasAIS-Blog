document.addEventListener("DOMContentLoaded", () => {

  const buttons = document.querySelectorAll(".lbh-share");

  if (!buttons.length) return;

  buttons.forEach(button => {

    button.addEventListener("click", async () => {

      const shareData = {
        title: document.title,
        text: "Mira este artículo de HormigasAIS:",
        url: window.location.href
      };

      try {

        if (navigator.share) {

          await navigator.share(shareData);

          console.log("✅ Compartido correctamente");

        } else {

          await navigator.clipboard.writeText(window.location.href);

          button.innerText = "✅ Enlace copiado";

          setTimeout(() => {
            button.innerText = "🚀 Compartir este artículo";
          }, 2500);

        }

      } catch(err) {

        console.error("LBH Share:", err);

      }

    });

  });

});
