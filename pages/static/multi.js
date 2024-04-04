document.addEventListener("DOMContentLoaded", function() {
    // Función para cargar el video de fondo
    function cargarVideoDeFondo() {
        // Obtener el elemento de video
        var video = document.querySelector(".video-background video");
        if (video) {
            // Comprobar si el video está disponible
            if (video.canPlayType("video/mp4")) {
                // Establecer la ruta del video
                video.src = "media/videos/Portfolio_Presentation.mp4";
                // Reproducir el video automáticamente y en bucle
                video.autoplay = true;
                video.loop = true;
                // Desactivar el sonido del video
                video.muted = true;
            }
        }
    }

    // Llamar a la función para cargar el video de fondo
    cargarVideoDeFondo();
});