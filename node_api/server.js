require('dotenv').config();

const express = require('express');
const app = express();
const port = 3000;
const { registerUser } = require('./userController');

app.use(express.json()); // For parsing application/json

// register user endpoint
app.post('/register', registerUser);

app.listen(port, () => {
  console.log(`API server listening at http://localhost:${port}`);
});
