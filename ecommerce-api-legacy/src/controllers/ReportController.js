const db = require('../config/db');

class ReportController {
    /**
     * Gera o relatório financeiro administrativo.
     * * Refatoração: Substitui múltiplas consultas ao banco por um JOIN único,
     * otimizando a performance para grandes volumes de dados.
     */
    async financialReport(req, res) {
        try {
            // Requisito de Modernização: Uso de Agregação SQL (JOIN, COUNT, SUM)
            // Isso evita o anti-padrão de buscar cursos e depois contar matrículas uma a uma.
            const sql = `
                SELECT 
                    c.name as course, 
                    COUNT(e.id) as sales, 
                    SUM(c.price) as total 
                FROM enrollments e
                JOIN courses c ON e.course_id = c.id
                GROUP BY c.id
            `;

            const report = await db.all(sql);

            // Retorno estruturado seguindo o padrão RESTful
            return res.status(200).json(report);

        } catch (error) {
            // Proteção de Auditoria: Log interno e resposta genérica ao cliente
            console.error('Erro ao gerar relatório financeiro:', error);
            return res.status(500).json({ error: 'Erro interno ao gerar o relatório.' });
        }
    }
}

module.exports = new ReportController();