const Ticket = require('../models/Ticket');

exports.createTicket = async (req, res) => {
    try {
        const ticket = await Ticket.create(req.body);
        res.status(201).json(ticket);
    } catch (error) {
        res.status(500).json({ error: 'Error creating ticket' });
    }
};

exports.getAllTickets = async (req, res) => {
    try {
        const tickets = await Ticket.findAll();
        res.status(200).json(tickets);
    } catch (error) {
        res.status(500).json({ error: 'Error retrieving tickets' });
    }
};

exports.getTicketById = async (req, res) => {
    try {
        const ticket = await Ticket.findByPk(req.params.id);
        if (!ticket) return res.status(404).json({ error: 'Ticket not found' });
        res.status(200).json(ticket);
    } catch (error) {
        res.status(500).json({ error: 'An error occurred' });
    }
};

exports.updateTicket = async (req, res) => {
    try {
        await Ticket.update(req.body, {
            where: {
                id: req.params.id
            }
        });
        res.status(200).json({ message: 'Ticket updated successfully' });
    } catch (error) {
        res.status(500).json({ error: 'Error updating ticket' });
    }
};

exports.deleteTicket = async (req, res) => {
    try {
        await Ticket.destroy({
            where: {
                id: req.params.id
            }
        });
        res.status(200).json({ message: 'Ticket deleted successfully' });
    } catch (error) {
        res.status(500).json({ error: 'Error deleting ticket' });
    }
};
