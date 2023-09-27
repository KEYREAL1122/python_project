const express = require('express');
const airlineController = require('../controllers/airlineController');
const router = express.Router();

// CRUD routes
router.get('/airlines', airlineController.getAllAirlines);
router.get('/airlines/:id', airlineController.getAirlineById);
router.post('/airlines', airlineController.createAirline);
router.put('/airlines/:id', airlineController.updateAirline);
router.delete('/airlines/:id', airlineController.deleteAirline);

module.exports = router;
