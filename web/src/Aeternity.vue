<template>
  <div id="Aeternity">
    <tag-index></tag-index>
    <router-view/>
    <bottom></bottom>
  </div>
</template>

<script>
import TagIndex from '@/components/tag_index/TagIndex'
import Bottom from '@/components/tag_index/Bottom'
export default {
  name: 'Aeternity',
  components: {
    TagIndex,
    Bottom
  }
}
</script>

<style>
#Aeternity {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
