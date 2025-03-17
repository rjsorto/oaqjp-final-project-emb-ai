const textToAnalyze = document.getElementById("textToAnalyze");
const sysResponse = document.getElementById("system_response");

let RunSentimentAnalysis = ()=>{
    sysResponse.innerHTML = '';
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        response = 'Invalid text! Please try again!.';
        if (this.readyState == 4 && this.status == 200) response = xhttp.responseText;
        sysResponse.innerHTML = response;
    };
    xhttp.open("GET", `./emotionDetector?textToAnalyze=${textToAnalyze.value}`, true);
    xhttp.send();
}
