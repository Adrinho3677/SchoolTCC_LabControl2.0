document.addEventListener('DOMContentLoaded', function() {
    const devolverButtons = document.querySelectorAll('.btn-primary[data-bs-toggle="modal"]');

    devolverButtons.forEach(button => {
        button.addEventListener('click', function() {
            const relatorioId = this.getAttribute('href').split('/').pop(); // Extrai o ID do href
            document.getElementById('relatorio_id').value = relatorioId; // Define o ID no input oculto
            
            // Atualiza a ação do formulário com o ID do relatório
            document.getElementById('devolucaoForm').action = '/devolver_comp/' + relatorioId + '';
        });
    });

    document.getElementById('submitDevolucao').addEventListener('click', function() {
        document.getElementById('devolucaoForm').submit(); // Envia o formulário
    });
});