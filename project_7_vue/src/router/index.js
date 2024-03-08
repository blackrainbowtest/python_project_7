import { createRouter, createWebHistory } from 'vue-router'

const routes = [

    { path: '/signin', name: 'signin', component: () => import('../views/User/SignInView.vue') },
    { path: '/signup', name: 'signup', component: () => import('../views/User/SignUpView.vue') },
    {
        path: '/', name: 'header', component: () => import('../components/Layout/HeaderComponent.vue'),
        children: [
            { path: '', name: 'home', component: () => import('../views/Home/HomeView.vue') },
            { path: 'todos', name: 'todos', component: () => import('../views/Todos/TodosView/TodosView.vue') },
            { path: 'archive', name: 'archive', component: () => import('../views/Archive/ArchiveView.vue') },
        //     { path: 'profile', name: 'profile', component: () => import('../views/User/ProfileView.vue') },
        //     { path: 'addquestion', name: 'addquestion', component: () => import('../views/Questions/AddQuestion.vue') },
        //     { path: 'question/:id', name: 'question', component: () => import('../views/Questions/QuestionCard.vue') },
        ]
    },
    { path: '/:pathMatch(.*)*', name: 'pagenotfound', component: () => import('../views/PageNotFound/PageNotFound.vue') },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router