const User = require('../models/User');

class UserController {
    /**
     * Deleta um usuário de forma segura usando parametrização.
     * Resolve a vulnerabilidade CRITICAL identificada na auditoria.
     */
    async deleteUser(req, res) {
        try {
            const { id } = req.params;
            
            // Requisito de Auditoria: Uso de Models para abstração
            const deleted = await User.delete(id); 

            if (!deleted) {
                return res.status(404).json({ error: 'Usuário não encontrado.' });
            }

            return res.status(200).json({ message: 'Usuário removido com sucesso.' });
        } catch (error) {
            return res.status(500).json({ error: 'Erro ao deletar usuário.' });
        }
    }
}

module.exports = new UserController();