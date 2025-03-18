import data from "./country_data.js"

const select = document.getElementById("countries")
const countryKeys = Object.keys(data[findIndex()]);

/**
 * Function to get the index of the searched value
 * @param search The value to search for
 * @returns The index of the searched value
 */
function findIndex(search) {
    return data.findIndex(obj => obj.country === search);
}

data.forEach((c) => {
    const o = document.createElement("option");
    o.innerText = c.country;
    o.value = c.country;
    select.appendChild(o);
})

function selection() {
    for (let i = 0; i < countryKeys.length; i++) {
        const item = document.getElementById(countryKeys[i]);
        item.innerHTML = data[findIndex(select.value)][countryKeys[i]];
    }
}
window.selection = selection;

selection();