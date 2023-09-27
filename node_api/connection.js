const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('flight_app', 'postgres', 'P@ssw0rd!', {
  host: 'localhost',
  dialect: 'postgres',
  port: 5432
});

sequelize.authenticate()
  .then(() => {
    console.log('Connection has been established successfully.');
  })
  .catch(err => {
    console.error('Unable to connect to the database:', err);
  });

module.exports = sequelize;
