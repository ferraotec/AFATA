const dashboardDataUrl = "/dashboard_data/";
// Função para exibir o formulário de cadastro e ocultar a tabela do dashboard
function exibirCadastro() {
    document.getElementById("cadastro-form").style.display = "block";
    document.getElementById("dashboard-table").style.display = "none";
}

// Função para exibir a tabela do dashboard e ocultar o formulário de cadastro
function exibirDashboard() {
    fetch(dashboardDataUrl)
        .then(response => response.json())
        .then(data => preencherTabelaDashboard(data))
        .catch(error => console.error("Erro ao carregar dados do Dashboard:", error));
}


// Função para preencher a tabela do dashboard com os dados recebidos da requisição AJAX
function preencherTabelaDashboard(data) {
    const tbody = document.querySelector("#dashboard-table tbody");
    tbody.innerHTML = ""; // Limpa os dados antigos da tabela

    data.liderancas.forEach(lideranca => {
        const row = `
            <tr>
                <td>${lideranca.id}</td>
                <td>${lideranca.nome}</td>
                <td>${lideranca.data_nascimento}</td>
                <td>${lideranca.sexo}</td>
                <td>${lideranca.estado_civil}</td>
                <td>${lideranca.endereco}</td>
                <td>${lideranca.regiao_atuante}</td>
                <td>${lideranca.assessor_coordenador}</td>
                <td>${lideranca.informacoes_gerais}</td>
            </tr>
        `;
        tbody.insertAdjacentHTML("beforeend", row);
    });

    // Exibe a tabela do dashboard e oculta o formulário de cadastro
    document.getElementById("cadastro-form").style.display = "none";
    document.getElementById("dashboard-table").style.display = "block";
}

// Adicione event listeners aos links do menu para chamar as funções apropriadas
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("cadastro-link").addEventListener("click", exibirCadastro);
    document.getElementById("dashboard-link").addEventListener("click", exibirDashboard);
});
