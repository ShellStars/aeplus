<template>
  <div id="foundation">
    <introduction></introduction>
    <aefoundation></aefoundation>
    <taginfo></taginfo>
    <cooperate></cooperate>
    <join-me></join-me>
  </div>
</template>

<script>
import introduction from '@/components/foundation/Introduction.vue'
import aefoundation from '@/components/foundation/AeternityFoundation.vue'
import taginfo from '@/components/foundation/TagInfo.vue'
import Cooperate from '@/components/foundation/Cooperate.vue'
import JoinMe from '@/components/foundation/JoinMe.vue'
export default {
  name: 'Foundation',
  components: {
    introduction,
    aefoundation,
    taginfo,
    Cooperate,
    JoinMe
  }
}
</script>

<style scoped>
  #foundation {
    min-width: 700px;
  }
</style>
