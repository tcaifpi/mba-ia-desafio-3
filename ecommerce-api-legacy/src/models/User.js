const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcryptjs');
const path = require('path');

// Configuração da conexão com o banco de dados
// Sugestão de Analista: No futuro, mover o caminho para process.env.DB_PATH
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
     * Resolve o anti-padrão de Hashing Inseguro.
     */
    static async create(name, email, password) {
        // Gerando o salt e o hash da senha usando bcryptjs
        const salt = await bcrypt.genSalt(10);
        const hashed_password = await bcrypt.hash(password, salt);

        return new Promise((resolve, reject) => {
            // Uso de Prepared Statements (?) para evitar SQL Injection [CRITICAL]
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
     * Implementa proteção contra Timing Attacks.
     */
    static async verifyLogin(email, password) {
        return new Promise((resolve, reject) => {
            // Consulta parametrizada segura
            const query = 'SELECT * FROM users WHERE email = ?';
            db.get(query, [email], async (err, row) => {
                if (err) return reject(err);
                if (!row) return resolve(null);

                // Verificação segura do hash
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
     * Retorna o usuário como objeto simples para a API, 
     * garantindo que o password_hash nunca seja exposto.
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