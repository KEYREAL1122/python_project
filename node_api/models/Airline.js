const { DataTypes } = require('sequelize');
const sequelize = require('../connection'); // Assuming connection.js is in the same directory as models

const Airline = sequelize.define('Airline', {
  name: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
  },
  country: {
    type: DataTypes.STRING,
    allowNull: false,
  },
});

module.exports = Airline;
