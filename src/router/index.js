import { createRouter, createWebHistory } from 'vue-router'
import MarkdownFile from '../pages/MarkdownFile.vue'
import App from '../App.vue'

const backendUrl = "http://0.0.0.0:8100/"

const routes = [
    {
        path: '/mdfile/:markdownFile',
        component: MarkdownFile,
        props: route => ({ markdownFile: route.params.markdownFile, backendUrl: backendUrl })
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
