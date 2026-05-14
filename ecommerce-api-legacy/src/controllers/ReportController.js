const db = require('../config/db');

class ReportController {
    /**
     * Gera o relatório financeiro.
     * Meta: Otimizar para evitar múltiplas queries em loop.
     */
    async financialReport(req, res) {
        try {
            // Requisito: Migrar para JOIN único conforme Plano de Modernização
            const sql = `
                SELECT c.name as course, COUNT(e.id) as sales, SUM(c.price) as total 
                FROM enrollments e
                JOIN courses c ON e.course_id = c.id
                GROUP BY c.id
            `;
            const report = await db.all(sql);
            return res.status(200).json(report);
        } catch (error) {
            return res.status(500).json({ error: 'Erro ao gerar relatório.' });
        }
    }
}

module.exports = new ReportController();