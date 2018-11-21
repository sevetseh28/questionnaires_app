import Vue from 'vue'
import Router from 'vue-router'
import QuestionnairesList from './views/QuestionnairesList.vue'
import Conversation from './views/Conversation.vue'

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: QuestionnairesList
        },
        {
            path: '/conversation/:convId',
            name: 'conversation',
            component: Conversation
        },
        {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
        }
    ]
})
