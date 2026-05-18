const sqlite3 = require('sqlite3').verbose();
const path = require('path');

// 1. Integração com o .env (Segurança [HIGH])
// Prioriza o caminho definido no .env, senão usa um fallback local
const dbPath = path.resolve(process.env.DB_PATH || './database.sqlite');

const db = new sqlite3.Database(dbPath, (err) => {
    if (err) {
        console.error('❌ Erro ao abrir o banco de dados:', err.message);
    } else {
        console.log(`✅ Conectado ao banco de dados em: ${dbPath}`);
    }
});

/**
 * Helper para transformar as funções do sqlite3 em Promises.
 * Isso permite usar async/await nos Controllers (ex: ReportController).
 */
const dbHelper = {
    all: (sql, params = []) => {
        return new Promise((resolve, reject) => {
            db.all(sql, params, (err, rows) => {
                if (err) reject(err);
                else resolve(rows);
            });
        });
    },
    run: (sql, params = []) => {
        return new Promise((resolve, reject) => {
            db.run(sql, params, function(err) {
                if (err) reject(err);
                else resolve({ id: this.lastID, changes: this.changes });
            });
        });
    },
    get: (sql, params = []) => {
        return new Promise((resolve, reject) => {
            db.get(sql, params, (err, row) => {
                if (err) reject(err);
                else resolve(row);
            });
        });
    }
};

module.exports = dbHelper;