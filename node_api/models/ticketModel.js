const Sequelize = require('sequelize');
const sequelize = require('../database/db');

const Ticket = sequelize.define('ticket', {
    ticketId: {
        type: Sequelize.INTEGER,
        allowNull: false,
        primaryKey: true,
        autoIncrement: true
    },
    flightId: {
        type: Sequelize.INTEGER,
        allowNull: false,
        references: {
            model: 'flights', // 'flights' refers to table name
            key: 'flightId', 
        },
        onDelete: 'cascade',
        onUpdate: 'cascade',
    },
    userId: {
        type: Sequelize.INTEGER,
        allowNull: false,
        references: {
            model: 'users', // 'users' refers to table name
            key: 'id', 
        },
        onDelete: 'cascade',
        onUpdate: 'cascade',
    },
    // Define other necessary fields here
});

module.exports = Ticket;
