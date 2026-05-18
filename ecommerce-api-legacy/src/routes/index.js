const express = require('express');
const router = express.Router();

// Importações Estruturadas: Cada controller no seu domínio
const CheckoutController = require('../controllers/CheckoutController');
const ReportController = require('../controllers/ReportController');
const UserController = require('../controllers/UserController');

/**
 * Mapeamento de Rotas RESTful
 * Resolve o débito técnico de "Endpoints Não Padronizados"
 */

// Rota de Checkout - Criação de Recurso (Matrícula)
router.post('/api/checkout', (req, res) => CheckoutController.handle(req, res));

// Rota Administrativa - Relatórios (Otimizada com JOIN)
router.get('/api/admin/financial-report', (req, res) => ReportController.financialReport(req, res));

// Rota de Utilizadores - Eliminação Segura (Prevenção de SQL Injection)
router.delete('/api/users/:id', (req, res) => UserController.deleteUser(req, res));

module.exports = router;