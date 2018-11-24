<template>
  <div id="projects">
    <introduction></introduction>
    <show-projects></show-projects>
  </div>
</template>

<script>
import introduction from '@/components/projects/Introduction.vue'
import ShowProjects from '@/components/projects/ShowProjects.vue'

export default {
  name: 'Projects',
  components: {
    introduction,
    ShowProjects
  }
}
</script>

<style scoped>
  #projects {
    min-width: 700px;
  }
</style>
