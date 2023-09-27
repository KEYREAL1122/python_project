const express = require('express');
const flightController = require('../controllers/flightController');
const router = express.Router();

// CRUD routes
router.get('/flights', flightController.getAllFlights);
router.get('/flights/:id', flightController.getFlightById);
router.post('/flights', flightController.createFlight);
router.put('/flights/:id', flightController.updateFlight);
router.delete('/flights/:id', flightController.deleteFlight);

module.exports = router;
