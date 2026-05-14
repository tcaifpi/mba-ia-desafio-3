const express = require('express');
const router = express.Router();

// Importações Corrigidas: Cada um no seu respectivo arquivo
const CheckoutController = require('../controllers/CheckoutController');
const ReportController = require('../controllers/ReportController');
const UserController = require('../controllers/UserController');

router.post('/api/checkout', (req, res) => CheckoutController.handle(req, res));
router.get('/api/admin/financial-report', (req, res) => ReportController.financialReport(req, res));
router.delete('/api/users/:id', (req, res) => UserController.deleteUser(req, res));

module.exports = router;