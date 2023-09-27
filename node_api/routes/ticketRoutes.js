const express = require('express');
const ticketController = require('../controllers/ticketController');
const router = express.Router();

// CRUD routes
router.get('/tickets', ticketController.getAllTickets);
router.get('/tickets/:id', ticketController.getTicketById);
router.post('/tickets', ticketController.createTicket);
router.put('/tickets/:id', ticketController.updateTicket);
router.delete('/tickets/:id', ticketController.deleteTicket);

module.exports = router;
