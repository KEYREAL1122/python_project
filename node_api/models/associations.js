const Airline = require('./models/Airline');
const Flight = require('./models/Flight');
const Ticket = require('./models/Ticket');

// Airline has many Flights
Airline.hasMany(Flight, {
  foreignKey: 'airlineId',
  onDelete: 'CASCADE', // delete all flights if the airline is deleted
});

// Flight belongs to one Airline
Flight.belongsTo(Airline, {
  foreignKey: 'airlineId',
});

// Flight has many Tickets
Flight.hasMany(Ticket, {
  foreignKey: 'flightId',
  onDelete: 'CASCADE', // delete all tickets if the flight is deleted
});

// Ticket belongs to one Flight
Ticket.belongsTo(Flight, {
  foreignKey: 'flightId',
});
