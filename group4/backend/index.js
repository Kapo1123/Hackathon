const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

app.get('/api/data', (req, res) => {
  res.json({ message: 'Hello from the back end!' });
});

app.listen(5000, () => {
  console.log('Back end running on http://localhost:5000');
});