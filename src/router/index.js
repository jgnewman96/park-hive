import { createRouter, createWebHistory } from 'vue-router'
import MarkdownFile from '../pages/MarkdownFile.vue'
import PostsByMedium from '../pages/PostsByMedium'
import PostsBySubject from '../pages/PostsBySubject'
import AboutPage from '../pages/AboutPage'

const backendUrl = "https://0.0.0.0:8100/"

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
    {
        path: '/',
        component: AboutPage,
        props: { pageName: "about_this_project", backendUrl: backendUrl }
    },
    {
        path: '/research',
        component: AboutPage,
        props: { pageName: "research", backendUrl: backendUrl }
    },
    {
        path: '/about_me',
        component: AboutPage,
        props: { pageName: "about_me", backendUrl: backendUrl }
    },
    {
        path: '/internet_reading',
        component: AboutPage,
        props: { pageName: "internet_reading", backendUrl: backendUrl }
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
