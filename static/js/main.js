var send_otp_btn = document.getElementById('send_otp');
send_otp_btn.addEventListener('click', myFetcher);

function myFetcher() {
   const requestOptions = {
      'method':'GET',
      // 'mode':'no-cors'
      'headers': {
         'Content-Type': 'application/json',
        }
      };
   var phone_ele = document.getElementsByClassName("phone")
   var data = {"phone":phone_ele[0].getElementsByTagName('input')[0].value};
   const queryParams = new URLSearchParams(data);
   fetch('http://172.18.0.1:8001/api/test1/user/login-otp?'+queryParams, requestOptions)
      .then(
         function(response) {
            if (response.status !== 200) {
               console.log('Looks like there was a problem. Status Code: '+response.status);
               return;
            }
            response.json().then(function(data) {
               console.log(data);
               var otp = document.getElementById('otp');
               var request_id = document.getElementById('request_id').getElementsByTagName('input')[0];
               console.log(otp.style);
               otp.style.display = 'inline';
               console.log(data.request_id);
               request_id.value = data.request_id;
               console.log(request_id.value)
            });
         })
      .catch(function(err) {
         console.log('Fetch Error :-S', err);
      })
   }