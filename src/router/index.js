import { createRouter, createWebHistory } from 'vue-router'
import Books from '../pages/Books.vue'
import App from '../App.vue'

const routes = [
    {
        path: '/books',
        name: 'Books',
        component: Books
    },
    {
        path: '/home',
        name: 'Home',
        component: App
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
