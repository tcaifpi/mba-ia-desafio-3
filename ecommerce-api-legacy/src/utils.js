// src/utils.js
require('dotenv').config();

const config = {
    dbUser: process.env.DB_USER || "admin",
    dbPass: process.env.DB_PASS || "pass123",
    paymentGatewayKey: process.env.PAYMENT_KEY || "sk_test_51Mz..."
};

// ... mantenha as funções logAndCache e badCrypto como estão ...
module.exports = { logAndCache, badCrypto, config };