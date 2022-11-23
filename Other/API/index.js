const express = require("express");
var exec = require('child_process').exec;
const app = express();
const cors = require('cors');
	


app.listen(process.env.PORT,
	() => console.log("Server Start at the Port"));
	
app.use(express.static('public'));
app.use(cors());


app.get('/api', alldata);

function alldata(request, response) {
	response.send(elements);
}


app.get('/api/:ip/:puerto/:dominio/', crearConf);

function crearConf(request, response) {

    var ip = request.params.ip;
	var puerto = request.params.puerto;
    var dominio = request.params.dominio;

	exec(`python3 index.py "${ip}" ${puerto} "${dominio}"`);

    var respuesta = {
        status:`RECIBIDO\n\n\n-> IP: ${ip}\n-> PUERTO: ${puerto}\n DOMINIO: ${dominio}`
    };
	response.send(respuesta);

}
