import { createRouter, createWebHistory } from 'vue-router'
import MarkdownFile from '../pages/MarkdownFile.vue'
import PostsByMedium from '../pages/PostsByMedium'
import PostsBySubject from '../pages/PostsBySubject'
import App from '../App.vue'

const backendUrl = "http://0.0.0.0:8100/"

const routes = [
    {
        path: '/post/:markdownFile',
        component: MarkdownFile,
        props: route => ({ markdownFile: route.params.markdownFile, backendUrl: backendUrl })
    },
    {
        path: '/medium/:medium',
        component: PostsByMedium,
        props: route => ({ medium: route.params.medium, backendUrl: backendUrl })
    },
    {
        path: '/subject/:subject',
        component: PostsBySubject,
        props: route => ({ subject: route.params.subject, backendUrl: backendUrl })
    },
    /// could make about this project have the path
    /// but then make the component be markdown file with certain parameters
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
