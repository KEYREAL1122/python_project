const Flight = require('../models/Flight');

exports.createFlight = async (req, res) => {
  try {
    const flight = await Flight.create(req.body);
    res.status(201).json(flight);
  } catch (error) {
    res.status(500).json({ error: 'Error creating flight' });
  }
};

exports.getAllFlights = async (req, res) => {
  try {
    const flights = await Flight.findAll();
    res.status(200).json(flights);
  } catch (error) {
    res.status(500).json({ error: 'Error retrieving flights' });
  }
};

exports.getFlightById = async (req, res) => {
  try {
      const flight = await Flight.findByPk(req.params.id);
      if (!flight) return res.status(404).json({ error: 'Flight not found' });
      res.status(200).json(flight);
  } catch (error) {
      res.status(500).json({ error: 'An error occurred' });
  }
};

exports.updateFlight = async (req, res) => {
  try {
      await Flight.update(req.body, {
          where: {
              id: req.params.id
          }
      });
      res.status(200).json({ message: 'Flight updated successfully' });
  } catch (error) {
      res.status(500).json({ error: 'Error updating flight' });
  }
};

exports.deleteFlight = async (req, res) => {
  try {
      await Flight.destroy({
          where: {
              id: req.params.id
          }
      });
      res.status(200).json({ message: 'Flight deleted successfully' });
  } catch (error) {
      res.status(500).json({ error: 'Error deleting flight' });
  }
};