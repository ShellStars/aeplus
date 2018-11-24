<template>
  <div id="overview">
    <first></first>
    <introduction></introduction>
    <idea></idea>
    <node></node>
    <cooperate></cooperate>
    <workstation></workstation>
    <email></email>
  </div>
</template>

<script>
import first from '@/components/overview/First'
import introduction from '@/components/overview/Introduction.vue'
import Idea from '@/components/overview/Idea.vue'
import Node from '@/components/overview/Node.vue'
import Cooperate from '@/components/overview/Cooperate.vue'
import Workstation from '@/components/overview/Workstation.vue'
import Email from '@/components/overview/Email.vue'

export default {
  name: 'Overview',
  components: {
    first,
    introduction,
    Idea,
    Node,
    Cooperate,
    Workstation,
    Email
  }
}
</script>

<style scoped>
  #overview {
    min-width: 700px;
  }
</style>
