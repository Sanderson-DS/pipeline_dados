# 🧠 Pipeline de Dados com API, MongoDB e MySQL

Projeto educacional que demonstra o processo completo de extração, transformação e carregamento de dados (ETL) usando Python. Os dados são coletados de uma API, transformados com Pandas e armazenados em bancos de dados MongoDB e MySQL.

## 🚀 Tecnologias Utilizadas

- Python 3.x
- MongoDB Atlas
- MySQL
- Pandas
- Requests
- PyMongo
- MySQL Connector
- dotenv

## 📁 Estrutura do Projeto

```
├── aulas/               # Anotações e materiais de aula (.md)
├── data/                # Dados brutos ou processados
├── notebooks/           # Jupyter Notebooks de análise e transformação
├── scripts/             # Scripts Python automatizados (ETL)
├── .gitignore           # Arquivos/pastas ignorados pelo Git
├── requirements.txt     # Dependências do projeto
```

## ⚙️ Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/Sanderson-DS/pipeline-de-dados.git
   cd pipeline-de-dados
   ```

2. Crie um ambiente virtual e ative:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate   # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` com suas configurações de ambiente:
   ```
   MONGO_URI=seu_uri_mongodb
   MYSQL_HOST=localhost
   MYSQL_USER=seu_usuario
   MYSQL_PASSWORD=sua_senha
   MYSQL_DATABASE=nome_do_banco
   ```

5. Execute os notebooks ou scripts Python conforme necessário.

## 🧪 Funcionalidades

- Conexão com MongoDB Atlas e MySQL
- Extração de dados via API
- Transformação e limpeza com Pandas
- Armazenamento estruturado dos dados
- Scripts reutilizáveis e notebooks explicativos

## ✍️ Autor

**Sanderson Bergmann**  
🔗 [LinkedIn](https://www.linkedin.com/in/sanderson-bergmann)  
💻 [GitHub](https://github.com/Sanderson-DS)

---

## 📌 Licença

Este projeto é livre para uso educacional e pessoal. Sinta-se à vontade para contribuir ou adaptar!
