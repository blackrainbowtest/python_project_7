import { createStore } from 'vuex'
// import router from '../router'
import userModule from '@/modules/userModule.js';
import taskModule from '@/modules/taskModule.js';

export default createStore({
    modules: {
        userModule,
        taskModule,
    }
})