ids = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','aa','ab','ac','ad'];

count = 0
function toggle_count() {
	//document.getElementsByTagName("span")[0].textContent = "100";
	cont = 0
	for (var i = ids.length - 1; i >= 0; i--) {
		if (document.getElementById(ids[i]).checked) {
			cont = cont+1
			console.log(`${ids[i]} == ${document.getElementById(ids[i]).checked}`)
		}
	}
	document.getElementById('contador').textContent = cont;
	console.log("info sent")
}
function disable_all() {
	for (var i = ids.length - 1; i >= 0; i--) {
		document.getElementById(ids[i]).checked = false;
	}
	toggle_count();
}

function enable_all() {
	for (var i = ids.length - 1; i >= 0; i--) {
		document.getElementById(ids[i]).checked = true;
	}
	toggle_count();
}

function switch_all() {
	for (var i = ids.length - 1; i >= 0; i--) {
		if (document.getElementById(ids[i]).checked == true){
			document.getElementById(ids[i]).checked = false;
		} else {
			document.getElementById(ids[i]).checked = true;
		}
	}
	toggle_count();
}
