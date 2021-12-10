function init() {
    canvas = document.getElementById('myCanvas')

    ctx = canvas.getContext('2d')
    ctx.fillStyle = 'white'
    ctx.fillRect(0,0,canvas.width, canvas.height)
    mousePressed = false
    $('#myCanvas').mousedown(function (e) {
        mousePressed = true
        draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, false)

    })

    $('#myCanvas').mousemove(function (e) {
        if (mousePressed){
            draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, true)
        }
    })

    $('#myCanvas').mouseup(function (e) {
        mousePressed = false
    })

    $('#myCanvas').mouseleave(function (e) {
        mousePressed = false
    })
}


function draw(x,y, isDown){
    if (isDown) {
        ctx.beginPath()

        ctx.strokeStyle = $('#selColor').val()
        ctx.lineWidth = $('#selWidth').val()
        ctx.lineJoin = "round"

        ctx.moveTo(lastX, lastY)
        ctx.lineTo(x, y)
        ctx.closePath()
        ctx.stroke()
    }
    lastX = x
    lastY = y
}

function clearCanvas() {
    ctx.setTransform(1,0,0,1,0,0)
    ctx.fillStyle = 'white'
    ctx.fillRect(0,0,canvas.width, canvas.height)
    document.getElementById('prediction').innerHTML = ""
}

function postImage() {
    var image = document.getElementById('myCanvas').toDataURL('image/png')
    image = image.replace(/^data:image\/(png|jpg);base64,/, "")

    $.ajax({
        type: 'POST',
        url: '/recognize',
        data: JSON.stringify({image: image}),
        contentType: 'application/json;charset=UTF-8',
        dataType: 'json',
        success: function (msg, status, jqXJHR) {
            console.log('Post image successfully')
            var data = JSON.parse(jqXJHR.responseText)
            var prediction = data.prediction
            document.getElementById('prediction').innerHTML = prediction
        }
    })
}