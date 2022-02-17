console.log("ok")

function copiarHTML() {
    let copyText = document.getElementsByTagName("html")[0];
    let input = document.createElement("input");
    input.id = "inp";
    input.value = copyText.outerHTML;
    copyText.appendChild(input);
    
    let copy = document.getElementById('pix');
    copy.select();
    document.execCommand("Copy");
    alert("A chave pix foi copiada: " + copy.value);
    
    copyText.removeChild(input);

    
    copyText.appendChild(textArea);
}
