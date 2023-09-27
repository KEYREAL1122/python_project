const express = require('express');
const userRoutes = require('./routes/userRoutes');
const flightRoutes = require('./routes/flightRoutes');
const airlineRoutes = require('./routes/airlineRoutes');
const ticketRoutes = require('./routes/ticketRoutes');

const app = express();

const path = require('path');
require('dotenv').config({ path: path.resolve(__dirname, '../.env') });

// access environment variables using process.env
const jwtSecret = process.env.JWT_SECRET;
const dbUsername = process.env.DB_USERNAME;
const dbPassword = process.env.DB_PASSWORD;
const dbName = process.env.DB_NAME;
const dbHost = process.env.DB_HOST;
const dbPort = process.env.DB_PORT;
const nodeServerUrl = process.env.NODE_SERVER_URL;
const myApiKey = process.env.MY_API_KEY;


// Middleware to handle JSON payloads
app.use(express.json());

// Logging Middleware
app.use((req, res, next) => {
    console.log(`${new Date().toISOString()} - ${req.method} ${req.originalUrl}`);
    next();
});

// Routes
app.use('/api', userRoutes);
app.use('/api', flightRoutes);
app.use('/api', airlineRoutes);
app.use('/api', ticketRoutes);

// Error Handling Middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
