const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcryptjs');
const path = require('path');

// Configuração da conexão com o banco de dados
const dbPath = path.resolve(__dirname, '../../database.db');
const db = new sqlite3.Database(dbPath);

class User {
    constructor(id, name, email, passwordHash) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.passwordHash = passwordHash;
    }

    /**
     * Cria um usuário com a senha criptografada (Hash Seguro).
     * @param {string} name 
     * @param {string} email 
     * @param {string} password 
     */
    static async create(name, email, password) {
        // Gerando o hash da senha (substituindo o werkzeug por bcrypt)
        const salt = await bcrypt.genSalt(10);
        const hashed_password = await bcrypt.hash(password, salt);

        return new Promise((resolve, reject) => {
            const query = 'INSERT INTO users (name, email, password) VALUES (?, ?, ?)';
            db.run(query, [name, email, hashed_password], function(err) {
                if (err) {
                    return reject(err);
                }
                resolve(this.lastID);
            });
        });
    }

    /**
     * Verifica se o login é válido e retorna a instância do usuário.
     */
    static async verifyLogin(email, password) {
        return new Promise((resolve, reject) => {
            const query = 'SELECT * FROM users WHERE email = ?';
            db.get(query, [email], async (err, row) => {
                if (err) return reject(err);
                if (!row) return resolve(null);

                // Verificação segura do hash (Blindagem contra Timing Attacks)
                const isMatch = await bcrypt.compare(password, row.password);
                if (isMatch) {
                    resolve(new User(row.id, row.name, row.email, row.password));
                } else {
                    resolve(null);
                }
            });
        });
    }

    /**
     * Retorna o usuário como objeto simples para a API, ocultando dados sensíveis.
     */
    toDict() {
        return {
            id: this.id,
            name: this.name,
            email: this.email
        };
    }
}

module.exports = User;