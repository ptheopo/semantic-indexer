const express = require('express');
const cors = require('cors');
const app = express();
const path = require('path');

app.use(cors());

app.use(express.static(path.join(__dirname, "node_modules")));
app.use(express.static(path.join(__dirname, "static")));

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.get('/directory', function(req, res) {
  res.sendFile(__dirname + '/directory.html');
});

app.get('/search', function(req, res) {
  res.sendFile(__dirname + '/search.html');
});

app.listen(8001);
