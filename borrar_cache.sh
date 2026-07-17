#!/data/data/com.termux/files/usr/bin/bash

echo "🧹 Limpiando caché del navegador..."

# Chrome
rm -rf /data/data/com.android.chrome/cache/* 2>/dev/null
rm -rf /data/data/com.android.chrome/app_cache/* 2>/dev/null

# WebView (usado por Chrome y otros navegadores)
rm -rf /data/data/com.android.webview/cache/* 2>/dev/null

# Opcional: más agresivo (descomenta si es necesario)
# rm -rf /data/data/com.android.chrome/app_chrome/Default/Cache/* 2>/dev/null

echo "✅ Caché borrado exitosamente."
echo "========================================"
echo "Ahora abre Chrome → Activa 'Sitio de escritorio'"
echo "y refresca la página."
