const express = require('express');
const cors = require('cors');
const app = express();
const path = require('path');

app.use(cors());

app.use(
  express.static(path.join(__dirname, "node_modules/bootstrap/dist/"))
);

/* Currently not an app, tmp */

// respond with "hello world" when a GET request is made to the homepage
app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.get('/directory', function(req, res) {
  res.sendFile(__dirname + '/directory.html');
});

app.listen(8001);
