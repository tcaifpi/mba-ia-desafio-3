const User = require('../models/User');
const db = require('../config/db'); // Importa o helper de Promises que criamos

class CheckoutController {
    async handle(req, res) {
        try {
            // Desestruturação com nomes claros (corrigindo o erro de "Variaveis Curtas")
            const { name, email, password, courseId, paymentMethod } = req.body;

            // 1. Validação de entrada (Requisito de Auditoria: LOW/MEDIUM)
            if (!email || !password || !courseId) {
                return res.status(400).json({ error: 'Dados obrigatórios ausentes.' });
            }

            // 2. Lógica de Usuário 
            // Buscamos se o usuário já existe para não duplicar no banco
            let user = await User.findByEmail(email);
            
            if (!user) {
                // Se não existe, criamos um novo (Com hashing seguro via Model)
                const userId = await User.create({ name, email, password });
                user = { id: userId, email };
            }

            // 3. Simulação de Integração de Pagamento (Requisito: Desacoplamento)
            // Em um sistema real, aqui chamaríamos um Service de Pagamento (ex: Stripe)
            const paymentAuthorized = true; 

            if (!paymentAuthorized) {
                return res.status(402).json({ error: 'Pagamento não autorizado.' });
            }

            // 4. Registro da Matrícula (Enrollment)
            // Uso de parametrização para evitar SQL Injection
            const enrollmentSql = `INSERT INTO enrollments (user_id, course_id, status) VALUES (?, ?, ?)`;
            await db.run(enrollmentSql, [user.id, courseId, 'active']);

            // 5. Resposta Sucesso
            return res.status(201).json({
                message: 'Matrícula realizada com sucesso!',
                user: user.email,
                courseId: courseId
            });

        } catch (error) {
            console.error('Erro crítico no Checkout:', error);
            // Proteção: Não expõe detalhes do erro/banco ao cliente final
            return res.status(500).json({ error: 'Erro interno ao processar checkout.' });
        }
    }
}

module.exports = new CheckoutController();