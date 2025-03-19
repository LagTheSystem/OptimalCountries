import data from "./country_data.js"

const select = document.getElementById("countries")

function findIndex() {
    return data.findIndex(obj => obj.country === select.value);
}

data.forEach((c) => {
    const o = document.createElement("option");
    o.innerText = c.country;
    o.value = c.country;
    select.appendChild(o);
})

const countryKeys = Object.keys(data[findIndex()]);

function selection() {
    for (let i = 0; i < countryKeys.length; i++) {
        const item = document.getElementById(countryKeys[i]);
        const itemValue = data[findIndex()][countryKeys[i]];
        if (itemValue == 1000) {
            item.innerText = "No Data";
        } else {
            item.innerText = itemValue;
        }
    }
}
window.selection = selection;

selection();