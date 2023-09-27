const Airline = require('../models/Airline');

exports.createAirline = async (req, res) => {
  try {
    const airline = await Airline.create(req.body);
    res.status(201).json(airline);
  } catch (error) {
    res.status(500).json({ error: 'Error creating airline' });
  }
};

exports.getAllAirlines = async (req, res) => {
  try {
    const airlines = await Airline.findAll();
    res.status(200).json(airlines);
  } catch (error) {
    res.status(500).json({ error: 'Error retrieving airlines' });
  }
};

exports.getAirlineById = async (req, res) => {
  try {
      const airline = await Airline.findByPk(req.params.id);
      if (!airline) return res.status(404).json({ error: 'Airline not found' });
      res.status(200).json(airline);
  } catch (error) {
      res.status(500).json({ error: 'An error occurred' });
  }
};

exports.updateAirline = async (req, res) => {
  try {
      await Airline.update(req.body, {
          where: {
              id: req.params.id
          }
      });
      res.status(200).json({ message: 'Airline updated successfully' });
  } catch (error) {
      res.status(500).json({ error: 'Error updating airline' });
  }
};

exports.deleteAirline = async (req, res) => {
  try {
      await Airline.destroy({
          where: {
              id: req.params.id
          }
      });
      res.status(200).json({ message: 'Airline deleted successfully' });
  } catch (error) {
      res.status(500).json({ error: 'Error deleting airline' });
  }
};
