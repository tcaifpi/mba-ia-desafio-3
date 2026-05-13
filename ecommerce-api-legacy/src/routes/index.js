const express = require('express');
const router = express.Router();
const { CheckoutController, ReportController, UserController } = require('../controllers/CheckoutController');

// Rotas refatoradas
router.post('/api/checkout', (req, res) => CheckoutController.handle(req, res));
router.get('/api/admin/financial-report', (req, res) => ReportController.financialReport(req, res));
router.delete('/api/users/:id', (req, res) => UserController.deleteUser(req, res));

module.exports = router;