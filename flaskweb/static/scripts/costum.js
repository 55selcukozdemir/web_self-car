var lower_h = document.getElementById("lower-h");
var lower_s = document.getElementById("lower-s");
var lower_v = document.getElementById("lower-v");
var upper_h = document.getElementById("upper-h");
var upper_s = document.getElementById("upper-s");
var upper_v = document.getElementById("upper-v");

function putThresholdValues(){

    console.log(lower_h.value )

    $.ajax({
        type: "POST",
        url: "segment",
        data: 
        "lower-h=" + window.lower_h.value+
        "&lower-s=" + window.lower_s.value+
        "&lower-v=" + window.lower_v.value+
        "&upper-h=" + window.upper_h.value+
        "&upper-s=" + window.upper_s.value+
        "&upper-v=" + window.upper_v.value,
        success: function (response) {
            window.lower_h.innerHTML = response['lower-h'];
            window.lower_s.innerHTML = response['lower-s'];
            window.lower_v.innerHTML = response['lower-v'];
            window.upper_h.innerHTML = response['upper-h'];
            window.upper_s.innerHTML = response['upper-s'];
            window.upper_v.innerHTML = response['upper-v'];

            
           
        }
    });
}

// setInterval(
//     function(){
//         $("#values").load("segment")
//     },100000
// )