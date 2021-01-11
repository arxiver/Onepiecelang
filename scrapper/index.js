const fetch = require("node-fetch");
data = fetch("https://randomwordgenerator.com/json/sentences.json").then(res => res.json()).then(data=> {data = data.data; data.forEach(e=>console.log(e.sentence));}
);