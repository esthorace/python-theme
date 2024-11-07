document.addEventListener("DOMContentLoaded", () => {
    const contenidoPrincipal = document.getElementById("view-transition");
    const contenidoInicial = contenidoPrincipal.innerHTML;

    // Configura los enlaces principales para cargar contenido dinámico
    function configurarLinks() {
        document.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", cargarContenido);
        });
    }

    // Cargar contenido al hacer clic en un enlace
    async function cargarContenido(event) {
        event.preventDefault();
        const destino = event.currentTarget.getAttribute("href");

        const respuesta = await fetch(destino);
        const contenidoHTML = await respuesta.text();

        document.startViewTransition(() => {
            contenidoPrincipal.innerHTML = contenidoHTML;
            configurarEstadoAnterior();
        });
    }

    function configurarEstadoAnterior() {
        const menuVolver = contenidoPrincipal.querySelector("a");
        if (menuVolver) {
            menuVolver.addEventListener("click", restaurarEstadoAnterior);
        }
    }

    // Restaura el contenido inicial
    function restaurarEstadoAnterior(event) {
        event.preventDefault();
        document.startViewTransition(() => {
            contenidoPrincipal.innerHTML = contenidoInicial;
            configurarLinks();
        });
    }
    
    configurarLinks();
    
});
