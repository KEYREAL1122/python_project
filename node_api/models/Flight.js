const { DataTypes, Sequelize } = require('sequelize'); // Import both DataTypes and Sequelize
const sequelize = require('../connection');

const Flight = sequelize.define('flight', {
  flightNumber: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
  },
  origin: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  destination: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  departureTime: {
    type: DataTypes.DATE,
    allowNull: false,
  },
  airlineId: {
    type: Sequelize.INTEGER, // Use Sequelize for the INTEGER type
    references: {
      model: 'airlines', // table name
      key: 'id',
    }
  },
});

module.exports = Flight;
