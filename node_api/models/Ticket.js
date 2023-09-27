const { DataTypes } = require('sequelize');
const sequelize = require('../connection'); // Assuming connection.js is in the same directory as models

const Ticket = sequelize.define('Ticket', {
  seatNumber: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  price: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
});

module.exports = Ticket;
