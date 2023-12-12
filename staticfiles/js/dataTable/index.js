$(document).ready(function() {
    let dataTable;
    let dataTableIsInitialized = false;

    const initDataTable = async () => {
        if (dataTableIsInitialized) {
            dataTable.destroy();
        }
        dataTable = $('#datatable-products').DataTable({
            // Configuración en español
            language: {
                "url": "//cdn.datatables.net/plug-ins/1.11.5/i18n/Spanish.json"
            }
        });
        dataTableIsInitialized = true;
    };

    window.addEventListener('load', async () => {
        await initDataTable();
    });
});