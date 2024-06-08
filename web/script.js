
// function play() {
//     fetch("http://localhost:8080/get-random-text")
//       .then(response => response.arrayBuffer())
//       .then(buffer => {
//         const text = new TextDecoder().decode(buffer);
//         document.getElementById("text").innerHTML = text;
//       })
//       .catch(error => {
//         console.error('Error fetching text:', error);
//       });

//       document.getElementById("play_button").disabled = true;
//       document.getElementById("text_input").disabled = false;
//       document.getElementById("text_input").value = "";
//       document.getElementById("text_input").focus();

//       const TIMER = 2;

//       function setTimeLabel( number ) {
//         document.getElementById("counter").innerHTML = TIMER - number;
//       }

//       function whenDone() {
//         document.getElementById("play_button").disabled = false;
//         document.getElementById("text_input").disabled = true;
//         var body = "{'text':'" + document.getElementById('text_input').value + "', 'test':'" + document.getElementById('text').innerHTML + "'}";
//         fetch("http://localhost:8080/text-processor", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify(body)
//         })}
//         document.getElementById("text_input").value = "";
//         document.getElementById("text_input").focus();

//       for (let i = 0; i < TIMER + 1; i++) {
//         setTimeout(setTimeLabel, 1000 * i, i);
//         if (i == TIMER - 1) {
//           setTimeout(whenDone, 1000 * (i + 1));
//         }
//       }
//     }

function play() {
    fetch("http://localhost:8080/quote")
      .then(response => response.arrayBuffer())
      .then(buffer => {
        const text = new TextDecoder().decode(buffer);
        document.getElementById("text").innerHTML = text;
      })
      .catch(error => {
        console.error('Error fetching text:', error);
      });

      document.getElementById("play_button").disabled = true;
      document.getElementById("text_input").disabled = false;
      document.getElementById("text_input").value = "";
      document.getElementById("text_input").focus();

      const TIMER = 30;

      function setTimeLabel( number ) {
        document.getElementById("counter").innerHTML = TIMER - number;
      }

      function whenDone() {
        document.getElementById("play_button").disabled = false;
        document.getElementById("text_input").disabled = true;
        var body = {'text': document.getElementById('text_input').value, 'test': document.getElementById('text').innerHTML};
        fetch("http://localhost:8080/text", {
            method: "POST",
            body: JSON.stringify(body)})
      .then(response => response.arrayBuffer())
      .then(buffer => {
        const text = new TextDecoder().decode(buffer);
        document.getElementById("text").innerHTML = text;})}

      for (let i = 0; i < TIMER + 1; i++) {
        setTimeout(setTimeLabel, 1000 * i, i);
        if (i == TIMER - 1) {
          setTimeout(whenDone, 1000 * (i + 1));
        }
      }
    }