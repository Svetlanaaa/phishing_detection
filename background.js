
const start = async function() {
  const model = await tf.loadLayersModel('https://raw.githubusercontent.com/Svetlanaaa/phishing_detection/master/model/model.json');
  return model;
}

const model = start();

chrome.extension.onRequest.addListener(function predict(features){
    model.then(model => {                 
        var prediction = model.predict(tf.tensor(features).reshape([1, 16]));
        prediction.data().then((dataArray) => {                
            if (dataArray[0] > dataArray[1]){
                alert("Внимание! Вы находитесь на подозрительном сайте")
            }
        });
    });
})

