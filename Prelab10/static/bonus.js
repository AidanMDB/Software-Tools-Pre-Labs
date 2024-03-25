function bonus(id, contents, date, postcode) {
    var hiddenLayer = document.getElementById("postval" + String(id));
    if (hiddenLayer.innerHTML == "") {
        hiddenLayer.removeAttribute("hidden");
        hiddenLayer.appendChild(document.createElement("button")).innerHTML="View"
        hiddenLayer.children[0].onclick = function () {
            window.location.href="/posts/"+postcode;
        }
        hiddenLayer.appendChild(document.createElement("p")).innerHTML=contents;
        hiddenLayer.appendChild(document.createElement("p")).innerHTML="Date: " + date;
    }
    else {
        hiddenLayer.innerHTML = "";
        hiddenLayer.setAttribute("hidden");
    }
}
