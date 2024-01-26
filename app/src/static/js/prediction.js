
const predictionForm = document.getElementById("form-prediction");

predictionForm.addEventListener('submit', async function(e) {
    e.preventDefault()

    predictionInputsfromForm = new FormData(predictionForm);
    
    const predictionResponse = await fetch('/predict',{'method':'POST', body:predictionInputsfromForm});

    const json_response = await predictionResponse.json();

    const predictionProbability = json_response.prediction
    document.getElementById("prediction-result").textContent = predictionProbability + ' %';

});
