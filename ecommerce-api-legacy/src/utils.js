/**
 * Utilitários de Integração e Segurança
 * Requisito: Todos os segredos devem vir do ambiente (.env)
 */
module.exports = {
    // Chaves de API removidas do código-fonte (Saneamento de Hardcoded Secrets)
    PAYMENT_GATEWAY_KEY: process.env.PAYMENT_GATEWAY_KEY,
    STRIPE_SECRET: process.env.STRIPE_SECRET,
    
    // Helper de log padronizado para a aplicação
    logAction: (action, details) => {
        const timestamp = new Date().toISOString();
        console.log(`[${timestamp}] ACTION: ${action} | DETAILS: ${details}`);
    }
};