function redirect(pagename) {
    window.location = pagename
}

function appearbig(image) {
    var src = image.src;
    var win = document.getElementById('imgdisplay')
    if (win) {
        win.parentNode.removeChild(win)
    }
    var close = document.createElement("div")
    var display = document.createElement("div")
    display.setAttribute("id", "imgdisplay")
    close.innerHTML = "x"
    close.style.textAlign = "center"
    close.style.position = "absolute";
    close.style.fontSize = "30px";
    close.style.color = "red"
    close.style.width = "30px"
    close.style.cursor = "hand"
    close.style.height = "20x"
    close.style.border = "1px solid orange"
    close.style.padding = "2px 4px"
    close.style.zIndex = 101
    close.style.right = 0;
    close.style.backgroundColor = "white"
    close.onclick = function() {
        var parent = document.getElementById('imgdisplay')
        parent.parentNode.removeChild(parent)
    }
    display.appendChild(close)
    var img = document.createElement("img")
    img.src = src;
    img.setAttribute("style", "width:100%;height:100%")
    display.appendChild(img)
    display.style.visibility = "visible"
    document.body.appendChild(display)
}

function selected_files(filename, outname) {
    var output = document.getElementById(outname)
    //output.innerHTML = ul;   
    files = filename.files;
    var content = ""
    var reader = new FileReader();  
    
    function readFile(index) {
      if( index >= files.length ) return;
      var file = files[index];
      reader.onload = function(e) {  
        // get file content  
        var bin = e.target.result;
        var img = document.createElement("img")
        img.setAttribute("style", "width:90px; height:90px; margin-right:5px;margin-bottom:2px;border:0.5px solid grey")
        img.src = bin
        output.appendChild(img)
        // do sth with bin
        readFile(index+1)
      }
      reader.readAsDataURL(file);
    }
    readFile(0);
    output.innerHTML = content
}

