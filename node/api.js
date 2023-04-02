const http = require("http");
const data = require("C:/GIT/it3038c-scripts/node/widgets.json");

const server = http.createServer(function (req, res) {
  if (req.url === "/") {
    res.writeHead(200, { "Content-Type": "text/json" });
    res.end(JSON.stringify(data));
  } else if (req.url === "/blue") {
    res.writeHead(200, { "Content-Type": "text/json" });
    listBlue(res);
  } else {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end(`Data not found`);
  }
});

function listBlue(res) {
  const colorBlue = data.filter(function (item) {
    return item.color === "blue";
  });

  res.end(JSON.stringify(colorBlue));
}

server.listen(3000);
console.log("Server listening on port 3000");

