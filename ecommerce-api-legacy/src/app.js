require('dotenv').config();
const express = require('express');
const routes = require('./routes');
const { initDb } = require('./config/db');

const app = express();
app.use(express.json());

// Inicia o Banco de Dados (Cria tabelas se não existirem)
// Aqui você pode adaptar o initDb do AppManager original para o db.js
// initDb(); 

app.use(routes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT} em modo MVC.`);
});