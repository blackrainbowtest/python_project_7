import { Axios } from "@/app/config.js"
import router from '../router'

export default {
    state: {
        user: { main: {}, profile: {} },
        developers: [],
        errors: {},
        recoverySuccess: '',
    },
    getters: {
        getUser(state) { return state.user },
        getErrors(state) { return state.errors },
        getDevelopers(state) { return state.developers },
        getCountDown(state) { return Number(state.errors?.countDown) },
        getRecoverySuccess(state) { return state.recoverySuccess }
    },
    mutations: {
        signUp(state, { data: payload }) { payload?.errors ? state.errors = payload?.errors : state.errors = {} },
        signIn(state, { data: payload }) { if (payload?.errors) { state.errors = payload?.errors } else { localStorage.setItem('user', payload?.token); state.errors = {} } },
        logout(state) {
            localStorage.removeItem('user');
            state.user = { main: {}, profile: {} }
        },
        profile(state, { data: payload }) { state.user.main = payload?.data },
        clear(state) { state.errors = {}; state.recoverySuccess = '' },
        developers(state, { data: payload }) { state.developers = payload.data },
        sendInvite(state, { data: payload }) {
            if (payload?.data) {
                alert(payload.data)
            } else if (payload?.errors) {
                alert(payload?.errors)
            }
        },
        countDownTime(state) {
            state.errors?.countDown && (state.errors = { ...state.errors, countDown: Number(state.errors.countDown) - 1 })
        },
        passwordRecover(state, { data: payload }) {
            state.recoverySuccess = payload.data
        },
        passwordChange(state, { data: payload }) {
            if (payload?.errors) { state.errors = payload.errors }
            else {
                state.errors = {};
                alert(payload.data);
                router.push('/')
            }
        },
    },
    actions: {
        signUp({ commit }, payload) {
            Axios.post('signup', payload
            ).then(response => { commit('signUp', response); router.push('/') }
            ).catch(error => console.log(error, '404 SignUp'))
        },
        signIn({ commit }, payload) {
            Axios.post('signin', payload
            ).then(response => { commit('signIn', response); router.push('/') }
            ).catch(error => console.log(error, '404 SignIn'))
        },
        logout({ commit }) {
            Axios.get('logout', { headers: { authorization: `Token ${localStorage.user}` } }
            ).then(() => { commit('logout') }
            ).catch(() => console.log('logout error'))

        },
        profile({ commit }) {
            Axios.get('profile', { headers: { authorization: `Token ${localStorage.user}` } }
            ).then(response => (commit('profile', response))
            ).catch(error => console.log(error, '404 Profile'))
        },
        developers({ commit }) {
            Axios.get('developers', { headers: { authorization: `Token ${localStorage.user}` } }
            ).then(response => (commit('developers', response))
            ).catch(error => console.log(error, '404 developers'))
        },
        sendInvite({ commit }, payload) {
            Axios.post('sendinvite', payload, { headers: { authorization: `Token ${localStorage.user}` } }
            ).then(response => { commit('sendInvite', response) }
            ).catch(error => console.log(error, '404 send invite'))
        },
        passwordRecover({ commit }, payload) {
            Axios.post('passwordrecovery', payload
            ).then(response => { commit('passwordRecover', response) }
            ).catch(error => console.log(error, '404 password recovery'))
        },
        passwordChange({ commit }, payload) {
            Axios.post('passwordchange', payload
            ).then(response => { commit('passwordChange', response) }
            ).catch(error => console.log(error, '404 password change'))
        },
    },
}