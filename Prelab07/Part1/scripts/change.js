function changecontent() {
    var row = parseInt(prompt("row to change:")) - 1;
    var column = parseInt(prompt("column to change:")) - 1;
    var text = prompt("New text:");
    table = document.getElementById("myTable")
    rows = table.getElementsByTagName("tr")
    cells = rows[row].getElementsByTagName('td')
    cells[column].innerHTML = text;
}