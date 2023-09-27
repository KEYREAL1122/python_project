const { Sequelize, DataTypes } = require('sequelize');
const sequelize = require('../database/connection');

const AirlineCompany = sequelize.define('AirlineCompany', {
  name: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true
  },
  country: {
    type: DataTypes.STRING,
    allowNull: false
  },
  founded: {
    type: DataTypes.DATE,
    allowNull: false
  },
  fleetSize: {
    type: DataTypes.INTEGER,
    allowNull: false
  }
});

module.exports = AirlineCompany;
