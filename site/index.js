import data from "./country_data.js"

const select = document.getElementById("countries")

function findIndex() {
    return data.findIndex(obj => obj.country === select.value);
}

for (var i = 0; i < data.length; i++) {
    let o = document.createElement("option");
    o.innerText = data[i].country;
    o.value = data[i].country;
    select.appendChild(o);
}

var countryKeys = Object.keys(data[findIndex()]);

function selection() {
    for (var i = 0; i < countryKeys.length; i++) {
        let item = document.getElementById(countryKeys[i]);
        item.innerHTML = data[findIndex()][countryKeys[i]];
    }
}
window.selection = selection;

selection();