require('dotenv').config();
const express = require('express');
const routes = require('./routes'); // Isto já carrega o src/routes/index.js

const app = express();
app.use(express.json());

// O app.js delega tudo para o roteador
app.use(routes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT} em modo MVC.`);
});