<template>
  <div id="resource">
    <introduction></introduction>
    <newcomer></newcomer>
    <progress-resource></progress-resource>
    <official-dynamics></official-dynamics>
    <help></help>
  </div>
</template>

<script>
import introduction from '@/components/resource/Introduction.vue'
import Newcomer from '@/components/resource/Newcomer.vue'
import ProgressResource from '@/components/resource/ProgressResource.vue'
import OfficialDynamics from '@/components/resource/OfficialDynamics.vue'
import Help from '@/components/resource/Help.vue'

export default {
  name: 'Resource',
  components: {
    introduction,
    Newcomer,
    ProgressResource,
    OfficialDynamics,
    Help
  }
}
</script>

<style scoped>
  #resource {
    min-width: 700px;
  }
</style>
