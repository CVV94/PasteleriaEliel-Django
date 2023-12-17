var estado = '{% if envio %}{{ envio.id_estadoenvio.nombre }}{% endif %}';  
var progressBar = document.getElementById('progressBar');  
var progressMarker = document.getElementById('progressMarker');  

switch (estado) {
    case 'P':
        progressBar.value = 33;
        progressMarker.style.left = "33%";
        break;
    case 'E':
        progressBar.value = 66;
        progressMarker.style.left = "66%";
        break;
    case 'R':
        progressBar.value = 100;
        progressMarker.style.left = "100%";
        break;
    default:
        progressBar.value = 0;
        progressMarker.style.left = "0%";
}