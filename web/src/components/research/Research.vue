<template>
  <div id="research">
    <introduction></introduction>
    <!--<c-t-a></c-t-a>-->
    <!--<s-t-p></s-t-p>-->
    <!--<industry-consultant></industry-consultant>-->
    <research-list></research-list>
    <research-info></research-info>
    <cooperate></cooperate>
  </div>
</template>

<script>
import introduction from '@/components/research/Introduction.vue'
// import STP from '@/components/research/STP.vue'
// import CTA from '@/components/research/CTA.vue'
// import IndustryConsultant from '@/components/research/IndustryConsultant.vue'
import ResearchList from '@/components/research/ResearchList.vue'
import ResearchInfo from '@/components/research/ResearchInfo.vue'
import Cooperate from '@/components/research/Cooperate.vue'

export default {
  name: 'Research',
  components: {
    introduction,
    // CTA,
    // STP,
    // IndustryConsultant,
    ResearchList,
    ResearchInfo,
    Cooperate
  }
}
</script>

<style scoped>
  #research {
    min-width: 700px;
  }
</style>
