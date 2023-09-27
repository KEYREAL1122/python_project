const User = require('../models/User');

exports.login = async (req, res) => {
  try {
      const { username, password } = req.body;
      const user = await User.findOne({ where: { username } });
      if (!user || user.password !== password) {
          return res.status(401).json({ error: 'Invalid credentials' });
      }
      res.status(200).json({ message: 'Logged in successfully' }); // Ideally, return a JWT token here
  } catch (error) {
      res.status(500).json({ error: 'Error logging in' });
  }
};

exports.getAllUsers = async (req, res) => {
  try {
    const users = await User.findAll();
    res.status(200).json(users);
  } catch (error) {
    res.status(500).json({ error: 'An error occurred' });
  }
};

exports.getUserById = async (req, res) => {
  try {
    const user = await User.findByPk(req.params.id);
    res.status(200).json(user);
  } catch (error) {
    res.status(500).json({ error: 'An error occurred' });
  }
};

// You can add more functions to handle creating, updating, and deleting users.
exports.createUser = async (req, res) => {
    try {
      const newUser = await User.create(req.body);
      res.status(201).json(newUser);
    } catch (error) {
      res.status(500).json({ error: 'Error creating user' });
    }
  };

  exports.updateUser = async (req, res) => {
    try {
      await User.update(req.body, {
        where: {
          id: req.params.id
        }
      });
      res.status(200).json({ message: 'User updated successfully' });
    } catch (error) {
      res.status(500).json({ error: 'Error updating user' });
    }
  };

  exports.deleteUser = async (req, res) => {
    try {
      await User.destroy({
        where: {
          id: req.params.id
        }
      });
      res.status(200).json({ message: 'User deleted successfully' });
    } catch (error) {
      res.status(500).json({ error: 'Error deleting user' });
    }
  };
  