const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');


http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
     ServerUpTime = new Date(os.uptime() * 1000).toISOString();
        totalMem = os.totalmem()/1048576;
        freeMem = os.freemem()/1048576;
        cpus = os.cpus().length+1;
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Up Time: ${ServerUpTime}</p>
        <p>Total Memory: ${totalMem} MB</p>
        <p>Free Memory: ${freeMem} MB</p>
        <p>Number of CPUs: ${cpus}</p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");