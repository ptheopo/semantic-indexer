const express = require('express');
const cors = require('cors');
const app = express();
const path = require('path');

app.use(cors());

app.use(
  express.static(path.join(__dirname, "node_modules/bootstrap/dist/"))
);

// respond with "hello world" when a GET request is made to the homepage
app.get('/', function(req, res) {
  res.sendFile('/home/theof/Sphere/semantic-indexer-app/index.html');
});

app.listen(8081);