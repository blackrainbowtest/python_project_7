import { Axios } from "@/app/config.js"
// import router from '../router'

export default {
    state: {
        tasks: { Archive: [] },
        categories: [],
        taskErrors: {},
    },
    getters: {
        getTasks: (state) => (key = 'Archive') => { return state.tasks[key] },
        getCategories(state) { return state.categories }
    },
    mutations: {
        tasksMutation(state, { data: payload }) {
            if (payload?.errors) { state.taskErrors = payload?.errors }
            else {
                if (payload?.data.length) { state.tasks[payload?.data[0].categories.name] = payload?.data }
                else { state.tasks[payload?.category] = [] }
            }
        },
        categories(state, { data: payload }) { state.categories = payload?.data },
    },
    actions: {
        tasks({ commit }, payload = 2) {
            Axios.get(`gettasks/${payload}`
            ).then(response => (commit('tasksMutation', response))
            ).catch(error => console.log(error, '404 getTasks'))
        },
        categories({ commit }) {
            Axios.get('getcategories'
            ).then(response => (commit('categories', response))
            ).catch(error => console.log(error, '404 getTasks'))
        },
        archive({ commit }, payload = 1) {
            Axios.get(`getarchive/${payload}`
            ).then(response => (commit('tasksMutation', response))
            ).catch(error => console.log(error, '404 getTasks'))
        },
        addTask({ commit }, payload) {
            Axios.post('addtask', payload, { headers: { authorization: `Token ${localStorage.user}` } }
            ).then(response => { commit('tasksMutation', response) }
            ).catch(error => console.log(error, '404 addTask'))

        },
        updateTitle({ commit }, payload) {
            Axios.put('updatetitle', payload, { headers: { authorization: `Token ${localStorage.user}` } }
            ).then(response => (commit('tasksMutation', response))
            ).catch(error => console.log(error, '404 updateTitle'))
        },
        updateDescription({ commit }, payload) {
            Axios.put('updatedescription', payload, { headers: { authorization: `Token ${localStorage.user}` } }
            ).then(response => (commit('tasksMutation', response))
            ).catch(error => console.log(error, '404 updateDescription'))
        },
        updateDraggable({ commit }, payload) {
            let tasksTemp = []
            payload.tasks.forEach(element => {
                tasksTemp.push(element.id);
            });
            payload.tasks = tasksTemp
            Axios.put('updatedraggable', payload, { headers: { authorization: `Token ${localStorage.user}` } }
            ).then(response => (commit('tasksMutation', response))
            ).catch(error => {alert(error.code); console.log('404 updateDraggable')})
        },
        deleteTask({ commit }, payload) {
            Axios.delete(`deletetask/${payload}`, { headers: { authorization: `Token ${localStorage.user}` } }
            ).then(response => (commit('tasksMutation', response))
            ).catch(error => console.log(error, '404 deleteTask'))
        },
        archiveTask({ commit }, payload) {
            Axios.put('archivetask', payload, { headers: { authorization: `Token ${localStorage.user}` } }
            ).then(response => (commit('tasksMutation', response))
            ).catch(error => console.log(error, '404 archiveTask'))
        },
        updateAssigned({ commit }, payload) {
            Axios.put('updateassigned', payload, { headers: { authorization: `Token ${localStorage.user}` } }
            ).then(response => (commit('tasksMutation', response))
            ).catch(error => console.log(error, '404 updateAssigned'))
        },
    },
}