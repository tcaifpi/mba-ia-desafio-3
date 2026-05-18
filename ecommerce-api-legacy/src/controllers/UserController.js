const User = require('../models/User');

class UserController {
    /**
     * Elimina um utilizador de forma segura.
     * Resolve a vulnerabilidade [CRITICAL] de SQL Injection através da Model.
     */
    async deleteUser(req, res) {
        try {
            const { id } = req.params;

            // 1. Validação de Parâmetros
            if (!id) {
                return res.status(400).json({ error: 'ID do utilizador é obrigatório.' });
            }

            // 2. Chamada à Model (Abstração de Dados)
            // A Model User.js encarrega-se de usar Prepared Statements
            const deleted = await User.delete(id); 

            if (!deleted) {
                return res.status(404).json({ error: 'Utilizador não encontrado.' });
            }

            // 3. Resposta de Sucesso (Padrão RESTful)
            return res.status(200).json({ message: 'Utilizador removido com sucesso.' });

        } catch (error) {
            // Proteção: Log interno detalhado, resposta externa genérica
            console.error(`Erro ao eliminar utilizador ${req.params.id}:`, error);
            return res.status(500).json({ error: 'Erro interno ao processar a eliminação.' });
        }
    }
}

module.exports = new UserController();