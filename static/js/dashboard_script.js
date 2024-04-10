function carregarDashboard() {
    // Faça uma requisição AJAX para buscar os dados do Dashboard
    fetch("{% url 'dashboard_data' %}")
        .then(response => response.json())
        .then(data => {
            // Limpe os dados antigos da tabela
            document.querySelector("#dashboard-table tbody").innerHTML = "";

            // Preencha a tabela com os novos dados
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
                document.querySelector("#dashboard-table tbody").insertAdjacentHTML("beforeend", row);
            });
        })
        .catch(error => console.error("Erro ao carregar dados do Dashboard:", error));
}