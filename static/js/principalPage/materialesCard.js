document.addEventListener('DOMContentLoaded', function () {
    const enlaces = document.querySelectorAll('.enlace');
    const tarjetas = document.querySelectorAll('.tarjeta');

    // Verifica si hay al menos una tarjeta antes de intentar acceder a la primera
    if (tarjetas.length > 0) {
        tarjetas[0].style.display = 'block';
    }

    enlaces.forEach(function (enlace) {
        enlace.addEventListener('click', function (event) {
            event.preventDefault(); // Evita el comportamiento predeterminado del enlace

            const target = this.getAttribute('data-target');

            tarjetas.forEach(function (tarjeta) {
                // Verifica si la tarjeta actual tiene el ID que estamos buscando
                if (tarjeta.id === target) {
                    tarjeta.style.display = 'block';
                } else {
                    tarjeta.style.display = 'none';
                }
            });
        });
    });
});
