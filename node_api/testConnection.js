const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('flight_app', 'postgres', 'P@ssw0rd!', {
  host: 'localhost',
  dialect: 'postgres',
  port: 5432,
  logging: console.log // Enable SQL logging to help debug the issue
});

console.log('Attempting to connect to the database...');

sequelize.authenticate()
  .then(() => {
    console.log('Connection has been established successfully.');
  })
  .catch(err => {
    console.error('Unable to connect to the database:', err);
  })
  .finally(() => {
    sequelize.close(); // Close the connection when done
  });
