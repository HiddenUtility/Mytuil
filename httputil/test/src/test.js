// import {getTest} from "./getTest";
// import {postTest} from "./postTest";

// const getTest = getTest;
// const postTest = postTest;


const getTest = () => {
    const request = document.getElementById('GetRquest').value;

    const url = `http://localhost:8080/get?search=${request}`;
    console.log(`getTest:${url}`);

    fetch(url)
        .then((resp) => {
            if (resp.ok) {
                return resp.json();
            } else {
                throw new Error('Bad Request');
            }
        })
        .then((json) => {
            console.log(json);
            const element = document.getElementById('GetResult');
            element.textContent = '';
            element.textContent = JSON.stringify(json);
        });
};

const postTest = () => {

    const url = 'http://localhost:8080/post';
    console.log('getTest:${url}');
    /** */
    const request = document.getElementById('PostRquest').value;
    console.log(request);
    bodyData = {
        request: request
    };

    fetch(url,
        {
            method: 'POST',
            body: JSON.stringify(bodyData),
        }
    )
        .then((resp) => {
            if (resp.ok) {
                return resp.json();
            } else {
                throw new Error('Bad Request');
            }
        })
        .then((json) => {
            console.log(json);
            const element = document.getElementById('PostResult');
            element.textContent = '';
            element.textContent = JSON.stringify(json);

        });
};

