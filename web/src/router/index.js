import Vue from 'vue'
import Router from 'vue-router'
import Overview from '@/components/overview/Overview'
import Research from '@/components/research/Research'
import Foundation from '@/components/foundation/foundation'
import Projects from '@/components/projects/Projects'
import Resource from '@/components/Resource/Resource'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: {name: 'overview'}
    },
    {
      path: '/overview/',
      name: 'overview',
      component: Overview
    },
    {
      path: '/research/',
      name: 'research',
      component: Research
    },
    {
      path: '/projects/',
      name: 'projects',
      component: Projects
    },
    {
      path: '/foundation/',
      name: 'foundation',
      component: Foundation
    },
    {
      path: '/resource/',
      name: 'resource',
      component: Resource
    }
  ]
})
