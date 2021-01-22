import { createRouter, createWebHashHistory } from 'vue-router'
import MarkdownFile from '../pages/MarkdownFile.vue'
import PostsByMedium from '../pages/PostsByMedium'
import PostsBySubject from '../pages/PostsBySubject'
import AboutPage from '../pages/AboutPage'
import Books from '../pages/Books'


const routes = [
    {
        path: '/post/:markdownFile',
        component: MarkdownFile,
        props: route => ({ markdownFile: route.params.markdownFile }),
    },
    {
        path: '/medium/book',
        component: Books,
    },
    {
        path: '/medium/:medium',
        component: PostsByMedium,
        props: route => ({ medium: route.params.medium })
    },
    {
        path: '/subject/:subject',
        component: PostsBySubject,
        props: route => ({ subject: route.params.subject })
    },
    {
        path: '/',
        component: AboutPage,
        props: { pageName: "about_this_project" }
    },
    {
        path: '/research',
        component: AboutPage,
        props: { pageName: "research" }
    },
    {
        path: '/about_me',
        component: AboutPage,
        props: { pageName: "about_me" }
    },
    {
        path: '/internet_reading',
        component: AboutPage,
        props: { pageName: "internet_reading" }
    },
]

const router = createRouter({
    history: createWebHashHistory(process.env.BASE_URL),
    routes
})

export default router
