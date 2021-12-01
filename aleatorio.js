let alunos = [
	"1301 Daniel",
	"1302 Mesquita",
	"1303 Brito",
	"1304 Jesus",
	"1305 Zerino",
	"1306 Allan Assis",
	"1307 Viana",
	"1308 Buhaten",
	"1309 Klinsmann",
	"1310 Igor Farias",
	"1311 João Batista",
	"1312 Abreu",
	"1313 Dantas",
	"1314 Pinto",
	"1315 Eduardo",
	"1316 Miquéias",
	"1317 Arthur",
	"1318 Bithencourt",
	"1319 Tadeu",
	"1320 Ronaldo",
	"1321 Juan",
	"1322 Jorge",
	"1323 Anderson",
	"1324 Silva Costa",
	"1325 Barros",
	"1326 Botelho",
	"1327 Rodrigues",
	"1328 A. Florêncio",
	"1329 M. Cruz",
	"1330 O. Calado"
];

function newAluno() {
	n = Math.floor(Math.random() * alunos.length);
	document.getElementById('trouxa').textContent = `${alunos[n]}`;
	console.log(n+1);
}