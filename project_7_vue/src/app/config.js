// export axios and baseURL
import axios from "axios";
export const baseURL = 'http://127.0.0.1:8000/'
export const Axios = axios.create({
    baseURL: baseURL
})