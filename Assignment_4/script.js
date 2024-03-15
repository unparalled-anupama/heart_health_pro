function predictRisk() {

    var age = document.getElementById('age').value;
  
    if (!age || age < 20 || age > 80) {
        alert('Please enter age from 20 to 80.');
        return;
    }

 var bloodPressure = document.getElementById('bloodPressure').value;


    if (!bloodPressure || bloodPressure < 90 || bloodPressure > 200) {
        alert('Please enter blood pressure from 90 to 200.');
        return;
    }
 
 var cholesterol = document.getElementById('cholesterol').value;
 

    if (!cholesterol || cholesterol < 0 || cholesterol > 500) {
        alert('Please enter cholesterol from 0 to 500.');
        return;
    }
     
     var heartRate = document.getElementById('heartRate').value;
     

    if (!heartRate || heartRate < 0 || heartRate > 300) {
        alert('Please enter maximum heart rate from 0 to 300.');
        return;
    }

var stDepression = document.getElementById('stDepression').value;


    if (!stDepression || stDepression < 0 || stDepression > 10) {
        alert('Please enter stDepression value from 0 to 10.');
        return;
    }
    
        var riskScore = Math.random(); 
        var risk = riskScore > 0.5 ? 'high' : 'low';
        var resultElement = document.getElementById('result');
        var resultMessage = 'At ' + risk + ' risk of cardiovascular disease';
        
      
        var detailedMessage = risk === 'high' ? 
            'Consult measures to decrease the risk based on recommended guideline.' : 
            'Suggest to maintain a healthy lifestyle to continue to stay at low risk.';
    
        
        resultElement.innerHTML = '<h3>' + resultMessage + '</h3><p>' + detailedMessage + '</p>';
        resultElement.className = risk === 'high' ? 'result-display high-risk' : 'result-display low-risk';
    

        console.log('Risk assessment complete. Score: ', riskScore);
    
  
document.getElementById('aboutBtn').addEventListener('click', function() {
    
});

document.getElementById('helpBtn').addEventListener('click', function() {
    
});

document.getElementById('recommendationBtn').addEventListener('click', function() {
   
});}