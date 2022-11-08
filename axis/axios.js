const getBtn = document.getElementById('get-btn');
const postBtn = document.getElementById('post-btn');

const getData = () => {

    // get the classification of cherishfood
    axios.get('https://stamp.family.com.tw/api/cherishfood/Classification')
    .then(response => {
        console.log(response);
    })
};

const sendData = () => {
    // get data according to the post data we send
    axios.post('https://stamp.family.com.tw/api/cherishfood/CherishFoods', {
        OldPKeys: ["000053"], PostInfo: "", Latitude: 0, Longitude: 0
        // OldPKeys: shop ID
        // PostInfo: shop list of an certain area (src/store/city.ts)
    })
    .then(response => {
        console.log(response.data);
    });
};

getBtn.addEventListener('click', getData);
postBtn.addEventListener('click', sendData);
