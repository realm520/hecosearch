import axios from 'axios';

const state = {
    url: null
};

function post_request(url, data) {
    return new Promise((resolve,reject) => {
        axios
        .post(url, JSON.stringify(data))
        .then(response => {
            const data = response.data;
            if(data && data.error) {
                reject(data.error);
            } else {
                resolve(response.data);
            }
        }, err => {
            reject(err)
        })
    })
}

export default {
    getUrl() {return state.url;},
    setUrl(url) {state.url = url;},
    get_invitation_reward(address, coin) {
        let data = {
            "jsonrpc": "2.0", 
            "method": "hecosearch.invitation.reward", 
            "params": [address,coin], 
            "id": 1
        }
        return post_request(state.url, data)
    }
}
